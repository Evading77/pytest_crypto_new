# Web&API自动化测试框架

## 框架介绍
- Web自动化框架：python3 + pytest-bdd + selenium + log + allure + jenkins。 
  - web自动化框架是基于pytest-bdd的行为驱动框架。
  - Web自动化框架支持运行失败时截图、用例成功运行完成后也进行截图，来保存用例成功运行的有力证据。
    这些截图会附在最后生成的allure报告中。
  - 通过pytest.ini文件配置运行参数，支持失败重跑和多线程运行。
  - 结合allure，运行后可以生成漂亮的allure测试报告。
  - 使用Jenkins持续集成。
    
- API自动化框架：python3 + pytest + requests + yaml + log + allure + jenkins。  
  - API自动化框架是基于pytest+requests，结合yaml的数据驱动框架。
  - 通过pytest.ini文件配置运行参数，支持失败重跑和多线程运行。
  - 结合allure，运行后可以生成漂亮的allure测试报告。
  - 使用Jenkins持续集成。

### 安装指南
1、pip install -r requirements.txt，导入相关依赖库。  
2、下载allure，解压，配置path路径。  
3、下载浏览器对应的driver，并放到对应路径下。  

### 用例说明
- task1:使用Chrome浏览器，访问https://crypto.com/exchange/markets，自动导航到ZIL/USDT的交易页面。
- task2：MyObservatory，在程序的9天预测页面中抓取相应接口，使用接口自动化，从响应中提取后天的相对湿度（例如，60-85%）。  
由于之前主要用的是数据驱动和关键字驱动，行为驱动模式是临时学习的，所以总共花了2天左右时间，还有一些不太完善的地方，欢迎交流和指正，谢谢。

### 更新说明
1、由于https://crypto.com/exchange/markets页面加载时间特别长，且不需要等页面所有元素都加载完成后才进行下一步。
所以在Web自动化的confest.py文件中生成driver时添加了DesiredCapabilities参数，并设置desired_capabilities["pageLoadStrategy"]="none"，
结合WebDriverWait，能够让Web自动化在不影响定位元素的前提下运行时间大大缩短。  
2、封装了web自动化中一些操作方法，并且在每次对元素操作前先判断元素是否可见，并加入try进行捕获异常，结合WebDriverWait，增强了代码的可维护性和强健性。  
3、其他一些小优化，如log日志中加入行号、区分失败截图和用例运行成功截图等。



