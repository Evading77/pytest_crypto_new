import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from common.log import Logger

logger=Logger(logger="base_page.py").getlog()
class BasePage:
    def __init__(self,driver):
        self.driver=driver

    #打开浏览器，加载网页
    def geturl(self,url):
        self.driver.get(url)
        logger.info("打开浏览器，跳转至{}".format(url))
        self.driver.maximize_window()

    #元素是否可见
    def element_is_display(self,args):
        try:
            wait=WebDriverWait(self.driver, 60)
            wait.until(lambda x: x.find_element(*args).is_displayed())
            logger.info("{}元素已找到".format(args))
            return True
        except Exception as e:
            logger.error("元素定位异常：{}".format(e))
            self.save_screen_allure("failure")
            assert False

    # 定位元素
    def locate_element(self, args):
        try:
            self.element_is_display(args)
            return self.driver.find_element(*args)
        except Exception as e:
            logger.error("元素定位异常：{}".format(e))

    # 单击
    def click(self, args):
        self.locat_element(args).click()

    #滚动条操作
    def scroll_to(self, x, y):
        js="window.scrollTo({0},{1});".format(x,y)
        self.driver.execute_script(js)
        logger.info("已拖动浏览器到坐标为({0},{1})的页面".format(x,y))

    #生成截图并加入到allure报告里面
    def save_screen_allure(self,status):
        # 获得一个时间戳的字符串
        str_time = time.strftime('%Y-%m-%d-%H-%M-%S-', time.localtime())
        # 图片路径
        imge_path = "./image/" + str_time + status+".png"
        # 截图
        self.driver.save_screenshot(imge_path)
        # 读取这个图片信息并且把它加入到allure报告里面
        with open(imge_path, mode="rb") as f:
            stream = f.read()
        allure.attach(body=stream, name=imge_path, attachment_type=allure.attachment_type.PNG)

    #断言
    def my_assert(self,exec,act):
        if exec in act:
            self.save_screen_allure("sucess")
            logger.info("用例运行成功并截图保存")
        else:
            logger.error("断言失败，预期值为{0}，实际值为{1}".format(exec, act))
            self.save_screen_allure("failure")


