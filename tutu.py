from flask import Flask,redirect,url_for, render_template

app=Flask(__name__)

@app.route("/<name1>")
def home(name1):
    return render_template("my.html", content=name1)

'''@app.route("/<name1>")
def user(name1):
    return f"Hello{name1}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name1="Admin!"))
'''
if __name__== "__main__":
    app.run()