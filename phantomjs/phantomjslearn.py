#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
#设置自定义header
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
dcap["phantomjs.page.settings.Accept"] = ("text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
dcap["phantomjs.page.settings.Accept-Encoding"] = ("gzip, deflate")
dcap["phantomjs.page.settings.Accept-Language"] = ("zh-CN,zh;q=0.8")
dcap["phantomjs.page.settings.Cache-Control"] = ("max-age=0")
dcap["phantomjs.page.settings.Connection"] = ("keep-alive")
dcap["phantomjs.page.settings.Host"] = ("www.qichacha.com")
dcap["phantomjs.page.settings.Referer"] = ("http://www.qichacha.com/")
dcap["phantomjs.page.settings.Upgrade-Insecure-Requests"] = ("1")

driver = webdriver.PhantomJS(desired_capabilities=dcap)

driver.set_page_load_timeout(10)
driver.maximize_window()

driver.get("http://www.qichacha.com/user_login")

# driver.save_screenshot('1.png')
slider = driver.find_element_by_css_selector('#nc_1_n1z')
print(slider.tag_name)

driver.quit()