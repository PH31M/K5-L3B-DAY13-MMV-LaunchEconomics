# Báo cáo nhóm · Lab 13

## 1. Thông tin nhóm

MMV, lớp L3B. Nhóm gồm Nguyễn Hữu An, Phạm Hoàng Đức Minh, Tào Quang Vinh và Nguyễn Văn Minh.

## 2. Mục tiêu và cách tiếp cận

Nhóm em muốn biết loại yêu cầu hoàn phí nào đáng đưa vào pilot và cần đo gì trước khi mở rộng. Từ 1.200 yêu cầu và 1.624 lượt chạy, nhóm cộng tiền token, tool và thời gian nhân viên cho mọi lượt, kể cả lượt lỗi. Khi tính chi phí mỗi việc thành công, mẫu số là 978 yêu cầu được giải quyết thành công.

## 3. Giải pháp

Nhóm dùng cùng một mô hình để tính chi phí theo loại yêu cầu và thử thay đổi từng giả định. Đức Minh tính lại bằng một chương trình riêng từ hai file CSV. Với 20 ca lỗi, nhóm so hai bộ nhãn và chọn một ca cho mỗi loại để ghi cách phát hiện, cách xử lý và người phụ trách. Kế hoạch pilot chia ngẫu nhiên theo nhân viên trong từng depot và giữ một nhánh đối chứng cùng thời gian. [Bảng chi phí](bang_chi_phi.md) · [Bảng lỗi](bang_loi.md) · [Kế hoạch pilot](pilot_plan.yaml)

## 4. Kết quả

- Toàn mẫu tốn **4.472 đ/việc thành công**. Khi tính cả chi phí nhân viên nhận các ca còn lại, giới hạn hai lượt rẻ nhất cho công ty, **6.901.220 đ trên 1.200 yêu cầu** (`simulated`).
- Trong đợt chạy thử, **82,83%** yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày. Nhân viên sửa hoặc bỏ **48/177** gợi ý đã xem. Có **51/1.200** yêu cầu mở lại. [Chỉ số và cách đo](chi_so.md)
- Nhóm đề xuất **Go có điều kiện** cho nội địa và hàng nặng. Hai loại này lần lượt tốn 0,22× và 0,69× chi phí thủ công (`simulated`). Trước khi mở pilot, nhóm cần chặn hoàn trùng, chốt cỡ mẫu, kiểm tra luồng chuyển nhân viên và chuẩn bị kiểm tra mẫu hằng tuần. [Hồ sơ launch v0](ho_so_launch_v0.md)

## 5. Khó khăn và cách xử lý

Giới hạn một lượt cho chi phí thấp nhất trên mỗi việc thành công nhưng đẩy 319 ca sang nhân viên. Hai lượt giảm còn 234 ca. Vì vậy nhóm lấy chi phí cả hệ thống làm căn cứ chọn giới hạn. Ở phần lỗi, hai bộ nhãn trùng 20/20. Vinh có tham khảo gợi ý của Claude ở bản nháp nên nhóm ghi rõ cách tạo bộ nhãn thứ nhất.

## 6. Tổng hợp đóng góp

An viết mô hình và tính cỡ mẫu. Đức Minh kiểm số độc lập. Vinh điền bảng chi phí A và rà bộ nhãn thứ nhất. Văn Minh gắn bộ nhãn thứ hai, tổng hợp bảng lỗi, chỉ số và hồ sơ launch. [Phân công và minh chứng](../../TEAM.md)

## 7. Hạn chế và hướng cải thiện

Thời gian xem lại và làm lại trong dữ liệu là `simulated`. Nếu phải xem lại 100%, chi phí có thể lên tới 1,03× mức thủ công (`simulated`), nên nhóm sẽ đo số phút thực tế ngay tuần đầu. Với 20 nhân viên mỗi nhánh, pilot cần 299 yêu cầu/người để phát hiện chênh lệch 6 điểm %. Nếu tác động thật chỉ là 5 điểm %, power ước tính còn 64%.

## 8. Tài liệu tham khảo

Nhóm dùng bộ trace LogiX-VN của đề bài, năm loại lỗi Google PAIR và công thức cỡ mẫu hai tỉ lệ trong [hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md). Cách tính các khoản chi phí được ghi trong [tài liệu dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md).
