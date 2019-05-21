# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Common.Public.Log import Mylog

logger=Mylog()


class BasePage:

    def __init__(self, driver: Chrome):
        self.driver = driver

    def wait_ele(self, locator, timeout=10, poll_frequency=0.5) -> WebElement:
        '''本函数用于等待元素'''
        Wait = WebDriverWait(self.driver,timeout,poll_frequency)
        try:
            ele = Wait.until(ec.presence_of_element_located((locator)))
            return ele
        except Exception as e:
            logger.error('出错啦错误是{}'.format(e))

            raise e

    def wait_click(self,locator,timeout=20,poll_frequency=0.5) -> WebElement:
        '''等待元素可以点击'''
        try:
            Wait = WebDriverWait(self.driver,timeout,poll_frequency)
            ele=Wait.until(ec.element_to_be_clickable(locator))
            return ele.click()
        except Exception as e:
            logger.error('出错啦错误是{}'.format(e))
            raise e

    def scroll_bar(self,ele):
        # 滚动页面到元素位置
        self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)

    def wait_list(self, locator, timeout=10, poll_frequency=0.5) -> list:
        '''本函数用于获取元素列表'''
        Wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            ele = Wait.until(ec.presence_of_all_elements_located(locator))
            return ele
        except Exception as e:
            logger.error('出错啦错误是{}'.format(e))
            raise e

    def screenshot(self,picture_path):
        # 截图
        self.driver.save_screenshot(picture_path)
