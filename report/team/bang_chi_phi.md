# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

Người kiểm số đã tính lại toàn bộ bảng A2–B4 bằng một script độc lập (chỉ dùng thư viện chuẩn của Python, không gọi hàm của `lab13.py`) từ hai file CSV gốc. Tiền làm tròn đến đồng, phần trăm làm tròn một chữ số thập phân.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (tính tay: (1 − 0,2²) ÷ 0,8 = 0,96 ÷ 0,8) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (tính tay: 1 ÷ 0,8) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (tính tay: E = 0,992 ÷ 0,8 = 1,24; P = 1 − 0,2³ = 0,992; 1,24 ÷ 0,992 = 1,25, tức 1/p vì (1 − (1 − p)^k) triệt tiêu) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút × 2.000 đ) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút × 2.000 đ) | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | có phần simulated |
| Số việc thành công | 978 | `ket_qua` = `thanh_cong` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,3 lần** (4.472 ÷ 274,7) [simulated].
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại, 51,8%**; tiếp theo xem lại 40,7%; token 5,6%; tool 1,9%. Giờ nhân viên (làm lại + xem lại) chiếm 92,5% [simulated].
- Lưu ý khi so với 12.000 đ: 4.472 đ chưa tính 148 ca `chuyen_nhan_vien` do nhân viên làm thay. Chi phí cả hệ thống mỗi yêu cầu = (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ = 0,49×** của 12.000 đ [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **`quoc_te`**: thành công 27,3%, chi phí 22.515 đ = 1,88× so với 12.000 đ [simulated]. Chạy lại không giúp: tỉ lệ `ok` giảm theo lần chạy, 30,0% (lần 1) → 11,4% (lần 2) → 2,2% (lần 3), nên lỗi lặp lại trên cùng yêu cầu và chỉ tốn thêm tiền.
- `doi_tac` (0,85×, thành công 54,4%, có điều khoản riêng) sát ngưỡng nên cũng không đưa vào phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi `noi_dia` + `hang_nang`: 982 yêu cầu, 900 việc thành công, chi phí mỗi việc thành công chưa gồm cố định là 3.414 đ (3.072.513 ÷ 900) [simulated]. Chi phí cố định 40.000.000 đ/tháng.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 (45.000 × 900 ÷ 1.200) | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? **Không đổi ở cả hai khối lượng**: vẫn rẻ hơn nhân viên tự làm (0,38× và 0,48×). Cố định mỗi việc tăng gấp đôi khi khối lượng giảm một nửa (1.185 → 2.370 đ). Kết luận chỉ đổi khi khối lượng xuống còn khoảng 6.200 yêu cầu/tháng (14% quy mô đầy đủ), tại đó 3.414 + cố định mỗi việc ≈ 12.000 đ [simulated].

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" bằng đúng nửa mức tăng của kịch bản "gấp đôi" (token 5,6 → 2,8; xem lại 40,7 → 20,3 (20,35 trước khi làm tròn); làm lại 51,8 → 25,9).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ, +46,3%** [simulated], đúng bằng tổng hai tác động riêng (5,6 + 40,7) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **số ca làm lại** (+51,8%) · 2. **tỉ lệ xem lại** (+40,7%) · 3. **lương nhân viên** (+23,1% với mức +25%) [simulated]. Giá token chỉ +5,6%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay).

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ [simulated] | 319 | 7.449.781 đ [simulated] | 4.111 đ [simulated] (thấp nhất) |
| 2 lần | 4.093.220 đ [simulated] | 234 | **6.901.220 đ [simulated] (rẻ nhất)** | 4.237 đ [simulated] |
| 3 lần | 4.373.585 đ [simulated] | 222 | 7.037.585 đ [simulated] | 4.472 đ [simulated] |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **Giới hạn 2 lần rẻ nhất** (6.901.220 đ), **không trùng** với giới hạn 1 lần có chi phí mỗi việc thành công thấp nhất (4.111 đ) [simulated].
- Tối ưu riêng chi phí mỗi việc thành công (1 lần) đẩy thêm 85 yêu cầu (319 − 234) sang nhân viên, làm cả hệ thống đắt hơn 548.561 đ so với 2 lần [simulated].

## B4 · Nếu phải xem lại tất cả

Phạm vi `noi_dia` + `hang_nang` (982 yêu cầu): 948 yêu cầu có ít nhất một lần chạy `ok` × 5 phút xem lại × 2.000 đ = 9.480.000 đ; 48 ca `lam_lai` × 9 phút × 2.000 đ = 864.000 đ; token + tool của mọi lần chạy trong phạm vi = 224.513 đ; chia cho 900 việc thành công.

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: **11.743 đ = 0,98×** (làm lại 9 phút/ca, theo đề) [simulated]. Dùng phút làm lại từ cột `phut_lam_lai_simulated` (trung bình 15,3 phút/ca, trung vị 14,5) thì **≈ 12.415 đ = 1,03×** [simulated], tức xem lại 100% còn đắt hơn nhân viên tự làm.
- Mức hoà vốn: mỗi lần xem lại phải ≤ **5,1 phút** (làm lại 9 phút) hoặc ≤ **4,8 phút** (làm lại 15,3 phút) [simulated].
- Kết quả này nói gì về thứ pilot cần học được? Khi xem lại 100%, tiền xem lại chiếm khoảng 90% chi phí và trợ lý gần như không tiết kiệm được gì. Pilot phải đo được tỉ lệ xem lại có thể giảm an toàn xuống bao nhiêu, và mỗi lần xem lại có ngắn hơn 5 phút được không (bằng phút đo thật thay cho phút simulated).
