from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
# Common Get Interface for POST
import cgi
class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content type', 'text/html')
				self.end_headers()

				output=""
				output+="<html><body>Hello!</body></html>"
				self.wfile.write(output)
				print output
				return
			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header('Content type', 'text/html')
				self.end_headers()

				output=""
				output+="<html><body>&#161Hola!<a href='/hello'>Back to hello</a></body></html>"
				self.wfile.write(output)
				print output
				return
		except IOError:
			self.send_error(404, "File not found at %s" % self.path)
	def do_POST(self):
		try:
			self.send_response(301)
			self.end_headers()

			

		except:

def main():
	try:
		port = 8080
		server = HTTPServer(('', port), webserverHandler)
		print "Server running on port %s" % port
		server.serve_forever()
	except KeyboardInterrupt:
		print " ^C entered, stopping webserver..."
		server.socket.close()

if __name__ == '__main__':
	main()
