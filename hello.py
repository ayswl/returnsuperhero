from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "First Flask App Baby"
 
if __name__ == "__main__":
    app.run()