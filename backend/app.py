import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from scraper import youtube_search
import table_creation
from routes.topic import topic_bp

load_dotenv()


app = Flask(__name__)
CORS(app)
app.register_blueprint(topic_bp)

api_key = os.getenv('YT_API_KEY')
print(api_key)

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
