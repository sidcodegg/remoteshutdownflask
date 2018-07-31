from flask import *
import os
app = Flask(__name__)
@app.route("/", methods=["GET"])
def init():
	return render_template("shutdown.html")
	
@app.route("/shutdown", methods=['POST'])
def shutdown():
	os.system('shutdown -s')
	return render_template("done.html")
	
	

app.run(debug=True)
