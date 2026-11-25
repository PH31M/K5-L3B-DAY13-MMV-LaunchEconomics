# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Trong đợt chạy thử là **82,83%** (`994/1.200`) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Trong đợt chạy thử là **27,12%** (`48/177`) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Trong đợt chạy thử là **4,25%** (`51/1.200`; trong phạm vi `noi_dia + hang_nang`: **3,97%**, `39/982`) |
| Dùng | Tỉ lệ tiếp nhận gợi ý trong nhóm can thiệp (nhóm tự đề xuất) | Số yêu cầu thuộc nhóm can thiệp có `agent_suggestion_shown`, chia tổng số yêu cầu trong phạm vi của nhóm can thiệp | Không cần tính |
| An toàn | Tỉ lệ hoàn sai tiền qua kiểm tra mẫu hằng tuần (nhóm tự đề xuất, bắt lỗi ngầm) | Số đơn có `so_tien_da_hoan != so_tien_dung` trong `audit_sample_checked`, chia tổng số đơn kiểm tra mẫu (100 đơn/tuần) | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Ứng dụng khách hàng | `request_id, depot, loai, so_tien_vnd, arm, trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `input_validation_failed` | Cổng tiếp nhận / Agent | `request_id, reason, trace_id` | Khi đầu vào của khách sai định dạng (mã vận đơn, STK) |
| `agent_run_completed` | Trợ lý hoàn phí (Agent) | `run_id, attempt, tokens_in, tokens_out, tool_calls, status, pricing_table_version, trace_id` | Sau mỗi lần chạy của agent, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `staff_id, so_tien_de_xuat, trace_id` | Khi gợi ý của trợ lý hiện trên màn hình nhân viên |
| `staff_review_decision` | Giao diện CSKH (Nhân viên) | `staff_id, quyet_dinh (giu/sua/bo), phut_xem_lai_thuc, trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Giao diện CSKH (Nhân viên) | `staff_id, phut_lam_lai_thuc, ly_do, trace_id` | Khi nhân viên hoàn tất làm lại yêu cầu sai |
| `refund_ledger_write` | Dịch vụ sổ cái hoàn tiền | `idempotency_key, so_tien_hoan, ket_qua (ok/loi), trace_id` | Khi ghi lệnh hoàn tiền xuống sổ cái |
| `refund_notification_sent` | Dịch vụ thông báo | `channel, status, so_tien_thong_bao, trace_id` | Khi gửi thông báo kết quả hoàn tiền cho khách |
| `handoff_to_staff` | Trợ lý hoàn phí (Agent) | `reason, loai, tom_tat, trace_id` | Khi trợ lý chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at, trong_24h, trace_id` | Khi yêu cầu được đóng |
| `ticket_reopened` | Hệ thống ticket (Khách) | `reopened_at, trong_7_ngay, reason, trace_id` | Khi khách mở lại yêu cầu sau khi đóng |
| `audit_sample_checked` | Hệ thống kế toán | `so_tien_da_hoan, so_tien_dung, pricing_table_version, trace_id` | Khi kế toán hoàn tất kiểm tra mẫu 100 đơn/tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **% yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày (Chính):** tính từ `refund_request_created` + `ticket_closed` (`trong_24h = 1`) + `ticket_reopened` (không có event với `trong_7_ngay = 1`), nối qua `trace_id` và tách theo `arm`.
- **Tỉ lệ bỏ qua gợi ý (Dùng):** tính từ `staff_review_decision` (`quyet_dinh ∈ {sua, bo}` chia tổng số `staff_review_decision`), nối `trace_id`.
- **Tỉ lệ lỗi lọt đến khách (An toàn):** tính từ `ticket_reopened` (`trong_7_ngay = 1`) chia tổng `refund_request_created`, nối `trace_id`.
- **Tỉ lệ tiếp nhận gợi ý trong nhóm can thiệp (Dùng — tự đề xuất):** tính từ `agent_suggestion_shown` chia tổng `refund_request_created` có `arm = treatment` và thuộc phạm vi pilot, nối `trace_id`.
- **Tỉ lệ hoàn sai tiền qua kiểm tra mẫu hằng tuần (An toàn — tự đề xuất):** tính từ `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung` chia tổng số bản ghi kiểm tra mẫu), nối `trace_id` với `agent_run_completed` (`pricing_table_version`).
- **Chi phí thật thay thế cho phần `simulated`:** tính từ `agent_run_completed` (`tokens_in`, `tokens_out`, `tool_calls`) + `staff_review_decision` (`phut_xem_lai_thuc`) + `staff_rework_completed` (`phut_lam_lai_thuc`).

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | **+51,8%**, chi phí tăng từ 4.472 đ lên **6.787 đ/việc thành công** (`simulated`, theo B1) | Tỉ lệ ca làm lại theo tuần > 7% (đợt chạy thử trong phạm vi `noi_dia + hang_nang`: 48/982 = 4,9%, theo `staff_rework_completed`) | Thu hẹp phạm vi về `noi_dia` và rà soát 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài | **11.743 đ = 0,98×** (làm lại 9 phút/ca, hoà vốn ≤ 5,1 phút xem lại) hoặc **12.415 đ = 1,03×** (làm lại 15,3 phút/ca như dữ liệu, hoà vốn ≤ 4,8 phút) (`simulated`, theo B4) | Tỉ lệ yêu cầu có `staff_review_decision` còn > 50% cuối bước rollout 0,25 hoặc thời gian xem lại trung bình > 4,8 phút/yêu cầu | Áp lộ trình giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% trong 1 tuần liên tiếp | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thấp hơn dự kiến làm đội chi phí cố định | Cố định 40 triệu đ/tháng: +1.185 đ/việc (**4.599 đ = 0,38×**) ở 45.000 YC/tháng; tăng lên +2.370 đ/việc (**5.784 đ = 0,48×**) nếu khối lượng giảm một nửa còn 22.500 YC/tháng (`simulated`, theo A4) | Số việc thành công theo tuần < 50% kế hoạch trong 2 tuần liên tiếp | Không mở rộng bước rollout tiếp theo; rà lại định mức chi phí cố định vận hành | Giám đốc vận hành LogiX-VN |
