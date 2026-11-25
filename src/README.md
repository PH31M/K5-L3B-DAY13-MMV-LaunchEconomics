# Source code

Bài làm và dữ liệu giả lập của Lab 13. **Mọi lệnh Python chạy trong thư mục `src/`.**

- File bắt đầu chạy và nộp: `lab13.py`. Bản gốc để đối chiếu là `lab13_starter.py`.
- Cách chạy: `python3 lab13.py`.
- Input: `logix_runs.csv`, `logix_requests.csv` cùng thư mục, file yêu cầu đọc bằng `pd.read_csv('logix_requests.csv', keep_default_na=False)`.
- Output: in ra stdout ba phép thử A1, các bảng A2, A3, độ nhạy (B) và cỡ mẫu (D1). Nhóm chép số vào các file trong `report/team/`.
- File học viên được sửa: `lab13.py`. Không sửa hai file CSV.

## Cài đặt

Cần Python 3.10 trở lên. Lab không cần khoá API và không cần mạng trong lúc làm.

macOS / Linux:

```bash
cd src
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels, yaml; print('san sang')"
python lab13.py
```

Windows PowerShell:

```powershell
cd src
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels, yaml; print('san sang')"
python lab13.py
```

Lệnh `python -c` kiểm tra thư viện phải in ra `san sang`.

## Chạy CP4

Từ thư mục gốc, vào `src/` và chạy chương trình. CP4 xuất hiện sau bảng B4.
Phần tính D1 dùng `pandas` và thư viện chuẩn Python.

```bash
cd src
python lab13.py
```

Đối chiếu năm dòng D1a–D1e và hai dòng mở lại trong 7 ngày:

- D1a và D1b lần lượt cho **1.251 yêu cầu/nhóm** và **3.103 yêu cầu, 42 nhân viên/nhóm**.
- D1c và D1d cho giới hạn cỡ mẫu hiệu dụng **dưới 1.000** và **dưới 300**.
- D1e cho **299 yêu cầu/nhân viên**, tức **5.980 thực tế** và **859,20 hiệu dụng** mỗi nhóm.
- Tỉ lệ mở lại là **51/1.200 (4,25%)** trên toàn mẫu và **39/982 (3,97%)** trong phạm vi pilot.

Kiểm tra file [pilot_plan.yaml](../report/team/pilot_plan.yaml) từ `src/`. Lệnh dùng PyYAML trong `requirements.txt`.

```bash
python -c "from pathlib import Path; import yaml; text = Path('../report/team/pilot_plan.yaml').read_text(encoding='utf-8'); pilot = yaml.safe_load(text)['pilot']; assert '?' not in text; assert len(pilot['stop_rules']) >= 3; print('CP4: YAML hợp lệ, đủ luật dừng')"
```

## File trong thư mục

| File | Nội dung |
| --- | --- |
| `lab13.py` | Bài làm của nhóm: kiểm tra A1, mô hình chi phí A2–A4, độ nhạy B1–B4 và cỡ mẫu D1 |
| `lab13_starter.py` | Bản gốc của `lab13.py`, giữ nguyên để đối chiếu. Tài liệu trong `docs/` gọi file này là "file khởi đầu" |
| `logix_runs.csv` | 1.624 lần chạy của agent |
| `logix_requests.csv` | 1.200 yêu cầu hoàn phí |
| `requirements.txt` | Thư viện cần cài |

Ý nghĩa từng cột và các công thức: [docs/du_lieu_va_cong_thuc.md](../docs/du_lieu_va_cong_thuc.md).

## Đọc dữ liệu đúng cách

```python
import pandas as pd
runs = pd.read_csv('logix_runs.csv')
reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
```

Thiếu `keep_default_na=False`, ô trống trong cột `quyet_dinh_xem_lai` bị đọc thành `NaN` và các phép so sánh phía sau sai.
