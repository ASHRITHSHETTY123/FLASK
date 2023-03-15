from flask import Flask,redirect,url_for, render_template, request, session

app=Flask(__name__)
app.secret_key="hello"

@app.route("/")
def home():
    return render_template("index.html",content="Testing")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        user=request.form["nm"]
        session["user"]=user      # store the information in teh session
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user=session["user "]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

#@app.route("/test")
#def test():
#    return render_template("new.html")

if __name__== "__main__":
    app.run(debug=True)