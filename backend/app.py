from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret-key'
CORS(app)
jwt = JWTManager(app)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    result = "predicted_value"  # replace with real ML logic
    return jsonify({'result': result})
