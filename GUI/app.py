from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/covidlogin")
def covidlogin():
	return render_template("covidlogin.html")

@app.route("/covidhome")
def covidhome():
	return render_template("covidhome.html")

@app.route("/countrymenu.html")
def countrymenu():
	return render_template("countrymenu.html")

@app.route("/statemenu.html")
def statemenu():
	return render_template("statemenu.html")

@app.route("/one")
def one():
	return render_template("file:///C:/Users/lenovo/Downloads/one.html")	

@app.route("/two")
def two():
	return render_template("file:///C:/Users/lenovo/Downloads/two.html")

@app.route("/three")
def three():
	return render_template("file:///C:/Users/lenovo/Downloads/three.html")

@app.route("/four")
def four():
	return render_template("file:///C:/Users/lenovo/Downloads/four.html")

@app.route("/six")
def six():
	return render_template("file:///C:/Users/lenovo/Downloads/six.html")

@app.route("/seven")
def seven():
	return render_template("file:///C:/Users/lenovo/Downloads/seven.html")

@app.route("/eight")
def eight():
	return render_template("file:///C:/Users/lenovo/Downloads/eight.html")

@app.route("/nine")
def nine():
	return render_template("file:///C:/Users/lenovo/Downloads/nine.html")

@app.route("/ten")
def ten():
	return render_template("file:///C:/Users/lenovo/Downloads/ten.html")

@app.route("/eleven")
def eleven():
	return render_template("file:///C:/Users/lenovo/Downloads/eleven.html")

@app.route("/twelve")
def twelve():
	return render_template("file:///C:/Users/lenovo/Downloads/twelve.html")

@app.route("/thirteen")
def thirteen():
	return render_template("file:///C:/Users/lenovo/Downloads/thirteen.html")	

@app.route("/fourteen")
def fourteen():
	return render_template("file:///C:/Users/lenovo/Downloads/fourteen.html")

@app.route("/fifteen")
def fifteen():
	return render_template("file:///C:/Users/lenovo/Downloads/fifteen.html")

@app.route("/sixteen")
def sixteen():
	return render_template("file:///C:/Users/lenovo/Downloads/sixteen.html")

@app.route("/seventeen")
def seventeen():
	return render_template("file:///C:/Users/lenovo/Downloads/seventeen.html")

@app.route("/measures")
def measures():
	return render_template("measures.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/covid")
def covid():
	return render_template("covid.html")

@app.route("/study")
def study():
	return render_template("study.html")