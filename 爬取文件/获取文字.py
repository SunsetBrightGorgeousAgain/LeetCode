#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/12/14 10:20
@Author  : YuJinNeng
@Site    :
@File    : 爬取代码.py
@Software: PyCharm
"""
import random
import time
from bs4 import BeautifulSoup
from urllib import request
import re

base_url = ""


def down_txt(href_content, book_name):
    number_content = href_content.split(".")[0]
    print(number_content)
    if '/' not in number_content:
        return None
    number_content = number_content.split("/")[1]
    print(number_content)
    if not number_content.isdigit():
        return None
    html_addr = base_url + number_content + ".html"
    print(html_addr)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"}
    html_content = request.Request(html_addr, headers=headers)
    content = request.urlopen(html_content).read().decode("utf-8")
    soup = BeautifulSoup(content, 'html.parser')

    all_content = soup.select(".articleList .content")[0]
    all_content = all_content.getText()
    return all_content


def get_add_url():
    lll = 0
    for i in range(1, 6):
        url_addr = "" % i
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"}
        html_content = request.Request(url_addr, headers=headers)
        content = request.urlopen(html_content).read().decode("utf-8")

        soup = BeautifulSoup(content, 'html.parser')  # 文档对象
        story_list = soup.select('.articleList .img-center')
        print(story_list)
        with open("成品展示.txt", 'a+', encoding='utf-8') as f:
            for j, one_story in enumerate(story_list):
                a_tag = one_story.contents[0]  # 名称
                href_content = one_story.get("href")  # 链接地址
                try:
                    content = down_txt(href_content, a_tag)
                except Exception as e:
                    content = None
                if content is not None:
                    f.write("第一章  ")
                    f.write(str(a_tag))
                    f.write('\n')
                    f.write("—————————————————————")
                    for content in content:
                        f.write(content)
                    f.write('\n'*5)
                # time.sleep(random.randint(3, 10))


if __name__ == '__main__':
    get_add_url()
