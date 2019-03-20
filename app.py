from flask import Flask
import routes

app = Flask(__name__)
routes.get_routes_api(app)
routes.get_routes_template(app)
routes.init_error_handlers(app)

if __name__ == "__main__":
	app.secret_key = 'super secret key'
	app.run(debug=True)
