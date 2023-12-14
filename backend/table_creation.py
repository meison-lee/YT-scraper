from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ARRAY, ForeignKey
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
print(DATABASE_URL)

engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define the user table
user = Table(
   'user', metadata,
   Column('id', Integer, primary_key=True),
   Column('username', String),
   Column('email', String)
)

# Define the topic table
topic = Table(
   'topic', metadata,
   Column('id', Integer, primary_key=True),
   Column('notes_id', ARRAY(String)),
   Column('user_id', Integer, ForeignKey('user.id'))
)

note = Table(
   'note', metadata,
   Column('id', Integer, primary_key=True),
   Column('title', String),
   Column('video', String),
   Column('content', String),
   Column('timestamp', String),
   Column('user_id', Integer, ForeignKey('user.id'))
)

# Create the table in the database
metadata.create_all(engine)