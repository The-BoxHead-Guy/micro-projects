notes = {
    "Ana": [4.5, 3.0, 5.0],
    "Luis": [2.0, 2.5, 3.5],
    "Mara": [5.0, 4.0, 4.5],
}

MIN_NOTE_TRESHOLD = 0.0
MAX_NOTE_TRESHOLD = 5.0
MIN_NOTE_APPROVAL = 3.0


def average(note_list: list) -> float | int:
    try:
        return sum(note_list) / len(note_list)
    except ZeroDivisionError:
        return 0


def has_approved(note_list: list) -> bool:
    notes_average = average(note_list)

    return notes_average >= MIN_NOTE_APPROVAL


def average_notes_per_student(notes: dict[str, list[float]]) -> dict:
    new_average = {}

    for key, value in notes.items():
        new_average[key] = average(value)

    return new_average


def approved_list(notes: dict[str, list[float]]) -> list:
    return [name for name, note in notes.items() if has_approved(note)]


def disapproved_list(notes: dict[str, list[float]]) -> list:
    return [name for name, note in notes.items() if not has_approved(note)]


def highest_score(notes: dict[str, list[float]]) -> str:
    highest_score = ""
    previous_score = 0.0

    for key, value in notes.items():
        current_average_score = average(value)

        if current_average_score >= previous_score:
            highest_score = key

        previous_score = current_average_score

    return highest_score


def report(notes: dict[str, list[float]]) -> dict[str, list[str] | str | int]:
    return {
        "total_students": len(notes),
        "approved_students": approved_list(notes),
        "approved_disapproved": disapproved_list(notes),
        "best_student": highest_score(notes),
    }


print(report(notes))
