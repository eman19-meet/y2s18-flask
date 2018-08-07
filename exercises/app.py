from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	favPlayers=["a","b","c"]
	return render_template("index.html", favPlayers=favPlayers)

if __name__ == '__main__':
   app.run(debug = True)