# Báo cáo cá nhân — Nguyễn Hữu An

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hữu An
- MSSV: 2A202604024
- Email: 26ai.annh2@vinuni.edu.vn
- Nhóm và lớp: MMV, L3B
- Vai trong nhóm: Người viết code

## 2. Phần việc phụ trách

Em phụ trách viết và chạy `src/lab13.py` cho CP1, CP2 và CP4. Em cũng phân vai trong nhóm và viết hướng dẫn chạy, kiểm tra kế hoạch pilot.

## 3. Đóng góp cụ thể

- **CP1:** Em viết ba phép tính A1 và mô hình chi phí A2–A4. Khi tính chi phí mỗi việc thành công, em cộng chi phí của mọi lượt chạy, kể cả lượt lỗi, rồi chia cho 978 yêu cầu thành công. Kết quả toàn mẫu là **4.472 đ/việc** (`simulated`).
- **CP2:** Em dùng lại mô hình để tính B1–B4. Nếu dừng sau một lượt, nhân viên phải nhận 319 yêu cầu. Cho phép lượt thứ hai giảm số này xuống 234. Giới hạn **2 lượt** cho chi phí cả hệ thống thấp nhất, **6.901.220 đ** trên mẫu 1.200 yêu cầu (`simulated`).
- **CP4:** Em tính cỡ mẫu và tỷ lệ mở lại, rồi điền kế hoạch pilot có đối chứng và 4 luật dừng. Với **20 nhân viên mỗi nhánh** và **299 yêu cầu mỗi người**, 5.980 yêu cầu thực tế mỗi nhánh tương đương khoảng **859 yêu cầu hiệu dụng** sau khi chia cho hệ số thiết kế 6,96.

## 4. Bằng chứng

- CP1 và điều chỉnh kiểm tra A1: `f683490`, `2dbac0e`. CP2: `4a36191`. Cả hai phần nằm trong [lab13.py](../../src/lab13.py).
- CP4: `536d673`, gồm [kế hoạch pilot](pilot_plan.yaml) và [hướng dẫn chạy](../../src/README.md#chạy-cp4). Phân vai: `6233c6f` trong [TEAM.md](../../TEAM.md).

## 5. Công cụ AI đã dùng

- Em dùng Codex để rà yêu cầu, đối chiếu minh chứng trong Git và hỗ trợ soạn báo cáo.
- Em kiểm tra số liệu bằng kết quả chạy `lab13.py` và đối chiếu A2, B3, D1e với script kiểm số độc lập `kiem_so.py`. Ba phép thử A1 đạt **1,20 · 1,25 · 1,25**. Em kiểm tra thêm `pilot_plan.yaml` bằng `yaml.safe_load`.

## 6. Tự đánh giá

Em tái sử dụng được mô hình chi phí từ CP1 để so các kịch bản CP2 trên cùng dữ liệu. Em cần chú ý hơn đến khả năng đạt cỡ mẫu của từng nhân viên, vì với cách chia đã chọn, nếu chênh lệch thật chỉ là **5 điểm phần trăm** thì power ước tính còn khoảng **64%**.
