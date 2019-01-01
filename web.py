from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def first():
    return 'welcome to flask'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
