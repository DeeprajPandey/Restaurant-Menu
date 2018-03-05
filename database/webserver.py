from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

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
