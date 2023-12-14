from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ARRAY, ForeignKey
# import psycopg2

# Replace with your actual database connection details
DATABASE_URL = "postgresql://Meison_Lee:nozZym-xemmy7-ceqsep@scraper-db.postgres.database.azure.com:5432/postgres?sslmode=require"

# psql -h scraper-db.postgres.database.azure.com -U Meison_Lee -d postgres

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