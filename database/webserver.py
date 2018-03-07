from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to metadata of Base so declaratives can be accessed through DBSession
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/restaurants"):
            	# To read names
            	allRestaurants = session.query(Restaurant).all()
            	self.send_response(200)
            	self.send_header('Content-type', 'text/html')
            	self.end_headers()
            	output=""
            	output+="<html><body>"
            	output+="<h1>List of Restaurants</h1>"
            	output+="<a href='/restaurants/new'><h2>Make a New Restaurant Here</h2></a>"
            	for restaurant in allRestaurants:
            		output+="<div><h3> %s </h3>" % restaurant.name
            		output+="<a href='/edit'>Edit</a>"
            		output+="&emsp;<a href='/delete'>Delete</a></div><br/><br/>"
            	output+="</body></html>"
            	self.wfile.write(output)
            	print output
            	return
            if self.path.endswith("/restaurants/new"):
            	self.send_response(200)
            	self.send_header('Content-type', 'text/html')
            	self.end_headers()
            	output=""
            	output+="<html><body>"
            	output+="<h1>Make a New Restaurant</h1><br/>"
            	output+='''<form method='POST' enctype='multipart/form-data' placeholder='New Restaurant Name'><input name='restaurantName' type='text'><input type='submit' value='Submit'></form>'''
            	output+="</html></body>"
            	self.wfile.write(output)
            	print output
            	return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
    	if self.path.endswith("/restaurants/new")
	        ctype, pdict = cgi.parse_header(
				self.headers.getheader('content-type'))
			if ctype == 'multipart/form-data':
				fields = cgi.parse_multipart(self.rfile, pdict)
				inputText = fields.get('restaurantName')
			newRestaurant = Restaurant(name=inputText[0])
			session.add(newRestaurant)
			session.commit()

			self.send_response(301)
			self.send_header('Content-type', 'text/html')
			self.send_header('Location', '/restaurants')
			self.end_headers()

		except:
			pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()