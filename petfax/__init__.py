from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, PetFax"

    @app.route('/test')
    def test():
        return {"fname": "Prashant", "lname": "Kumar"}

    # register blueprints
    from . import pet
    app.register_blueprint(pet.bp)
    
    return app