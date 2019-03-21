from flask import jsonify, abort, make_response
from service.CandidateService import CandidateService

db_engine = 'sqlite:////Users/charlyboisson/Documents/MYDIGITALSCHOOL/COURS/PYTHON/tp-exo-python/db/test.db'
DATA_PROVIDER = CandidateService(db_engine)

# candidate_service = CandidateService(5)

def get_candidates(serialize=True):
    candidates = candidate_service.get_candidates()
    if(serialize):
        return jsonify(candidates)
    else:
        return candidates

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

def get_experiences(serialize=True):
    candidats = candidate_service.get_candidates()
    experiences = []
    for candidat in candidats:
        experiences.append(candidat['experience'])

    if(serialize):
        return jsonify(experiences)
    else:
        return experiences

def get_projects(serialize=True):
    candidats = candidate_service.get_candidates()
    projects = []
    for candidat in candidats:
        experiences = candidat['experience']
        for experience in experiences:
            projects.append(experience['projects'])

    if(serialize):
        return jsonify(projects)
    else:
        return projects

def init_database():
    DATA_PROVIDER.init_database()
    resp = { "message": "Instanciation BDD reussis !" }
    return jsonify(resp)


def fill_database():
    DATA_PROVIDER.fill_database()
    resp = { "message": "Creation des jeux de données de la BDD reussis !" }
    return jsonify(resp)
