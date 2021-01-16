from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/isprime/<string:num>')
def isprime(num):
    prime = True
    try:
    	n = int(num)
    except:
    	return jsonify({"status":"invalid object"})
    for i in range(2, int(math.sqrt(n)+1)):
    	if n%i ==0:
    		prime =False
    result ={
    	"Number":num,
    	"Prime": prime,
    	"Server IP": "127.0.0.1"
    }
    return jsonify(result)

if __name__== "__main__":
	app.run(debug=True)
