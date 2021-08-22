from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome("C:/Users/mldhc/OneDrive/바탕 화면/연습/selenium/chromedriver.exe")
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("이준기")
elem.send_keys(Keys.RETURN)
count = 1
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
for image in images:
    try:
        image.click()   
        time.sleep(2)
        imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl,str(count) +".jpg")
        count = count +1
    except:
        pass
print("finished")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()