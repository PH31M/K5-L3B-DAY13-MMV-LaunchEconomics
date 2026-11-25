# Báo cáo cá nhân — Nguyễn Hữu An

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hữu An
- MSSV: 2A202604024
- Email: 26ai.annh2@vinuni.edu.vn
- Nhóm và lớp: MMV, L3B
- Vai trong nhóm: Người viết code

## 2. Phần việc phụ trách

Em phụ trách phần code CP1, CP2 và CP4, phân vai nhóm và viết hướng dẫn chạy pilot.

## 3. Đóng góp cụ thể

- **CP1:** Em cộng chi phí của mọi lượt chạy, kể cả lượt lỗi, cùng chi phí xem lại và làm lại. Chia tổng cho 978 yêu cầu thành công được **4.472 đ/việc** (`simulated`).
- **CP2:** Em dùng lại mô hình CP1 để so các kịch bản B1–B4. Giới hạn **2 lượt** cho chi phí cả hệ thống thấp nhất, khoảng **6,90 triệu đ** trên 1.200 yêu cầu (`simulated`).
- **CP4:** Em tính cỡ mẫu, tỷ lệ mở lại và viết kế hoạch có đối chứng với 4 luật dừng. Với **20 nhân viên mỗi nhánh**, 299 yêu cầu mỗi người cho khoảng **859 yêu cầu hiệu dụng mỗi nhánh**.

## 4. Bằng chứng

- [Mã CP1–CP2](../../src/lab13.py) (`f683490`, `2dbac0e`, `4a36191`).
- [Kế hoạch pilot](pilot_plan.yaml) và [cách chạy CP4](../../src/README.md#chạy-cp4) (`536d673`, `eaf3da5`).

## 5. Công cụ AI đã dùng

Em dùng Codex để rà đề và soát báo cáo. Em chạy lại A1, đối chiếu A2, B3 và D1e với `kiem_so.py`, rồi kiểm tra file pilot bằng `yaml.safe_load`.

## 6. Tự đánh giá

Qua B3, em thấy giới hạn 1 lượt cho chi phí mỗi việc thành công thấp nhất, còn 2 lượt cho tổng chi phí thấp nhất khi tính cả phần nhân viên làm thay. Khi lập pilot, em cần kiểm tra lượng yêu cầu đến từng nhân viên sớm hơn. Nếu hiệu ứng thật là **5 điểm phần trăm**, power ước tính chỉ khoảng **64%**.
