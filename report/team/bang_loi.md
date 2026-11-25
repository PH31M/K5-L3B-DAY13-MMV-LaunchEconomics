# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Tào Quang Vinh (`2A202604081`, nhãn nháp có Claude gợi ý, người gắn nhãn 1 đã review) · Người gắn nhãn 2: Nguyễn Văn Minh (`2A202604117`, gắn độc lập trước khi so nhãn) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca không trùng (đồng thuận 20/20 = 100%, đạt vượt ngưỡng 80%). Ghi chú quy tắc gốc mà hai người cùng áp dụng cho các ca dễ lẫn:
  - **Ca 6, 9 (`Do người dùng`):** nguyên nhân gốc là khách chọn sai mục hoặc nhập sai loại mã; việc trợ lý thiếu gợi ý thuộc phần khắc phục.
  - **Ca 8, 15 (`Hệ thống`, không phải `Ngầm`):** sai đã lộ ra (trích dẫn nhìn thấy được hoặc nhân viên xem lại bắt được); `Ngầm` chỉ dùng khi cả khách lẫn hệ thống không nhận ra cho tới khi kiểm tra mẫu hoặc rà soát chi phí (như ca 5, 12, 17).
  - **Ca 13 (`Giới hạn hệ thống`):** sản phẩm ngoài phạm vi trợ lý thì nguyên nhân gốc là giới hạn hệ thống, kể cả khi cách trả lời chưa rõ ràng.
  - **Ca 18 (`Ngữ cảnh`):** số tiền hoàn đúng thiết kế/chính sách, chỉ giả định khách tự hiểu cách tính là không khớp hoàn cảnh của khách.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (`reason = ma_khong_hop_le`); cảnh báo theo ngày khi vượt **2%** tổng yêu cầu/ngày | Nhận diện định dạng mã sàn TMĐT để ánh xạ sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn kèm ảnh vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ giữa `refund_notification_sent` (`status = da_hoan`) và `refund_ledger_write` (`ket_qua = ok`) cùng `trace_id`; ngưỡng **> 0 ca** kích cảnh báo khẩn | Chỉ gửi thông báo "đã hoàn" khi sổ cái trả `ok` với `idempotency_key`; sau 3 lần lỗi 503 chuyển trạng thái "đang xử lý" và gọi `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` (`reason = thieu_tien`) có số tiền hậu kiểm đúng chính sách; tổng hợp theo tuần, cảnh báo khi **> 1%** số đơn hoàn một phần | Bắt buộc mẫu tin nhắn hoàn tiền ghi rõ công thức tính (ví dụ: `30.000 đ × 50% = 15.000 đ`) kèm điều khoản áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` (`reason = thieu_du_lieu`) tách theo `loai`; tổng hợp theo tuần, rà soát khi vượt **5%** tổng yêu cầu trong phạm vi pilot | Giữ luồng chuyển nhân viên kèm tóm tắt và loại nhóm `quoc_te` khỏi phạm vi pilot (theo A3: 22.515 đ/việc = 1,88× `simulated`, tỉ lệ thành công 27,3%) | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu **100 đơn/tuần** so với bảng giá hiện hành; cảnh báo khi **≥ 1%** đơn lệch tiền hoặc lệch `pricing_table_version` | Tự động xoá bộ nhớ đệm ngay khi cập nhật bảng giá và ghi `pricing_table_version` vào mọi event `agent_run_completed` để đối soát | Kế toán trưởng |
