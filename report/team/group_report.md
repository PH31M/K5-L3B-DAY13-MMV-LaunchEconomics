# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: MMV
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm dựng bộ hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN (12 depot, khoảng 40 nhân viên CSKH, khoảng 45.000 yêu cầu mỗi tháng) để hội đồng Gate 2a quyết định có cho chạy pilot hay không. Bộ hồ sơ trả lời bốn câu hỏi: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, và pilot thiết kế thế nào để ra được quyết định.

Cách tiếp cận: mọi con số đều tính từ `src/lab13.py` trên mẫu 1.200 yêu cầu (1.624 lần chạy của agent). Các số dựa trên hai cột `_simulated` ghi nhãn `simulated`. Chi phí mỗi việc thành công lấy tử số là mọi lần chạy (kể cả lần lỗi) cộng giờ nhân viên xem lại và làm lại; mẫu số chỉ đếm yêu cầu có `ket_qua` là `thanh_cong`. Trước khi làm tiếp, nhóm bắt buộc qua ba phép thử A1 (1,20 · 1,25 · 1,25).

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A · Chi phí mỗi việc thành công | Hàm `mo_hinh` tính từ trace; tách theo 4 loại yêu cầu; cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` | `src/lab13.py`, `report/team/bang_chi_phi.md` |
| B · Bảng độ nhạy | Gọi lại `mo_hinh` cho 9 kịch bản, một cặp kịch bản, ba giới hạn số lần chạy và kịch bản xem lại 100% | `report/team/bang_chi_phi.md` |
| C · Bảng lỗi | So hai bộ nhãn của 20 ca theo 5 loại của Google PAIR. Bộ nhãn thứ nhất có tham khảo Claude. Nhóm lập bảng khắc phục 5 ca đủ 5 loại. | `report/team/bang_loi.md` |
| D · Kế hoạch pilot | Tính cỡ mẫu theo yêu cầu, nhân viên, depot; chọn chia theo nhân viên 20 + 20, viết bốn luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ | `report/team/pilot_plan.yaml` |
| E · Chỉ số, rủi ro, hồ sơ | Đặc tả ba chỉ số, danh sách event có `trace_id`, rủi ro kinh tế lấy số từ bảng độ nhạy, hồ sơ launch một trang bảy mục | `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md` |

## 4. Kết quả

Số chính (từ `ho_so_launch_v0.md`):

- Chi phí mỗi việc thành công: **4.472 đ** [simulated], gấp **16,3 lần** hoá đơn token và tool chia số yêu cầu (274,7 đ). Giờ nhân viên chiếm 92,5% tổng chi phí (làm lại 51,8%, xem lại 40,7%) [simulated]. Một lần chạy của agent chỉ tốn khoảng 203 đ, nên tiền máy chỉ là phần nhỏ.
- So với nhân viên tự làm (12.000 đ): cả hệ thống 5.865 đ mỗi yêu cầu = **0,49×** [simulated]. Theo loại: `noi_dia` 0,22×, `hang_nang` 0,69×, `doi_tac` 0,85×, `quoc_te` **1,88×** (thành công 27,3%, chạy lại không giúp: 30,0% → 11,4% → 2,2%) [simulated]. Phạm vi pilot cộng chi phí cố định: 0,38× (45.000 yêu cầu/tháng) và 0,48× (một nửa khối lượng) [simulated].
- Ba yếu tố nhạy nhất: số ca làm lại gấp đôi **+51,8%**, xem lại gấp đôi **+40,7%**, lương tăng 25% **+23,1%** [simulated]. Giá token gấp đôi chỉ +5,6%. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ) dù giới hạn 1 lần cho chi phí mỗi việc thấp nhất (4.111 đ) [simulated].
- Xem lại 100% trong phạm vi pilot: 11.743 đ (0,98×) với 9 phút làm lại, hoặc 12.415 đ (1,03×) với trung bình giả lập 15,3 phút/ca [simulated]. Hoà vốn khi mỗi lần xem lại không quá 4,8–5,1 phút.
- Chỉ số trong đợt chạy thử (không có đối chứng): chính 82,83% (994/1.200), tỉ lệ bỏ qua gợi ý 27,12% (48/177), mở lại trong 7 ngày 4,25% (51/1.200).
- Bảng lỗi: đồng thuận **20/20 = 100%** giữa hai người gắn nhãn; bảng khắc phục 5 ca (9, 7, 18, 4, 17) đủ 5 loại, mỗi dòng có event, ngưỡng và một vai trò phụ trách.
- Pilot: chia theo nhân viên 20 + 20, phân tầng theo depot, seed 13; chấp nhận mức chênh 6 điểm với 859 yêu cầu hiệu dụng mỗi nhóm (hệ số thiết kế 6,96); quyết định ngày 2027-02-02.

**Đề xuất cuối: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, với bốn điều kiện có người phụ trách và ngày kiểm tra (sửa khoá chống trùng và đối soát sổ cái ca 7, 20; ký chấp nhận mức chênh 6 điểm; bật event có `trace_id` và giới hạn 2 lần chạy; kiểm tra mẫu 100 đơn mỗi tuần cho lỗi ngầm).

Theo xác nhận của lab coach, phần kết quả duyệt chéo Gate 2a được miễn điền.

## 5. Khó khăn và cách xử lý

- Phép thử A1 ban đầu chưa qua vì điều kiện kiểm tra `k` bị sai; người viết code sửa lại điều kiện (commit "Sửa điều kiện kiểm tra k ở A1") rồi mới làm tiếp A2.
- Chi phí 4.472 đ chưa tính phần nhân viên làm thay 222 ca chuyển hoặc làm lại; nhóm bổ sung chi phí cả hệ thống (5.865 đ mỗi yêu cầu) để so sánh công bằng với 12.000 đ.
- Không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm với 40 nhân viên (chia theo nhân viên tối đa 1.000 hiệu dụng so với 1.251 cần có). Nhóm chấp nhận mức chênh 6 điểm và ghi rõ con số bất lợi (power khoảng 64% nếu tác động thật là 5 điểm).
- Nhiều người cùng sửa các file trong `report/team/` nên có lúc nhánh `main` bị lệch (diverged); nhóm dùng `git pull --rebase origin main` trước mỗi lần push, không dùng force-push.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` và báo cáo cá nhân trong `report/team/`.

## 7. Hạn chế và hướng cải thiện

- Mọi số xem lại và làm lại là `simulated`; pilot phải thay bằng phút đo thật (event `staff_review_decision`, `staff_rework_completed`) sau tuần 1.
- Đợt chạy thử không có nhóm đối chứng nên chỉ được viết "chỉ số trong đợt chạy thử là…", không viết "trợ lý đã nâng chỉ số".
- Power khoảng 64% nếu tác động thật chỉ 5 điểm; cần mở rộng số nhân viên hoặc số yêu cầu mỗi người nếu muốn thấy mức chênh nhỏ hơn.
- Tỉ lệ mở lại 7 ngày là 4,25% ở toàn mẫu nên ngưỡng an toàn tuyệt đối 3% sẽ dừng pilot ngay tuần đầu; nhóm dùng chênh lệch +2 điểm so với đối chứng kèm trần 6%.
- Mẫu chỉ 1.200 yêu cầu từ 6 depot, chưa đại diện hết 12 depot.
- Hai loại `quoc_te` và `doi_tac` bị loại khỏi pilot, chưa có phương án riêng cho chúng.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", pair.withgoogle.com
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`)
- Đề bài và hướng dẫn của lab: `README.md`, `CHECKPOINTS.md`, `docs/`
