# Báo cáo cá nhân — Phạm Hoàng Đức Minh · 2A202604114

## 1. Thông tin thành viên

- Họ tên: Phạm Hoàng Đức Minh
- MSSV: 2A202604114
- Email: ducminh03102005@gmail.com
- Vai trong nhóm: người kiểm số

## 2. Phần việc phụ trách

Người kiểm số: tính lại độc lập các con số của nhiệm vụ A và B để đối chiếu với `src/lab13.py`, điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4), và kiểm trước các số của D1 và E1 mà hồ sơ sau này dùng lại.

## 3. Đóng góp cụ thể

- A1: tính tay ba phép thử (p = 0,8): 1,20 · 1,25 · 1,25.
- A2–A4: tính lại từ hai file CSV gốc bằng script độc lập `src/kiem_so.py` (chỉ dùng thư viện chuẩn của Python, không gọi hàm của `lab13.py`). Kết quả: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); khoản lớn nhất là làm lại, 51,8% [simulated]. Chi phí cả hệ thống mỗi yêu cầu là 5.865 đ = 0,49× của 12.000 đ [simulated].
- B1–B4: 9 kịch bản độ nhạy; cặp token ×2 + xem lại ×2 (+46,3%); bảng giới hạn chạy lại (2 lần rẻ nhất cả hệ thống: 6.901.220 đ [simulated]; 1 lần có chi phí mỗi việc thành công thấp nhất: 4.111 đ [simulated]); B4 xem lại 100% (11.743 đ = 0,98×, hoặc ≈ 12.415 đ = 1,03× nếu dùng phút làm lại thật 15,3 phút; hoà vốn ở 5,1 và 4,8 phút xem lại) [simulated].
- Kiểm tra chéo: mỗi kịch bản "giảm một nửa" bằng nửa mức tăng của "gấp đôi"; tổng hai tác động riêng bằng tác động của cặp.
- Kiểm trước số cho các nhiệm vụ sau: D1 (1.251 · 3.103 · 1.000 · 300 · m ≥ 299) và E1 (82,83% = 994/1.200; 27,12% = 48/177; 4,25% = 51/1.200).
- Một điểm khác với tài liệu hướng dẫn: ở B4 với phút làm lại 15,3, số của tôi là 12.415 đ (hướng dẫn ghi 12.414 đ), chênh vì cách làm tròn, không đáng kể.

## 4. Bằng chứng

- `report/team/bang_chi_phi.md`: bảng A1–A4 và B1–B4 đã điền, mọi số tính từ cột `_simulated` có nhãn `simulated`.
- `src/kiem_so.py`: script kiểm số độc lập, in ra toàn bộ số ở trên. Chạy trong `src/`: `python3 -I kiem_so.py`.
- Đối chiếu với `src/lab13.py` của người viết code (commit `4a36191`): `python3 lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`; các bảng A2, A3, A4, B1, B2, B3 và B4 in ra trùng với số trong `bang_chi_phi.md` (B4: 11.743 đ và 12.415 đ; hoà vốn 5,1 và 4,8 phút).
- Commit: `e26a9ea` ("B1-B4"), đã push và merge vào `main` ở `7459cf9`.

## 5. Công cụ AI đã dùng

- Claude Code (model Claude Sonnet 5.5): đọc repo và tài liệu để xác định vai người kiểm số; viết script kiểm số độc lập và soạn nội dung bảng trong `bang_chi_phi.md` từ kết quả script; hỗ trợ soạn báo cáo này.
- Cách tự kiểm tra: tính tay A1 trước khi nhìn kết quả script; so từng số của script với bảng đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 2%); chạy kiểm tra nhất quán (nửa mức tăng, tổng hai tác động riêng); tự đếm lại các số 994 và 51 từ CSV; so với output của `lab13.py`. Các câu trả lời có số đều lấy từ output của script, không lấy từ trí nhớ của AI.

## 6. Tự đánh giá

Tôi đã tính lại độc lập và điền đủ bảng A1–A4, B1–B4. Số khớp đáp án trong dung sai 2% và khớp output của `lab13.py`. Số D1 và E1 tôi đã tính trước bằng `src/kiem_so.py`.
