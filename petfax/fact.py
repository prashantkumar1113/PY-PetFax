import imp
from flask import (Blueprint, render_template)
bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route("/new")
def new():
    return "return new fact form"