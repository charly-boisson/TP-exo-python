from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")
def index():

	quotes = [{
			"author": "Elbert Hubbard",
			"quote": "Do not take life too seriously. You will never get out of it alive."
		},
		{
			"author": "Mark Twain",
			"quote": "Get your facts first, then you can distort them as you please."
		}
	]
	nr_of_quotes = len(quotes)
	selected_quote = quotes[random.randint(0, nr_of_quotes - 1)]
	return jsonify(selected_quote)


if __name__ == "__main__":
	app.run(debug=True)
