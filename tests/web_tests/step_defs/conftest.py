import os
import sys

import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

from common.log import Logger
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
logger=Logger(logger="conftest.py").getlog()

driver=None
#获取chromedriver.exe路径
base_dir = os.path.join(sys.path[1], '')
driver_path=base_dir+'/drivers/chromedriver.exe'

@pytest.fixture(scope='session',autouse=True)
def browser():
    global driver
    if driver is None:
        #不用等页面所有的资源加载完才进行下一步操作
        desired_capabilities=DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"]="none"
        driver=webdriver.Chrome(desired_capabilities=desired_capabilities,service=Service(driver_path))
        logger.info("成功得到driver")
    yield driver
    driver.quit()
    logger.info("关闭浏览器，自动化测试结束")