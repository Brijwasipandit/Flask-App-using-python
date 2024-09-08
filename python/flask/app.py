from flask import Flask, render_template, jsonify

app = Flask(__name__)

# API route
@app.route('/status')
def status():
    return jsonify({"message": "Server is up and running"}), 200

# Main route to serve greeting page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)

