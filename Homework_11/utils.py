import json


def load_candidates_from_json() -> list[dict]:
    """Возвращает список всех кандидатов"""
    with open("candidates.json", "r", encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id: int) -> dict:
    """возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json():
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    result = []
    for candidate in load_candidates_from_json():
        if candidate_name.lower() in candidate["name"].lower():
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    result = []
    candidates = load_candidates_from_json()
    for candidate in candidates:
        skills = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            result.append(candidate)
    return result
