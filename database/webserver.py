from BaseHTTPServer import BaseHTTPRequestHandler, BaseHTTPServer

class webserverHander(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content type', 'text/html')
				self.end_headers()

				output=""
				output+="<html><body>Hello!</body></html>"

def main():
	try:
		port = 8080
		server = HTTPserver(('',port), webserverHandler)
		print "Web server is running on port %s" % port
		serve.serve_forever()
	except KeyboardInterrupt:
		print("^C entered, stopping server...")
		server.socket.close
	else:
		pass
	finally:
		pass

if __name__ == '__main__':
	main()
