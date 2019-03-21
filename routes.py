from flask import abort
import middlewares.api as api
import middlewares.website as website
import middlewares.errors as errors

def get_routes_api(app):
    app.add_url_rule('/api/candidates', 'candidates', api.get_candidates, methods=['GET'])
    app.add_url_rule('/api/candidates/<string:id>', '<string:id>', api.get_candidat, methods=['GET'])
    # app.add_url_rule('/api/candidates/<string:id>', 'id', api.delete_candidat, methods=['DELETE'])
    app.add_url_rule('/api/experiences', 'experiences', api.get_experiences, methods=['GET'])
    app.add_url_rule('/api/projects', 'projects', api.get_projects, methods=['GET'])
    app.add_url_rule('/api/initdb', 'initdb', api.init_database, methods=['GET'])
    app.add_url_rule('/api/filldb5', 'filldb5', api.fill_database, methods=['GET'])

def get_routes_template(app):
    app.add_url_rule('/index', 'index', website.page_index, methods=['GET'])
    app.add_url_rule('/about', 'about', website.page_about, methods=['GET'])
    app.add_url_rule('/candidate', 'candidate', website.page_candidate, methods=['GET'])
    app.add_url_rule('/experience', 'experience', website.page_experience, methods=['GET'])
    app.add_url_rule('/project', 'project', website.page_project, methods=['GET'])

def init_error_handlers(app):
    app.errorhandler(404)(errors.handle_error_404)
    app.errorhandler(500)(errors.handle_error_500)
    app.add_url_rule('/crash', 'crash', errors.crash)
