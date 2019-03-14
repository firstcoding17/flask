from flask import Flask, request
app = Flask(__name__)
print(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return"<h1> Hello World %s</h1>" % user_agent

@app.route("/user/<name>")
def user(name):
    return "<h1> Hello World %s !</h1>" % name
    
if __name__ == "__main__" :
    app.run()