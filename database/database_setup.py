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