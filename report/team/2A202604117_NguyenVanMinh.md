# Báo cáo cá nhân — NguyenVanMinh-2A202604117

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Minh
- MSSV: 2A202604117
- Email: vm140205@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi (Nhiệm vụ C, CP3) theo 5 loại của Google PAIR, sau đó đối chiếu với Người gắn nhãn 1 (Tào Quang Vinh) để tính tỉ lệ đồng thuận, thống nhất quy tắc phân biệt và hoàn thiện bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Giữ và cập nhật xuyên suốt hồ sơ một trang `report/team/ho_so_launch_v0.md` từ đầu buổi tới mốc 17:00 duyệt chéo Gate 2a, kiểm tra tuân thủ 5 quy tắc lab (nhãn `simulated`, không dùng từ cấm, người phụ trách là một vai trò cụ thể).
- Phối hợp xây dựng đặc tả chỉ số tự đề xuất, danh sách event có `trace_id` và khung rủi ro kinh tế trong `report/team/chi_so.md`.
- *(Cập nhật thêm nếu luân phiên vai viết code ở CP4 sau giờ giải lao và tham gia duyệt chéo `phieu_cham.md`.)*

## 3. Đóng góp cụ thể

- Hoàn thành gắn nhãn độc lập toàn bộ 20 ca lỗi theo nguyên nhân gốc (Google PAIR), đối chiếu với Người gắn nhãn 1 (Tào Quang Vinh) đạt đồng thuận **20/20 = 100%**, chốt quy tắc phân biệt các ca dễ lẫn và hoàn thiện bảng khắc phục 5 ca (Ca `9, 7, 18, 4, 17`) trong `report/team/bang_loi.md`.
- Hoàn thiện `report/team/chi_so.md`: điền 3 chỉ số tính thử E1 theo `src/kiem_so.py`, đề xuất 2 chỉ số bổ sung (1 chỉ số dùng, 1 chỉ số an toàn cho lỗi ngầm), xây dựng 12 event có `trace_id` kèm kiểm tra chéo ánh xạ chỉ số → event và 3 dòng rủi ro kinh tế E2 lấy số từ A4, B1, B4 (`simulated`).
- Dựng và hoàn thiện đủ **7/7 mục** cùng đề xuất **Go có điều kiện** (4 điều kiện gắn người phụ trách và ngày kiểm tra, nêu rõ các con số bất lợi như power ~64% ở mức 5 điểm % và B4 xem lại 100% tốn 0,98×–1,03× `simulated`) trong `report/team/ho_so_launch_v0.md` sẵn sàng cho mốc 17:00 duyệt chéo Gate 2a.
- *(Chờ cập nhật tiếp sau khi hoàn tất duyệt chéo Gate 2a `phieu_cham.md` và `group_report.md`.)*

## 4. Bằng chứng

- `report/team/bang_loi.md` (hai bộ nhãn độc lập đồng thuận 20/20 = 100%, quy tắc phân biệt và bảng khắc phục 5 loại lỗi).
- `report/team/chi_so.md` (E1 đủ 5 chỉ số, 12 event có `trace_id`, kiểm tra chéo và 3 dòng rủi ro kinh tế E2).
- `report/team/ho_so_launch_v0.md` (hoàn chỉnh 7/7 mục và đề xuất Go có điều kiện sẵn sàng duyệt chéo Gate 2a).
- Các commit đã push (`b340480`, `c2f7dbc` và commit chốt hồ sơ).

## 5. Công cụ AI đã dùng

- Công cụ: Antigravity (Gemini) để rà soát yêu cầu trong `README.md`, `RULES.md`, `RUBRIC.md`, `SUBMISSION.md`, kiểm tra chéo nhất quán giữa event trong `chi_so.md` và cách phát hiện lỗi trong `bang_loi.md`, và chạy script tự kiểm tra ràng buộc nộp bài.
- Cách tự kiểm tra: đọc trực tiếp 20 mô tả ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và tự đối chiếu từng ca với câu hỏi nhận diện nguyên nhân gốc của Google PAIR; kiểm tra bằng lệnh tự động rằng không có từ cấm, mỗi người phụ trách đều là một vai trò cụ thể, mọi event đều có `trace_id`, và không bịa bất kỳ con số nào phụ thuộc vào code của thành viên khác.

## 6. Tự đánh giá

- Điểm làm tốt: tách bạch rõ phần việc độc lập (làm trước ngay) và phần phụ thuộc dây chuyền (đợi số liệu từ `src/lab13.py` và bộ nhãn độc lập của Người gắn nhãn 1) để đảm bảo đúng quy định liêm chính và không xung đột merge.
- Phần cần hoàn thiện tiếp: đối chiếu nhãn độc lập với Tào Quang Vinh ở CP3, ghép đầy đủ số liệu verified từ An & Đức Minh vào `chi_so.md` và `ho_so_launch_v0.md`, và hoàn tất duyệt chéo Gate 2a trước 17:45.
