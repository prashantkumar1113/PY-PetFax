from flask import Flask
from flask_migrate import Migrate

# factory 
def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://PK:postgres@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

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