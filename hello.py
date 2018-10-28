from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
    return 'Index'

@app.route("/testing")
def testing():
    return 'Testing Route'

@app.route("/profile")
def profile():
    return 'Profile'
 
@app.route("/profile/<string:name>")
def getProfile(name):
    return name

if __name__ == "__main__":
    app.run()