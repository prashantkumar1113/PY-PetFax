from operator import mod
from flask import (Blueprint, render_template, request, redirect)
from . import models

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
        submitter = request.form["submitter"]
        fact = request.form["fact"]

        new_fact = models.Fact(submitter=submitter, fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        redirect('/facts')

    # return "This is the facts index"
    results = models.Fact.query.all()
    # for fact in results:
    #     print(f"submitter: {fact.submitter}, fact:{fact.fact}")
    return render_template("facts/index.html", facts=results)


@bp.route("/new")
def new():
    return render_template("facts/new.html")