# Classes create tables and mapper code creates columns
# manipulate python RTE
import sys
# mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for foreign key relationships, for mapper
from sqlalchemy.orm import relationship

# for configuration
from sqlalchemy import create_engine

Base = declarative_base()

# Create a table for restaurants
class Restaurant(Base):
	__tablename__ = 'restaurant'
	name = Column(
		String(80), nullable = False)
	id = Column(
		Integer, primary_key = True)

#Create a table for menu items

