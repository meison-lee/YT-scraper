# app.py
import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from scraper import youtube_search



app = Flask(__name__)
CORS(app)

api_key = os.getenv('api_key')

@app.route('/api/search', methods=['GET'])
# @cross_origin(origin='http://localhost:3000')
def search():
    print("in the search function")
    query = request.args.get('query', '')
    results, ids = youtube_search(api_key, query, max_results=10)

    # Implement your search logic here
    # For example, you might query a database or an external API
    return jsonify(results, ids)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "CORS is working"})


if __name__ == '__main__':
    app.run(port=8080, debug=True)
