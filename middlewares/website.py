from flask import render_template

def page_index():
	return render_template('index.html')
	# return render_template('index.html', selected_menu_item="index")

def page_about():
	return render_template('about.html')


def page_candidate():
	return render_template('candidate.html')


def page_experience():
	return render_template('experience.html')


def page_project():
	return render_template('project.html')
