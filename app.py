from flask import Flask, render_template, url_for
from routes.site import site_route

app = Flask(__name__)

app.register_blueprint(site_route)


app.run(debug=True, host="0.0.0.0")