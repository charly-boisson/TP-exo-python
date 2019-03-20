from flask import Flask
import routes

app = Flask(__name__)
routes.get_routes_api(app)
routes.get_routes_template(app)

if __name__ == "__main__":
	app.run(debug=True)
