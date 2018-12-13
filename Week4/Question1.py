"""
1. 인스타그램에 로그인을 하여, 자신이 관심있거나 좋아하는 태그로 검색을 한 후, 
나오는 포스팅 100개 대표 이미지를 크롤링하여 다운로드받는 프로그램을 작성합니다. 
(셀레니움만을 이용해서 작성해주세요). 
태그로 검색하는 URL은 https://www.instagram.com/explore/tags/[태그명] 입니다. 
인스타그램 로그인을 하는 것도 셀레니움을 통해서 할 수 있습니다. 
코드 제출할 때는 인스타그램 아이디와 비밀번호는 절대로 포함하지 말고 제출해주세요 :) 
(코드 링크를 기입해 주세요) *

# regex 체크
 - https://regex101.com/
"""
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # 명시적 대기를 위해 사용
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import urllib.request


class CrawlingInstagram:
    driver = wd.Chrome(executable_path='chromedriver.exe')
    url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'


    def login(self, id, pwd):
        self.driver.get(self.url)

        # 로그인 정보 입력
        inputs = self.driver.find_elements_by_css_selector('.f0n8F>._2hvTZ') # id는 계속 바껴서 사용 불가
        for input in inputs:
            attribute = input.get_attribute('type');
            if attribute == 'text':
                input.send_keys(id)
            elif attribute == 'password':
                input.send_keys(pwd)

        # 로그인 클릭
        buttons = self.driver.find_elements_by_css_selector('.HmktE button._0mzm-')
        for button in buttons:
            attribute = button.get_attribute('type')
            if attribute == 'submit':
                button.click()
    
        # 암묵적 대기
        #self.driver.implicitly_wait(3) # 가끔 에러나는데 왜? DOM 전체 로드 아녔나?
        # 명시적 대기
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'HoLwm')))
        except Exception as e:
            print('search error', e)


        #알람 있으면 삭제
        later_button = self.driver.find_element_by_css_selector('.piCib>.mt3GC>.HoLwm ')
        if later_button is not None:
            later_button.click()

        # 검색창 있으면 검색
        isReady = False
        search_input = self.driver.find_element_by_css_selector('.MWDvN>.LWmhU>input.XTCLo')
        if search_input is not None:
            isReady = True
        return isReady

    def search(self, tag):
        # 검색어 입력
        search_input = self.driver.find_element_by_css_selector('.MWDvN>.LWmhU>input.XTCLo')
        search_input.send_keys(tag)
        
        # 명시적 대기
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'yCE8d')))
        except Exception as e:
            print('search error', e)

        # 링크 목록에서 tag와 같은거 있으면 클릭
        links = self.driver.find_elements_by_css_selector('.drKGC>.fuqBx>a.yCE8d')
        for link in links:
            href = link.get_attribute('href')
            target = re.findall('^https:\/\/www.instagram.com\/explore\/tags\/(\S+)\/', href)
            if len(target) == 1 and target[0] == tag:
                link.click()
                self.driver.implicitly_wait(10)
                return True

    def crawl(self):
        link_list = self.get_link_list();
        if len(link_list) > 0:
            self.download_image(link_list);
            
    def get_link_list(self):
        link_list = []
        link_list = self.driver.find_elements_by_css_selector('.eLAPa>.KL4Bh>img.FFVAD')
        return link_list

    def download_image(self, link_list):
        if len(link_list) > 0:
            for link in link_list:
                src = link.get_attribute('src')
                fild_address = src.split('?')
                words = fild_address[0].split('/')
                file_name = words[len(words) - 1]
                urllib.request.urlretrieve(src, file_name)


    def __del__(self):
        self.driver.close()
         
                    



# __main__
ci = CrawlingInstagram()
#ci.crawl('okinawa')
isReady = ci.login('id', 'pwd')
if isReady:
    isEnteredSearchResult = ci.search('okinawa')
    if isEnteredSearchResult:
        ci.crawl()