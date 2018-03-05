from BaseHttpServer import HTTPServer, BaseHTTPRequestHandler

def main():
	try:
		port = 8080
		server = HTTPServer(('', port), webserverHandler)
		print "Server is running on port %s" % port
		server.run_forever()

	except KeyboardInterrupt:
		print " ^C entered, closing server..."
		server.socket.close()

if __name__ == '__main__':
	main()