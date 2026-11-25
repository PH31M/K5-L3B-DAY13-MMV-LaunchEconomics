# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN

**MMV · L3B · Gate 2a** — Phạm vi đề xuất gồm yêu cầu nội địa và hàng nặng tại 12 depot.

| Mục | Kết quả làm căn cứ | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1. Chi phí | 4.472 đ/việc thành công, gấp 16,3 lần tiền token và tool trên mỗi yêu cầu. Thời gian nhân viên chiếm 92,5% tổng chi phí (`simulated`). | Giả lập | PM trợ lý hoàn phí |
| 2. Độ nhạy | Chi phí tăng 51,8% khi số ca làm lại gấp đôi, 40,7% khi tỉ lệ xem lại gấp đôi và 23,1% khi lương tăng 25% (`simulated`). | Giả lập | PM trợ lý hoàn phí |
| 3. Phạm vi | So với 12.000 đ nhân viên tự làm, nội địa tốn 0,22× và hàng nặng 0,69×. Quốc tế tốn 1,88×. Đơn đối tác tốn 0,85× nhưng có điều khoản riêng nên vẫn giao nhân viên (`simulated`). | Giả lập | Giám đốc vận hành |
| 4. Chỉ số | Trong đợt chạy thử, 994/1.200 yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày (82,83%). Nhân viên sửa hoặc bỏ 48/177 gợi ý đã xem (27,12%). Có 51/1.200 yêu cầu mở lại (4,25%). | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5. Lỗi | Hai bộ nhãn trùng 20/20 ca. Bộ thứ nhất có AI gợi ý. Nhóm lập phương án cho 5 loại lỗi, ưu tiên ca 7 báo hoàn khi ghi sổ lỗi và ca 20 hoàn trùng. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6. Pilot | Bốc thăm 20 nhân viên mỗi nhánh theo depot. Với 299 yêu cầu/người, mỗi nhánh đạt 859 yêu cầu hiệu dụng. Mức chênh cần phát hiện là 6 điểm %. Nếu chỉ chênh 5 điểm %, power còn khoảng 64%. Có 4 luật dừng và lịch quyết định ngày 02/02/2027. | Xong, có bằng chứng | Giám đốc vận hành |
| 7. Rủi ro | Xem lại 100% khiến chi phí đạt 0,98–1,03× mức thủ công. Nếu khối lượng giảm một nửa, phần cố định tăng từ 1.185 lên 2.370 đ/việc thành công (`simulated`). | Giả lập | PM trợ lý hoàn phí |

**Điều kiện của pilot**

- **29/11/2026 · Kỹ sư trưởng agent** kiểm tra khóa chống hoàn trùng, chỉ gửi thông báo sau khi ghi sổ thành công và đối soát mỗi giờ.
- **30/11/2026 · Giám đốc vận hành** chốt danh sách 20/20, mức chênh 6 điểm % và ngày phân tích chính.
- **30/11/2026 · PM trợ lý hoàn phí** kiểm tra 12 event có `trace_id` và luồng chuyển nhân viên sau hai lượt lỗi. Hai lượt cho chi phí hệ thống thấp nhất, 6.901.220 đ/1.200 yêu cầu (`simulated`). **08/12/2026 · Trưởng nhóm CSKH** dùng số phút đo được để tính lại chi phí và xét giảm xem lại khi tỉ lệ sửa hoặc bỏ dưới 15% trong một tuần.
- **30/11/2026 · Kế toán trưởng** kiểm tra cách lấy mẫu 100 đơn/tuần, cảnh báo khi ít nhất 1% đơn lệch và kiểm tra phiên bản bảng giá sau mỗi lần cập nhật.

**Đề xuất: Go có điều kiện.**
