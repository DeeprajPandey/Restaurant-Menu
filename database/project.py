
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
	output = restaurant.name + '<br/>'
	for i in items:
		output += i.name
		output += '</br>'
		output += i.price
		output += '</br>'
		output += i.description
		output += '</br>'
		output += '</br>'
	return output
@app.route('/restaurants/<int:restaurant_id>/new')

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit')

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete')

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)