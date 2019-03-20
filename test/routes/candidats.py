from flask import Flask, jsonify, abort, make_response
from services.data_provider_service import DataProviderService as candidatServices

generate_candidats = candidatServices(5)

def get_candidats():
	candidats = generate_candidats.get_candidates()
	return jsonify(candidats)

def get_candidat(id):
	candidat = generate_candidats.get_candidate(id)
	if candidat:
		return jsonify(candidat)
	else:
		return abort(404)

def delete_candidat(id):
	deletecandidat = generate_candidats.delete_candidate(id)
	if deletecandidat:
		resp = { "message": "Candidat supprimé !" }
		return make_response(jsonify(resp), 200)
	else:
		return abort(404)
