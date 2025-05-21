from flask import Flask, render_template, request, jsonify
from test_case_generator import generate
import json
from flask import Response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_test_cases():
    data = request.get_json()
    user_input = data.get('prompt', '')
    
    # Here we'll need to modify the generate function to return the response
    # instead of printing it
    response = generate(user_input)
    # return jsonify({'response': response})
    pretty_response = json.dumps({'response': response}, indent=4)
    return Response(pretty_response, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True) 