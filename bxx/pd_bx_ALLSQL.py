# coding=UTF-8
# import warnings
# warnings.filterwarnings("ignore")

bx_click = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_click_3 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
LEFT Anti JOIN (select mobile from tbx.push where product != 'bx_pinci') y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

xd_click_alibx329 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.loan where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
join (select mobile from ali.bx329 where score >= {}) b on a.mobile = b.mobile 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_click_bxdata = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
join (SELECT mobile FROM push.insure p join rules.mmh3 r on p.label = r.cypher where p.pdate >= {} and p.pdate <= {} and 
p.product = murmur_hash3_32('MOFANG_CPA_NW') and r.label like "%bxdata%") b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_click_alibx329 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
join (select mobile from ali.bx329 where score >= {}) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_click_alibx331 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
join (select mobile from ali.bx331 where score >= {}) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_alibx329 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM ali.bx329 where score >= {} and operator = {} and city in {}) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''
bx_alibx362 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM ali.bx362 where score >= {} and operator = {} and city in {}) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_click_alibx362 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
join (select mobile from ali.bx362 where score >= {}) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_cmpp_black = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(select mobile,pdate,city,operator FROM pre.black where pdate>={} and pdate<={} and operator = {} and city in {} and label = {}) a
join (select status,mobile from black.cmpp where status in {}) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''


bx_click_2 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {} and status = {}) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_click_with_ggj = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
join veggie.tomato b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_click_with_house = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
join veggie.carrot b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_click_with_car = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
join veggie.broccoli b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_click_with_dirty = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile, ip FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
join (select ip from access.dirty) b on a.ip = b.ip
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_xhdx = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile, rule FROM dpi.xhdx where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {}) a 
JOIN (SELECT codeid, ruleid, rule FROM rules.mw where codeid in {}) b on a.rule = b.ruleid
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_xhdx_mix = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile, rule FROM dpi.xhdx_mix where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_xhdx_mix_status0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile, rule FROM dpi.xhdx_mix where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
join (SELECT mobile from loan.zhongan where status = 0 and (remark = 1 or remark = 2)) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_xhdx_mix_status1 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile, rule FROM dpi.xhdx_mix where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
join (SELECT mobile from loan.zhongan where status = 1 or (status = 0 and remark = null)) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_xhdx_mix_with_bxzk = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile, rule FROM dpi.xhdx_mix where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 union all SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_xhdx_mix_out_bxzk = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile, rule FROM dpi.xhdx_mix where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
LEFT Anti JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 union all SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_aitao = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_aitao_xz = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a
LEFT Anti JOIN( SELECT mobile from dpi.aitao_mix where pdate <= '{}') z on a.mobile = z.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_aitao_badclick = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
LEFT Anti JOIN (select mobile from(select mobile from sms.insure where pdate >= 20250101 and send_status = 1 GROUP BY mobile HAVING count(mobile)>=8) a left anti join access.insure b on a.mobile = b.mobile) z on a.mobile = z.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_aitao_bt = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, rule, mobile FROM dpi.aitao where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {}) a
join (select codeid,ruleid from rules.mw where codeid in {})b on a.rule = b.ruleid
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_aitao_status0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
join (SELECT mobile from loan.zhongan where status = 0 and (remark = 1 or remark = 2)) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''
bx_aitao_status1 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
join (SELECT mobile from loan.zhongan where status = 1 or (status = 0 and remark = null)) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''
bx_aitao_with_cj = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= '{3}' and pdate <= '{4}' and operator = {5} and city in {6} and rule in {7}) a 
join (select mobile from dpi.cj where pdate >= '{3}' and pdate <= '{4}' and rule in {8}) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{9}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {10}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {11}
'''

bx_aitao_app = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.aitao_app where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_cj = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.cj where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_cj_zad_status0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.cj where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
join (SELECT mobile from loan.zhongan where status = 0 and (remark = 1 or remark = 2)) c on a.mobile = c.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_sdk = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM sdk.jiguang where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

sdk_cyjd = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM sdk.cyjd where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and biz = {} and rule = {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_yax = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.yax where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_yax_lt = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.yax_lt where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_yax_lt_alibx329 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.yax_lt where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
join (select mobile from ali.bx329 where score   >= {}) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''


bx_yax_lt_mb = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.yax_lt_mb where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_yax_lt_with_age = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.yax_lt where pdate >= '{3}' and pdate <= '{4}' and operator = {5} and city in {6} and rule in {7}) a 
join (select mobile from veggie.potato where level = {8} union all select mobile from veggie.cucumber where level = {8}) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{9}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {10}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {11}
'''

qjzk_status = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM other.qijia where operator = {} and city in {} and status = {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

jz_succ = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM wh.jiazhuang_succ where operator = {} and city in {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

usedcar_succ = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM wh.usedcar_succ where operator = {} and city in {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

credit_click_out_bxzk_status_0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.credit where pdate >= {} and operator = {} and city in {}) a 
left anti join (SELECT mobile FROM insure.nuanwa WHERE status = 0 union all SELECT mobile FROM insure.taikang WHERE status = 0 union all SELECT mobile FROM insure.zhonganbx WHERE status = 0) d on a.mobile = d.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

credit_click_and_bxzk_status_0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.credit where pdate >= {} and operator = {} and city in {}) a 
join (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 union all SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) d on a.mobile = d.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

loan_click_and_bxzk_status_0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.loan where pdate >= {} and operator = {} and city in {}) a 
join (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 union all SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) d on a.mobile = d.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

pfzk_cf_out_bxzk_status_0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM credit.pufa_cf where pdate >= {} and operator = {} and city in {}) a 
left anti join (SELECT mobile FROM insure.nuanwa WHERE status = 0 union all SELECT mobile FROM insure.taikang WHERE status = 0 union all SELECT mobile FROM insure.zhonganbx WHERE status = 0) d on a.mobile = d.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

pfzk_cf_and_bxzk_status_0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM credit.pufa_cf where pdate >= {} and operator = {} and city in {}) a 
join (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 union all SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) d on a.mobile = d.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_dpi_fre = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT m.operator, m.city, m.mobile, count(m.mobile) as num FROM 
    (SELECT operator, city, mobile FROM dpi.xhdx where pdate >= 20240101 and operator = {3} and city in {4} and rule in (SELECT ruleid FROM rules.mw where codeid like 'BT%' OR codeid like 'BS%')
    union all SELECT operator, city, mobile FROM dpi.xhdx_mix where pdate >= 20240101 and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%')
    union all SELECT operator, city, mobile FROM dpi.cj where pdate >= 20240101 and operator = {3} and city in {4} and rule in (100250,100251,100242,100243,100245)
    union all SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= 20240101 and operator = {3} and city in {4} and (rule like 'BT%' OR rule like 'BS%')
	union all SELECT operator, city, mobile FROM dpi.yax where pdate >= 20240101 and operator = {3} and city in {4} and (rule like 'BT%' OR rule like 'BS%')
	union all SELECT operator, city, mobile FROM dpi.yax_lt where pdate >= 20240101 and operator = {3} and city in {4} and (rule like 'BT%' OR rule like 'BS%')) m
GROUP BY m.operator, m.city, m.mobile HAVING num >= {5} and num <= {6}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {9}
'''

bx_dpi_time_fre = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT m.operator, m.city, m.mobile, count(m.mobile) as num FROM 
    (SELECT operator, city, mobile FROM dpi.xhdx where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule in (SELECT ruleid FROM rules.mw where codeid like 'BT%' OR codeid like 'BS%')
    union all SELECT operator, city, mobile FROM dpi.xhdx_mix where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%')
    union all SELECT operator, city, mobile FROM dpi.cj where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule in (100250,100251,100242,100243,100245)
    union all SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%')
	union all SELECT operator, city, mobile FROM dpi.yax where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%')
	union all SELECT operator, city, mobile FROM dpi.yax_lt where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%')) m
GROUP BY m.operator, m.city, m.mobile HAVING num >= {7} and num <= {8}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{9}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {10}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {11}
'''

bx_click_time_fre = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT m.operator, m.city, m.mobile, count(m.mobile) as num FROM 
    (SELECT operator, city, mobile FROM access.insure where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6}) m
GROUP BY m.operator, m.city, m.mobile HAVING num >= {7} and num <= {8}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{9}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {10}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {11}
'''

kj_bx = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM score.kj where pdate >= {} and pdate <= {} and operator = {} and city in {} and model = {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

kj_rule_bx = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM score.kj where pdate >= {} and pdate <= {} and operator = {} and city in {} and model = {} and rule = {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_click_fre = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT m.operator, m.city, m.mobile, count(m.mobile) as num FROM 
    (SELECT operator, city, mobile FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {}) m
GROUP BY m.operator, m.city, m.mobile HAVING num >= {} and num <= {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_aitao_fre = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT m.operator, m.city, m.mobile, count(m.mobile) as num FROM 
    (SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= {} and pdate <= {} and operator = {} and city in {} and rule in {}) m
GROUP BY m.operator, m.city, m.mobile HAVING num >= {} and num <= {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_zk_status_0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM insure.nuanwa where pdate >= {} and operator = {} and city in {} and status = 0 and label = murmur_hash3_32('zkbiaoqian') 
union all SELECT operator, city, mobile FROM insure.zhonganbx where pdate >= {} and operator = {} and city in {} and status = 0 and label = murmur_hash3_32('zkbiaoqian')) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_nwzk_status_0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM insure.nuanwa where pdate >= {} and operator = {} and city in {} and status = 0 and label = murmur_hash3_32('zkbiaoqian')) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_zazk_status_0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM insure.zhonganbx where pdate >= {} and operator = {} and city in {} and status = 0 and label = murmur_hash3_32('zkbiaoqian')) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_zk_status_0_alibx329 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM insure.nuanwa where pdate >= {} and operator = {} and city in {} and status = 0
union all SELECT operator, city, mobile FROM insure.zhonganbx where pdate >= {} and operator = {} and city in {} and status = 0) a 
join (select mobile from ali.bx329 where score >= {}) b on b.mobile = a.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_zk_status_0_new = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM insure.nuanwa where pdate >= {} and operator = {} and city in {} and status = 0 and label = murmur_hash3_32('zkbiaoqian') 
union all SELECT operator, city, mobile FROM insure.zhonganbx where pdate >= {} and operator = {} and city in {} and status = 0 and label = murmur_hash3_32('zkbiaoqian')) a
LEFT Anti JOIN (select mobile from push.insure where pdate >= 20250201 and label = murmur_hash3_32('CMCC_bx_zk_status_0')) y on a.mobile = y.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_zhzk_status_0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM insure.zhonghui where pdate >= {} and operator = {} and city in {} and status = 0 and label = murmur_hash3_32('zkbiaoqian')) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_xhdx_jzk0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile, rule FROM dpi.xhdx where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {}) a 
JOIN (SELECT codeid, ruleid, rule FROM rules.mw where codeid in {}) b on a.rule = b.ruleid
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and label = murmur_hash3_32('zkbiaoqian') and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and label = murmur_hash3_32('zkbiaoqian') and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {}
'''

bx_aitao_jzk0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and label = murmur_hash3_32('zkbiaoqian') and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and label = murmur_hash3_32('zkbiaoqian') and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {}
'''

bx_cj_jzk0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.cj where pdate >= '{}' and pdate <= '{}' and operator = {} and city in {} and rule in {}) a 
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and label = murmur_hash3_32('zkbiaoqian') and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and label = murmur_hash3_32('zkbiaoqian') and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {}
'''

bx_click_jzk0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and label = murmur_hash3_32('zkbiaoqian') and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and label = murmur_hash3_32('zkbiaoqian') and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {}
'''

bx_dpi_and_bxzk0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.xhdx where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule in (SELECT ruleid FROM rules.mw where codeid like 'BT%' OR codeid like 'BS%')
    union all (SELECT operator, city, mobile FROM dpi.xhdx_mix where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))
	union all (SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))
    union all (SELECT operator, city, mobile FROM dpi.cj where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule in (100250,100251,100242,100243,100245))
	union all (SELECT operator, city, mobile FROM dpi.yax where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))
	union all (SELECT operator, city, mobile FROM dpi.yax_lt where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {9}
'''

bx_dpi_and_alibx329 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.xhdx where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule in (SELECT ruleid FROM rules.mw where codeid like 'BT%' OR codeid like 'BS%')
    union all (SELECT operator, city, mobile FROM dpi.xhdx_mix where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))
	union all (SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))
    union all (SELECT operator, city, mobile FROM dpi.cj where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule in (100250,100251,100242,100243,100245))
	union all (SELECT operator, city, mobile FROM dpi.yax where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))
	union all (SELECT operator, city, mobile FROM dpi.yax_lt where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM ali.bx329 where score >= {9}) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {10}
'''

bx_dpi_and_bxzk0_oppo = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.xhdx where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule in (SELECT ruleid FROM rules.mw where codeid like 'BT%' OR codeid like 'BS%')
    union all (SELECT operator, city, mobile FROM dpi.xhdx_mix where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))
	union all (SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))
    union all (SELECT operator, city, mobile FROM dpi.cj where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule in (100250,100251,100242,100243,100245))
	union all (SELECT operator, city, mobile FROM dpi.yax where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))
	union all (SELECT operator, city, mobile FROM dpi.yax_lt where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile
JOIN (SELECT mobile FROM brand.tianyuan WHERE brand = 2) z1 on a.mobile = z1.mobile  
ORDER BY RAND()
limit {9}
'''

bx_dpi_cj_and_bxzk0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.cj where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule in (100250,100251,100242,100243,100245)) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {9}
'''

bx_dpi_aitao_and_bxzk0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%')) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {9}
'''

bx_dpi_yax_and_bxzk0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.yax where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%')) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {9}
'''

bx_dpi_xhdx_and_bxzk0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile from dpi.xhdx where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule in (SELECT ruleid FROM rules.mw where codeid in ('BT703', 'BT086', 'BT081', 'BT541', 'BT559', 'BT703',
 'BT063', 'BT087', 'BT541', 'BT086', 'BT584', 'BT081', 'BT086', 'BT544', 'BT544', 'BT081', 'BT081', 'BT583', 'BT541', 'BT209', 'BT063', 'BT541', 'BT086', 'BT087', 'BT188', 'BT087', 'BT209', 'BT069', 'BT104', 'BT559',
  'BT554', 'BT583', 'BT099', 'BT531', 'BT069', 'BT541', 'BT099', 'BT188', 'BT599', 'BT177', 'BT541', 'BT063', 'BT087', 'BT542', 'BT584', 'BT185', 'BT556', 'BT531', 'BT387'))) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {9}
'''

bx_click_and_bxzk0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6}) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {9}
'''

bx_click_and_bxzk0_ti = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6}) a
LEFT Anti JOIN (SELECT mobile FROM access.insure where pdate >= {4} and operator = {5} and city in {6}) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {9}
'''

bx_click_and_bxzk0_ti_zad_status0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM access.insure where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6}) a
join (SELECT mobile from loan.zhongan where status = 0 and (remark = 1 or remark = 2)) c on a.mobile = c.mobile
LEFT Anti JOIN (SELECT mobile FROM access.insure where pdate >= {4} and operator = {5} and city in {6}) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {9}
'''

bx_app_and_bxzk0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.aitao_app where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule like 'APPBX%') a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {9}
'''

bx_push_and_bxzk0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM push.insure where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and product = murmur_hash3_32('NUANWA')) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {9}
'''

bx_push_and_bxzk0_2 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM push.insure where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and product = murmur_hash3_32('ZHONGHUI')) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {9}
'''

bx_nwza_zk = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM insure.nuanwa where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and status = {7} and label = murmur_hash3_32('zkbiaoqian')
union all SELECT operator, city, mobile FROM insure.zhonganbx where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and status = {7} and label = murmur_hash3_32('zkbiaoqian')) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{8}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {9}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {10}
'''

bx_nwza_zk_2 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM insure.nuanwa where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and status = {7}
union all SELECT operator, city, mobile FROM insure.zhonganbx where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and status = {7}) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{8}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {9}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {10}
'''

bx_send_ls = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM push.insure where pdate >= {} and pdate <= {} and operator = {} and city in {} and product = murmur_hash3_32('{}')) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_send_ls_bxzk = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM push.insure where pdate >= {} and pdate <= {} and operator = {} and city in {} and product = murmur_hash3_32('{}')) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {}
'''

bx_send_sb_bxzk = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM push.insure where pdate >= {} and pdate <= {} and operator = {} and city in {} and product = murmur_hash3_32('{}')) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and send_status = -1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.nuanwa WHERE pdate >= 20250201 and status = 0 UNION ALL SELECT mobile FROM insure.zhonganbx WHERE pdate >= 20250201 and status = 0) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {}
'''

bx_dpi_and_zhzk_status_0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.xhdx where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule in (SELECT ruleid FROM rules.mw where codeid like 'BT%' OR codeid like 'BS%')
    union all (SELECT operator, city, mobile FROM dpi.xhdx_mix where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))
	union all (SELECT operator, city, mobile FROM dpi.aitao_mix where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))
    union all (SELECT operator, city, mobile FROM dpi.cj where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and rule in (100250,100251,100242,100243,100245))
	union all (SELECT operator, city, mobile FROM dpi.yax where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))
	union all (SELECT operator, city, mobile FROM dpi.yax_lt where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and (rule like 'BT%' OR rule like 'BS%'))) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.zhonghui WHERE pdate >= 20250201 and status = 0 and biz = 8) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {9}
'''

bx_nwza_and_zhzk_status_0 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM insure.nuanwa where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and status = {7} and label = murmur_hash3_32('zkbiaoqian')
union all SELECT operator, city, mobile FROM insure.zhonganbx where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and status = {7} and label = murmur_hash3_32('zkbiaoqian')) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{8}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {9}) y on a.mobile = y.mobile
JOIN (SELECT mobile FROM insure.zhonghui WHERE pdate >= 20250201 and status = 0 and biz = 8 and label = murmur_hash3_32('zkbiaoqian')) z on a.mobile = z.mobile 
ORDER BY RAND()
limit {10}
'''

sample_taikang_duodian = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM sample.taikang_duodian where pdate >= {} and pdate <= {} and operator = {} and city in {} and upgrade_times = {} and match_num in {}) a
LEFT Anti JOIN (select mobile from tbx.push where product != 'bx_pinci') y on a.mobile = y.mobile
LEFT Anti JOIN (select mobile from black.cmpp where status in (1,2,3)) x on a.mobile = x.mobile
ORDER BY RAND()
limit {}
'''

sample_taikang_duodian_2 = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM sample.taikang_duodian_202506 where pdate >= {} and pdate <= {} and operator = {} and city in {} and upgrade_times = {} and match_num in {}) a
LEFT Anti JOIN (select mobile from tbx.push where product != 'bx_pinci') y on a.mobile = y.mobile
LEFT Anti JOIN (select mobile from black.cmpp where status in (1,2,3)) x on a.mobile = x.mobile
ORDER BY RAND()
limit {}
'''

sample_taikang_duodian_2_today = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM sample.taikang_duodian_202506 where pdate >= {} and pdate <= {} and operator = {} and city in {} and upgrade_times = {} and match_num in {}) a
LEFT Anti JOIN (select mobile from tbx.push where product != 'bx_pinci') y on a.mobile = y.mobile
LEFT Anti JOIN (select mobile from black.cmpp where status in (1,2,3)) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from push.insure where pdate = {}) p on p.mobile = a.mobile
ORDER BY RAND()
limit {}
'''

bxdata_biz = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM tbx.bxdata where pdate >= {} and pdate <= {} and operator = {} and city in {} and biz = {}) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

nature_snow = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM nature.snow where pdate >= {} and pdate <= {} and operator = {} and city in {}) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

nature_snow_biz = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM nature.snow where pdate >= {} and pdate <= {} and operator = {} and city in {} and biz = {}) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

nature_rain = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM nature.rain where pdate >= {} and pdate <= {} and operator = {} and city in {} and score >= {} and score <= {} and rule = {}) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

cj_date_with_date = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM dpi.cj where pdate >= {} and pdate <= {} and operator = {} and city in {} and rule in (100242,100243,100245,100250,100251)) a
join (SELECT mobile FROM dpi.cj WHERE pdate >= {} and rule in (100242,100243,100245,100250,100251)) b on a.mobile = b.mobile
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

bx_push_yesterday = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, '{}' as product, '{}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM push.insure where pdate = {} and operator = {} and city in {} and product= murmur_hash3_32('{}') and label = murmur_hash3_32('{}')) a
LEFT Anti JOIN (select mobile from tbx.push where product != "bx_pinci") y on a.mobile = y.mobile
ORDER BY RAND()
limit {}
'''

nature_snow_biz_before = '''
INSERT INTO tbx.push
SELECT DISTINCT '{0}' as pdate, a.operator, '{1}' as product, '{2}' as label, a.city, a.mobile FROM 
(SELECT operator, city, mobile FROM push.insure where pdate >= {3} and pdate <= {4} and operator = {5} and city in {6} and product = murmur_hash3_32('MOFANG_CPA_NW') and label = murmur_hash3_32('{2}')) a
LEFT Anti JOIN (SELECT mobile from sms.insure where pdate >= '{7}' and product = murmur_hash3_32('NUANWA') and submit_status = 1) x on a.mobile = x.mobile
LEFT Anti JOIN (select mobile from tbx.push union all select mobile from push.insure where pdate >= {8}) y on a.mobile = y.mobile
ORDER BY RAND()
limit {9}
'''















