"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # raise NotImplementedError('VIẾT Ở ĐÂY')
    if k is not None and (not isinstance(k, int) or k < 1):
        raise TypeError("k phải là số nguyên dương")
    if p <= 0 or p > 1:
        raise ValueError("p phải nằm trong khoảng (0, 1]")
    if k is not None:
        return (1 - (1 - p)**k) / p
    return 1 / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    # raise NotImplementedError('VIẾT Ở ĐÂY')
    if k is not None and (not isinstance(k, int) or k < 1):
        raise TypeError("k phải là số nguyên dương")
    if p <= 0 or p > 1:
            raise ValueError("p phải nằm trong khoảng (0, 1]")
    if k is not None:
        return 1 - (1 - p)**k
    return 1.0


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # raise NotImplementedError('VIẾT Ở ĐÂY')
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Tính chín chỉ tiêu A2 cho tập yêu cầu, kể cả chi phí các lượt chạy lỗi.

    Chi phí xem lại và làm lại lấy từ hai cột phút giả lập.
    Khi giới hạn lượt chạy, yêu cầu vượt giới hạn được chuyển cho nhân viên.
    Tỉ số có mẫu số bằng 0 được biểu thị bằng NaN.
    """
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    so_yeu_cau = len(reqs)

    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        # Ca chuyển cho nhân viên không phát sinh phút xem lại hoặc làm lại của trợ lý.
        reqs = reqs[reqs['so_lan_chay'] <= max_lan_chay]

    token_moi_lan = (runs['tokens_in'] * gia_vao + runs['tokens_out'] * gia_ra) / 1000
    tool_moi_lan = runs['tool_calls'] * gia_tool
    token = token_moi_lan.sum()
    tool = tool_moi_lan.sum()
    chay_lai = (token_moi_lan + tool_moi_lan)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = reqs['ket_qua'].eq('thanh_cong').sum()

    return {
        'token': token,
        'tool': tool,
        'chay_lai': chay_lai,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong if thanh_cong else math.nan,
        'hoa_don_moi_yc': (token + tool) / so_yeu_cau if so_yeu_cau else math.nan,
    }


def in_bang_a3(runs, reqs):
    """In chi phí theo loại yêu cầu và tỉ lệ lượt chạy có trạng thái ok."""
    print('\nA3 · Chi phí theo loại yêu cầu')
    print(f'{"Loại":<12} {"Số yêu cầu":>10} {"Thành công":>11} '
          f'{"Lượt/YC":>8} {"đ/việc (simulated)":>19} {"So baseline (simulated)":>24}')
    for loai, nhom in reqs.groupby('loai'):
        ket_qua = mo_hinh(runs, nhom)
        ti_le = ket_qua['thanh_cong'] / len(nhom)
        luot_trung_binh = nhom['so_lan_chay'].mean()
        cps = ket_qua['cps']
        print(f'{loai:<12} {len(nhom):>10,} {ti_le:>11.1%} '
              f'{luot_trung_binh:>8.2f} {cps:>19,.0f} {cps / BASELINE:>23.2f}×')

    runs_theo_loai = runs.merge(reqs[['request_id', 'loai']],
                               on='request_id', validate='many_to_one')
    runs_theo_loai['ok'] = runs_theo_loai['status'].eq('ok')
    ti_le_ok = runs_theo_loai.groupby(['loai', 'attempt'])['ok'].mean().unstack()
    ti_le_ok = ti_le_ok.rename(columns=lambda attempt: f'Lượt {attempt}')
    print('\nA3 · Tỉ lệ ok trên các lượt thực sự chạy')
    print(ti_le_ok.to_string(float_format='{:.1%}'.format, na_rep='—'))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    in_bang_a3(runs, reqs)

    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    ket_qua_a4 = mo_hinh(runs, pham_vi)
    ty_le_thanh_cong_tren_toan_bo = ket_qua_a4['thanh_cong'] / len(reqs)
    chi_phi_co_dinh_thang = 40_000_000

    print('\nA4 · Chi phí cố định cho noi_dia và hang_nang')
    for khoi_luong in (45_000, 22_500):
        thanh_cong_thang = khoi_luong * ty_le_thanh_cong_tren_toan_bo
        co_dinh_moi_viec = chi_phi_co_dinh_thang / thanh_cong_thang
        cps_co_co_dinh = ket_qua_a4['cps'] + co_dinh_moi_viec

        print(
            f'{khoi_luong:,.0f} yêu cầu/tháng | '
            f'{thanh_cong_thang:,.0f} việc thành công | '
            f'{co_dinh_moi_viec:,.0f} đ cố định/việc | '
            f'{cps_co_co_dinh:,.0f} đ/việc thành công (simulated) | '
            f'{cps_co_co_dinh / BASELINE:.2f}× mức nhân viên tự làm (simulated)'
        )

    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
