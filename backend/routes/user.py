from flask import Flask, request, jsonify, Blueprint
from sqlalchemy.orm import Session
# from sqlalchemy import create_engine
from table_creation import engine, user, note, user

# app = Flask(__name__)
user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['GET'])
def get_user():
    return jsonify({"message": "in the get user route"}), 201

@user_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    print("data = ", data)
    new_user = user.insert().values(username=data['username'], email=data['email'])
    with engine.connect() as connection:
        result = connection.execute(new_user)
    print("result = ", result)
    return jsonify({"message": "Topic created successfully"}), 201

@user_bp.route('/user/<int:topic_id>', methods=['PUT'])
def modify_topic(topic_id):
    data = request.get_json()
    update_topic = user.update().where(user.c.id == topic_id).values(title=data['title'], note=data['note'])
    with engine.connect() as connection:
        result = connection.execute(update_topic)
    return jsonify({"message": "Topic updated successfully"}), 200

# if __name__ == '__main__':
#     app.run(debug=True)