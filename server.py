from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", color1="black",color2="red", x=8,y=8)


@app.route('/<int:x>')
def eight_by_four(x):
    return render_template("index.html", color1="black",color2="red", x=x,y=8)

@app.route('/<int:x>/<int:y>')
def x_by_y(x,y):
    return render_template("index.html", color1="black",color2="red", x=x,y=y)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def so_many_options(x,y,color1,color2):
    return render_template("index.html", color1=color1,color2=color2, x=x,y=y)


if __name__=="__main__":
    app.run(debug=True)