import json
from pprint import pprint

PATH = 'candidates.json'


def load_candidates():
    with open(PATH, 'r', encoding="utf-8") as file:
        candidates = json.load(file)
    #
    # for candidate in candidates:
    #     candidate["first_name"] = candidate["name"].split(" ")[0]

    return candidates


def get_candidate(id_):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["id"] == id_:
            return candidate


def get_candidate_by_name(name):
    all_candidates = load_candidates()
    sorted_candidates = []
    for candidate in all_candidates:
        if name in candidate["name"]:
            sorted_candidates.append(candidate)

    return sorted_candidates


def get_candidate_by_skill(skill):
    all_candidates = load_candidates()
    sorted_candidates = []
    for candidate in all_candidates:
        if skill in candidate["skills"].lower().split(', '):
            sorted_candidates.append(candidate)

    return sorted_candidates



pprint(get_candidate_by_name("Leo"))
