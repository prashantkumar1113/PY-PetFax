from flask import Flask, url_for

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, PetFax"

    @app.route('/test')
    def test():
        return {"fname": "Prashant", "lname": "Kumar"}

    # register blueprints
    from . import pet, fact
    app.register_blueprint(pet.bp)
    app.register_blueprint(fact.bp)
    
    return app