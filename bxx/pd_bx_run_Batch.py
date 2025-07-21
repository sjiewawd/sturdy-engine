# !/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import traceback
import os
import datetime
import time
import pd_bx_ALLSQL

# 定义函数
# region

def get_datetime(deltadays):
	date_str = datetime.date.strftime(datetime.date.today() + datetime.timedelta(deltadays), '%Y-%m-%d')
	return date_str

def get_datetime2(deltadays):
	date_str2 = datetime.date.strftime(datetime.date.today() + datetime.timedelta(deltadays), '%Y-%m-%d %H:%M:%S')
	return date_str2

def get_datetime3(deltadays):
	date_str3 = datetime.date.strftime(datetime.date.today() + datetime.timedelta(deltadays), '%Y%m%d')
	return date_str3

def get_datetime4(now_time, deltadays):
	date_str4 = datetime.date.strftime(datetime.datetime.strptime(now_time, "%Y%m%d") - datetime.timedelta(deltadays), '%Y%m%d')
	return date_str4

# endregion

# 定义特殊日期
# region

Time_Begain = datetime.datetime.now()
Time_End = datetime.datetime.now()
hl_time = get_datetime3(0)

# 跑明天数
yesterday_time = get_datetime3(-1)
today_time = get_datetime3(0)
tomorrow_time = get_datetime3(1)

date_fetch = get_datetime3(-3)
date_before2 = get_datetime3(0)
date_before3 = get_datetime3(-1)
date_before4 = get_datetime3(-2)
date_before5 = get_datetime3(-3)
date_before7 = get_datetime3(-5)
date_before10 = get_datetime3(-8)
date_before15 = get_datetime3(-13)
date_before20 = get_datetime3(-18)
date_before30 = get_datetime3(-28)
date_before40 = get_datetime3(-38)
date_before60 = get_datetime3(-58)
date_before90 = get_datetime3(-88)
date_before120 = get_datetime3(-118)

# 跑今天数
# yesterday_time = get_datetime3(-2)
# today_time = get_datetime3(-1)
# tomorrow_time = get_datetime3(0)
#
# date_fetch = get_datetime3(-4)
# date_before3 = get_datetime3(-2)
# date_before4 = get_datetime3(-3)
# date_before5 = get_datetime3(-4)
# date_before7 = get_datetime3(-6)
# date_before10 = get_datetime3(-9)
# date_before15 = get_datetime3(-14)
# date_before20 = get_datetime3(-19)
# date_before30 = get_datetime3(-29)
# date_before40 = get_datetime3(-39)
# date_before60 = get_datetime3(-59)
# date_before90 = get_datetime3(-89)
# date_before120 = get_datetime3(-119)

# endregion

# 定义城市
# region

nuanwa_city = (140100, 140200, 140300, 140400, 140500, 140600, 140800, 140900, 141000, 141100, 150100, 150200, 150300, 150400, 150500, 150600, 150700, 150800, 150900, 152200,
			   152500, 152900, 210100, 210200, 210300, 210400, 210500, 210600, 210700, 210800, 210900, 211000, 211100, 211200, 211300, 211400, 320100, 320200, 320300, 320400,
			   320600, 320700, 320800, 320900, 321000, 321100, 321200, 321300, 340100, 340200, 340300, 340400, 340500, 340600, 340700, 340800, 341000, 341100, 341200, 632800,
			   341300, 341500, 341600, 341700, 341800, 350100, 350200, 350300, 350400, 350600, 350700, 350800, 350900, 360100, 360200, 360300, 360400, 360500, 360600, 360700,
			   360800, 360900, 361000, 361100, 410100, 410200, 410300, 410400, 410500, 410600, 410700, 410800, 410900, 411000, 411100, 411200, 411300, 411400, 411500, 411600,
			   411700, 419001, 420100, 420200, 420300, 420500, 420600, 420700, 420800, 420900, 421000, 421100, 421200, 421300, 422800, 429004, 429005, 429006, 429021, 430100,
			   430200, 430300, 430400, 430500, 430600, 430700, 430800, 430900, 431000, 431100, 431200, 431300, 433100, 460100, 460200, 460300, 460400, 469001, 469002, 469005,
			   469006, 469007, 469021, 469022, 469023, 469024, 469025, 469026, 469027, 469028, 469029, 469030, 500000, 510100, 510400, 510500, 510600, 510700, 510800, 510900,
			   511000, 511100, 511300, 511400, 511500, 511600, 511700, 511800, 511900, 512000, 513200, 513300, 513400, 520100, 520200, 520300, 520400, 520500, 520600, 522300,
			   522600, 522700, 610100, 610200, 610300, 610400, 610500, 610600, 610700, 610800, 610900, 611000, 620100, 620200, 620300, 620400, 620500, 620600, 620700, 620800,
			   620900, 621000, 621100, 621200, 622900, 623000, 630100, 630200, 632200, 632300, 632500, 632600, 632700, 330100, 320500
			   )

nuanwa_city_lie = (140100,140200,140300,140400,140500,140600,140800,140900,141000,141100,632800,350100,350200,350300,350400,350600,350700,350800,350900,360100,360200,360300,
				   360400,360500,360600,360700,360800,360900,361000,361100,410100,410200,410300,410400,410500,410600,410700,410800,410900,411000,411100,411200,411300,411400,
				   411500,411600,411700,419001,430100,430200,430300,430400,430500,430600,430700,430800,430900,431000,431100,431200,431300,433100,460100,460200,460300,460400,
				   469001,469002,469005,469006,469007,469021,469022,469023,469024,469025,469026,469027,469028,469029,469030,500000,610100,610200,610300,610400,610500,610600,
				   610700,610800,610900,611000,630100,630200,632200,632300,632500,632600,632700,330100
				   )
nuanwa_city_you = (150100,150200,150300,150400,150500,150600,150700,150800,150900,152200,152500,152900,210100,210200,210300,210400,210500,210600,210700,210800,210900,211000,
				   211100,211200,211300,211400,320100,320200,320300,320400,320600,320700,320800,320900,321000,321100,321200,321300,340100,340200,340300,340400,340500,340600,
				   340700,340800,341000,341100,341200,341300,341500,341600,341700,341800,420100,420200,420300,420500,420600,420700,420800,420900,421000,421100,421200,421300,
				   422800,429004,429005,429006,429021,510100,510400,510500,510600,510700,510800,510900,511000,511100,511300,511400,511500,511600,511700,511800,511900,512000,
				   513200,513300,513400,520100,520200,520300,520400,520500,520600,522300,522600,522700,620100,620200,620300,620400,620500,620600,620700,620800,620900,621000,
				   621100,621200,622900,623000,320500
				   )


nuanwa_yixian_city = (320100, 320200, 340100, 410100, 420100, 430100, 500000, 510100, 610100, 330100, 320500)

nuanwa_yxother_city = (140100, 140200, 140300, 140400, 140500, 140600, 140800, 140900, 141000, 141100, 150100, 150200, 150300, 150400, 150500, 150600, 150700, 150800, 150900,
					   152200, 152500, 152900, 210100, 210200, 210300, 210400, 210500, 210600, 210700, 210800, 210900, 211000, 211100, 211200, 211300, 211400, 320300, 320400,
					   320600, 320700, 320800, 320900, 321000, 321100, 321200, 321300, 340200, 340300, 340400, 340500, 340600, 340700, 340800, 341000, 341100, 341200, 632800,
					   341300, 341500, 341600, 341700, 341800, 350100, 350200, 350300, 350400, 350600, 350700, 350800, 350900, 360100, 360200, 360300, 360400, 360500, 360600,
					   360700, 360800, 360900, 361000, 361100, 410200, 410300, 410400, 410500, 410600, 410700, 410800, 410900, 411000, 411100, 411200, 411300, 411400, 411500,
					   411600, 411700, 419001, 420200, 420300, 420500, 420600, 420700, 420800, 420900, 421000, 421100, 421200, 421300, 422800, 429004, 429005, 429006, 429021,
					   430200, 430300, 430400, 430500, 430600, 430700, 430800, 430900, 431000, 431100, 431200, 431300, 433100, 460100, 460200, 460300, 460400, 469001, 469002,
					   469005, 469006, 469007, 469021, 469022, 469023, 469024, 469025, 469026, 469027, 469028, 469029, 469030, 510400, 510500, 510600, 510700, 510800, 510900,
					   511000, 511100, 511300, 511400, 511500, 511600, 511700, 511800, 511900, 512000, 513200, 513300, 513400, 520100, 520200, 520300, 520400, 520500, 520600,
					   522300, 522600, 522700, 610200, 610300, 610400, 610500, 610600, 610700, 610800, 610900, 611000, 620100, 620200, 620300, 620400, 620500, 620600, 620700,
					   620800, 620900, 621000, 621100, 621200, 622900, 623000, 630100, 630200, 632200, 632300, 632500, 632600, 632700)

zhonghui_cps_city = (120000, 140100, 140200, 140300, 140400, 140500, 140600, 140700, 140800, 140900, 141000, 141100, 150100, 150200, 150300, 150400, 150500, 150600, 150700,
					 150800, 150900, 152200, 152500, 152900, 210100, 210200, 210300, 210400, 210500, 210600, 210700, 210800, 210900, 211000, 211100, 211200, 211300, 211400,
					 220100, 220200, 220300, 220400, 220500, 220600, 220700, 220800, 222400, 230100, 230200, 230300, 230400, 230500, 230600, 230700, 230800, 230900, 231100,
					 231200, 232700, 320100, 320200, 320300, 320400, 320500, 320600, 320700, 320800, 320900, 321000, 321100, 321200, 321300, 330100, 330200, 330300, 330400,
					 330500, 330600, 330700, 330800, 330900, 331000, 331100, 340100, 340200, 340300, 340400, 340500, 340600, 340700, 340800, 341000, 341100, 341200, 341300,
					 341500, 341600, 341700, 341800, 350100, 350200, 350300, 350400, 350500, 350600, 350700, 350800, 350900, 360100, 360200, 360300, 360400, 360500, 360600,
					 360700, 360800, 360900, 361000, 361100, 370100, 370200, 370300, 370400, 370500, 370600, 370700, 370800, 370900, 371000, 371100, 371300, 371400, 371500,
					 371600, 371700, 410100, 410200, 410300, 410400, 410500, 410600, 410700, 410800, 410900, 411000, 411100, 411200, 411300, 411400, 411500, 411600, 411700,
					 419001, 420100, 420200, 420300, 420500, 420600, 420700, 420800, 420900, 421000, 421100, 421200, 421300, 422800, 429004, 429005, 429006, 429021, 430100,
					 430200, 430300, 430400, 430500, 430600, 430700, 430800, 430900, 431000, 431100, 431200, 431300, 433100, 440200, 440400, 440500, 440600, 440700, 440800,
					 440900, 441200, 441300, 441400, 441500, 441600, 441700, 441800, 441900, 442000, 445100, 445200, 445300, 450100, 450200, 450300, 450400, 450500, 450600,
					 450700, 450800, 450900, 451000, 451100, 451200, 451300, 451400, 460100, 460200, 460300, 460400, 469001, 469002, 469005, 469006, 469007, 469021, 469022,
					 469023, 469024, 469025, 469026, 469027, 469028, 469029, 469030, 500000, 510100, 510300, 510400, 510500, 510600, 510700, 510800, 510900, 511000, 511100,
					 511300, 511400, 511500, 511600, 511700, 511800, 511900, 512000, 513200, 513300, 513400, 520100, 520200, 520300, 520400, 520500, 520600, 522300, 522600,
					 522700, 530100, 530300, 530400, 530500, 530600, 530700, 530800, 530900, 532300, 532500, 532600, 532800, 532900, 533100, 533300, 533400, 620100, 620200,
					 620300, 620400, 620500, 620600, 620700, 620800, 620900, 621000, 621100, 621200, 622900, 623000, 630100, 630200, 632200, 632300, 632500, 632600, 632700,
					 632800, 640100, 640200, 640300, 640400, 640500)

zhonghui_cpa_city = (120000, 140100, 140200, 140300, 140400, 140500, 140600, 140700, 140800, 140900, 141000, 141100, 150100, 150200, 150300, 150400, 150500, 150600, 150700,
					 150800, 150900, 152200, 152500, 152900, 210100, 210200, 210300, 210400, 210500, 210600, 210700, 210800, 210900, 211000, 211100, 211200, 211300, 211400,
					 220100, 220200, 220300, 220400, 220500, 220600, 220700, 220800, 222400, 230100, 230200, 230300, 230400, 230500, 230600, 230700, 230800, 230900, 231000,
					 231100, 231200, 232700, 310000, 320100, 320200, 320300, 320400, 320500, 320600, 320700, 320800, 320900, 321000, 321100, 321200, 321300, 330100, 330200,
					 330300, 330400, 330500, 330600, 330700, 330800, 330900, 331000, 331100, 340100, 340200, 340300, 340400, 340500, 340600, 340700, 340800, 341000, 341100,
					 341200, 341300, 341500, 341600, 341700, 341800, 350100, 350200, 350300, 350400, 350500, 350600, 350700, 350800, 350900, 360100, 360200, 360300, 360400,
					 360500, 360600, 360700, 360800, 360900, 361000, 361100, 370100, 370200, 370300, 370400, 370500, 370600, 370700, 370800, 370900, 371000, 371100, 371300,
					 371400, 371500, 371600, 371700, 410100, 410200, 410300, 410400, 410500, 410600, 410700, 410800, 410900, 411000, 411100, 411200, 411300, 411400, 411500,
					 411600, 411700, 419001, 420100, 420200, 420300, 420500, 420600, 420700, 420800, 420900, 421000, 421100, 421200, 421300, 422800, 429004, 429005, 429006,
					 429021, 430100, 430200, 430300, 430400, 430500, 430600, 430700, 430800, 430900, 431000, 431100, 431200, 431300, 433100, 440200, 440400, 440500, 440600,
					 440700, 440800, 440900, 441200, 441300, 441400, 441500, 441600, 441700, 441800, 441900, 442000, 445100, 445200, 445300, 450100, 450200, 450300, 450400,
					 450500, 450600, 450700, 450800, 450900, 451000, 451100, 451200, 451300, 451400, 460100, 460200, 460300, 460400, 469001, 469002, 469005, 469006, 469007,
					 469021, 469022, 469023, 469024, 469025, 469026, 469027, 469028, 469029, 469030, 500000, 510100, 510300, 510400, 510500, 510600, 510700, 510800, 510900,
					 511000, 511100, 511300, 511400, 511500, 511600, 511700, 511800, 511900, 512000, 513200, 513300, 513400, 520100, 520200, 520300, 520400, 520500, 520600,
					 522300, 522600, 522700, 530100, 530300, 530400, 530500, 530600, 530700, 530800, 530900, 532300, 532500, 532600, 532800, 532900, 533100, 533300, 533400,
					 540100, 540200, 540300, 540400, 540500, 540600, 542500, 610100, 610200, 610300, 610400, 610500, 610600, 610700, 610800, 610900, 611000, 620100, 620200,
					 620300, 620400, 620500, 620600, 620700, 620800, 620900, 621000, 621100, 621200, 622900, 623000, 630100, 630200, 632200, 632300, 632500, 632600, 632700,
					 632800, 640100, 640200, 640300, 640400, 640500, 650100, 650200, 650400, 650500, 652300, 652700, 652800, 652900, 653000, 653100, 653200, 654000, 654200,
					 654300, 659001, 659002, 659003, 659004, 659005, 659006, 659007, 659008, 659009, 659010, 659011)

zhonganmf_dd_city = (120000, 130100, 130200, 130300, 130400, 130500, 130600, 130700, 130800, 130900, 131000, 131100, 140100, 140200, 140300, 140400, 140500, 140600, 140700,
					 140800, 140900, 141000, 141100, 150100, 150200, 150300, 150400, 150500, 150600, 150700, 150800, 150900, 152200, 152500, 152900, 210100, 210200, 210300,
					 210400, 210500, 210600, 210700, 210800, 210900, 211000, 211100, 211200, 211300, 211400, 220100, 220200, 220300, 220400, 220500, 220600, 220700, 220800,
					 222400, 230100, 230200, 230300, 230400, 230500, 230600, 230700, 230800, 230900, 231000, 231100, 231200, 232700, 320100, 320200, 320300, 320400, 320500,
					 320600, 320700, 320800, 320900, 321000, 321100, 321200, 321300, 330100, 330200, 330300, 330400, 330500, 330600, 330700, 330800, 330900, 331000, 331100,
					 340100, 340200, 340300, 340400, 340500, 340600, 340700, 340800, 341000, 341100, 341200, 341300, 341500, 341600, 341700, 341800, 350100, 350200, 350300,
					 350400, 350500, 350600, 350700, 350800, 350900, 360100, 360200, 360300, 360400, 360500, 360600, 360700, 360800, 360900, 361000, 361100, 370100, 370200,
					 370300, 370400, 370500, 370600, 370700, 370800, 370900, 371000, 371100, 371300, 371400, 371500, 371600, 371700, 410100, 410200, 410300, 410400, 410500,
					 410600, 410700, 410800, 410900, 411000, 411100, 411200, 411300, 411400, 411500, 411600, 411700, 419001, 420100, 420200, 420300, 420500, 420600, 420700,
					 420800, 420900, 421000, 421100, 421200, 421300, 422800, 429004, 429005, 429006, 429021, 430100, 430200, 430300, 430400, 430500, 430600, 430700, 430800,
					 430900, 431000, 431100, 431200, 431300, 433100, 450100, 450200, 450300, 450400, 450500, 450600, 450700, 450800, 450900, 451000, 451100, 451200, 451300,
					 451400, 460100, 460200, 460300, 460400, 469001, 469002, 469005, 469006, 469007, 469021, 469022, 469023, 469024, 469025, 469026, 469027, 469028, 469029,
					 469030, 500000, 510100, 510300, 510400, 510500, 510600, 510700, 510800, 510900, 511000, 511100, 511300, 511400, 511500, 511600, 511700, 511800, 511900,
					 512000, 513200, 513300, 513400, 520100, 520200, 520300, 520400, 520500, 520600, 522300, 522600, 522700, 530100, 530300, 530400, 530500, 530600, 530700,
					 530800, 530900, 532300, 532500, 532600, 532800, 532900, 533100, 533300, 533400, 540100, 540200, 540300, 540400, 540500, 540600, 542500, 610100, 610200,
					 610300, 610400, 610500, 610600, 610700, 610800, 610900, 611000, 620100, 620200, 620300, 620400, 620500, 620600, 620700, 620800, 620900, 621000, 621100,
					 621200, 622900, 623000, 630100, 630200, 632200, 632300, 632500, 632600, 632700, 632800, 640100, 640200, 640300, 640400, 640500, 650100, 650200, 650400,
					 650500, 652300, 652700, 652800, 652900, 653000, 653100, 653200, 654000, 654200, 654300, 659001, 659002, 659003, 659004, 659005, 659006, 659007, 659008,
					 659009, 659010, 659011)

zhonghui_cpa_city_xx = (540100, 540200, 540300, 540400, 540500, 540600, 542500, 650100, 650200, 650400, 650500, 652300, 652700, 652800, 652900, 653000, 653100, 653200, 654000,
						654200, 654300, 659001, 659002, 659003, 659004, 659005, 659006, 659007, 659008, 659009, 659010, 659011)

# endregion

# 定义过滤条件
# region

# I.清表
push_tbx_delete = '''
TRUNCATE TABLE tbx.push
'''

# I.清暖哇表
push_nwtbx_delete = '''
DELETE FROM tbx.push where product in ("MOFANG_CPA_NW","ZHONGANMF_CPA_NW")
'''

# II.过频3天一次
ruku3d = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, 'bx_pinci' as product, 'ruku3d' as label, a.city, a.mobile from 
	((SELECT operator, city, mobile from sms.insure where pdate >= '{}' and submit_status = 1)) a
'''.format(tomorrow_time, date_before3)
# III.历史撞库不可营销数据
zk = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, 'bx_pinci' as product, 'zk' as label, a.city, a.mobile from
	(SELECT operator, city, mobile from insure.zhonganbx WHERE pdate >= 20241122 and pdate <= 20250201 and status = 0 
	UNION all SELECT operator, city, mobile from insure.nuanwa WHERE pdate >= 20241122 and pdate <= 20250201 and status = 0) a
'''.format(tomorrow_time)
# IV.保险营销黑名单
black = '''
INSERT INTO tbx.push
SELECT DISTINCT '{}' as pdate, a.operator, 'bx_pinci' as product, 'black' as label, a.city, a.mobile from 
	(select operator, city, mobile from sms.black 
	union all select operator, city, mobile from black.xhb 
	union all select operator, city, mobile from black.taikang_duodian 
	union all select operator, city, mobile from black.taikang_duodian_cbirc
	union all select operator, city, mobile from black.aibang 
	union all select operator, city, mobile from black.junbo 
	union all select operator, city, mobile from black.cmpp where status in (1,2,3)) a
'''.format(tomorrow_time)

# endregion

# 取数
NUANWA = [

	# ('CMCC_dpi_cj_30_60d_with_30d', pd_bx_ALLSQL.cj_date_with_date.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_30_60d_with_30d', date_before60, date_before30, 1, nuanwa_city, date_before30, date_before3, date_before3, 5000)),
	# ('CMCC_dpi_cj_7_30d_with_7d', pd_bx_ALLSQL.cj_date_with_date.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_7_30d_with_7d', date_before30, date_before7, 1, nuanwa_city, date_before7, date_before3, date_before3, 5000)),

	# ('CMCC_sdk_cyjd_biz4_21', pd_bx_ALLSQL.sdk_cyjd.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_sdk_cyjd_biz4_21', 20250430, 20250430, 1, nuanwa_city, 4, 21, date_before3, date_before3, 10000)),
	# ('CMCC_sdk_cyjd_biz4_22', pd_bx_ALLSQL.sdk_cyjd.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_sdk_cyjd_biz4_22', 20250430, 20250430, 1, nuanwa_city, 4, 22, date_before3, date_before3, 10000)),
	# ('CMCC_sdk_cyjd_biz4_23', pd_bx_ALLSQL.sdk_cyjd.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_sdk_cyjd_biz4_23', 20250430, 20250430, 1, nuanwa_city, 4, 23, date_before3, date_before3, 10000)),
	# ('CMCC_sdk_cyjd_biz4_24', pd_bx_ALLSQL.sdk_cyjd.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_sdk_cyjd_biz4_24', 20250430, 20250430, 1, nuanwa_city, 4, 24, date_before3, date_before3, 10000)),

	# ('CTCC_dpi_xhdx_BS046_3d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS046_3d', date_before5, tomorrow_time, 0, nuanwa_city, ('BS046', 'BS046'), date_before3, date_before3, 3000)),
	# ('CTCC_dpi_xhdx_BS046_10d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS046_10d', date_before10, tomorrow_time, 0, nuanwa_city, ('BS046', 'BS046'), date_before3, date_before3, 5000)),
	# ('CTCC_dpi_xhdx_BS042', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS042', date_before20, tomorrow_time, 0, nuanwa_city, ('BS042', 'BS042'), date_before3, date_before3, 200000)),
	# ('CTCC_dpi_xhdx_BS044', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS044', date_before20, tomorrow_time, 0, nuanwa_city, ('BS044', 'BS044'), date_before3, date_before3, 200000)),
	# ('CTCC_dpi_xhdx_BS040', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS040', date_before20, tomorrow_time, 0, nuanwa_city, ('BS040', 'BS040'), date_before3, date_before3, 200000)),
	# ('CTCC_dpi_xhdx_BS057', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS057', date_before20, tomorrow_time, 0, nuanwa_city, ('BS057', 'BS057'), date_before3, date_before3, 2000)),
	# ('CTCC_dpi_xhdx_BS058', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS058', date_before20, tomorrow_time, 0, nuanwa_city, ('BS058', 'BS058'), date_before3, date_before3, 2000)),
	# ('CTCC_dpi_xhdx_BS059', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS059', date_before20, tomorrow_time, 0, nuanwa_city, ('BS059', 'BS059'), date_before3, date_before3, 2000)),
	# ('CTCC_dpi_xhdx_BS060', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS060', date_before20, tomorrow_time, 0, nuanwa_city, ('BS060', 'BS060'), date_before3, date_before3, 2000)),
	# ('CTCC_dpi_xhdx_BS061', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS061', date_before20, tomorrow_time, 0, nuanwa_city, ('BS061', 'BS061'), date_before3, date_before3, 2000)),
	# ('CTCC_dpi_xhdx_BS038_3d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS038_3d', date_before5, tomorrow_time, 0, nuanwa_city, ('BS038', 'BS038'), date_before3, date_before3, 10000)),
	# ('CTCC_dpi_xhdx_BS038_3d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS038_3d', date_before5, tomorrow_time, 0, nuanwa_city, ('BS038', 'BS038'), date_before3, date_before3, 10000)),
	('CTCC_dpi_xhdx_BS029_10d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_dpi_xhdx_BS029_10d', date_before10, tomorrow_time, 0, nuanwa_city, ('BS029', 'BS029'), date_before3, date_before3, 10000)),
	('CTCC_dpi_xhdx_BS029_30d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_dpi_xhdx_BS029_30d', date_before30, tomorrow_time, 0, nuanwa_city, ('BS029', 'BS029'), date_before3, date_before3, 5000)),
	# ('CTCC_dpi_xhdx_BS036_3d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS036_3d', date_before5, tomorrow_time, 0, nuanwa_city, ('BS036', 'BS036'), date_before3, date_before3, 5000)),
	# ('CTCC_dpi_xhdx_BS037_3d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS037_3d', date_before5, tomorrow_time, 0, nuanwa_city, ('BS037', 'BS037'), date_before3, date_before3, 5000)),
	# ('CTCC_dpi_xhdx_BS062', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS062', date_before20, tomorrow_time, 0, nuanwa_city, ('BS062', 'BS062'), date_before3, date_before3, 10000)),
	# ('CTCC_dpi_xhdx_BS074', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS074', date_before20, tomorrow_time, 0, nuanwa_city, ('BS074', 'BS074'), date_before3, date_before3, 10000)),
	# ('CTCC_dpi_xhdx_BS_other_10d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS_other_10d', date_before10, tomorrow_time, 0, nuanwa_city, ('BS057', 'BS059', 'BS060', 'BS061',
	# 															'BS064', 'BS065', 'BS066', 'BS067', 'BS068', 'BS070', 'BS071', 'BS072', 'BS073', 'BS075', 'BS076', 'BS077'), date_before3, date_before3, 10000)),
	('CTCC_dpi_xhdx_BS_other_2_3d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_dpi_xhdx_BS_other_2_3d', date_before5, tomorrow_time, 0, nuanwa_city, ('BS058', 'BS063', 'BS069'), date_before3, date_before3, 5000)),
	('CTCC_dpi_xhdx_BS_other_2', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_dpi_xhdx_BS_other_2', date_before20, tomorrow_time, 0, nuanwa_city, ('BS058', 'BS063', 'BS069'), date_before3, date_before3, 3000)),
	# ('CTCC_dpi_xhdx_BS_other_2_status0', pd_bx_ALLSQL.bx_xhdx_mix_status0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS_other_2_status0', date_before20, tomorrow_time, 0, nuanwa_city, ('BS058', 'BS063', 'BS069'), date_before3, date_before3, 3500)),
	# ('CTCC_dpi_xhdx_BS_other_2_status1', pd_bx_ALLSQL.bx_xhdx_mix_status1.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS_other_2_status1', date_before20, tomorrow_time, 0, nuanwa_city, ('BS058', 'BS063', 'BS069'), date_before3, date_before3, 3500)),
	# ('CTCC_dpi_xhdx_BS030_10d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS030_10d', date_before10, tomorrow_time, 0, nuanwa_city, ('BS030', 'BS030'), date_before3, date_before3, 200000)),
	# ('CTCC_dpi_xhdx_BS041_3d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS041_3d', date_before5, tomorrow_time, 0, nuanwa_city, ('BS041', 'BS041'), date_before3, date_before3, 5000)),
	# ('CTCC_dpi_xhdx_BS059_10d', pd_bx_ALLSQL.bx_xhdx_mix.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_dpi_xhdx_BS059_10d', date_before10, tomorrow_time, 0, nuanwa_city, ('BS059', 'BS059'), date_before3, date_before3, 5000)),

	# ('CMCC_dpi_aitao_BS025_3d', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS025_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('BS025', 'BS025'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS026_3d', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS026_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('BS026', 'BS026'), date_before3, date_before3, 10000)),
	('CMCC_dpi_aitao_BS028_3d', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 3000)),

	# ('CMCC_dpi_aitao_BS025_3d_x1', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS025_3d_x1', date_before5, tomorrow_time, 1, nuanwa_city, ('BS025', 'BS025'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS026_3d_x1', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS026_3d_x1', date_before5, tomorrow_time, 1, nuanwa_city, ('BS026', 'BS026'), date_before3, date_before3, 10000)),
    # ('CMCC_dpi_aitao_BS103', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS103', date_before20, tomorrow_time, 1, nuanwa_city, ('BS103', 'BS103'), date_before3, date_before3, 3500)),
    # ('CMCC_dpi_aitao_BS104', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS104', date_before20, tomorrow_time, 1, nuanwa_city, ('BS104', 'BS104'), date_before3, date_before3, 3500)),
    # ('CMCC_dpi_aitao_BS105', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS105', date_before20, tomorrow_time, 1, nuanwa_city, ('BS105', 'BS105'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_aitao_BT069', pd_bx_ALLSQL.bx_aitao_bt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BT069', date_before20, tomorrow_time, 1, nuanwa_city, ('BT069', 'BT069'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_aitao_BT067', pd_bx_ALLSQL.bx_aitao_bt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BT067', date_before20, tomorrow_time, 1, nuanwa_city, ('BT067', 'BT067'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_aitao_BT600', pd_bx_ALLSQL.bx_aitao_bt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BT600', date_before20, tomorrow_time, 1, nuanwa_city, ('BT600', 'BT600'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_aitao_BT542', pd_bx_ALLSQL.bx_aitao_bt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BT542', date_before20, tomorrow_time, 1, nuanwa_city, ('BT542', 'BT542'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_aitao_BT544', pd_bx_ALLSQL.bx_aitao_bt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BT544', date_before20, tomorrow_time, 1, nuanwa_city, ('BT544', 'BT544'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_aitao_BT599', pd_bx_ALLSQL.bx_aitao_bt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BT599', date_before20, tomorrow_time, 1, nuanwa_city, ('BT599', 'BT599'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_aitao_BT531', pd_bx_ALLSQL.bx_aitao_bt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BT531', date_before20, tomorrow_time, 1, nuanwa_city, ('BT531', 'BT531'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_aitao_BT047', pd_bx_ALLSQL.bx_aitao_bt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BT047', date_before20, tomorrow_time, 1, nuanwa_city, ('BT047', 'BT047'), date_before3, date_before3, 2000)),




	('CMCC_dpi_aitao_BS106', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS106', date_before5, tomorrow_time, 1, nuanwa_city, ('BS106', 'BS106'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS107', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS107', date_before20, tomorrow_time, 1, nuanwa_city, ('BS107', 'BS107'), date_before3, date_before3, 2000)),
	('CMCC_dpi_aitao_BS108', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS108', date_before5, tomorrow_time, 1, nuanwa_city, ('BS108', 'BS108'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS109', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS109', date_before20, tomorrow_time, 1, nuanwa_city, ('BS109', 'BS109'), date_before3, date_before3, 2000)),


	# ('CMCC_dpi_aitao_BS027', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS027', date_before20, tomorrow_time, 1, nuanwa_city, ('BS027', 'BS027'), date_before3, date_before3, 3500)),
	('CMCC_dpi_aitao_BS027', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS027', date_before5, tomorrow_time, 1, nuanwa_city, ('BS027', 'BS027'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028_cspf', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_cspf', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028_Q22', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_Q22', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028_jh_cpa', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANGJH_CPA_NW', 'CMCC_dpi_aitao_BS028_jh_cpa', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028_jh_cpas', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANGJH_CPAS_NW', 'CMCC_dpi_aitao_BS028_jh_cpas', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028_Q17', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_Q17', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028_Q23', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_Q23', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS028_Q24', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_Q24', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS026', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS026', date_before20, tomorrow_time, 1, nuanwa_city, ('BS026', 'BS026'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS024', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024', 'BS024'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS024_with_cj_100242_10d', pd_bx_ALLSQL.bx_aitao_with_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_with_cj_100242_10d', date_before10, tomorrow_time, 1, nuanwa_city, ('BS024', 'BS024_25', 'BS024_30',
	# 																				'BS024_35', 'BS024_40', 'BS024_45', 'BS024_50', 'BS024_55', 'BS024_60', 'BS024_65'), (100242, 100242), date_before3, date_before3, 5000)),

	# ('CMCC_dpi_aitao_BS025', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS025', date_before20, tomorrow_time, 1, nuanwa_city, ('BS025', 'BS025'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS024_25', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_25', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024_25', 'BS024_25'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS024_30', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_30', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024_30', 'BS024_30'), date_before3, date_before3, 30000)),
	# ('CMCC_dpi_aitao_BS024_35', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_35', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024_35', 'BS024_35'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS024_40', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_40', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024_40', 'BS024_40'), date_before3, date_before3, 30000)),
	# ('CMCC_dpi_aitao_BS024_45', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_45', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024_45', 'BS024_45'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS024_50', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_50', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024_50', 'BS024_50'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS024_55', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_55', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024_55', 'BS024_55'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS024_60', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_60', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024_60', 'BS024_60'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS024_65', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_65', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024_65', 'BS024_65'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS024_70', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_70', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024_70', 'BS024_70'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS024_70', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_70', date_before10, tomorrow_time, 1, nuanwa_city, ('BS024_70', 'BS024_70'), date_before3, date_before3, 5000)),
	('CMCC_dpi_aitao_BS024_75', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_75', date_before5, tomorrow_time, 1, nuanwa_city, ('BS024_75', 'BS024_75'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS024_80', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_80', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024_80', 'BS024_80'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS024_PV10', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_PV10', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024_PV10', 'BS024_PV10'), date_before3, date_before3, 5000)),

	# ('CMCC_dpi_aitao_BS028_25', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_25', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028_25', 'BS028_25'), date_before3, date_before3, 200000)),
	('CMCC_dpi_aitao_BS028_30', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_30', date_before5, tomorrow_time, 1, nuanwa_city, ('BS028_30', 'BS028_30'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028_35', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_35', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028_35', 'BS028_35'), date_before3, date_before3, 200000)),
	# ('CMCC_dpi_aitao_BS028_40', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_40', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028_40', 'BS028_40'), date_before3, date_before3, 3000)),
	# ('CMCC_dpi_aitao_BS028_45', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_45', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028_45', 'BS028_45'), date_before3, date_before3, 200000)),
	# ('CMCC_dpi_aitao_BS028_50', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_50', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028_50', 'BS028_50'), date_before3, date_before3, 3000)),
	# ('CMCC_dpi_aitao_BS028_55', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_55', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028_55', 'BS028_55'), date_before3, date_before3, 200000)),
	('CMCC_dpi_aitao_BS028_60', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_60', date_before5, tomorrow_time, 1, nuanwa_city, ('BS028_60', 'BS028_60'), date_before3, date_before3, 200000)),
	('CMCC_dpi_aitao_BS028_65', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_65', date_before5, tomorrow_time, 1, nuanwa_city, ('BS028_65', 'BS028_65'), date_before3, date_before3, 10000)),
	('CMCC_dpi_aitao_BS028_65_badclick', pd_bx_ALLSQL.bx_aitao_badclick.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_65_badclick', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028_65', 'BS028_65'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028_65_badclick', pd_bx_ALLSQL.bx_aitao_badclick.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_dpi_aitao_BS028_65_badclick', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028_65', 'BS028_65'), date_before3, date_before3, 1186)),
	('CMCC_dpi_aitao_BS028_70', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_70', date_before5, tomorrow_time, 1, nuanwa_city, ('BS028_70', 'BS028_70'), date_before3, date_before3, 200000)),
	('CMCC_dpi_aitao_BS028_75', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_75', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028_75', 'BS028_75'), date_before3, date_before3, 200000)),
	# ('CMCC_dpi_aitao_BS028_80', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_80', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028_80', 'BS028_80'), date_before3, date_before3, 200000)),

	# ('CMCC_dpi_aitao_BS028_55_20d_40d', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_55_20d_40d', date_before40, date_before20, 1, nuanwa_city, ('BS028_55', 'BS028_55'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS028_60_20d_40d', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_60_20d_40d', date_before40, date_before20, 1, nuanwa_city, ('BS028_60', 'BS028_60'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS028', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS028_xz_15d', pd_bx_ALLSQL.bx_aitao_xz.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_xz_15d', date_before15, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before15, date_before3, date_before3, 1500)),
	# ('CMCC_dpi_aitao_BS028_xz_15d', pd_bx_ALLSQL.bx_aitao_xz.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_dpi_aitao_BS028_xz_15d', date_before15, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before15, date_before3, date_before3, 1500)),
	# ('CMCC_dpi_aitao_BS028_status1', pd_bx_ALLSQL.bx_aitao_status1.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_status1', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_aitao_BS028_status0', pd_bx_ALLSQL.bx_aitao_status0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_status0', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_aitao_BS028_x1', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_x1', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 200000)),
	# ('CMCC_dpi_aitao_BS024_x1', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS024_x1', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024', 'BS024'), date_before3, date_before3, 200000)),
	# ('CMCC_dpi_aitao_BS025_x1', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS025_x1', date_before20, tomorrow_time, 1, nuanwa_city, ('BS025', 'BS025'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS026_x1', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS026_x1', date_before20, tomorrow_time, 1, nuanwa_city, ('BS026', 'BS026'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS078', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS078', date_before20, tomorrow_time, 1, nuanwa_city, ('BS078', 'BS078'), date_before3, date_before3, 3000)),
	# ('CMCC_dpi_aitao_BS079', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS079', date_before20, tomorrow_time, 1, nuanwa_city, ('BS079', 'BS079'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS080', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS080', date_before20, tomorrow_time, 1, nuanwa_city, ('BS080', 'BS080'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS083', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS083', date_before20, tomorrow_time, 1, nuanwa_city, ('BS083', 'BS083'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS084', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS084', date_before20, tomorrow_time, 1, nuanwa_city, ('BS084', 'BS084'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS085', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS085', date_before20, tomorrow_time, 1, nuanwa_city, ('BS085', 'BS085'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_aitao_BS086', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS086', date_before20, tomorrow_time, 1, nuanwa_city, ('BS086', 'BS086'), date_before3, date_before3, 5000)),

	# ('CMCC_dpi_cj_100250_10d', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100250_10d', date_before10, tomorrow_time, 1, nuanwa_city, ('100250', '100250'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_cj_100250_zad_status0', pd_bx_ALLSQL.bx_cj_zad_status0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100250_zad_status0', date_before20, tomorrow_time, 1, nuanwa_city, ('100250', '100250'), date_before3, date_before3, 200000)),
	('CMCC_dpi_cj_100251_3d', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100251_3d', date_before3, tomorrow_time, 1, nuanwa_city, ('100251', '100251'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_cj_100251_3d', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_dpi_cj_100251_3d', date_before3, tomorrow_time, 1, nuanwa_city, ('100251', '100251'), date_before3, date_before3, 1000)),
	# ('CMCC_dpi_cj_100250_3d', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100250_3d', date_before3, tomorrow_time, 1, nuanwa_city, ('100250', '100250'), date_before3, date_before3, 10000)),
	('CMCC_dpi_cj_100250_3d', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100250_3d', date_before3, tomorrow_time, 1, nuanwa_city, ('100250', '100250'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_cj_100251', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100251', date_before20, tomorrow_time, 1, nuanwa_city, ('100251', '100251'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_cj_100245', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100245', date_before10, tomorrow_time, 1, nuanwa_city, ('100245', '100245'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_cj_100242', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100242', date_before10, tomorrow_time, 1, nuanwa_city, ('100242', '100242'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_cj_100243', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100243', date_before10, tomorrow_time, 1, nuanwa_city, ('100243', '100243'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_cj_100706', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100706', date_before20, tomorrow_time, 1, nuanwa_city, ('100706', '100706'), date_before3, date_before3, 10000)),

	# ('CMCC_dpi_cj_100243_3', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100243_3', 20250415, tomorrow_time, 1, nuanwa_city, ('100243', '100243'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_cj_100242_4', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100242_4', 20250425, tomorrow_time, 1, nuanwa_city, ('100242', '100242'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_cj_100242_3', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100242_3', 20250415, 20250424, 1, nuanwa_city, ('100242', '100242'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_cj_100242_3_Q17', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100242_3_Q17', 20250415, tomorrow_time, 1, nuanwa_city, ('100242', '100242'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_cj_100251_3', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100251_3', 20250415, tomorrow_time, 1, nuanwa_city, ('100251', '100251'), date_before3, date_before3, 10000)),

	# ('CMCC_dpi_cj_100243_3d', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100243_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('100243', '100243'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_cj_100245_3d', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100245_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('100245', '100245'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_cj_100242_3d', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100242_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('100242', '100242'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_cj_100251_3d', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100251_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('100251', '100251'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_cj_100242_3d_x1', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_100242_3d_x1', date_before5, tomorrow_time, 1, nuanwa_city, ('100242', '100242'), date_before3, date_before3, 200000)),
	# ('CMCC_dpi_cj_101246', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_101246', date_before20, tomorrow_time, 1, nuanwa_city, ('101246', '101246'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_cj_101247', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_101247', date_before20, tomorrow_time, 1, nuanwa_city, ('101247', '101247'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_cj_101248', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_101248', date_before20, tomorrow_time, 1, nuanwa_city, ('101248', '101248'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_cj_101249', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_101249', date_before20, tomorrow_time, 1, nuanwa_city, ('101249', '101249'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_cj_101250', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_101250', date_before20, tomorrow_time, 1, nuanwa_city, ('101250', '101250'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_cj_101251', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_101251', date_before20, tomorrow_time, 1, nuanwa_city, ('101251', '101251'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_cj_101252', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_101252', date_before20, tomorrow_time, 1, nuanwa_city, ('101252', '101252'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_cj_101253', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_101253', date_before20, tomorrow_time, 1, nuanwa_city, ('101253', '101253'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_cj_101254', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_101254', date_before20, tomorrow_time, 1, nuanwa_city, ('101254', '101254'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_cj_101255', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_101255', date_before20, tomorrow_time, 1, nuanwa_city, ('101255', '101255'), date_before3, date_before3, 2000)),
	# ('CMCC_dpi_cj_101256', pd_bx_ALLSQL.bx_cj.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_cj_101256', date_before20, tomorrow_time, 1, nuanwa_city, ('101256', '101256'), date_before3, date_before3, 2000)),

	# ('CMCC_dpi_yax_BT099_10d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT099_10d', date_before10, tomorrow_time, 1, nuanwa_city, ('BT099', 'BT099'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_yax_BT099_3d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_dpi_yax_BT099_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('BT099', 'BT099'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_yax_BT599_10d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT599_10d', date_before10, tomorrow_time, 1, nuanwa_city, ('BT599', 'BT599'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_yax_BT599_3d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT599_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('BT599', 'BT599'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_yax_BT583_10d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT583_10d', date_before10, tomorrow_time, 1, nuanwa_city, ('BT583', 'BT583'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_yax_BT107_3d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT107_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('BT107', 'BT107'), date_before3, date_before3, 5000)),
	('CMCC_dpi_yax_BT541_3d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT541_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('BT541', 'BT541'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_yax_BT984', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT541', date_before20, tomorrow_time, 1, nuanwa_city, ('BT984', 'BT984'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_yax_BT985', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT541', date_before20, tomorrow_time, 1, nuanwa_city, ('BT985', 'BT985'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_yax_BT986', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT541', date_before20, tomorrow_time, 1, nuanwa_city, ('BT986', 'BT986'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_yax_BT987', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT541', date_before20, tomorrow_time, 1, nuanwa_city, ('BT987', 'BT987'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_yax_BT988', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT541', date_before20, tomorrow_time, 1, nuanwa_city, ('BT988', 'BT988'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_yax_BT989', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT541', date_before20, tomorrow_time, 1, nuanwa_city, ('BT989', 'BT989'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_yax_BT209', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT209', date_before20, tomorrow_time, 1, nuanwa_city, ('BT209', 'BT209'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_yax_BT544', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT544', date_before20, tomorrow_time, 1, nuanwa_city, ('BT544', 'BT544'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_yax_BT184', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT184', date_before20, tomorrow_time, 1, nuanwa_city, ('BT184', 'BT184'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_yax_BT068_3d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT068_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('BT068', 'BT068'), date_before3, date_before3, 200000)),
	# ('CMCC_dpi_yax_BT068_10d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT068_10d', date_before10, tomorrow_time, 1, nuanwa_city, ('BT068', 'BT068'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_yax_BT531_3d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT531_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('BT531', 'BT531'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_yax_BT541_3d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT541_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('BT541', 'BT541'), date_before3, date_before3, 200000)),
	# ('CMCC_dpi_yax_BT541_10d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT541_10d', date_before10, tomorrow_time, 1, nuanwa_city, ('BT541', 'BT541'), date_before3, date_before3, 5000)),
	# ('CMCC_dpi_yax_BT063', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT063', date_before20, tomorrow_time, 1, nuanwa_city, ('BT063', 'BT063'), date_before3, date_before3, 5000)),

	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a002', pd_bx_ALLSQL.bx_yax_lt_mb.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a002', date_before5, tomorrow_time, 2, nuanwa_city, ('bx_A_a_a002', 'bx_A_a_a002'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a003', pd_bx_ALLSQL.bx_yax_lt_mb.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a003', date_before5, tomorrow_time, 2, nuanwa_city, ('bx_A_a_a003', 'bx_A_a_a003'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a004', pd_bx_ALLSQL.bx_yax_lt_mb.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a004', date_before5, tomorrow_time, 2, nuanwa_city, ('bx_A_a_a004', 'bx_A_a_a004'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a007', pd_bx_ALLSQL.bx_yax_lt_mb.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a007', date_before5, tomorrow_time, 2, nuanwa_city, ('bx_A_a_a007', 'bx_A_a_a007'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a008', pd_bx_ALLSQL.bx_yax_lt_mb.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a008', date_before5, tomorrow_time, 2, nuanwa_city, ('bx_A_a_a008', 'bx_A_a_a008'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a009', pd_bx_ALLSQL.bx_yax_lt_mb.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a009', date_before5, tomorrow_time, 2, nuanwa_city, ('bx_A_a_a009', 'bx_A_a_a009'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a010', pd_bx_ALLSQL.bx_yax_lt_mb.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a010', date_before5, tomorrow_time, 2, nuanwa_city, ('bx_A_a_a010', 'bx_A_a_a010'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a011', pd_bx_ALLSQL.bx_yax_lt_mb.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a011', date_before5, tomorrow_time, 2, nuanwa_city, ('bx_A_a_a011', 'bx_A_a_a011'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a018', pd_bx_ALLSQL.bx_yax_lt_mb.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a018', date_before5, tomorrow_time, 2, nuanwa_city, ('bx_A_a_a018', 'bx_A_a_a018'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_B_a_a017', pd_bx_ALLSQL.bx_yax_lt_mb.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_B_a_a017', date_before5, tomorrow_time, 2, nuanwa_city, ('bx_B_a_a017', 'bx_B_a_a017'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_B_a_a015', pd_bx_ALLSQL.bx_yax_lt_mb.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_B_a_a015', date_before5, tomorrow_time, 2, nuanwa_city, ('bx_B_a_a015', 'bx_B_a_a015'), date_before3, date_before3, 2000)),

	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a002', pd_bx_ALLSQL.bx_push_yesterday.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a002', 20250701, 2, nuanwa_city, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a002',2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a003', pd_bx_ALLSQL.bx_push_yesterday.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a003', 20250701, 2, nuanwa_city, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a003', 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a004', pd_bx_ALLSQL.bx_push_yesterday.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a004', 20250701, 2, nuanwa_city, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a003', 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a007', pd_bx_ALLSQL.bx_push_yesterday.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a007', 20250701, 2, nuanwa_city, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a003', 2000)),
	# ('CUCC_dpi_yax_lt_mb_bx_A_a_a008', pd_bx_ALLSQL.bx_push_yesterday.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a008', 20250701, 2, nuanwa_city, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_mb_bx_A_a_a003', 2000)),

	# ('CUCC_dpi_yax_lt_BS050_3d_city_you', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_3d_city_you', date_before5, tomorrow_time, 2, nuanwa_city_you, ('BS050', 'BS050'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_BS050_3d_city_lie', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_3d_city_lie', date_before5, tomorrow_time, 2, nuanwa_city_lie, ('BS050', 'BS050'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_BS050_3d_alibx329', pd_bx_ALLSQL.bx_yax_lt_alibx329.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_dpi_yax_lt_BS050_3d_alibx329', date_before5, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), 9800, date_before3, date_before3, 3000)),
	('CUCC_dpi_yax_lt_BS050_3d', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_3d', date_before5, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 200000)),
	# ('CUCC_dpi_yax_lt_BS050_with_age_level_0', pd_bx_ALLSQL.bx_yax_lt_with_age.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_with_age_level_0', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), 0, date_before3, date_before3, 3000)),
	# ('CUCC_dpi_yax_lt_BS050_with_age_level_1', pd_bx_ALLSQL.bx_yax_lt_with_age.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_with_age_level_1', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), 1, date_before3, date_before3, 3000)),
	# ('CUCC_dpi_yax_lt_BS050_with_age_level_2', pd_bx_ALLSQL.bx_yax_lt_with_age.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_with_age_level_2', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), 2, date_before3, date_before3, 3000)),
	# ('CUCC_dpi_yax_lt_BS050_with_age_level_3', pd_bx_ALLSQL.bx_yax_lt_with_age.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_with_age_level_3', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), 3, date_before3, date_before3, 3000)),
	# ('CUCC_dpi_yax_lt_BS050_with_age_level_4', pd_bx_ALLSQL.bx_yax_lt_with_age.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_with_age_level_4', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), 4, date_before3, date_before3, 3000)),
	# ('CUCC_dpi_yax_lt_BS050_with_age_level_5', pd_bx_ALLSQL.bx_yax_lt_with_age.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_with_age_level_5', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), 5, date_before3, date_before3, 3000)),
	# ('CUCC_dpi_yax_lt_BS050_with_age_level_6', pd_bx_ALLSQL.bx_yax_lt_with_age.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_with_age_level_6', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), 6, date_before3, date_before3, 3000)),
	# ('CUCC_dpi_yax_lt_BS050_with_age_level_7', pd_bx_ALLSQL.bx_yax_lt_with_age.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_with_age_level_7', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), 7, date_before3, date_before3, 3000)),
	# ('CUCC_dpi_yax_lt_BS050_with_age_level_8', pd_bx_ALLSQL.bx_yax_lt_with_age.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_with_age_level_8', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), 8, date_before3, date_before3, 3000)),
	# ('CUCC_dpi_yax_lt_BS050_with_age_level_9', pd_bx_ALLSQL.bx_yax_lt_with_age.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_with_age_level_9', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), 9, date_before3, date_before3, 3000)),
	# ('CUCC_dpi_yax_lt_BS050_with_age_level_10', pd_bx_ALLSQL.bx_yax_lt_with_age.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_with_age_level_10', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), 10, date_before3, date_before3, 3000)),
	# ('CUCC_dpi_yax_lt_BS050', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS050_10d', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_10d', get_datetime4(tomorrow_time,10), tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS050_Q26', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_Q26', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS050_Q1', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_Q1', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS050_Q24', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_Q24', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS050_cspf_T10', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_cspf_T10', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS050_cspf_T11', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_cspf_T11', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS050_cspf_Q23', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_cspf_Q23', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 5000)),
	# ('CUCC_dpi_yax_lt_BS050_cspf_Q24', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_cspf_Q24', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 5000)),
	# ('CUCC_dpi_yax_lt_BS050_cspf_Q11', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_cspf_Q11', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 5000)),
	# ('CUCC_dpi_yax_lt_BS050_cspf_Q15', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_cspf_Q15', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 5000)),
	# ('CUCC_dpi_yax_lt_BS050_yixiancity', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_yixiancity', date_before20, tomorrow_time, 2, nuanwa_yixian_city, ('BS050', 'BS050'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS050_yixiancity_cspf', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_yixiancity_cspf', date_before20, tomorrow_time, 2, nuanwa_yixian_city, ('BS050', 'BS050'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS050_yxothercity_cspf', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_yxothercity_cspf', date_before20, tomorrow_time, 2, nuanwa_yxother_city, ('BS050', 'BS050'), date_before3, date_before3, 5000)),
	# ('CUCC_dpi_yax_lt_BS050_cspf', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050_cspf', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS050', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS050', date_before20, tomorrow_time, 2, nuanwa_city, ('BS050', 'BS050'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS144_Q15', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS144_Q15', date_before20, tomorrow_time, 2, nuanwa_city, ('BS144', 'BS144'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS144', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS144', date_before20, tomorrow_time, 2, nuanwa_city, ('BS144', 'BS144'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS144_3d', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS144_3d', date_before5, tomorrow_time, 2, nuanwa_city, ('BS144', 'BS144'), date_before3, date_before3, 5000)),
	# ('CUCC_dpi_yax_lt_BS057', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS057', date_before20, tomorrow_time, 2, nuanwa_city, ('BS057', 'BS057'), date_before3, date_before3, 10000)),

	# ('CUCC_dpi_yax_lt_BS058_T14', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS058_T14', date_before20, tomorrow_time, 2, nuanwa_city, ('BS058', 'BS058'), date_before3, date_before3, 1000)),
	('CUCC_dpi_yax_lt_BS058_3d', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS058_3d', date_before5, tomorrow_time, 2, nuanwa_city, ('BS058', 'BS058'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS058', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_dpi_yax_lt_BS058', date_before20, tomorrow_time, 2, nuanwa_city, ('BS058', 'BS058'), date_before3, date_before3, 10000)),
	# ('CUCC_dpi_yax_lt_BS058_3d', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS058_3d', date_before3, tomorrow_time, 2, nuanwa_city, ('BS058', 'BS058'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_BS055_3d', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS055_3d', date_before3, tomorrow_time, 2, nuanwa_city, ('BS055', 'BS055'), date_before3, date_before3, 2000)),
	# ('CUCC_dpi_yax_lt_BS056_3d', pd_bx_ALLSQL.bx_yax_lt.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_dpi_yax_lt_BS056_3d', date_before3, tomorrow_time, 2, nuanwa_city, ('BS056', 'BS056'), date_before3, date_before3, 2000)),

	# ('CMCC_bx_click_and_alibx329', pd_bx_ALLSQL.bx_click_alibx329.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_and_alibx329', date_before60, date_before30, 1, nuanwa_city, 9800,date_before3, date_before3, 1500)),
	# ('CMCC_bx_click_and_alibx329', pd_bx_ALLSQL.bx_click_alibx329.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_bx_click_and_alibx329', date_before60, date_before30, 1, nuanwa_city, 9800,date_before3, date_before3, 1500)),
 	('CTCC_bx_click_and_alibx329', pd_bx_ALLSQL.bx_click_alibx329.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_click_and_alibx329', date_before60, date_before30, 0, nuanwa_city, 9800,date_before3, date_before3, 3000)),
	# ('CMCC_bx_dpi_60d_and_alibx329', pd_bx_ALLSQL.bx_dpi_and_alibx329.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_dpi_60d_and_alibx329', date_before60, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 9000, 3000)),
	# ('CMCC_bx_alibx329', pd_bx_ALLSQL.bx_alibx329.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_alibx329', 9800, 1, nuanwa_city, date_before3, date_before3, 3000)),
	# ('CMCC_bx_alibx329_100', pd_bx_ALLSQL.bx_alibx329.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_alibx329_100', 10000, 1, nuanwa_city, date_before3, date_before3, 3000)),
	# ('CUCC_bx_alibx329', pd_bx_ALLSQL.bx_alibx329.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_alibx329', 9800, 2, nuanwa_city, date_before3, date_before3, 3000)),

	# ('CMCC_bx_alibx362', pd_bx_ALLSQL.bx_alibx362.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_alibx362', 10000, 1, nuanwa_city, date_before3, date_before3, 3000)),

	# ('CMCC_bx_click_and_alibx331', pd_bx_ALLSQL.bx_click_alibx329.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_and_alibx331', date_before60, date_before30, 1, nuanwa_city, 9000,date_before3, date_before3, 3000)),
	# ('CMCC_bx_click_and_alibx362', pd_bx_ALLSQL.bx_click_alibx362.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_and_alibx362', date_before60, date_before30, 1, nuanwa_city, 9000,date_before3, date_before3, 3000)),
	# ('CUCC_bx_click_and_alibx362', pd_bx_ALLSQL.bx_click_alibx362.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_bx_click_and_alibx362', date_before60, date_before30, 2, nuanwa_city, 9000,date_before3, date_before3, 3000)),
	('CTCC_bx_click_and_alibx362', pd_bx_ALLSQL.bx_click_alibx362.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_click_and_alibx362', date_before60, date_before30, 0, nuanwa_city, 9000,date_before3, date_before3, 3000)),

	# ('CMCC_bx_click_30d_and_bxdata', pd_bx_ALLSQL.bx_click_bxdata.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_bx_click_30d_and_bxdata', date_before30, tomorrow_time, 1, nuanwa_city, date_before30, tomorrow_time, date_before3, date_before3, 695)),
	# ('CMCC_bx_click_30d_and_bxdata', pd_bx_ALLSQL.bx_click_bxdata.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_and_bxdata', date_before30, tomorrow_time, 1, nuanwa_city, date_before30, tomorrow_time, date_before3, date_before3, 696)),
	# ('CMCC_bx_click_30d_60d_and_bxdata', pd_bx_ALLSQL.bx_click_bxdata.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_bx_click_30d_60d_and_bxdata', date_before60, date_before30, 1, nuanwa_city, date_before30, tomorrow_time, date_before3, date_before3, 4564)),
	# ('CMCC_bx_click_30d_60d_and_bxdata', pd_bx_ALLSQL.bx_click_bxdata.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_60d_and_bxdata', date_before60, date_before30, 1, nuanwa_city, date_before30, tomorrow_time, date_before3, date_before3, 4564)),
	('CUCC_bx_click_30d_60d_and_bxdata', pd_bx_ALLSQL.bx_click_bxdata.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_bx_click_30d_60d_and_bxdata', date_before60, date_before30, 2, nuanwa_city, date_before30, tomorrow_time, date_before3, date_before3, 986)),
	('CUCC_bx_click_30d_60d_and_bxdata', pd_bx_ALLSQL.bx_click_bxdata.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_click_30d_60d_and_bxdata', date_before60, date_before30, 2, nuanwa_city, date_before30, tomorrow_time, date_before3, date_before3, 10000)),

	# ('CMCC_bx_click_60d_90d_and_alibx362', pd_bx_ALLSQL.bx_click_alibx362.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_60d_90d_and_alibx362', date_before90, date_before60, 1, nuanwa_city, 9000, date_before3, date_before3, 3000)),

	# ('CMCC_xd_click_and_alibx329', pd_bx_ALLSQL.xd_click_alibx329.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_xd_click_and_alibx329', date_before60, date_before30, 1, nuanwa_city, 9800, date_before3, date_before3, 3000)),

	# ('CMCC_bx_click_30d_T0', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_bx_click_30d_T0', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 2000)),
	('CMCC_bx_click_7d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_7d', date_before7, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 10000)),
	('CMCC_bx_click_15d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_15d', date_before15, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CMCC_bx_click_7d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_7d', date_before7, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 3000)),
	# ('CMCC_bx_click_30d_T0', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_T0', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 2000)),
	# ('CMCC_bx_click_30d_Q26', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_Q26', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 2000)),
	('CMCC_bx_click_30d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 20000)),
	# ('CMCC_bx_click_30d_T18', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_T18', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 3000)),
	# ('CMCC_bx_click_30d_T14', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_T14', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bx_click_30d_T17', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_T17', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 5000)),
	# ('CMCC_bx_click_30d_Q27', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_Q27', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 5000)),

	# ('CMCC_bx_click_30d_Q15', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_Q15', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 20000)),
	# ('CMCC_bx_click_30d_T7', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_T7', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CMCC_bx_click_30d_T0', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_T0', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CMCC_bx_click_30d_x1', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_x1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CMCC_bx_click_30d_60d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_60d', date_before60, date_before30, 1, nuanwa_city, date_before3, date_before3, 5000)),
	('CTCC_bx_click_30d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_click_30d', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 3000)),
	# ('CTCC_bx_click_30d_T0', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_click_30d_T0', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 3000)),
	# ('CTCC_bx_click_30d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bx_click_30d', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 20000)),
	('CTCC_bx_click_30d_60d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_click_30d_60d', date_before60, date_before30, 0, nuanwa_city, date_before3, date_before3, 2000)),

	# ('CUCC_bx_click_30d_Q2', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_click_30d_Q2', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 2000),),
	# ('CUCC_bx_click_30d_T20', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_click_30d_T20', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 1500)),
	('CUCC_bx_click_30d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_bx_click_30d', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 1075)),
	('CUCC_bx_click_30d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_click_30d', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CUCC_bx_click_30d_T0', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_click_30d_T0', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000),),
	# ('CUCC_bx_click_30d_60d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_click_30d_60d', date_before60, date_before30, 2, nuanwa_city, date_before3, date_before3, 5000)),
	# ('CUCC_bx_click_60d_90d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_click_60d_90d', date_before90, date_before60, 2, nuanwa_city, date_before3, date_before3, 10000)),

	# ('CUCC_bx_zk_status_0', pd_bx_ALLSQL.bx_zk_status_0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_zk_status_0', 20250201, 2, nuanwa_city, 20250201, 2, nuanwa_city, date_before3, date_before3, 5000)),
	('CUCC_bx_dpi_xz_and_nwzk0_30d', pd_bx_ALLSQL.bx_nwzk_status_0.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_bx_dpi_xz_and_nwzk0_30d', date_before30, 2, nuanwa_city, date_before3, date_before3, 330)),
	('CUCC_bx_dpi_xz_and_nwzk0_30d', pd_bx_ALLSQL.bx_nwzk_status_0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_dpi_xz_and_nwzk0_30d', date_before30, 2, nuanwa_city, date_before3, date_before3, 10000)),
	('CUCC_bx_dpi_xz_and_zazk0_30d', pd_bx_ALLSQL.bx_zazk_status_0.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_bx_dpi_xz_and_zazk0_30d', date_before30, 2, nuanwa_city, date_before3, date_before3, 10000)),
	('CUCC_bx_dpi_xz_and_bxzk0_30d', pd_bx_ALLSQL.bx_zk_status_0.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_bx_dpi_xz_and_bxzk0_30d', date_before30, 2, nuanwa_city, date_before30, 2, nuanwa_city, date_before3, date_before3, 5000)),
	('CUCC_bx_dpi_xz_and_bxzk0_60d', pd_bx_ALLSQL.bx_zk_status_0.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_bx_dpi_xz_and_bxzk0_60d', date_before60, 2, nuanwa_city, date_before60, 2, nuanwa_city, date_before3, date_before3, 494)),
	('CUCC_bx_dpi_xz_and_bxzk0_60d', pd_bx_ALLSQL.bx_zk_status_0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_dpi_xz_and_bxzk0_60d', date_before60, 2, nuanwa_city, date_before60, 2, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CMCC_bx_dpi_xz_and_bxzk0_30d', pd_bx_ALLSQL.bx_zk_status_0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_dpi_xz_and_bxzk0_30d', date_before30, 1, nuanwa_city, date_before30, 1, nuanwa_city, date_before3, date_before3, 2000)),

	('CTCC_bx_dpi_xz_and_nwzk0_30d', pd_bx_ALLSQL.bx_nwzk_status_0.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_dpi_xz_and_nwzk0_30d', date_before30, 0, nuanwa_city, date_before3, date_before3, 10000)),
	('CTCC_bx_dpi_xz_and_zazk0_30d', pd_bx_ALLSQL.bx_zazk_status_0.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_dpi_xz_and_zazk0_30d', date_before30, 0, nuanwa_city, date_before3, date_before3, 10000)),
	('CTCC_bx_dpi_xz_and_bxzk0_30d', pd_bx_ALLSQL.bx_zk_status_0.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_dpi_xz_and_bxzk0_30d', date_before30, 0, nuanwa_city, date_before30, 0, nuanwa_city, date_before3, date_before3, 5000)),
	# ('CMCC_bx_alibx329_and_bxzk0', pd_bx_ALLSQL.bx_zk_status_0_alibx329.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_alibx329_and_bxzk0', 20250201, 1, nuanwa_city, 20250201, 1, nuanwa_city, 9800, date_before3, date_before3, 2000)),

	('CMCC_bx_dpi_7d_and_bxzk0', pd_bx_ALLSQL.bx_dpi_and_bxzk0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_dpi_7d_and_bxzk0', date_before7, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 100000)),
	# ('CMCC_bx_dpi_30d_and_bxzk0', pd_bx_ALLSQL.bx_dpi_and_bxzk0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_dpi_30d_and_bxzk0', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 2000)),
	('CUCC_bx_dpi_30d_and_bxzk0', pd_bx_ALLSQL.bx_dpi_and_bxzk0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_dpi_30d_and_bxzk0', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 3188)),
	('CUCC_bx_dpi_30d_and_bxzk0', pd_bx_ALLSQL.bx_dpi_and_bxzk0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_dpi_30d_and_bxzk0', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 3188)),
	# ('CMCC_bx_dpi_30d_60d_and_bxzk0', pd_bx_ALLSQL.bx_dpi_and_bxzk0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_dpi_30d_60d_and_bxzk0', date_before60, date_before30, 1, nuanwa_city, date_before3, date_before3, 2000)),
	('CTCC_bx_dpi_30d_and_bxzk0', pd_bx_ALLSQL.bx_dpi_and_bxzk0.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_dpi_30d_and_bxzk0', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 3000)),
	('CTCC_bx_dpi_60d_and_bxzk0', pd_bx_ALLSQL.bx_dpi_and_bxzk0.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_dpi_60d_and_bxzk0', date_before60, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 3000)),
	# ('CTCC_bx_dpi_30d_60d_and_bxzk0_x1', pd_bx_ALLSQL.bx_dpi_and_bxzk0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bx_dpi_30d_60d_and_bxzk0_x1', date_before60, date_before30, 0, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CTCC_bx_dpi_30d_60d_and_bxzk0', pd_bx_ALLSQL.bx_dpi_and_bxzk0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bx_dpi_30d_60d_and_bxzk0', date_before60, date_before30, 0, nuanwa_city, date_before3, date_before3, 2000)),

	# ('CMCC_bx_dpi_cj_and_bxzk0', pd_bx_ALLSQL.bx_dpi_cj_and_bxzk0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_dpi_cj_and_bxzk0', 20240101, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 5000)),

	('CTCC_bx_click_30d_60d_and_bxzk0', pd_bx_ALLSQL.bx_click_and_bxzk0_ti.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_click_30d_60d_and_bxzk0', date_before60, date_before30, 0, nuanwa_city, date_before3, date_before3, 2500)),
	# ('CTCC_bx_click_30d_60d_and_bxzk0', pd_bx_ALLSQL.bx_click_and_bxzk0_ti.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bx_click_30d_60d_and_bxzk0', date_before60, date_before30, 0, nuanwa_city, date_before3, date_before3, 2500)),
	# ('CMCC_bx_click_30d_60d_and_bxzk0_x1', pd_bx_ALLSQL.bx_click_and_bxzk0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_60d_and_bxzk0_x1', date_before60, date_before30, 1, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CMCC_bx_click_30d_60d_and_bxzk0', pd_bx_ALLSQL.bx_click_and_bxzk0_ti.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_60d_and_bxzk0', date_before60, date_before30, 1, nuanwa_city, date_before3, date_before3, 2000)),
	# ('CMCC_bx_click_30d_60d_and_bxzk0_zad_status0', pd_bx_ALLSQL.bx_click_and_bxzk0_ti_zad_status0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_60d_and_bxzk0_zad_status0', date_before60, date_before30, 1, nuanwa_city, date_before3, date_before3, 20000)),
	# ('CMCC_bx_click_30d_60d_and_bxzk0', pd_bx_ALLSQL.bx_click_and_bxzk0_ti.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_60d_and_bxzk0', date_before60, date_before30, 1, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CMCC_bx_click_60d_90d_and_bxzk0', pd_bx_ALLSQL.bx_click_and_bxzk0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_60d_90d_and_bxzk0', date_before90, date_before60, 1, nuanwa_city, date_before3, date_before3, 10000)),

	# ('CTCC_credit_click_and_bxzk_status_0', pd_bx_ALLSQL.credit_click_and_bxzk_status_0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_credit_click_and_bxzk_status_0', 20200101, 0, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CUCC_credit_click_and_bxzk_status_0', pd_bx_ALLSQL.credit_click_and_bxzk_status_0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_credit_click_and_bxzk_status_0', 20200101, 2, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CMCC_credit_click_and_bxzk_status_0', pd_bx_ALLSQL.credit_click_and_bxzk_status_0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_credit_click_and_bxzk_status_0', 20200101, 1, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CMCC_credit_click_and_bxzk_status_0_x1', pd_bx_ALLSQL.credit_click_and_bxzk_status_0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_credit_click_and_bxzk_status_0_x1', 20200101, 1, nuanwa_city, date_before3, date_before3, 10000)),

	# ('CTCC_bx_dpi_fre_above_3', pd_bx_ALLSQL.bx_dpi_time_fre.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bx_dpi_fre_above_3', date_before30, tomorrow_time, 0, nuanwa_city, 3, 100, date_before3, date_before3, 5000)),
	# ('CMCC_bx_dpi_fre_above_4', pd_bx_ALLSQL.bx_dpi_time_fre.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_dpi_fre_above_4', date_before30, tomorrow_time, 1, nuanwa_city, 4, 100, date_before3, date_before3, 5000)),

	# ('CTCC_bx_click_30d_60d_fre_above_2', pd_bx_ALLSQL.bx_click_time_fre.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bx_click_30d_60d_fre_above_2', date_before60, date_before30, 0, nuanwa_city, 2, 100, date_before3, date_before3, 5000)),
	# ('CMCC_bx_click_30d_60d_fre_above_2', pd_bx_ALLSQL.bx_click_time_fre.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_click_30d_60d_fre_above_2', date_before60, date_before30, 1, nuanwa_city, 2, 100, date_before3, date_before3, 5000)),

]



caogao = [
	# ('CMCC_bxdata_0625_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0625_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
    # ('CTCC_bxdata_0625_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0625_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
    # ('CUCC_bxdata_0625_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0625_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0624_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0624_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
    # ('CTCC_bxdata_0624_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0624_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
    # ('CUCC_bxdata_0624_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0624_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0623_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0623_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
    # ('CTCC_bxdata_0623_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0623_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
    # ('CUCC_bxdata_0623_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0623_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0622_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0622_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0622_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0622_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0622_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0622_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0621_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0621_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0621_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0621_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0621_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0621_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0617_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0617_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0617_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0617_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0617_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0617_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0618_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0618_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0618_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0618_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0618_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0618_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0619_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0619_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0619_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0619_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0619_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0619_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0620_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0620_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0620_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0620_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0620_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0620_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0615_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0615_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0615_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0615_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0615_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0615_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	#
	# ('CMCC_bxdata_0614_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0614_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0614_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0614_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0614_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0614_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# # ('CMCC_dpi_aitaoapp_APPBX001', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX001', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX001', 'APPBX001'), date_before3, date_before3, 4000)),
	# # ('CMCC_dpi_aitaoapp_APPBX002', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX002', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX002', 'APPBX002'), date_before3, date_before3, 2000)),
	# # ('CMCC_dpi_aitaoapp_APPBX003', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX003', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX003', 'APPBX003'), date_before3, date_before3, 2000)),
	# # ('CMCC_dpi_aitaoapp_APPBX004', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX004', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX004', 'APPBX004'), date_before3, date_before3, 2000)),
	# # ('CMCC_dpi_aitaoapp_APPBX005', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX005', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX005', 'APPBX005'), date_before3, date_before3, 2000)),
	# # ('CMCC_dpi_aitaoapp_APPBX006', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX006', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX006', 'APPBX006'), date_before3, date_before3, 2000)),
	# # ('CMCC_dpi_aitaoapp_APPBX007', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX007', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX007', 'APPBX007'), date_before3, date_before3, 2000)),
	# # ('CMCC_dpi_aitaoapp_APPBX008', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX008', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX008', 'APPBX008'), date_before3, date_before3, 2000)),
	# # ('CMCC_dpi_aitaoapp_APPBX009', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX009', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX009', 'APPBX009'), date_before3, date_before3, 2000)),
	# # ('CMCC_dpi_aitaoapp_APPBX010', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX010', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX010', 'APPBX010'), date_before3, date_before3, 4000)),
	# # ('CMCC_dpi_aitaoapp_APPBX011', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX011', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX011', 'APPBX011'), date_before3, date_before3, 2000)),
	# # ('CMCC_dpi_aitaoapp_APPBX012', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX012', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX012', 'APPBX012'), date_before3, date_before3, 2000)),
	# # ('CMCC_dpi_aitaoapp_APPBX013', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX013', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX013', 'APPBX013'), date_before3, date_before3, 2000)),
	# # ('CMCC_dpi_aitaoapp_APPBX014', pd_bx_ALLSQL.bx_aitao_app.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitaoapp_APPBX014', date_before30, tomorrow_time, 1, nuanwa_city, ('APPBX014', 'APPBX014'), date_before3, date_before3, 2000)),
	#
	# ('CMCC_bxdata_0612_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0612_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0612_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0612_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0612_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0612_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0610_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0610_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0610_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0610_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0610_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0610_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0611_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0611_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0611_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0611_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0611_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0611_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	#
	# ('CMCC_bxdata_0609_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0609_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0609_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0609_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0609_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0609_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0608_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0608_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0608_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0608_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0608_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0608_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	#
	#
	# # ('CMCC_bxdata_0606_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0606_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0606_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0606_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CUCC_bxdata_0606_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0606_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0607_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0607_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0607_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0607_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0607_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0607_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# # ('CMCC_bxdata_0605_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0605_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0605_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0605_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0605_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0605_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0604_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0604_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CTCC_bxdata_0604_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0604_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0604_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0604_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0603_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0603_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0603_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0603_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0603_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0603_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0602_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0602_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0602_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0602_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0602_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0602_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0601_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0601_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CTCC_bxdata_0601_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0601_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0601_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0601_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	#
	# ('CMCC_bxdata_0605_biz_3', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0605_biz_3', date_before30, tomorrow_time, 1, nuanwa_city, 3, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0605_biz_3', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0605_biz_3', date_before30, tomorrow_time, 0, nuanwa_city, 3, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0605_biz_3', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0605_biz_3', date_before30, tomorrow_time, 2, nuanwa_city, 3, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0531_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0531_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0531_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0531_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0531_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0531_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0530_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0530_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0530_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0530_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0530_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0530_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0529_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0529_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0529_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0529_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0529_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0529_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0528_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0528_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0528_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0528_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0528_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0528_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0527_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0527_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0527_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0527_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0527_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0527_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0526_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0526_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CMCC_bxdata_0525_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0525_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CMCC_bxdata_0524_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0524_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CTCC_bxdata_0526_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0526_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0525_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0525_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0524_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0524_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# # ('CUCC_bxdata_0526_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0526_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0525_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0525_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0524_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0524_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# # ('CMCC_bxdata_0523_biz_2', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0523_biz_2', date_before30, tomorrow_time, 1, nuanwa_city, 2, date_before3, date_before3, 200000)),
	# # ('CTCC_bxdata_0523_biz_2', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0523_biz_2', date_before30, tomorrow_time, 0, nuanwa_city, 2, date_before3, date_before3, 200000)),
	# # ('CUCC_bxdata_0523_biz_2', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0523_biz_2', date_before30, tomorrow_time, 2, nuanwa_city, 2, date_before3, date_before3, 200000)),
	#
	# ('CMCC_bxdata_0507_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0507_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CTCC_bxdata_0507_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0507_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0507_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0507_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# # ('CMCC_bxdata_0523_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0523_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0522_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0522_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0521_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0521_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0520_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0520_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CTCC_bxdata_0523_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0523_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0522_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0522_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0521_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0521_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CTCC_bxdata_0520_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0520_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CUCC_bxdata_0523_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0523_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0522_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0522_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CUCC_bxdata_0521_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0521_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0520_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0520_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# # ('CMCC_bxdata_0515', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0515', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0514', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0514', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0513', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0513', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0512', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0512', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0511', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0511', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CMCC_bxdata_0510', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0510', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0509', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0509', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CTCC_bxdata_0515', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0515', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0514', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0514', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CTCC_bxdata_0513', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0513', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0512', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0512', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0510', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0510', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CTCC_bxdata_0509', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0509', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CUCC_bxdata_0515', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0515', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0514', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0514', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0513', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0513', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0512', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0512', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CUCC_bxdata_0511', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0511', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0510', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0510', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# # ('CUCC_bxdata_0509', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0509', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# # ('CMCC_bxdata_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_biz_1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_biz_1', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_biz_1', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_biz_1', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# # ('CMCC_bxdata_biz_2', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_biz_2', 20250508, 20250508, 1, nuanwa_city, 2, date_before3, date_before3, 200000)),
	# # ('CUCC_bxdata_biz_2', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_biz_2', 20250508, 20250508, 2, nuanwa_city, 2, date_before3, date_before3, 200000)),
	# # ('CTCC_bxdata_biz_2', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_biz_2', 20250508, 20250508, 0, nuanwa_city, 2, date_before3, date_before3, 200000)),

	# ('CMCC_zh_ysj_30d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_zh_ysj_30d', get_datetime4(tomorrow_time, 30), tomorrow_time, 1, nuanwa_city, 1, (1, 2), 5000)),
	# ('CMCC_zh_ysj_30_60d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_zh_ysj_30_60d', get_datetime4(tomorrow_time, 60), get_datetime4(tomorrow_time, 30), 1, nuanwa_city, 1, (1, 2), 5000)),
	# ('CMCC_zh_ysj_60_90d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_zh_ysj_60_90d', get_datetime4(tomorrow_time, 90), get_datetime4(tomorrow_time, 60), 1, nuanwa_city, 1, (1, 2), 5000)),

	# ('CMCC_zh_wsj_3d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_zh_wsj_3d', get_datetime4(tomorrow_time, 5), tomorrow_time, 1, nuanwa_city, 0, (1, 2, 3), 200000)),
	('CTCC_zh_wsj_3d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_zh_wsj_3d', get_datetime4(tomorrow_time, 5), tomorrow_time, 0, nuanwa_city, 0, (1, 2, 3), 200000)),
	('CUCC_zh_wsj_3d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_zh_wsj_3d', get_datetime4(tomorrow_time, 5), tomorrow_time, 2, nuanwa_city, 0, (1, 2, 3), 200000)),

	# ('CMCC_zh_wsj_15d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_zh_wsj_15d', get_datetime4(tomorrow_time, 15), tomorrow_time, 1, nuanwa_city, 0, (1, 2), 200000)),
	('CTCC_zh_wsj_15d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_zh_wsj_15d', get_datetime4(tomorrow_time, 15), tomorrow_time, 0, nuanwa_city, 0, (1, 2), 200000)),
	('CUCC_zh_wsj_15d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_zh_wsj_15d', get_datetime4(tomorrow_time, 15), tomorrow_time, 2, nuanwa_city, 0, (1, 2), 200000)),

	('CMCC_zh_wsj_30d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_zh_wsj_30d', get_datetime4(tomorrow_time, 30), tomorrow_time, 1, nuanwa_city, 0, (1, 2), 200000)),
	('CTCC_zh_wsj_30d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_zh_wsj_30d', get_datetime4(tomorrow_time, 30), tomorrow_time, 0, nuanwa_city, 0, (1, 2), 200000)),
	('CUCC_zh_wsj_30d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_zh_wsj_30d', get_datetime4(tomorrow_time, 30), tomorrow_time, 2, nuanwa_city, 0, (1, 2), 200000)),

	# ('CMCC_zh_wsj_60d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_zh_wsj_60d', get_datetime4(tomorrow_time, 60), tomorrow_time, 1, nuanwa_city, 0, (1, 2), 200000)),
	('CTCC_zh_wsj_60d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_zh_wsj_60d', get_datetime4(tomorrow_time, 60), tomorrow_time, 0, nuanwa_city, 0, (1, 2), 200000)),
	('CUCC_zh_wsj_60d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_zh_wsj_60d', get_datetime4(tomorrow_time, 60), tomorrow_time, 2, nuanwa_city, 0, (1, 2), 200000)),

	# ('CMCC_zh_wsj_90d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_zh_wsj_90d', get_datetime4(tomorrow_time, 90), tomorrow_time, 1, nuanwa_city, 0, (1, 2), 1304)),
	# ('CMCC_zh_wsj_90d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_zh_wsj_90d', get_datetime4(tomorrow_time, 90), tomorrow_time, 1, nuanwa_city, 0, (1, 2), 1304)),
	('CTCC_zh_wsj_90d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_zh_wsj_90d', get_datetime4(tomorrow_time, 90), tomorrow_time, 0, nuanwa_city, 0, (1, 2), 10000)),
	('CUCC_zh_wsj_90d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_zh_wsj_90d', get_datetime4(tomorrow_time, 90), tomorrow_time, 2, nuanwa_city, 0, (1, 2), 529)),
	('CUCC_zh_wsj_90d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_zh_wsj_90d', get_datetime4(tomorrow_time, 90), tomorrow_time, 2, nuanwa_city, 0, (1, 2), 10000)),

	('CUCC_zh_wsj_120d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_zh_wsj_120d', get_datetime4(tomorrow_time, 120), tomorrow_time, 2, nuanwa_city, 0, (1, 2), 2701)),
	('CUCC_zh_wsj_120d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_zh_wsj_120d', get_datetime4(tomorrow_time, 120), tomorrow_time, 2, nuanwa_city, 0, (1, 2), 10000)),

	('CUCC_zh_wsj_180d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_zh_wsj_180d', get_datetime4(tomorrow_time, 180), tomorrow_time, 2, nuanwa_city, 0, (1, 2), 1386)),
	('CUCC_zh_wsj_180d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_zh_wsj_180d', get_datetime4(tomorrow_time, 180), tomorrow_time, 2, nuanwa_city, 0, (1, 2), 10000)),

	('CUCC_zh_wsj_dayu_180d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_zh_wsj_dayu_180d', 20241015, get_datetime4(tomorrow_time, 180), 2, nuanwa_city, 0, (1, 2), 2000)),

	# ('CMCC_bxdata_0515', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0515', 20250515, 20250515, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0514', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0514', 20250514, 20250514, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0513', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0513', 20250513, 20250513, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0512', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0512', 20250512, 20250512, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0511', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0511', 20250511, 20250511, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0510', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0510', 20250510, 20250510, 1, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CMCC_bxdata_0509', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxdata_0509', 20250509, 20250509, 1, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CTCC_bxdata_0515', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0515', 20250515, 20250515, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0514', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0514', 20250514, 20250514, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0513', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0513', 20250513, 20250513, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0512', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0512', 20250512, 20250512, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0511', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0511', 20250511, 20250511, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0510', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0510', 20250510, 20250510, 0, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CTCC_bxdata_0509', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CTCC_bxdata_0509', 20250509, 20250509, 0, nuanwa_city, date_before3, date_before3, 200000)),
	#
	# ('CUCC_bxdata_0515', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0515', 20250515, 20250515, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0514', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0514', 20250514, 20250514, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0513', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0513', 20250513, 20250513, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0512', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0512', 20250512, 20250512, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0511', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0511', 20250511, 20250511, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0510', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0510', 20250510, 20250510, 2, nuanwa_city, date_before3, date_before3, 200000)),
	# ('CUCC_bxdata_0509', pd_bx_ALLSQL.nature_snow_biz_before.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bxdata_0509', 20250509, 20250509, 2, nuanwa_city, date_before3, date_before3, 200000)),

	# ('CMCC_bxmodel_score_9198_9210', pd_bx_ALLSQL.nature_rain.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxmodel_score_9198_9210', 20250516, 20250516, 1, nuanwa_city, 9198, 9210, date_before3, date_before3, 10000)),
	# ('CMCC_bxmodel_score_9211_9400', pd_bx_ALLSQL.nature_rain.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bxmodel_score_9211_9400', 20250516, 20250516, 1, nuanwa_city, 9211, 9400, date_before3, date_before3, 10000)),
	# ('CMCC_bxmodel_score_2400_2500', pd_bx_ALLSQL.nature_rain.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_bxmodel_score_2400_2500', 20250714, 20250714, 1, nuanwa_city, 2400, 2500, 2, date_before3, date_before3, 3000)),
	# ('CMCC_bxmodel_score_2500_2600', pd_bx_ALLSQL.nature_rain.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_bxmodel_score_2500_2600', 20250714, 20250714, 1, nuanwa_city, 2500, 2600, 2, date_before3, date_before3, 3000)),
	# ('CMCC_bxmodel_score_2600_2700', pd_bx_ALLSQL.nature_rain.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_bxmodel_score_2600_2700', 20250714, 20250714, 1, nuanwa_city, 2600, 2700, 2, date_before3, date_before3, 3000)),
	# ('CMCC_bxmodel_score_3200_3300', pd_bx_ALLSQL.nature_rain.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_bxmodel_score_3200_3300', 20250714, 20250714, 1, nuanwa_city, 3200, 3300, 2, date_before3, date_before3, 3000)),
	# ('CMCC_bxmodel_score_3300_3400', pd_bx_ALLSQL.nature_rain.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_bxmodel_score_3300_3400', 20250714, 20250714, 1, nuanwa_city, 3300, 3400, 2, date_before3, date_before3, 3000)),

	# ('CMCC_dpi_aitao_BS028_Q16', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'NUANWA', 'CMCC_dpi_aitao_BS028_Q16', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028_Q17', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'NUANWA', 'CMCC_dpi_aitao_BS028_Q17', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028_Q18', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'NUANWA', 'CMCC_dpi_aitao_BS028_Q18', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 30000)),
	# ('CMCC_dpi_aitao_BS028_Q19', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'NUANWA', 'CMCC_dpi_aitao_BS028_Q19', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS028_Q20', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'NUANWA', 'CMCC_dpi_aitao_BS028_Q20', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before3, date_before3, 10000)),

	# ('CMCC_dpi_aitao_BS024_Q16', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'NUANWA', 'CMCC_dpi_aitao_BS024_Q16', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024', 'BS024'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS024_Q17', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'NUANWA', 'CMCC_dpi_aitao_BS024_Q17', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024', 'BS024'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS024_Q18', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'NUANWA', 'CMCC_dpi_aitao_BS024_Q18', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024', 'BS024'), date_before3, date_before3, 30000)),
	# ('CMCC_dpi_aitao_BS024_Q19', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'NUANWA', 'CMCC_dpi_aitao_BS024_Q19', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024', 'BS024'), date_before3, date_before3, 10000)),
	# ('CMCC_dpi_aitao_BS024_Q20', pd_bx_ALLSQL.bx_aitao.format(tomorrow_time, 'NUANWA', 'CMCC_dpi_aitao_BS024_Q20', date_before20, tomorrow_time, 1, nuanwa_city, ('BS024', 'BS024'), date_before3, date_before3, 10000)),

	# ('CMCC_bx_click_30d_Q16_x1', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'NUANWA', 'CMCC_bx_click_30d_Q16_x1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CMCC_bx_click_30d_Q17_x1', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'NUANWA', 'CMCC_bx_click_30d_Q17_x1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CMCC_bx_click_30d_Q18_x1', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'NUANWA', 'CMCC_bx_click_30d_Q18_x1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 30000)),
	# ('CMCC_bx_click_30d_Q19_x1', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'NUANWA', 'CMCC_bx_click_30d_Q19_x1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 10000)),
	# ('CMCC_bx_click_30d_Q20_x1', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'NUANWA', 'CMCC_bx_click_30d_Q20_x1', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 10000)),
	('CMCC_cmpp_black_bxclick', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_cmpp_black_bxclick', 20250510, tomorrow_time, 1, nuanwa_city, 110, (1, 2, 3), date_before3, date_before3, 20000)),
    ('CUCC_cmpp_black_bxclick', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_cmpp_black_bxclick', 20250510, tomorrow_time, 2, nuanwa_city, 110, (1, 2, 3), date_before3, date_before3, 20000)),
    ('CUCC_cmpp_black_bxsend', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_cmpp_black_bxsend', 20250510, tomorrow_time, 2, nuanwa_city, 111, (1, 2, 3), date_before3, date_before3, 20000)),
    ('CMCC_cmpp_black_bxdpi', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_cmpp_black_bxdpi', 20250617, tomorrow_time, 1, nuanwa_city, 114, (1, 2, 3), date_before3, date_before3, 20000)),
    # # ('CUCC_cmpp_black_bxdpi', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_cmpp_black_bxdpi', 20250617, tomorrow_time, 2, nuanwa_city, 114, (1, 2, 3), date_before3, date_before3, 20000)),
	# # ('CMCC_cmpp_black_bxsend_status1', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_cmpp_black_bxsend_status1', 20250510, tomorrow_time, 1, nuanwa_city, 111, (1,1), date_before3, date_before3, 10000)),
	('CMCC_cmpp_black_bxsend_status2', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_cmpp_black_bxsend_status2', 20250510, tomorrow_time, 1, nuanwa_city, 111, (2,2), date_before3, date_before3, 20000)),
	#
	# # ('CMCC_cmpp_black_bxzk', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_cmpp_black_bxzk', 20250510, tomorrow_time, 1, nuanwa_city, 113, (1, 2, 3), date_before3, date_before3, 20000)),
	# # ('CUCC_cmpp_black_bxzk', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_cmpp_black_bxzk', 20250510, tomorrow_time, 2, nuanwa_city, 113, (1, 2, 3), date_before3, date_before3, 20000)),
	# # ('CMCC_cmpp_black_bxdpi', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_cmpp_black_bxdpi', 20250613, 20250613, 1, nuanwa_city, 114, (1, 2, 3), date_before3, date_before3, 10000)),
	# # ('CUCC_cmpp_black_bxdpi', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_cmpp_black_bxdpi', 20250613, 20250613, 2, nuanwa_city, 114, (1, 2, 3), date_before3, date_before3, 10000)),
	#
	('CMCC_cmpp_black_bxsend_status1', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_cmpp_black_bxsend_status1', 20250613, 20250613, 1, nuanwa_city, 111, (1,1), date_before3, date_before3, 10000)),
	# # ('CMCC_cmpp_black_bxsend_status2', pd_bx_ALLSQL.bx_cmpp_black.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_cmpp_black_bxsend_status2', 20250613, 20250613, 1, nuanwa_city, 111, (2,2), date_before3, date_before3, 10000)),

]

BUSHU = [
	# ('CUCC_zh_wsj_120d_pm5', pd_bx_ALLSQL.sample_taikang_duodian_2_today.format(hl_time, 'MOFANG_CPA_NW', 'CUCC_zh_wsj_120d_pm5', get_datetime4(hl_time, 120), hl_time, 2, nuanwa_city, 0, (1, 2), hl_time, 5000)),
	# ('CUCC_zh_wsj_120d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_zh_wsj_120d', get_datetime4(tomorrow_time, 120), tomorrow_time, 2, nuanwa_city, 0, (1, 2), 3000)),
	# ('CUCC_bx_click_30d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_bx_click_30d', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 3000)),
	# ('CMCC_dpi_aitao_BS028_65_badclick', pd_bx_ALLSQL.bx_aitao_badclick.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_65_badclick', date_before20, tomorrow_time, 1, nuanwa_city, ('BS028_65', 'BS028_65'), date_before3, date_before3, 3000)),
	# ('CMCC_dpi_aitao_BS028_xz_15d', pd_bx_ALLSQL.bx_aitao_xz.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_aitao_BS028_xz_15d', date_before15, tomorrow_time, 1, nuanwa_city, ('BS028', 'BS028'), date_before15, date_before3, date_before3, 5000)),
	# ('CMCC_bx_dpi_7d_and_bxzk0', pd_bx_ALLSQL.bx_dpi_and_bxzk0.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_bx_dpi_7d_and_bxzk0', date_before7, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 100000)),
	# ('CMCC_dpi_yax_BT541_3d', pd_bx_ALLSQL.bx_yax.format(tomorrow_time, 'MOFANG_CPA_NW', 'CMCC_dpi_yax_BT541CMCC_dpi_yax_BT541_3d', date_before5, tomorrow_time, 1, nuanwa_city, ('BT541', 'BT541'), date_before3, date_before3, 10000)),
	# ('CUCC_bx_click_30d_60d_and_bxdata', pd_bx_ALLSQL.bx_click_bxdata.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_bx_click_30d_60d_and_bxdata', date_before60, date_before30, 2, nuanwa_city, date_before30, tomorrow_time, date_before3, date_before3, 10000)),
	# ('CUCC_zh_wsj_90d', pd_bx_ALLSQL.sample_taikang_duodian_2.format(tomorrow_time, 'MOFANG_CPA_NW', 'CUCC_zh_wsj_90d', get_datetime4(tomorrow_time, 90), tomorrow_time, 2, nuanwa_city, 0, (1, 2), 10000)),
    ('CTCC_bx_click_and_alibx362', pd_bx_ALLSQL.bx_click_alibx362.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_click_and_alibx362', date_before60, date_before30, 0, nuanwa_city, 9000, date_before3, date_before3, 1)),

]
ZHONGANMF_CPA_NW = [
	('CMCC_bx_click_30d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CMCC_bx_click_30d', date_before30, tomorrow_time, 1, nuanwa_city, date_before3, date_before3, 3000)),
	('CTCC_bx_click_30d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CTCC_bx_click_30d', date_before30, tomorrow_time, 0, nuanwa_city, date_before3, date_before3, 3000)),
	('CUCC_bx_click_30d', pd_bx_ALLSQL.bx_click.format(tomorrow_time, 'ZHONGANMF_CPA_NW', 'CUCC_bx_click_30d', date_before30, tomorrow_time, 2, nuanwa_city, date_before3, date_before3, 3000)),

]
HL = [
	# ('CMCC_zh_wsj_dt_2h', pd_bx_ALLSQL.sample_taikang_duodian_2.format(hl_time, 'ZHONGHUI_CPA_DD_HL', 'CMCC_zh_wsj_dt_2h', hl_time, tomorrow_time, 1, zhonghui_cpa_city, 0, (1, 2, 3), 10000)),
	('CUCC_zh_wsj_dt_2h', pd_bx_ALLSQL.sample_taikang_duodian_2.format(hl_time, 'ZHONGHUI_CPA_DD_HL', 'CUCC_zh_wsj_dt_2h', hl_time, tomorrow_time, 2, zhonghui_cpa_city, 0, (1, 2, 3), 10000)),

# ('CMCC_bx_click_30d_dthl', pd_bx_ALLSQL.bx_click_3.format(hl_time, 'MOFANG_CPA_NW_HL', 'CMCC_bx_click_30d_dthl', hl_time, hl_time, 1, nuanwa_city, 30000)),
# ('CUCC_bx_click_30d_dthl', pd_bx_ALLSQL.bx_click_3.format(hl_time, 'MOFANG_CPA_NW_HL', 'CUCC_bx_click_30d_dthl', hl_time, hl_time, 2, nuanwa_city, 30000)),
# ('CMCC_bx_click_30d_dthl', pd_bx_ALLSQL.bx_click_3.format(hl_time, 'ZHONGHUI_CPA_DD_HL', 'CMCC_bx_click_30d_dthl', hl_time, hl_time, 1, zhonghui_cpa_city, 30000)),
# ('CUCC_bx_click_30d_dthl', pd_bx_ALLSQL.bx_click_3.format(hl_time, 'ZHONGHUI_CPA_DD_HL', 'CUCC_bx_click_30d_dthl', hl_time, hl_time, 2, zhonghui_cpa_city, 30000)),

]

# 跑数产品列表
# region

bank_list = {
	'02caogao': caogao,
	'03NUANWA': NUANWA,
	# '01BUSHU': BUSHU,
	# 'HL':HL
}

# endregion

# 跑数代码
# region


def list_run():
	print(Time_Begain)
	print(today_time + "—————— data_insert_list begin   !!!")
	fwq166 = pymysql.connect(
		host="192.168.5.169",
		user="wangshaojie",
		password="em!2T3X8TycF",
		port=9030,
		db="tcc",
		charset='utf8')
	cursor = fwq166.cursor()

	# I.清表
	print(push_tbx_delete)
	cursor.execute(push_tbx_delete)
	print("push_tbx_delete is over !!!")
	# # I.清暖哇表
	print("开始清暖哇表")
	cursor.execute(push_nwtbx_delete)
	print("暖哇数据已清除 !!!")
	# II.插入3天营销
	print(ruku3d)
	cursor.execute(ruku3d)
	print("ruku3d is over !!!")
	# III.插入历史撞库不可营销数据
	print(zk)
	cursor.execute(zk)
	print("zk is over !!!")
	# IV.插入保险营销黑名单
	print(black)
	cursor.execute(black)
	print("black is over !!!")

	print(today_time + "data_save_list begin   !!!")

	for bank_name, bank_sql in sorted(bank_list.items()):
		print(bank_name + "—————— data_insert_list begin   !!!")
		for tup in bank_sql:
			time.sleep(1)
			rule_name = list(tup)[0]
			rule_sql = list(tup)[1]
			try:
				print(rule_sql)
				cursor.execute(rule_sql)
				print(rule_name + "—————— data insert is over")
			except:
				print(rule_name + "——————  is bug Fail !!!!!")
				traceback.print_exc()
				pass
			continue
		print(bank_name + "!!!   product list is over   !!!")
	print(today_time + "!!!   tcc_push_all list is over   !!!")

	fwq166.commit()
	print("数据更新完成！！！！")
	# time.sleep(2)
	fwq166.close()
	print(Time_End)
	print(today_time + "!!!   all list is over   !!!")

# endregion


if __name__ == '__main__':
	list_run()


