from selenium import webdriver
import time
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

driver = webdriver.Chrome(r"C:\PARK_TIL\chromedriver.exe") # 크롬 창 열기

keyword = 'jbl+free+x'
url = 'https://search.shopping.naver.com/detail/detail.nhn?cat_id=50002334&nv_mid=15784793132&query=' + keyword
driver.get(url) # get = 이동시키는 역할
time.sleep(1)


cnt = driver.find_elements("css_selector",'#_review_list li.thumb_nail')
print('네이버쇼핑_{}_상품평'.format(keyword))
sheet.append(['no', '후기제목', '정보'])


# page: 페이지수 ex(1, 11): 1~10페이지 크롤링
# 1~136

for page in range(1, 136):
    page_buttons = driver.find_elements("css_selector",'#_review_paging a')
    
    for i in range(0, len(cnt)):

        try : 
            review_list = driver.find_elements("css_selector",'#_review_list li.thumb_nail')
            title = review_list[i].find_elements("css_selector",'p').text
            content = review_list[i].find_elements("css_selector",'div.atc').text
            info = review_list[i].find_elements("css_selector",'div.avg_area span.info').text
            print(i+1)
            print(title)
            print(info)
            sheet.append([i+1, title, info])
            time.sleep(1)
            driver.implicitly_wait(10)
        
        except : 
            print()

    if page < 11:
        page_buttons[page-1].click()
        time.sleep(1.5)
        driver.implicitly_wait(10)
        
    elif page % 10 == 0 :
        driver.find_elements("css_selector",'#_review_paging a.next').click()
        time.sleep(1.5)
        driver.implicitly_wait(10)
    
    else:
        page_buttons[page % 10 + 1].click()
        time.sleep(1.5)
        driver.implicitly_wait(10)

wb.save('네이버쇼핑_'+keyword+'_리뷰.xlsx')