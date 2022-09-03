#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time : 2022/8/27 10:29 PM
# @File : keywd_demo.py
# @Author : Meteor
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


class Keyworld(object):
    # 构造函数
    def __init__(self, browser_type, url):
        self.browser_init(browser_type)
        self.visit_url(url)

    # 创建Webdriver对象
    def browser_init(self, browser_type):
        if browser_type == 'chrome':
            self.wd = webdriver.Chrome()
            return self.wd
        if browser_type == 'firefox':
            self.wd = webdriver.Firefox()
            return self.wd
        else:
            self.wd = webdriver.Ie()
            return self.wd
    # 访问Url
    def visit_url(self, url):
        self.wd.get(url)
    # 查找元素
    def find_el(self, type, value):
        if type == 'id':
            self.el = self.wd.find_element(By.ID, value)
            return self.el
        if type == 'xpath':
            self.el = self.wd.find_element(By.XPATH, value)
            return self.el
        if type == 'name':
            self.el = self.wd.find_element(By.NAME, value)
            return self.el
        if type == 'css':
            self.el = self.wd.find_element(By.CSS_SELECTOR, value)
            return self.el
        if type == 'class':
            self.el = self.wd.find_element(By.CLASS_NAME, value)
            return self.el
        if type == 'link':
            self.el = self.wd.find_element(By.LINK_TEXT, value)
            return self.el
        if type == 'tag':
            self.el = self.wd.find_element(By.TAG_NAME, value)
            return self.el
        if type == 'partial_link':
            self.el = self.wd.find_element(By.PARTIAL_LINK_TEXT, value)
            return self.el
        else:
            print('输入的元素查找方式有误')
    # 查找多个元素
    def find_els(self, type, value):
        if type == 'id':
            self.els = self.wd.find_elements(By.ID, value)
            return self.els
        if type == 'xpath':
            self.els = self.wd.find_elements(By.XPATH, value)
            return self.els
        if type == 'name':
            self.els = self.wd.find_elements(By.NAME, value)
            return self.els
        if type == 'css':
            self.els = self.wd.find_elements(By.CSS_SELECTOR, value)
            return self.els
        if type == 'class':
            self.els = self.wd.find_elements(By.CLASS_NAME, value)
            return self.els
        if type == 'link':
            self.els = self.wd.find_elements(By.LINK_TEXT, value)
            return self.els
        if type == 'tag':
            self.els = self.wd.find_elements(By.TAG_NAME, value)
            return self.els
        if type == 'partial_link':
            self.els = self.wd.find_elements(By.PARTIAL_LINK_TEXT, value)
            return self.els
        else:
            print('输入的元素查找方式有误')
    # 清除输入框
    def clear(self):
        self.el.clear
    # 输入内容
    def input_text(self, value):
        self.el.send_keys(value)
    # 敲回车
    def input_enter(self):
        self.el.send_keys(Keys.ENTER)
    # 添加隐式等待
    def implicitly_wait(self, value):
        self.wd.implicitly_wait(value)
    # 点击
    def click(self):
        self.el.click()
    # 鼠标悬停
    def hover(self):
        ActionChains(self.wd).move_to_element(self.el).perform()
    # 关闭标签页
    def close(self):
        self.wd.close()
    # 悬停点击
    def hover_click(self):
        ActionChains(self.wd).click(self.el).perform()

    # 关闭浏览器
    def quit(self):
        self.wd.quit()

if __name__ == '__main__':
    print('重复调用')