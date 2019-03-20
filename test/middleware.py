from flask import Flask, jsonify, abort, make_response
from services.data_provider_service import DataProviderService as candidatServices

generate_candidats = candidatServices(5)

def get_candidats():
	return jsonify(generate_candidats.get_candidates())

# @app.route("/")
# def page_index():
# 	return render_template('index.html')
# 	# return render_template('index.html', selected_menu_item="index")
#
# @app.route("/about")
# def page_about():
# 	return render_template('about.html')
#
# @app.route("/candidate")
# def page_candidate():
# 	return render_template('candidate.html')
#
# @app.route("/experience")
# def page_experience():
# 	return render_template('experience.html')
#
# @app.route("/project")
# def page_project():
# 	return render_template('project.html')
#
# # Requetes Index
# @app.route("/api")
# def index():
#
# 	quotes = [{
# 			"author": "Elbert Hubbard",
# 			"quote": "Do not take life too seriously. You will never get out of it alive."
# 		},
# 		{
# 			"author": "Mark Twain",
# 			"quote": "Get your facts first, then you can distort them as you please."
# 		}
# 	]
#
# 	nr_of_quotes = len(quotes)
# 	selected_quote = quotes[random.randint(0, nr_of_quotes - 1)]
# 	return jsonify(selected_quote)
#
# # Requetes Candidats
# @app.route("/api/candidats",methods=["GET"])
# def get_candidats():
# 	return routesCandidats.get_candidats()
#
# @app.route("/api/candidat/<string:id>",methods=["GET"])
# def get_candidat(id):
# 	return routesCandidats.get_candidat(id)
#
# @app.route("/api/candidat/delete/<string:id>",methods=["GET"])
# def delete_candidat(id):
# 	return routesCandidats.delete_candidat(id)
#
# # Requetes Projects
# @app.route("/api/projects",methods=["GET"])
# def get_project():
# 	return routesProjects.get_projects()
#
# # Requetes Experiences
# @app.route("/api/experiences",methods=["GET"])
# def get_experiences():
# 	return routesExperiences.get_experiences()
