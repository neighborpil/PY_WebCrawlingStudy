"""
# XPath
 - XPath(XML Path Language)는 W3C의 표준으로 확장 생성 언어 문서의 구조를 통해
   경로 위에 지정한 구문을 사용하여 항목을 배치하고 처리하는 방법을 기술하는 언어
# 문법
 - https://www.w3schools.com/xml/xpath_syntax.asp
 - //* : Selects all elements in the document
 - @ : Selects attributes
"""
from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='chromedriver.exe')
browser.get("http://nid.naver.com/nidlogin.login") # get방식으로 naver login화면에 접속

id = browser.find_element_by_css_selector("#id").send_keys("naver_id") # .send_keys(태그에 입력)
pw = browser.find_element_by_xpath('//*[@id="pw"]').send_keys("naver_pw")

# browser.implicitly_wait(10)
time.sleep(2) # 절대적 대기

browser.find_element_by_css_selector("#frmNIDLogin > fieldset > input").click()

browser.implicitly_wait(10) 
# browser.quit()

# 자동접속 방지 입력 문자가 뜨는데 뭔가 막아놨나보다