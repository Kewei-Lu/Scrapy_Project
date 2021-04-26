from  selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import hashlib
import re
import random
import sys

driver = webdriver.Chrome('./chrome_driver/chromedriver.exe')
print(sys.path)



def exception_process():
    pass


def qiandao():
    global driver
    print('hello,today is '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    print('You are now using the baidu tieba auto qiandao tool')
    print('please input you id')
    user_id = 'lkw1998517'
    print('please enter your password')
    user_pass = 'Lkw1998517'
    url = 'https://tieba.baidu.com/index/tbwise/forum?shownew=1'
    url1 = 'https://tieba.baidu.com/index.html?traceid=#'
    # //*[@id="com_userbar"]/ul/li[4]
    # cookie = 'BIDUPSID=8D8060EBED10F14FC3300599A6F4966A; PSTM=1607349920; BDUSS=W9LUk9VOE1KWDcxckdoaGNKTWNFR1B4SDNqSzA0TkFnaTAzenNXb2g3eVJ0RVpnRVFBQUFBJCQAAAAAAAAAAAEAAADbbu4DbGt3MTk5ODUxNwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJEnH2CRJx9gO; BAIDUID=A2573DF3B26C7E1A7F6626CA52FDA478:FG=1; H_PS_PSSID=33423_33355_33344_31253_33392_33584_26350; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PHPSESSID=64k4bca6nfarq9d5kh19c1s032; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1613391593; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1613391593'
    # cookie = cookie.split(';')
    # cookie_default = {}
    # for item in cookie:
    #     pp = item.split('=')
    #     cookie_default[pp[0]] = pp[1]
    #
    # driver.add_cookie()
    driver.get(url1)
    time.sleep(5)
    try:
        login_obj = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,'登录')))
        time.sleep(3)
        #login_href = element.get_attribute('href')
        login_obj.click()
    except:
        print('some problems in finding the login')
        exception_process()
    try:
        '''id_login = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.LINK_TEXT,'用户名登录')))
        id_login.click()'''
        time.sleep(3)
        id_login = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]')
        id_login.click()
    except:
        print('some problems in finding the id login')
    try:
        id_obj = WebDriverWait(driver,13).until(EC.presence_of_element_located((By.XPATH,'//*[@class="pass-button pass-button-submit"]')))
        login_obj_1 = WebDriverWait(driver,13).until(EC.presence_of_element_located((By.XPATH,'//*[@class="pass-text-input pass-text-input-userName"]')))
        password_obj =  WebDriverWait(driver,13).until(EC.presence_of_element_located((By.XPATH,'//*[@class="pass-text-input pass-text-input-password"]')))
        login_obj_1.send_keys('lkw1998517')
        time.sleep(3)
        password_obj.send_keys('Lkw1998517')
        time.sleep(3)
        id_obj.click()
    except:
        print('some problems in  id login')
    try:
        personal_index = WebDriverWait(driver,13).until(EC.presence_of_element_located((By.XPATH,'//*[@id="j_u_username"]')))
        time.sleep(3)
        personal_index.click()
    except:
        print('some problems in finding personal index')
    try:
        guanzhu =WebDriverWait(driver,13).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ihome_nav_wrap"]/ul/li[4]/div')))
        handle = driver.current_window_handle
        time.sleep(2)
        guanzhu.click()
    except:
        print('some problems in finding ai guang de ba')
    try:
        #weiye = WebDriverWait(driver,13).until(EC.presence_of_element_located((By.XPATH,'//*[contains(text(),"尾页")]')))
        handles = driver.window_handles
        for newhandle in handles:
            if newhandle != handle:
                driver.switch_to.window(newhandle)
        weiye = driver.find_element_by_xpath('//*[contains(text(),"尾页")]')
        weiye = weiye.get_attribute('href')
        weiye = re.split(r'=',weiye)[-1]
        print(weiye)
    finally:
        pass
    #try:
        #drag_start = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="TANGRAM__PSP_3__userName"]')))


    '''.find_element_by_link_text('登录')
    login_href = login_obj.get_attribute('href')'''
    forum_href = []
    for q in range(1,int(weiye)+1,1):
        print(q)
        name_of_forum =WebDriverWait(driver,13).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="like_pagelet"]/div[@class="forum_main"]/div[@class="forum_table"]/table/tbody/tr/td[1]/a')))
        for i in range(0, len(name_of_forum), 1):
            forum_href.append(name_of_forum[i].get_attribute('href'))
        time.sleep(1)
        if q != int(weiye):
            xiayiye = driver.find_element_by_xpath('//*[contains(text(),"下一页")]').click()
            time.sleep(1)
    for item_url in forum_href:
        driver.get(item_url)
        qiandao_button = WebDriverWait(driver, 13).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pagelet_forum/pagelet/sign_mod"]'))).click()
        time.sleep((random.random()) * 2)
        # driver.back()


def user_info_encryption():
    user_id_hash = md5.update(user_id,encode('utf-8'))
    pass





if __name__ == '__main__':
    qiandao()