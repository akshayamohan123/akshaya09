from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "<h1>hello</h1>"

@app.route('/hello/<name>')
def hello1(name):
    return "<h1>hello" + name + "</h1>"

@app.route('/hello/<int:name>')
def hello2(name):
    return "num->%d"%name

def welcome1():
    return 'welcome'

app.add_url_rule('/w','nn',welcome1)

if __name__=="__main__":
    app.run(debug=True)



