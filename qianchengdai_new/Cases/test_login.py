# -*- coding:utf-8 -*-
from Data.test_data import login_data
from Common.Public.Log import Mylog
import pytest
logger=Mylog()


@pytest.mark.error
# @pytest.mark.skip(reason='不需测试')
@pytest.mark.parametrize('data',login_data.error_info)
def test_01_login_error(data, init_login):
    logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},登录名是:{},登录密码是:{},期望值是:{}'.format(data['module'],
                            data['Caseid'],data['title'], data['username'],data['password'],data['expect']))
    login=init_login[1]
    login.register(data['username'], data['password'])
    actual = login.get_error_info()
    try:
        assert(data['expect']==actual)
        Testresult = 'pass'
    except AssertionError as e:
        Testresult = 'fail'
        raise e
    finally:
        logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'],data['Caseid'],Testresult))


@pytest.mark.error
@pytest.mark.parametrize('data', login_data.alter_error)
def test_02_login_alter_error(data,init_login):
    logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},登录名是:{},登录密码是:{},期望值是:{}'.format(data['module'],
                            data['Caseid'],data['title'], data['username'],data['password'],data['expect']))
    login = init_login[1]
    login.register(data['username'], data['password'])
    actual = login.get_alter_error()
    try:
        assert(data['expect'] == actual)
        Testresult = 'pass'
    except AssertionError as e:
        Testresult = 'fail'
        raise e
    finally:
        logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'],data['Caseid'],Testresult))


# @pytest.mark.skip(reason="不需测试")
@pytest.mark.success
@pytest.mark.parametrize('data',login_data.success_data)
def test_03_login_success(data,init_login):
    logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},登录名是:{},登录密码是:{},期望值是:{}'.format(data['module'],
                            data['Caseid'],data['title'], data['username'],data['password'],data['expect']))
    login=init_login[1]
    # 登录
    login.register(data['username'],data['password'])
    # 获取登录用户名
    login_name=login.get_actual_loginname()
    try:
        assert(data['expect']==login_name)
        Testresult='pass'
    except AssertionError as e:
        Testresult = 'fail'
        raise e
    finally:
        logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'],data['Caseid'],Testresult))


if __name__ == '__main__':
   pytest.main()