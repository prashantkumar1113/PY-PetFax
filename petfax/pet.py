import imp
from flask import (Blueprint, render_template)
bp = Blueprint('pet', __name__, url_prefix='/pets')

import json
pets = json.load(open("pets.json"))
# print(pets)


@bp.route('/')
def index():
    # return "This is the pets index"
    return render_template("pets/index.html", pets=pets)

@bp.route('/<int:index>')
def show(index):
    return render_template("pets/pet.html", pet=pets[index])