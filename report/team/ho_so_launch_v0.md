# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm MMV · Lớp L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ/việc**, gấp 16,3× hóa đơn token và tool (`simulated`). | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2 **+51,8%**, xem lại ×2 **+40,7%**, lương +25% **+23,1%** (`simulated`). | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống **5.865 đ/yêu cầu (0,49×)**. Chọn `noi_dia` (0,22×) và `hang_nang` (0,69×), giữ `quoc_te` (1,88×) và `doi_tac` (0,85×, điều khoản riêng) ở luồng thủ công. Có phí cố định, phạm vi pilot ở mức **0,38×–0,48×** tại 45.000–22.500 yêu cầu/tháng (`simulated`). | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, dùng, an toàn | Trong đợt chạy thử, đóng đúng hạn và không mở lại **82,83%**, sửa/bỏ gợi ý **27,12%**, mở lại **4,25%** (trong phạm vi **3,97%**). [Đặc tả 12 event](chi_so.md). | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và khắc phục | Hai bộ nhãn trùng **20/20**, bộ thứ nhất có tham khảo Claude. [Bảng khắc phục 5 ca](bang_loi.md) có ngưỡng và vai trò phụ trách. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | **20/20 nhân viên**, phân tầng 12 depot, seed 13. MDE **6 điểm %**, cần **299 yêu cầu/người** (859 hiệu dụng/nhánh, DE 6,96). Power khoảng **64%** ở mức 5 điểm %. [Bốn luật dừng và rollback 30 phút](pilot_plan.yaml). Quyết định **2027-02-02**. | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Xem lại 100% tốn **0,98×–1,03×** mức thủ công. Nửa khối lượng làm phí cố định mỗi việc tăng từ **1.185 lên 2.370 đ** (`simulated`). | Giả lập | PM trợ lý hoàn phí |

**Điều kiện mở pilot**

1. **Kỹ sư trưởng agent · 2026-11-29** — Chặn hoàn trùng bằng `idempotency_key`, chỉ báo đã hoàn khi sổ cái trả `ok`, đối soát mỗi giờ và cảnh báo khi có sai lệch (ca 7, 20).
2. **Giám đốc vận hành · 2026-11-30** — Chấp nhận MDE 6 điểm %, khóa phân nhóm 20/20 và chỉ kiểm định chỉ số chính một lần vào ngày quyết định.
3. **PM trợ lý hoàn phí · 2026-11-30** — Bật 12 event có `trace_id`, kiểm tra chuyển nhân viên khi cả **2 lượt chạy** đều lỗi, tính cả lượt đầu và áp dụng từ rollout 10%. B3 ước tính **6.901.220 đ/1.200 yêu cầu** (`simulated`). Sau tuần 1, cập nhật chi phí bằng số phút đo được. **Trưởng nhóm CSKH · 2026-12-08** — Kiểm tra lộ trình giảm xem lại khi tỷ lệ sửa/bỏ dưới 15%.
4. **Kế toán trưởng · 2026-11-30** — Kiểm tra mẫu 100 đơn/tuần, cảnh báo khi lệch từ 1%, xóa cache lúc cập nhật bảng giá và ghi phiên bản vào trace.

**Đề xuất — Go có điều kiện** cho `noi_dia` và `hang_nang` tại 12 depot.
