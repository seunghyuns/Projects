from collections import defaultdict
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import csv
from datetime import datetime
import time
import pymssql
import PrintUsageDB as db
from pandas import Series, DataFrame

개발실 = 206
에몬스홈 = 220
전시장 = 214

findDept = ''

db.dbConnect()
rdr ={}

f = open('StandardAccount.csv','r')
rdr = csv.DictReader(f)


# setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# Login
driver.get('http://192.168.0.206/sws.login/gnb/loginView.sws?basedURL=undefined&popupid=id_Login') 
driver.find_element_by_name('IDUserId').send_keys('admin') # 값 입력
driver.find_element_by_name('IDUserPw').send_keys('soa4007@')
driver.find_element_by_name('IDUserPw').send_keys(Keys.ENTER)
#driver.find_element_by_xpath('//*[@id="IDLogin"]').click() # 버튼클릭하기


'''
#userSite = 'http://192.168.0.206/sws.application/userManagement/accountingQuotaView.sws'
userSite = 'http://192.168.0.206/sws.application/userProfile/userProfileView.sws'
#userSite = 'http://192.168.0.220/sws.application/userManagement/accountingQuotaView.sws?ruiFw_id=StandardAccounting&ruiFw_pid=UserAccessControl&ruiFw_title=%ED%91%9C%EC%A4%80%20%EA%B3%84%EC%A0%95%20%EC%A0%95%EB%B3%B4'
driver.get(userSite)

driver.current_url
searchPath = '//*[@id="userProfile_list"]'

#element = driver.find_element_by_id("swshomeFrame")
#driver.switch_to.frame(element)
r = driver.page_source
soup = BeautifulSoup(r, 'html.parser') # BeautifulSoup사용하기

#tableuser = tableid.find('tr',{'id':'1'})
print(new)
#value = '220040'
'''

timestr = time.strftime("%Y%m%d-%H%M%S")
value={}
filedName = ['부서','성명','사번','컬러출력','흑백출력']
dictWrite = open(timestr+'.csv','a',newline="")
dictWrite = csv.DictWriter(dictWrite,fieldnames=filedName)
dictWrite.writeheader()


for i in rdr:
    
    UsePrintSite = 'http://192.168.0.206/sws.application/userManagement/editAccountID.sws?userid={}&popupid=editAccountID'.format(i['AcountID'])

    driver.get(UsePrintSite)
    html = driver.page_source # 페이지의 elements모두 가져오기

    soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기

    colorPrintUse = soup.find('td',{'id':'colorPrintUse'}).text
    monoPrintUse = soup.find('td',{'id':'monoPrintUse'}).text
    

    
    db.dbExcute(db.FindQuery(i['AcountID']))
    DeptandUserName = db.dbFetchOne()
    while DeptandUserName:
        #print("부서" + str(DeptandUserName[0]) + ", 성명 " + str(DeptandUserName[1]))
        DeptName = str(DeptandUserName[0])
        UserName = str(DeptandUserName[1])
        #print(DeptName + UserName)
        DeptandUserName = db.dbFetchOne()
        dictWrite.writerow({'부서':DeptName,'성명': UserName,'사번' : i['AcountID'], '컬러출력' : colorPrintUse, '흑백출력' : monoPrintUse})

        #raw_data = {'부서':DeptName,'성명': UserName,'사번' : i['AcountID'], '컬러출력' : colorPrintUse, '흑백출력' : monoPrintUse}
        #dataFrame = DataFrame(raw_data,index=[i])
        #print(dataFrame)

    
    
    





db.dbClose()        

