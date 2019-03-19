
def candidate_by_id(id):
	candidat = candidat_fixtures.get_candidat(id)
	return jsonify(candidat)
