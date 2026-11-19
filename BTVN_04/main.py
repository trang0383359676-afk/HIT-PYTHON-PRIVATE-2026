#bai1
def normalize_name(text):
    return " ".join(text.split());
print(normalize_name("   Nguyễn     An   "))
print(normalize_name("minh"))
print(normalize_name("     "))
#bai2
def average_score(scores: list[float]) -> float | None:
    if len(scores) == 0:
        return None

    return sum(scores) / len(scores)
def count_passed(scores: list[float], threshold: float = 5) -> int:
    count = 0

    for score in scores:
        if score >= threshold:
            count += 1

    return count
scores = [8, 4, 9, 5]

print("Điểm trung bình:", average_score(scores))
print("Số đạt (ngưỡng 5):", count_passed(scores))
print("Số đạt (ngưỡng 8):", count_passed(scores, 8))
#bai3

def rank_students(score_by_name: dict[str, int]) -> dict[str, int]:
    sorted_items = sorted(
        score_by_name.items(),
        key=lambda item: (-item[1], item[0])
    )

    return dict(sorted_items)

score_by_name = {"Minh": 9, "Lan": 7, "An": 9, "Vy": 5}

result = rank_students(score_by_name)

print(result)
print(rank_students({}))
