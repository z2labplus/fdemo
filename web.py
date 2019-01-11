from flask import Flask
import time
app = Flask(__name__)
@app.route('/')
def hello_world():
    response = 'Hello World '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return response
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=9999)
