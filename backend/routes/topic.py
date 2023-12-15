from flask import Flask, request, jsonify, Blueprint
from sqlalchemy.orm import Session
# from sqlalchemy import create_engine
from table_creation import engine, topic, note, user

# app = Flask(__name__)
topic_bp = Blueprint('topic', __name__)

@topic_bp.route('/topic', methods=['GET'])
def get_topic():
    print("in the create_topic function")
    return jsonify({"message": "in the get topic route"}), 201

@topic_bp.route('/topic', methods=['POST'])
def create_topic():
    data = request.get_json()
    print("data = ", data)
    new_topic = topic.insert().values(notes_id=data['notes_id'], user_id=data['user_id'])
    with engine.connect() as connection:
        result = connection.execute(new_topic)
    print("result = ", result)
    return jsonify({"message": "Topic created successfully"}), 201

@topic_bp.route('/topic/<int:topic_id>', methods=['PUT'])
def modify_topic(topic_id):
    data = request.get_json()
    update_topic = topic.update().where(topic.c.id == topic_id).values(title=data['title'], note=data['note'])
    with engine.connect() as connection:
        result = connection.execute(update_topic)
    return jsonify({"message": "Topic updated successfully"}), 200

# if __name__ == '__main__':
#     app.run(debug=True)