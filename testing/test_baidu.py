# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBaidu():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()

  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_baidu(self):
    self.driver.get("https://www.baidu.com/")
    self.driver.set_window_size(1293, 773)
    self.driver.find_element(By.ID, "kw").click()
    self.driver.find_element(By.ID, "kw").send_keys("霍格沃茨魔法学校")
    self.driver.find_element(By.ID, "su").click()
    time.sleep(5)

    self.driver.close()
  
