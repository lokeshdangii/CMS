from flask import Flask, render_template


# import blueprint from scripts
from car_color import manage_car_color
from car_category import manage_car_category
from car_engine import manage_car_engine
from car_model import manage_car_model
from car_variant import manage_car_variant
from car import manage_car
from auth import auth
from links import links
from context_processor import usernames


app = Flask(__name__)
app.secret_key = '1df90c98804d9e99099c4356a9d4c3989b681e578d413d79f7759c305b18e6b1'

@app.route("/")
def index():
    return render_template('index.html')



# Register the context processor
# Context processors are functions that run before rendering a template and can add variables to the context that are available to all templates.
app.context_processor(usernames)

# register blueprint
app.register_blueprint(manage_car_color)
app.register_blueprint(manage_car_category)
app.register_blueprint(manage_car_engine)
app.register_blueprint(manage_car_model)
app.register_blueprint(manage_car_variant)
app.register_blueprint(manage_car)
app.register_blueprint(auth)
app.register_blueprint(links)


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
    # app.run(debug=False)
