# Báo cáo cá nhân — Tào Quang Vinh - 2A202604081

## 1. Thông tin thành viên

- Họ tên: Tào Quang Vinh
- MSSV: 2A202604081
- Email: qvinhh2312@gmail.com
- Vai trong nhóm: người gắn nhãn 1

## 2. Phần việc phụ trách

- Đọc đề, theo dõi điều kiện "Xong khi" của từng checkpoint và đối chiếu số của nhóm với số đáp án (lệch tối đa 2%).
- CP3: gắn nhãn 20 ca lỗi theo năm loại của Google PAIR, so nhãn với người gắn nhãn 2, ghi quy tắc cho các ca dễ lẫn và điền bảng khắc phục 5 ca trong `report/team/bang_loi.md`.

## 3. Đóng góp cụ thể

- CP1: chạy lại `src/lab13.py` của người viết code, đối chiếu từng số với đáp án: ba phép thử A1 ĐẠT; token 245.585 đ, tool 84.000 đ, tổng 4.373.585 đ, 978 việc thành công, 4.472 đ mỗi việc thành công [simulated]; A3 bốn loại; A4 4.599 đ (0,38×) và 5.784 đ (0,48×) [simulated]. Tất cả khớp, không phát hiện lệch.
- CP1: điền A1–A4 vào `report/team/bang_chi_phi.md`, ghi nhãn `simulated` ở mọi số tính từ hai cột `_simulated`.
- CP2: đối chiếu B1–B4: 9 dòng độ nhạy khớp, kiểm tra "giảm một nửa = nửa mức gấp đôi" đạt, B3 (giới hạn 2 lần rẻ nhất cho cả hệ thống, 6.901.220 đ [simulated]), B4 (11.743 đ = 0,98× và 12.415 đ = 1,03× [simulated]). Chênh 1 đ ở B4 so với hướng dẫn (12.414 đ), nằm trong sai số 2%.
- CP3: gắn nhãn nháp 20 ca (4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn hệ thống, 3 Ngầm), review từng ca, rồi so với người gắn nhãn 2: đồng thuận 20/20 = 100%, không có ca không trùng.
- Bóc tách chi phí một lần chạy để hiểu số: trung bình 202,95 đ mỗi lần chạy (token vào 92,40 đ, token ra 58,82 đ, tool 51,72 đ); tiền máy chỉ chiếm 7,5% tổng chi phí, giờ nhân viên [simulated] chiếm 92,5%.

## 4. Bằng chứng

- Commit: `7e5c042` (báo cáo cá nhân), `489bfc1` (điền A1–A4 vào `bang_chi_phi.md`), cùng các commit của nhóm cập nhật `bang_loi.md`.
- File: `report/team/bang_loi.md` (hai bộ nhãn, tỉ lệ đồng thuận 20/20), `report/team/bang_chi_phi.md` (bảng A1–A4).
- Lệnh tự chạy: `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` và các bảng A, B.

## 5. Công cụ AI đã dùng

- Claude Code: đọc đề bài, tóm tắt checklist theo từng checkpoint, giải thích khái niệm (chi phí mỗi việc thành công, cộng tuyến tính, bốn câu hỏi phân loại lỗi)

- Chạy lại `python lab13.py` trên máy mình và đối chiếu mọi số với đáp án trong hướng dẫn và slide chữa (lệch tối đa 2%); kiểm tra ghi nhãn `simulated` ở mọi số có cột `_simulated`; tính lại tổng chi phí từ từng thành phần nhỏ (token vào, token ra, tool, xem lại, làm lại).

## 6. Tự đánh giá

- Làm tốt: theo sát điều kiện "Xong khi" của CP1 và CP2, đối chiếu số kịp thời; hiểu được vì sao chi phí mỗi việc thành công gấp 16,3 lần hoá đơn token (giờ nhân viên chiếm 92,5%).
- Cần cải thiện: nhãn 20 ca lỗi chưa thật sự gắn độc lập mà có tham khảo AI
- Chưa làm được: chưa đo bằng dữ liệu thật; mọi số xem lại và làm lại là `simulated`, nên kết luận chỉ đúng trong giả định của lab.
