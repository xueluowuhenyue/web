# -*- coding:utf-8 -*-
from Data.test_data import bid_data
from Common.Public.Log import Mylog
import pytest

logger=Mylog()


@pytest.mark.error
@pytest.mark.parametrize('data', bid_data.error_data)
def test_01_error(data,init_bid):
    logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},项目名字是：{},投资金额是:{},期望结果:{}'.format(data['module'],
                    data['Caseid'], data['title'],data['bid_name'], data['amount'], data['expect']))

    bid = init_bid[0]
    # 清空输入框
    bid.clear_input()
    # 输入投资金额
    bid.input_money(data['amount'])
    # 点击投资按钮
    bid.get_button()
    # 获取错误提示
    context=bid.get_error_prompt()
    # print(context)
    # 点击确认
    bid.click_confirm()
    try:
        assert(context == data['expect'])
        Testresult = 'pass'
    except AssertionError as e:
        Testresult = 'fail'
        raise e
    finally:
        logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'], data['Caseid'], Testresult))


@pytest.mark.error
@pytest.mark.parametrize('data',bid_data.error_whole_ten)
def test_02_whole_ten(data,init_bid):
    logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},项目名字是：{},投资金额是:{},期望结果:{}'.format(data['module'],
            data['Caseid'], data['title'],data['bid_name'], data['amount'],data['expect']))
    bid = init_bid[0]
    # 清空输入框
    bid.clear_input()
    # 输入不是10的倍数金额
    bid.input_money(data['amount'])
    # 获取提示
    context=bid.get_button_prompt()
    try:
        assert(context==data['expect'])
        Testresult = 'pass'
    except AssertionError as e:
        Testresult = 'fail'
        raise e
    finally:
        logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'], data['Caseid'], Testresult))


@pytest.mark.success
@pytest.mark.parametrize('data',bid_data.success_data)
def test_03_success(data,init_bid):
    logger.info('正在执行{}模块第{}条测试用例,用例名字是:{},项目名字是：{},投资金额是:{},期望结果:{}'.format(data['module'],
    data['Caseid'], data['title'], data['bid_name'], data['amount'], data['expect']))
    bid = init_bid[0]
    personal = init_bid[1]
    # 获取投资前的金额
    begin_money = int(bid.get_begin_money() * 100)
    # print(begin_money)
    # 投资
    bid.input_money(data['amount'])
    # 点击投资按钮
    bid.get_button()
    # 获取提示
    prompt = bid.get_prompt()
    # 点击弹窗按钮
    bid.alter_click()
    # 获取投资后的余额
    end_money = int(personal.get_balance() * 100)
    # print(end_money)
    try:
        assert(prompt==data['expect'])
        assert(begin_money==end_money + int(data['amount']) * 100)
        Testresult = 'pass'
    except AssertionError as e:
        Testresult = 'fail'
        raise e
    finally:
        logger.info('{}模块第{}条测试用例,测试结果是{}'.format(data['module'], data['Caseid'], Testresult))


if __name__ == '__main__':
    pytest.main()