Feature:谷歌访问https://crypto.com/exchange/markets，
  自动导航到ZIL/USDT的交易页面
  Scenario: 场景1：正常跳转到到ZIL/USDT的交易页面
    When 谷歌访问https://crypto.com/exchange/markets
    And 点击ZIL/USDT
    Then 进入到了ZIL/USDT的交易页面