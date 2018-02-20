##
 # database_setup.py
 #
 # Deepraj Pandey
 # deepraj11pandey@gmail.com
 # Classes create tables and mapper code creates columns

# Manipulate python RTE
import sys
# Mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# For configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# For foreign key relationships, for mapper
from sqlalchemy.orm import relationship

# For configuration
from sqlalchemy import create_engine
############

# Restaurant table
class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(
                  String(80), nullable = False)
    id = Column(
                Integer, primary_key = True)

# Menu table
class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(
                  String(80), nullable = False)
    id = Column(
                Integer, priamry_key = True)
    course = Column(
                    String(80))
    description = Column(
                         String(250))
    price = Column(
                   String(8))
    restaurant_id = Column(
                           Integer, ForeignKey = 'restaurant.id')
    restaurant = relationship(Restaurant)

############
# Create the database
engine = create_engine(
                       sqlite:///restaurantmenu.db)

# Adds classes as new tables in the database
Base.metadata.create_all(engine)
