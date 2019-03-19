from flask import Flask, jsonify
import random
import candidat_fixtures


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

@app.route("/candidats")
def get_candidats():

	candidats = candidat_fixtures.get_candidats()
	nr_of_candidats = len(candidats)
	selected_candidat = candidats[random.randint(0, nr_of_candidats - 1)]
	return jsonify(selected_candidat)

@app.route("/api/candidat/<string:id>", methods=["GET"])
def candidate_by_id(id):
	candidat = candidat_fixtures.get_candidat(id)
	return jsonify(candidat)

if __name__ == "__main__":
	app.run(debug=True)
