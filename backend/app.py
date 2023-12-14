# app.py
import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from scraper import youtube_search
import table_creation
# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
# # import psycopg2

# # Replace with your actual database connection details
# DATABASE_URL = "postgresql://Meison_Lee:nozZym-xemmy7-ceqsep@scraper-db.postgres.database.azure.com:5432/postgres?sslmode=require"

# # psql -h scraper-db.postgres.database.azure.com -U Meison_Lee -d postgres

# engine = create_engine(DATABASE_URL)
# metadata = MetaData()

# # Define a new table with columns
# my_table = Table('my_table', metadata,
#                  Column('id', Integer, primary_key=True),
#                  Column('name', String),
#                  Column('value', String)
#                  )

# # Create the table in the database
# metadata.create_all(engine)




app = Flask(__name__)
CORS(app)

api_key = os.getenv('api_key')

@app.route('/api/search', methods=['GET'])
# @cross_origin(origin='http://localhost:3000')
def search():
    print("in the search function")
    query = request.args.get('query', '')
    results = youtube_search(api_key, query, max_results=2)
    print(results)
    # Implement your search logic here
    # For example, you might query a database or an external API
    return jsonify(results)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "CORS is working"})


if __name__ == '__main__':
    app.run(port=8080, debug=True)
