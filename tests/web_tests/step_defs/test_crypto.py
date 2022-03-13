import allure
from pytest_bdd import when, parsers, then, scenario
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from common.log import Logger

logger=Logger(logger="test_crypto.py").getlog()

@when(parsers.parse("谷歌访问{url}"))
@allure.step("谷歌访问https://crypto.com/exchange/markets")
def go_to_url(url,browser):
    base=BasePage(browser)
    base.geturl(url)

@when("点击ZIL/USDT")
@allure.step("点击ZIL/USDT")
def click_trade(browser):
    base = BasePage(browser)
    #等待加载出部分页面，然后拖动滚动条到底部，ele_load_locate为Markets-Spot下数据区域
    ele_load_locat=(By.XPATH,"//div[@id='swiper-container-2']")
    base.element_is_display(ele_load_locat)
    base.scroll_to(0,100000)
    #定位到ZIL/USDT图标，并点击
    ele_target_locat=(By.XPATH, "//img[@alt='ZIL']")
    ele_target=base.locate_element(ele_target_locat)
    browser.execute_script("arguments[0].click();", ele_target)

@then("进入到了ZIL/USDT的交易页面")
@allure.step("进入到了ZIL/USDT的交易页面")
def zil_page(browser):
    base = BasePage(browser)
    # 等待加载出Trading History,然后拖动滚动条到底部，ele_load_locate为Trading History
    ele_load_locat=(By.XPATH,"//div[@class='trading-history-title']")
    base.element_is_display(ele_load_locat)
    base.scroll_to(0,0)
    #目标页面的关键信息
    exec="ZIL/USDT"
    ele_target_locat = (By.XPATH, "//div[@class='toggle']")
    act=base.locate_element(ele_target_locat).text
    #断言
    base.my_assert(exec, act)

@scenario("../features/crypto.feature","场景1：正常跳转到到ZIL/USDT的交易页面")
def test_crypt():
    pass



