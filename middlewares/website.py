from flask import render_template
import middlewares.api as api

def page_index():
	return render_template('index.html')
	# return render_template('index.html', selected_menu_item="index")

def page_about():
	return render_template('about.html')


def page_candidate():
	candidates = api.get_candidates(False)
	return render_template('candidate.html', candidates=candidates)


def page_experience():
	experiences = api.get_experiences(False)
	return render_template('experience.html', experiences=experiences)


def page_project():
	projects = api.get_projects(False)
	return render_template('project.html', projects=projects)
