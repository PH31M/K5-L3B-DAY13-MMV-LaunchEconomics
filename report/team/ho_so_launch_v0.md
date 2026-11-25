# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: MMV · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu: **4.472 đ/việc** (`simulated`), gấp **16,3×** hoá đơn token+tool (`274,7 đ/YC`), giờ nhân viên chiếm 92,5% (làm lại 51,8%, xem lại 40,7%). Phạm vi `noi_dia + hang_nang`: `3.414 đ` biến đổi; cộng cố định 40 triệu đ/tháng thành **4.599 đ** (45.000 YC/tháng) hoặc **5.784 đ** (22.500 YC/tháng) (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1) Số ca làm lại ×2: **+51,8%** (`6.787 đ`), 2) Xem lại ×2: **+40,7%** (`6.292 đ`), 3) Lương +25%: **+23,1%** (`5.506 đ`); giá token ×2 chỉ `+5,6%` (`4.723 đ`). Cặp token ×2 + xem lại ×2 = `6.543 đ` (`+46,3%`). Giới hạn **2 lần chạy** rẻ nhất cả hệ thống (`6.901.220 đ` so với 1 lần `7.449.781 đ`, 3 lần `7.037.585 đ`) (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống toàn mẫu (gồm 222 ca làm thay × 12.000 đ): **5.865 đ/YC = 0,49×** (`simulated`). Theo loại: chọn `noi_dia` **0,22×** (95,0%), `hang_nang` **0,69×** (74,1%); loại `quoc_te` **1,88×** (27,3%, ok lượt 3: 2,2%) và `doi_tac` **0,85×** (54,4%). Phạm vi pilot có cố định: **0,38×** (đầy đủ) / **0,48×** (nửa khối lượng). Rủi ro B4 — xem lại 100%: **11.743 đ = 0,98×** (9 phút làm lại) hoặc **12.415 đ = 1,03×** (15,3 phút thực tế dữ liệu) (`simulated`) | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (chưa có đối chứng): chỉ số chính **82,83%** (`994/1.200`), tỉ lệ bỏ qua gợi ý **27,12%** (`48/177`), lỗi lọt mở lại 7 ngày **4,25%** (`51/1.200`; phạm vi pilot **3,97%**). Đề xuất thêm 1 chỉ số dùng (tỉ lệ tiếp nhận gợi ý) & 1 chỉ số an toàn (kiểm tra mẫu 100 đơn/tuần bắt lỗi ngầm); đủ **12 event có `trace_id`** trong `chi_so.md` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn độc lập (Tào Quang Vinh & Nguyễn Văn Minh) đồng thuận **20/20 = 100%** (4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn hệ thống, 3 Ngầm). Đã lập bảng khắc phục 5 ca (Ca `9, 7, 18, 4, 17`) đủ 5 loại có event, ngưỡng, tần suất và 1 vai trò phụ trách trong `bang_loi.md`; chặn lỗi nghiêm trọng ca 7 & 20 trước khi mở pilot | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | *(Chờ CP4 từ `src/lab13.py` & `pilot_plan.yaml`: cách chia cụm, MDE, cỡ mẫu hiệu dụng, đánh đổi power, ≥ 3 luật dừng đủ 4 vế)* | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | 3 rủi ro định lượng trong `chi_so.md`: làm lại ×2 (**+51,8%**, `6.787 đ`), xem lại 100% kéo dài (**0,98×–1,03×**, hoà vốn ≤ 4,8–5,1 phút xem lại), và giảm 50% khối lượng tăng cố định `1.185 → 2.370 đ/việc` (**0,48×**) (`simulated`) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** *(Chờ hoàn tất CP1–CP4 để chốt một trong ba: Go · Go có điều kiện · No-go; nêu rõ cả con số bất lợi và điều kiện + người phụ trách + ngày kiểm tra trước 17:00.)*

- *(Sẽ chốt ngay khi đủ số liệu từ `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`.)*
