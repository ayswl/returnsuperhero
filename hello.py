from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def index():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)

@app.route("/anotherone")
def this():
    author = "Me"
    name = "You"
    return render_template('this.html', author=author, name=name)

@app.route("/andanotherone")
def that():
    author = "Me"
    name = "You"
    return render_template('that.html', author=author, name=name)

if __name__ == "__main__":
    app.run()