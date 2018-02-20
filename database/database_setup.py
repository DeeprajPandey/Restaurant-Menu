##
 # database_setup.py
 #
 # Deepraj Pandey
 # deepraj11pop@gmail.com
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

############
# Create the database
engine = create_engine(
                       sqlite:///restaurantmenu.db)

# Adds classes as new tables in the database
Base.metadata.create_all(engine)
