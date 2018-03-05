from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content type', 'text/html')
				self.end_headers()

				output = ""
				output += "<html><body>Hello!</body></html>"
				self.wfile.write(output)
				print output
				return

		except IOError:
			self.send_error(404, "Requested file not found at %s" % self.path)

def main():
	try:
		port = 8080
		server = HTTPServer(('', port), webserverHandler)
		print "Server is running on port %s" % port
		server.serve_forever()
	except KeyboardInterrupt:
		print " ^C entered, stopping server..."
		server.socket.close()

if __name__ == '__main__':
	main()
