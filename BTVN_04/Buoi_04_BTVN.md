# Buổi 04 · Hàm, lambda và bảng xếp hạng

**Bối cảnh:** CLB cần chuẩn hóa tên, thống kê điểm và in bảng xếp hạng. Làm cả ba bài trong `buoi_04/main.py`, dùng dữ liệu đặt ngay trong code.

## Chuẩn bị môi trường

Mở terminal tại thư mục `buoi_04`. Bài này không cần cài thêm gói.

| Máy | Tạo môi trường một lần | Chạy bằng Python trong môi trường |
|---|---|---|
| Windows | `py -m venv .venv` | `.venv\Scripts\python.exe main.py` |
| macOS/Linux | `python3 -m venv .venv` | `.venv/bin/python main.py` |

Trong VS Code, chọn Python trong `.venv` qua **Python: Select Interpreter**. Thử thay `main.py` trong lệnh chạy bằng `-m pip --version`; đường dẫn pip in ra nên nằm trong `.venv`. Thêm `.venv/` vào `.gitignore`.

## Bài 1 · Chuẩn hóa tên

Viết `normalize_name(text)` trả một chuỗi mới. Bỏ khoảng trắng hai đầu và gom khoảng trắng giữa các từ thành một dấu cách. Giữ nguyên chữ hoa/thường; hàm không tự in.

| Lời gọi | Giá trị trả về |
|---|---|
| `normalize_name("  Nguyễn   An  ")` | `"Nguyễn An"` |
| `normalize_name("minh")` | `"minh"` |
| `normalize_name("   ")` | `""` |

## Bài 2 · Tính điểm trung bình và số đạt

Viết `average_score(scores)` và `count_passed(scores, threshold=5)`. Danh sách điểm đã là số trong khoảng 0–10. Điểm bằng ngưỡng vẫn đạt; không sửa list đầu vào. Thêm type hint và docstring ngắn cho cả hai hàm. Gọi và in kết quả bên ngoài hàm.

| Đầu vào | Trung bình | Số đạt với ngưỡng mặc định | Số đạt với ngưỡng 8 |
|---|---:|---:|---:|
| `[8, 4, 9, 5]` | 6.5 | 3 | 2 |
| `[5]` | 5.0 | 1 | 0 |
| `[]` | `None` | 0 | 0 |

## Làm quen với lambda trước khi làm bài 3

`lambda tham_so: bieu_thuc` tạo một hàm không tên. Phần sau dấu `:` là **một biểu thức**; giá trị của nó được trả về tự động. Ví dụ `lambda word: len(word)` nhận một từ và trả độ dài, tương đương phần thân `return len(word)` của một hàm viết bằng `def`.

```python
words = ["python", "git", "oop"]
print(sorted(words, key=lambda word: len(word)))
# ['git', 'oop', 'python']
```

`key` nhận một hàm để lấy giá trị dùng khi so sánh. Trong ví dụ này, danh sách kết quả vẫn chứa **từ**, không phải độ dài. Dùng `def` nếu logic cần nhiều bước hoặc hàm cần tái sử dụng ở nhiều nơi.

## Bài 3 · Sắp xếp dict bằng lambda

```python
score_by_name = {"Minh": 9, "Lan": 7, "An": 9, "Vy": 5}
```

Viết `rank_students(score_by_name)` trả một **dict mới có thứ tự duyệt theo xếp hạng**:

1. Điểm cao hơn đứng trước. Nếu bằng điểm, tên đứng trước theo thứ tự A–Z đứng trước. Dữ liệu bài dùng tên không dấu, cùng kiểu viết hoa như ví dụ.
2. Dùng `sorted(..., key=lambda ...)` trên các cặp từ `.items()`, rồi tạo dict từ kết quả. Không thay đổi dict ban đầu.
3. In dict kết quả. Thử thêm dict rỗng; kết quả phải là `{}`.

**Gợi ý:** `score_by_name.items()` cho các cặp như `("Minh", 9)`. Python so sánh tuple lần lượt từ phần tử đầu. Ví dụ khóa `(-9, "An")` đứng trước `(-9, "Minh")` và `(-7, "Lan")`.

**Kết quả để đối chiếu:** `{"An": 9, "Minh": 9, "Lan": 7, "Vy": 5}`. Sau khi gọi hàm, dict ban đầu vẫn bắt đầu bằng khóa `"Minh"`.

**Nộp:** `buoi_04/main.py` chạy được, có lời gọi thử cho cả ba bài. Không nộp thư mục `.venv`.
