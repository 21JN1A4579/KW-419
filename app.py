from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.json
    # Process and save the data as needed
    print(data)
    
    # Replace this with your actual processing logic
    response = {'message': 'Form submitted successfully'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
