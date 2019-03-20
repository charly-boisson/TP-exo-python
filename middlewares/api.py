from flask import jsonify, abort, make_response
from service.CandidateService import CandidateService

candidate_service = CandidateService(5)

def get_candidates():
    candidates = candidate_service.get_candidates()
    return jsonify(candidates)

def get_candidat(id):
	candidat = candidate_service.get_candidate(id)
	if candidat:
		return jsonify(candidat)
	else:
		return abort(404)

def delete_candidat(id):
	deletecandidat = candidate_service.delete_candidate(id)
	if deletecandidat:
		resp = { "message": "Candidat supprimé !" }
		return make_response(jsonify(resp), 200)
	else:
		return abort(404)

def get_experiences():
    candidats = candidate_service.get_candidates()
    experiences = []
    for candidat in candidats:
        experiences.append(candidat['experience'])

    return jsonify(experiences)

def get_projects():
    candidats = candidate_service.get_candidates()
    projects = []
    for candidat in candidats:
        experiences = candidat['experience']
        for experience in experiences:
            projects.append(experience['projects'])

    return jsonify(projects)
