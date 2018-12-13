"""
# selenium
 - api 설명 : https://selenium-python.readthedocs.io/
# 인터파크 투어 사이트에서 여행지를 입력 후 검색 -> 잠시후 -> 결과
# 로그인시 PC 웹 사이트에서 처리가 어려울 경우 -> 모바일 로그인으로 진입

"""
# 모듈 가져오기
# pip install selenium
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # 명시적 대기를 위해 사용
from selenium.webdriver.support import expected_conditions as EC
import time
from Tour import TourInfo

# 사전에 필요한 정보를 로드 => 디비 혹은 쉘, 배치 파일에서 인자로 받아서 세팅
main_url = 'https://tour.interpark.com/'
keyword = '로마'
# 상품 정보를 담는 리스트(TourInfo 리스트)
tour_list = []

# 드라이버 로드
driver = wd.Chrome(executable_path='chromedriver.exe')
# 차후 -> 옵션 부여하여(프록시, 에이전트 조작, 이미지 배제)
# 크롤링을 오래 돌리면 => 임시파일이 쌓인다!! 주의!! -> 템프 파일 삭제
# 사이트 접속 (get)
driver.get(main_url)
# 검색창을 찾아서 검색어를 입력
# id : SearchGNBText
driver.find_element_by_id('SearchGNBText').send_keys(keyword)
# 수정할 경우 => 뒤에 내용이 붙어버림 => .clear() -> send_keys('내용')
# 검색 버튼을 클릭
driver.find_element_by_css_selector('button.search-btn').click()
# 잠시 대기 => 페이지가 로드 되고 나서 즉각적으로 데이터를 획득하는 행위는 자제
# 명시적 대기 => 특정 요소가 로케이트(발견될 때까지 대기)
try:
    element = WebDriverWait(driver, 10).until( # 최대 10초간 기다림
        # 지정한 한개의 요소가 올라오면 wait를 종료
        EC.presence_of_element_located((By.CLASS_NAME, 'oTravelBox'))
    )
except Exception as e:
    print('오류 발생', e)
# 암묵적 대기 => DOM이 다 로드 될 때까지 대기하고 로드되면 바로 진행
# 요소를 찾을 특정 시간동안 DOM의 풀링을 지시, 예를 들어 10초 이내라도 발견되면 진행
driver.implicitly_wait(10)
# 절대적 대기 => time.sleep(10) 무조건 기다림 => 클라우드 페이어(디도스 방어 솔루션) 뚫을 때 사용
# 더보기 눌러서 => 게시판 진입
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click() # ">" : 자식을 의미함

# 게시판에서 데이터를 가져올 때
# 데이터가 많으면 세션(혹시 로그인을 해서 접근되는 사이트일 경우) 관리
# 특정 단위별로 로그아웃 로그인을 계속 시도
# 특정 게시물이 사라질 경우 => 팝업 발생( 없는 ...) => 팝업 처리 검토
# 게시판 스캔시 => 임계점을 모름!!
# 게시판을 스캔 => 메타정보 획득 => loop를 돌려서 일괄적으로 접근 처리

# 스크립트 실행 : searchModule.SetCategoryList(1, '')
# 17은 임시값, 게시물을 넘어갔을 때 현상을 확인하고자
for page in range(1, 2):#17): # 임시로 끊음
    try:
        # 자바스크립트 구동하기
        driver.execute_script("searchModule.SetCategoryList(%s, '')" % page)
        time.sleep(2)
        print("%s 페이지 이동" % page)
        ###################################
        # 여러 사이트에서 정보를 수집할 경우 공통 정보 정의 단계 필요
        # 상품명, 코멘트, 기간1, 기간2, 가격, 평점, 섬네일, 링크(실제 상세 정보)
        boxItems = driver.find_elements_by_css_selector('.oTravelBox>.boxList>li')
        # 상품 하나 하나 접근
        for li in boxItems:
            # 이미지를 링크값에 사용할것인가?
            # 직접 다운로드 해서 우리 서버에 업로드(ftp) 할 것인가?
            print('썸네일', li.find_element_by_css_selector('img').get_attribute('src'))
            print('링크', li.find_element_by_css_selector('a').get_attribute('onClick'))
            print('상품명', li.find_element_by_css_selector('h5.proTit').text)
            print('코멘트', li.find_element_by_css_selector('.proSub').text)
            print('가격', li.find_element_by_css_selector('.proPrice').text)
            area = ''
            for info in li.find_elements_by_css_selector('.info-row .proInfo'):
                print(info.text)
            print('='*100)
            # 데이터 모음
            # li.find_elements_by_css_selector('.info-row .proInfo')[1].text
            #  데이터가 부족하거나 없을 수도 있으므로 직접 인덱스로 표현은 위험성이 있음
            obj = TourInfo(
                li.find_element_by_css_selector('h5.proTit').text,
                li.find_element_by_css_selector('.proPrice').text,
                li.find_elements_by_css_selector('.info-row .proInfo')[1].text,
                li.find_element_by_css_selector('a').get_attribute('onClick'),
                li.find_element_by_css_selector('img').get_attribute('src')
            )
            tour_list.append(obj)
    except Exception as e1:
        print("오류 ", e1)

print(tour_list, len(tour_list))
# 수집한 정보 개수를 루프 => 페이지 방문 => 콘텐츠 획득(상품상세정보) =>
for tour in tour_list:
    # tour => TourInfo
    print(type(tour))
    # 링크 데이터에서 실데이터 획득
    # 분해
    arr = tour.link.split(',')
    # 대체
    if arr: # 있으면 true?
        # 대체
        link = arr[0].replace('searchModule.OnClickDetail(', '')
        # 슬라이싱 => 앞의 ', 뒤의 ' 제거
        detail_url = link[1:-1]
        # 상세페이지 이동 : URL 값이 완성된 형태인지 확인(HTTP~)
        driver.get(detail_url)
        time.sleep(1)

# 종료
driver.close()
driver.quit()
import sys
try:
    sys.exit()
finally:
    print('sys error')
