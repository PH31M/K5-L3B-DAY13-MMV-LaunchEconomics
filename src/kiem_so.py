"""Kiem so doc lap (stdlib). Chay: python3 -I kiem_so.py (trong src/)"""
import csv, math, copy
from statistics import NormalDist, median
R=list(csv.DictReader(open('logix_runs.csv'))); Q=list(csv.DictReader(open('logix_requests.csv')))
for r in R:
    for k in('attempt','tokens_in','tokens_out','tool_calls'): r[k]=int(r[k])
for q in Q:
    for k in('so_lan_chay','duoc_xem_lai','dong_trong_24h','mo_lai_trong_7_ngay'): q[k]=int(q[k])
    for k in('phut_xem_lai_simulated','phut_lam_lai_simulated'): q[k]=float(q[k] or 0)

def mh(Q,R,gv=26,gr=130,gt=15,lp=2000,hx=1.0,hl=1.0,mx=None):
    Q=copy.deepcopy(Q); ids={q['request_id'] for q in Q}
    R=[r for r in R if r['request_id'] in ids]
    if mx is not None:
        R=[r for r in R if r['attempt']<=mx]
        for q in Q:
            if q['so_lan_chay']>mx:
                q['ket_qua']='chuyen_nhan_vien'; q['phut_xem_lai_simulated']=q['phut_lam_lai_simulated']=0
    tok=sum(r['tokens_in']/1000*gv+r['tokens_out']/1000*gr for r in R)
    tool=sum(r['tool_calls']*gt for r in R)
    cl=sum(r['tokens_in']/1000*gv+r['tokens_out']/1000*gr+r['tool_calls']*gt for r in R if r['attempt']>1)
    xl=sum(q['phut_xem_lai_simulated'] for q in Q)*lp*hx
    ll=sum(q['phut_lam_lai_simulated'] for q in Q)*lp*hl
    tong=tok+tool+xl+ll; tc=sum(q['ket_qua']=='thanh_cong' for q in Q)
    return dict(token=tok,tool=tool,chay_lai=cl,xem_lai=xl,lam_lai=ll,tong=tong,tc=tc,cps=tong/tc,
                hd=(tok+tool)/len(Q),n=len(Q),khong_tc=len(Q)-tc)
g=mh(Q,R)
print("A2",{k:round(v,1) for k,v in g.items()})
print(" x hoa don",round(g['cps']/g['hd'],2)," lam_lai%",round(100*g['lam_lai']/g['tong'],1)," xem_lai%",round(100*g['xem_lai']/g['tong'],1)," gio NV%",round(100*(g['lam_lai']+g['xem_lai'])/g['tong'],1)," token%",round(100*g['token']/g['tong'],1)," tool%",round(100*g['tool']/g['tong'],1))
print(" he thong/yc",(g['tong']+148*0+222*12000)/1200, "(=", (g['tong']+222*12000)/1200/12000,"x)")
print("A3")
for l in('noi_dia','hang_nang','quoc_te','doi_tac'):
    q=[x for x in Q if x['loai']==l]; m=mh(q,R)
    runs=sum(x['so_lan_chay'] for x in q)
    print(f" {l:10s} n={len(q)} tc={m['tc']/len(q)*100:.1f}% lan/yc={runs/len(q):.2f} cps={m['cps']:.0f} x={m['cps']/12000:.2f}  tong={m['tong']:.0f} tc={m['tc']}")
print("ok theo attempt")
by={q['request_id']:q['loai'] for q in Q}
for l in('noi_dia','hang_nang','quoc_te','doi_tac'):
    row=[]
    for a in(1,2,3):
        s=[r['status']=='ok' for r in R if by[r['request_id']]==l and r['attempt']==a]
        row.append(f"{100*sum(s)/len(s):.1f}% (n={len(s)})" if s else '-')
    print(" ",l,row)
print("A4")
sc=[q for q in Q if q['loai'] in('noi_dia','hang_nang')]; m=mh(sc,R)
print(" scope n",len(sc),"tc",m['tc'],"tong",round(m['tong']),"cps",round(m['cps']))
for name,vol in(("45000",45000),("22500",22500)):
    tcm=vol*m['tc']/1200; cd=40e6/tcm
    print(f" {name}: tc/thang={tcm:.0f} (=vol*{m['tc']}/1200) cd/viec={cd:.0f} cps+cd={m['cps']+cd:.0f} x={ (m['cps']+cd)/12000:.3f}")
print("B1")
kb={'Token x2':dict(gv=52,gr=260),'Token /2':dict(gv=13,gr=65),'Xem lai x2':dict(hx=2),'Xem lai /2':dict(hx=.5),
    'Lam lai x2':dict(hl=2),'Lam lai /2':dict(hl=.5),'Luong +25%':dict(lp=2500),'Max 2':dict(mx=2),'Max 1':dict(mx=1)}
for n,kw in kb.items():
    c=mh(Q,R,**kw)['cps']; print(f" {n:12s} {c:8.0f} {100*(c/g['cps']-1):+.2f}%")
c=mh(Q,R,gv=52,gr=260,hx=2)['cps']; print("B2 token x2 + xem lai x2",round(c),f"{100*(c/g['cps']-1):+.2f}%")
print("B3")
for k in(1,2,3):
    m=mh(Q,R,mx=k); print(f" {k}: tong={m['tong']:.0f} khong_tc={m['khong_tc']} he_thong={m['tong']+12000*m['khong_tc']:.0f} cps={m['cps']:.0f} tc={m['tc']}")
print("B4")
ids={q['request_id'] for q in sc}
okreq={r['request_id'] for r in R if r['status']=='ok' and r['request_id'] in ids}
ll=[q for q in sc if q['ket_qua']=='lam_lai']
tt=sum(r['tokens_in']/1000*26+r['tokens_out']/1000*130+r['tool_calls']*15 for r in R if r['request_id'] in ids)
tcn=sum(q['ket_qua']=='thanh_cong' for q in sc)
tl=mean_ll=sum(q['phut_lam_lai_simulated'] for q in Q if q['ket_qua']=='lam_lai')/sum(q['ket_qua']=='lam_lai' for q in Q)
print(" yc co >=1 lan ok",len(okreq),"lam_lai in scope",len(ll),"token+tool",round(tt),"tc",tcn)
for ml in(9,tl):
    tong=len(okreq)*5*2000+len(ll)*ml*2000+tt
    print(f" lam lai {ml:.1f} ph: tong={tong:.0f} cps={tong/tcn:.0f} x={tong/tcn/12000:.3f}")
allL=[q['phut_lam_lai_simulated'] for q in Q if q['ket_qua']=='lam_lai']
print(" TB lam lai/ca",tl,"trung vi",median(allL),"n lam_lai toan bo",len(allL))
for ml in(9,tl):
    rest=len(ll)*ml*2000+tt; hv=(12000*tcn-rest)/len(okreq)/2000; print(f" hoa von xem lai <= {hv:.2f} ph (lam lai {ml:.1f})")
print("E1")
print(" chinh",sum(q['dong_trong_24h']==1 and q['mo_lai_trong_7_ngay']==0 for q in Q),"/1200")
xem=[q for q in Q if q['duoc_xem_lai']==1]; print(" bo qua",sum(q['quyet_dinh_xem_lai'] in('sua','bo') for q in xem),"/",len(xem))
print(" an toan",sum(q['mo_lai_trong_7_ngay'] for q in Q),"/1200; scope",sum(q['mo_lai_trong_7_ngay'] for q in sc),"/",len(sc))
print(" lam_lai% scope", sum(q['ket_qua']=='lam_lai' for q in sc)/len(sc))
print("D1")
def cm(p1,p2,a=.05,pw=.8):
    za,zb=NormalDist().inv_cdf(1-a/2),NormalDist().inv_cdf(pw); pb=(p1+p2)/2
    return math.ceil((za*math.sqrt(2*pb*(1-pb))+zb*math.sqrt(p1*(1-p1)+p2*(1-p2)))**2/(p2-p1)**2)
n5=cm(.70,.75); n6=cm(.70,.76); de=1+74*.02
print(" a",n5," b DE",de,"n",math.ceil(n5*de),"nguoi/nhom",math.ceil(n5*de/75)," c",20/.02," d",6/.02," n6",n6)
m=math.ceil(n6*0.98/(20-n6*0.02)); print(" e m>=",m,"DE",1+(m-1)*.02, "check eff", 20*m/(1+(m-1)*.02))
