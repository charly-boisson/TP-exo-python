from flask import Flask, jsonify
import random
import routes.candidats as routesCandidats
import routes.projects as routesProjects
import routes.experiences as routesExperiences

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

# Requetes Candidats
@app.route("/api/candidats",methods=["GET"])
def get_candidats():
	return routesCandidats.get_candidats()

@app.route("/api/candidat/<string:id>",methods=["GET"])
def get_candidat(id):
	return routesCandidats.get_candidat(id)

@app.route("/api/candidat/delete/<string:id>",methods=["GET"])
def delete_candidat(id):
	return routesCandidats.delete_candidat(id)

# Requetes Projects
@app.route("/api/projects",methods=["GET"])
def get_project():
	return routesProjects.get_projects()

# Requetes Experiences
@app.route("/api/experiences",methods=["GET"])
def get_experiences():
	return routesExperiences.get_experiences()

# app.add_url_rule('/api/candidats', 'candidats', routesCandidats.get_candidats())
# app.add_url_rule('/api/candidats/<string:id>', '<string:id>', get_candidats)


if __name__ == "__main__":
	app.run(debug=True)
