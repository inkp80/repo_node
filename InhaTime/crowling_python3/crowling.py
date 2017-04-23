    	#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import time
import re
import requests
import mysql.connector
from mysql.connector import errorcode

def Substr(str,start,stop):
	return str[start:stop]

def parse(tr):
	data = []
	tds = tr.find_all('td')
	for td in tds:
		data.append(td.text)
	return data

try:
    cnn = mysql.connector.connect(
        user= 'root',
        password= 'root',
        host= 'localhost',
        database= 'inha'
    )
    print("IT WORKS")
except mysql.connector.Error as e:
    if e.errno == errcode.ER_ACCESS_DENIDED_ERROR:
        print("user name or pass-word is invalid")
    elif e.errno == errcode.ER_BAD_DB_ERR:
        print("no database")
    else:
        print(e)

cursor = cnn.cursor()
# # addName = ("INSERT INTO name (fname, lastname) VALUES (%s,  %s)")
#
#
#
# firstN = "hel11lo"
# SecN = "wor22ld"
# empName = (firstN, SecN)
# print(empName)
# #
#
# query = """INSERT INTO name (fname, lastname) VALUES (%s,%s)"""
#
# cursor.execute(query, empName)
# cnn.commit()
# cursor.close()
# cnn.close

seldef = ['1','2','3','4','5','6','7','8','9','0436','0807','1206']

major_codes = ['0194002','0198005', '1013446', '1014514', '0220021', '1015304', '0223022','1035515' ,'1016386', '1017516', '0225028', '1104537', '0233156', '1018305', '0930430', '0208014', '0209015', '1184217', '1185283','1019517','1067522','1063157','1064040','1065039','1066041', '1022306', '1023307', '1186074', '0333045','1025431', '0934339', '1187268', '0267059','0268065','0275054', '0273057','0276055', '0749160', '0478051', '0477053', '0479215', '1188047', '1189364', '1190557', '1191555', '1026369','0301071','0302072','1192556','1028485','0294067','1029486','1030371','1031487', '0317077', '0321079', '0318078', '1200563', '1201559', '1202560', '1203561', '1204562', '0756344','1193558', '1194341', '1195519', '1196372', '1197288', '1207569']
for codes in major_codes:
	url = 'http://sugang.inha.ac.kr/sugang/SU_51001/Lec_Time_Search.aspx'
	r = requests.get(url)

	soup = BeautifulSoup(r.text,'html.parser')
	select = soup.find('select',id='ddlTime1')
	options = select.find_all('option')

	timedatas = []

	for o in options:
	    if o['value'] == '선택':
	        continue
	    timedatas.append({
	        'name': o.text,
	        'value': o['value']
	    })

	event_target = ''
	event_argument = ''
	last_focus = ''
	view_state = soup.find('input',id='__VIEWSTATE')['value']
	view_state_generator = soup.find('input',id='__VIEWSTATEGENERATOR')['value']
	event_validation = soup.find('input',id='__EVENTVALIDATION')['value']

	r = requests.post(url,data={
	    'ddlDept': codes,
	    '__EVENTTARGET': event_target,
	    '__EVENTARGUMENT': event_argument,
	    '__LASTFOCUS': last_focus,
	    '__VIEWSTATE': view_state,
	    '__VIEWSTATEGENERATOR': view_state_generator,
	    '__EVENTVALIDATION': event_validation,
	    'rdoKwamokGubun': '99',
	    'ibtnSearch3.x': '48',
	    'ibtnSearch3.y': '12',
	    'ibtnSearch3': '��ȸ'
	})
	soup = BeautifulSoup(r.text, "html.parser")
	table = soup.find('table', id='dgList')
	trs = table.find_all('tr')

	#이거 파싱을 해야하는데
	for tr in trs:
	    data = parse(tr)
	    if not data:
	        continue
	    print(data)

	    lecture_id = data[0]
	    # grp = data[1]
	    lecture_title = data[2]
	    grade = data[3]
	    credit = data[4]
	    class_type = data[5]
	    place = data[6]
	    instructor = data[7]
	    eval_method = data[8]
	    remarks = data[9]
	    lecture_time = data[12]

	    query = """INSERT INTO Lecture (lecture_id, lecture_title, grade, credit, class_type, place, instructor, eval_method, remarks, lecture_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
	    empLec =(lecture_id, lecture_title, grade, credit, class_type, place, instructor, eval_method, remarks, lecture_time)


        # lecture_code = Substr(lecture_id,0,3);
	    lecture_code = Substr(lecture_id,0,7)
	    major = codes
	    predict_rating = 0
	    rating = 0
	    MAE = 0
	    distinct_id = lecture_code + instructor
	    print(distinct_id)
	    print(lecture_code)
	    query2 = """INSERT IGNORE INTO evaluation (lecture_code, lecture_title, instructor, eval_method, class_type, grade, credit, major, predict_rating, rating, MAE, distinct_id) VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
	    empEval =(lecture_code, lecture_title, instructor, eval_method, class_type, grade, credit, major, predict_rating, rating, MAE, distinct_id)
	    cursor.execute(query, empLec)



	    cursor.execute(query2, empEval)
	    cnn.commit()
cursor.close()
cnn.close

    #
    # for idx in data:
    #     print(idx);
	    #    print (';'.join(parse(tr)))



#
# var arr = new arr(0194002, 0198005, 1013446, 1014514, 0220021, 1015304, 0223022,1035515,1016386, 1017516, 0225028, 1104537, 0233156, 1018305, 0930430, 0208014, 0209015, 1184217, 1185283,1019517,1067522,1063157,1064040,1065039,1066041, 1022306, 1023307, 1186074, 0333045,1025431, 0934339, 1187268, 0267059,0268065,0275054, 0273057,0276055, 0749160, 0478051, 0477053, 0479215, 1188047, 1189364,1190557, 1191555, 1026369,0301071,0302072,1192556,1028485,0294067,1029486,1030371,10314870317077, 0321079, 0318078, 1200563, 1201559, 1202560, 1203561, 1204562, 0756344,
#     1193558, 1194341, 1195519, 1196372, 1197288, 1207569);
