#!/usr/local/bin/python
# -*- coding: utf8 -*-
'''
Created on 2016年9月2日

@author: PaoloLiu
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import PIL.Image as image
import time, re, io, urllib, random
from urllib import request


def get_merge_image(filename, location_list):
    '''
    根據位置對圖片進行合並還原
    :filename:圖片
    :location_list:圖片位置
    '''
    pass

    im = image.open(filename)

    new_im = image.new('RGB', (260, 116))

    im_list_upper = []
    im_list_down = []

    for location in location_list:

        if location['y'] == -58:
            pass
            im_list_upper.append(im.crop((abs(location['x']), 58, abs(location['x']) + 10, 166)))
        if location['y'] == 0:
            pass

            im_list_down.append(im.crop((abs(location['x']), 0, abs(location['x']) + 10, 58)))

    new_im = image.new('RGB', (260, 116))

    x_offset = 0
    for im in im_list_upper:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    x_offset = 0
    for im in im_list_down:
        new_im.paste(im, (x_offset, 58))
        x_offset += im.size[0]

    return new_im


def get_image(driver, div):
    '''
    下載並還原圖片
    :driver:webdriver
    :div:圖片的div
    '''
    pass

    # 找到圖片所在的div
    background_images = driver.find_elements_by_xpath(div)

    location_list = []

    imageurl = ''

    for background_image in background_images:
        location = {}

        # 在html裏面解析出小圖片的url地址，還有長高的數值
        location['x'] = int(re.findall("background-image: url\(\"(.*)\"\); background-position: (.*)px (.*)px;",
                                       background_image.get_attribute('style'))[0][1])
        location['y'] = int(re.findall("background-image: url\(\"(.*)\"\); background-position: (.*)px (.*)px;",
                                       background_image.get_attribute('style'))[0][2])
        imageurl = re.findall("background-image: url\(\"(.*)\"\); background-position: (.*)px (.*)px;",
                              background_image.get_attribute('style'))[0][0]

        location_list.append(location)

    imageurl = imageurl.replace("webp", "jpg")

    jpgfile = io.BytesIO(urllib.request.urlopen(imageurl).read())

    # 重新合並圖片
    image = get_merge_image(jpgfile, location_list)

    return image


def is_similar(image1, image2, x, y):
    '''
    對比RGB值
    '''
    pass

    pixel1 = image1.getpixel((x, y))
    pixel2 = image2.getpixel((x, y))

    for i in range(0, 3):
        if abs(pixel1[i] - pixel2[i]) >= 50:
            return False

    return True


def get_diff_location(image1, image2):
    '''
    計算缺口的位置
    '''

    i = 0

    for i in range(0, 260):
        for j in range(0, 116):
            if is_similar(image1, image2, i, j) == False:
                return i


def get_track(length):
    '''
    根據缺口的位置模擬x軸移動的軌跡
    '''
    pass

    list = []

    #     間隔通過隨機範圍函數來獲得
    x = random.randint(5, 10)

    while length - x >= 10:
        list.append(x)

        length = length - x
        x = random.randint(5, 10)

    for i in range(length):
        list.append(1)

    return list


def main():
    #     這裏的文件路徑是webdriver的文件路徑
    driver = webdriver.Chrome(executable_path=r"E:\chromedriver\chromedriver.exe")
    #     driver = webdriver.Firefox()

    #     打開網頁
    driver.get("http://www.gsxt.gov.cn/index.html")

    WebDriverWait(driver, 30).until(
        lambda the_driver:the_driver.find_element_by_xpath('//*[@id="keyword"]').is_displayed())

    WebDriverWait(driver, 30).until(
        lambda the_driver: the_driver.find_element_by_xpath('//*[@id="btn_query"]').is_displayed())

    driver.find_element_by_xpath('//*[@id="keyword"]').send_keys('上海秦苍')

    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="btn_query"]').click()


    #     等待頁面的上元素刷新出來
    WebDriverWait(driver, 30).until(
        lambda the_driver: the_driver.find_element_by_xpath("//div[@class='gt_slider_knob gt_show']").is_displayed())
    WebDriverWait(driver, 30).until(
        lambda the_driver: the_driver.find_element_by_xpath("//div[@class='gt_cut_bg gt_show']").is_displayed())
    WebDriverWait(driver, 30).until(
        lambda the_driver: the_driver.find_element_by_xpath("//div[@class='gt_cut_fullbg gt_show']").is_displayed())

    #     下載圖片
    image1 = get_image(driver, "//div[@class='gt_cut_bg gt_show']/div")
    image2 = get_image(driver, "//div[@class='gt_cut_fullbg gt_show']/div")

    #     計算缺口位置
    loc = get_diff_location(image1, image2)

    #     生成x的移動軌跡點
    track_list = get_track(loc)

    #     找到滑動的圓球
    element = driver.find_element_by_xpath("//div[@class='gt_slider_knob gt_show']")
    location = element.location
    #     獲得滑動圓球的高度
    y = location['y']

    #     鼠標點擊元素並按住不放
    print("第一步,點擊元素")
    ActionChains(driver).click_and_hold(on_element=element).perform()
    time.sleep(0.15)

    print("第二步，拖動元素")
    track_string = ""
    for track in track_list:
        track_string = track_string + "{%d,%d}," % (track, y - 445)
        #         xoffset=track+22:這裏的移動位置的值是相對於滑動圓球左上角的相對值，而軌跡變量裏的是圓球的中心點，所以要加上圓球長度的一半。
        #         yoffset=y-445:這裏也是一樣的。不過要註意的是不同的瀏覽器渲染出來的結果是不一樣的，要保證最終的計算後的值是22，也就是圓球高度的一半
        ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=track + 22,
                                                         yoffset=y - 445).perform()
        #         間隔時間也通過隨機函數來獲得
        time.sleep(random.randint(10, 30) / 100)
    print(track_string)
    #     xoffset=21，本質就是向後退一格。這裏退了5格是因為圓球的位置和滑動條的左邊緣有5格的距離
    ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=21, yoffset=y - 445).perform()
    time.sleep(0.1)
    ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=21, yoffset=y - 445).perform()
    time.sleep(0.1)
    ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=21, yoffset=y - 445).perform()
    time.sleep(0.1)
    ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=21, yoffset=y - 445).perform()
    time.sleep(0.1)
    ActionChains(driver).move_to_element_with_offset(to_element=element, xoffset=21, yoffset=y - 445).perform()

    print("第三步，釋放鼠標")
    #     釋放鼠標
    ActionChains(driver).release(on_element=element).perform()

    time.sleep(3)

    #     點擊驗證
    submit = driver.find_element_by_xpath("//input[@id='embed-submit']")
    ActionChains(driver).click(on_element=submit).perform()

    time.sleep(5)

    driver.quit()


if __name__ == '__main__':
    pass

    main()
