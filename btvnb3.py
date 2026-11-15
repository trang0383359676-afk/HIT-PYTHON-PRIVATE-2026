#Bai1
def average_score(scores):
    """Trả về trung bình hoặc None nếu rỗng."""
    if len(scores) == 0:
        return None
    else:
        return sum(scores) / len(scores)
print(average_score([8, 7, 9]))
print(average_score([10]))
print(average_score([]))
#Bai2
def normalize_name(text):
    text = text.strip()
    text = text.split()
    return " ".join(text)
print(normalize_name("   Nguyen   Van An   "))
print(normalize_name("       "))
#Bai3
def count_passed(scores, threshold=5):
    dem = 0

    for score in scores:
        if score >= threshold:
            dem += 1

    return dem
print(count_passed([4, 5, 8]))
print(count_passed([4, 5, 8], 8))
print(count_passed([]))
#Bai4
def calculate(a, b, operation):
    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            return None
        return a / b

    else:
        return None
print(calculate(6, 3, "add"))
print(calculate(6, 3, "subtract"))
print(calculate(6, 3, "multiply"))
print(calculate(6, 3, "divide"))

print(calculate(6, 0, "divide"))
print(calculate(6, 3, "hello"))
