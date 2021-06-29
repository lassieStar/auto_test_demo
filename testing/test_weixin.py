import time
import webbrowser
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pprint import pprint


def test_login():
    # 复用浏览器
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    driver.find_element_by_id("menu_contacts").click()
    sleep(1)
    cookies=driver.get_cookies()
    # 把cookies写入文件
    with open("data.yaml","w",encoding="UTF-8") as f:
        yaml.dump(cookies,f)
    print(driver.get_cookies())

def test_wework():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851052706118'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'kwSMmAStJXHTjsNlllUEomh8GHWzZItTtcGtuLoNhApjmkxFSkhM97YRwRsgLlRNXaEYYtE9aa7j-kgc6SiENvur_2uTq23vMSY5FGXGzQbNv4EEhpHBHiXQID2xWNEpqxM7polaim_Mye5Ofmk0m4xmiLOvI_ccQwO8PtGJTyHmAEGADXRUGltGCARDG1_B9KGCkYAqe1fVoipBAXHtbGLIwNPehjKWIX4XqAA8sDXQFDjZRArjRmmRQW15Nnzm_bHAGPW6CHGsPuGAz_SKKw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '5gdV6YTrve80IfFhhMbuPdw23LeHpxuG-Kdi_vQzuuHMNMvlje9gILp4LqsBF5Pz'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a4556423'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325044262083'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851052706118'}, {'domain': 'work.weixin.qq.com', 'expiry': 1625010136, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5mramee'}, {'domain': '.qq.com', 'expiry': 1625066120, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1654086485.1624978542'}, {'domain': '.work.weixin.qq.com', 'expiry': 1656515096, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1624540117,1624544054'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '2836970250'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1627757419, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1688051720, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.574386459.1592492840'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '974d6a5753b47638d8c09a4333e4553b239c797b1c645d20c76b9a5ee705a0f9'}, {'domain': '.qq.com', 'expiry': 2147483653, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'lRbRdBdS6F'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1624979096'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '330634795951441'}, {'domain': '.qq.com', 'expiry': 1918739644, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '0d3bdbc51bb23f96'}, {'domain': '.qq.com', 'expiry': 1624979780, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '1120555008'}, {'domain': '.work.weixin.qq.com', 'expiry': 1627571721, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
    with open("data.yaml","r",encoding="UTF-8") as f:
        yaml_data=yaml.safe_load(f)
    for cookie in yaml_data:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    time.sleep(1)
    driver.quit()
# 完成添加联系人操作