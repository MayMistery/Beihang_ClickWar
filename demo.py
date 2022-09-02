import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

# 打开Chrome
chrome = Chrome()

# 打开vpn
chrome.get("https://vpn.buaa.edu.cn/")
#chrome.execute_script("window.open('https://www.baidu.com')")
#chrome.execute_script("window.open('https://www.baidu.com')")
#chrome.switch_to.window(chrome.window_handles[2])

#赶紧手动登录 30s
time.sleep(30)

#chrome.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/div[1]/div[1]/div/input").send_keys("*****")

#chrome.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/input").send_keys("*****")

# 点击同意隐私
#chrome.find_element("/html/body/div[2]/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div[2]/form/div[3]/span/input").click()

# 点击登录
#chrome.find_element("/html/body/div[2]/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button").click()

#打开教务
chrome.get("need a href")

#赶紧手动登录
time.sleep(30)

#chrome.find_element(By.CSS_SELECTOR, "#unPassword").send_keys("*****")

#chrome.find_element(By.CSS_SELECTOR, "#pwPassword").send_keys("*****")

#chrome.find_element(By.XPATH, "#content-con > div:nth-child(1) > div:nth-child(7) > input").click()

#time.sleep(30)

#抢课程1
flag1=1
while(flag1):

    #进入核心专选栏目
    chrome.get("need a href")

    time.sleep(1)

    #输入课程号
    chrome.find_element(By.CSS_SELECTOR, "#queryform > ul > li:nth-child(4) > input").send_keys("B3I023160")

    #查询
    chrome.find_element(By.CSS_SELECTOR, "#queryform > ul > li:nth-child(7) > div > a").click()

    #找到课程，点击选课  
    chrome.find_element(By.XPATH, "/html/body/div[7]/div/div[6]/table/tbody/tr[2]/td[1]/div/a").click()

    print(chrome.switch_to.alert.text)

    #选课成功字符长度短（可酌情改变
    if(len(chrome.switch_to.alert.text) <= 6):
        flag1 = 0

    chrome.switch_to.alert.accept()

