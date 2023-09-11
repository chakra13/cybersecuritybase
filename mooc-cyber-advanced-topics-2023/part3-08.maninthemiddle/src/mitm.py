import http.server as hs
import requests
import sys


class Mitm(hs.BaseHTTPRequestHandler):

	remote_address = None # domain name to connect

	def do_GET(self):

		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(self.path.encode()) # write requires byte array


def start_server(local_port, remote_address):
	Mitm.remote_address = remote_address
	server = hs.HTTPServer(("localhost", local_port), Mitm)
	server.serve_forever()


# This makes sure the main function is not called immediately
# when TMC imports this module
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('usage: python %s local_port remote_address' % sys.argv[0])
    else:
        start_server(int(sys.argv[1]), sys.argv[2])
