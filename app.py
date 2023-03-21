from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def index_page():
    candidates = utils.load_candidates()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:id_>")
def candidate_page(id_):
    candidate = utils.get_candidate(id_)
    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search_page(candidate_name):
    candidates = utils.get_candidate_by_name(candidate_name)
    total = len(candidates)
    return render_template("search.html", candidates=candidates, total=total)


@app.route("/skill/<skill_name>")
def skill_page(skill_name):
    candidates = utils.get_candidate_by_skill(skill_name)
    total = len(candidates)
    return render_template("skill.html",
                           candidates=candidates,
                           total=total,
                           skill_name=skill_name)


app.run(debug=True)
