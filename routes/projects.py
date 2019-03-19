from flask import Flask, jsonify, abort, make_response
from services.data_provider_service import DataProviderService as candidatServices

generate_candidats = candidatServices(5)

def get_projects():
    candidats = generate_candidats.get_candidates()
    print(candidats)
    return jsonify(candidats)
