from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "hello ramya"

if __name__=="__main__":
    app.run(debug=True,threaded=True)