from BaseHTTPServer import BaseHTTPRequestHandler, BaseHTTPServer

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