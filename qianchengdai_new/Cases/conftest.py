#  -*- coding:utf-8  -*-

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from Data.test_data import bid_data
from Pages.bid import BidPage
from Pages.home import HomePage
from Pages.login import LoginPage
import pytest

from Pages.personal import PersonalPage


@pytest.fixture(scope="module")
def init_login():
    driver = Chrome()
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # driver = Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(30)
    # 初始化登录页面
    login = LoginPage(driver)
    yield driver,login
    driver.quit()


@pytest.fixture(scope="module")
def init_bid():
    driver=Chrome()
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # driver = Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(30)
    # 初始化登录页面
    login = LoginPage(driver)
    # 首页
    home = HomePage(driver)
    # 投资页面
    bid = BidPage(driver)
    # 个人页面
    personal = PersonalPage(driver)
    # 登录
    login.register(bid_data.login_data['user_name'], bid_data.login_data['password'])
    # 选择投标项目
    home.get_bid_project()
    yield bid,personal
    driver.quit()