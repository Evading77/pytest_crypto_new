import os
import yaml

#读取yaml测试用例文件
def read_testcase_yaml(yaml_name):
    with open(os.getcwd()+'/tests/api_tests/data/'+yaml_name,encoding='utf-8') as f:
        value=yaml.load(stream=f,Loader=yaml.FullLoader)
        return value

