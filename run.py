import os

import pytest

if __name__ == '__main__':

    pytest.main(['-vs'])
    # os.system('allure generate ./report/tempdata -o ./report/report --clean')
