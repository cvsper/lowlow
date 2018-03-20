from flask import Flask, request, Response, render_template
import offerup, proxy

app = Flask(__name__)


@app.before_request
def data():
	name = offerup.main()
	return name

@app.route('/')
def index():
	return render_template('index.html', name=data())


if __name__ == '__main__':
	app.run(debug=True)