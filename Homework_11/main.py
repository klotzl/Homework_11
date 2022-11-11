from flask import Flask, render_template
from utils import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def candidates_list():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:cid>")
def candidate_information(cid):
    candidate = get_candidate(cid)
    if not candidate:
        return "Кандидат не найден"
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def search_by_name(candidate_name):
    find_candidate = get_candidates_by_name(candidate_name)
    if not find_candidate:
        return "Кандидат не найден"
    return render_template('search.html', candidates=find_candidate)


@app.route("/skill/<skill_name>")
def search_by_sill(skill_name):
    find_by_skill = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=find_by_skill)


app.run(debug=True)
