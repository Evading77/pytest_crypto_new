import datetime
import json

import pytest
from common.all_request import AllRequest
from common.log import Logger
from common.yaml_util import read_testcase_yaml

logger=Logger(logger="test_api.py").getlog()

class TestApi:
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("get_humidity.yaml"))
    def test_get_humidity(self, caseinfo):
        #获取请求参数
        url = caseinfo['request']['url']
        method = caseinfo['request']['method']
        params = caseinfo['request']['params']
        res = AllRequest().all_send_request(method, url=url, data=params)
        result = json.loads(res.content)
        logger.info("接口返回数据为：{}".format(result))
        #获取返回的最大湿度和最小湿度
        max_rh = result['forecast_detail'][1]["max_rh"]
        min_rh = result['forecast_detail'][1]["min_rh"]
        #按照返回值的格式得到后天的日期
        exc= (datetime.datetime.now()+datetime.timedelta(days=2)).strftime('%Y%m%d')
        logger.info("后天的期望值为：{}".format(exc))
        #获取返回值的后天日期
        act = result['forecast_detail'][1]['forecast_date']
        logger.info("后天的实际值为：{}".format(act))
        #断言取到的数据是否是后天的
        assert exc==act,logger.info("后天：{0}，湿度为：{1}~{2}".format(act, min_rh, max_rh))
