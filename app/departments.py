# departments.py
# Atef Kai Benothman 6/25/2019
#
# This module adds all the relevant course information to the dept_dict dictionary

from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def initialize_dept_dict(dept_list_path):
    d = defaultdict()
    for line in open(dept_list_path, "r"):
        d[line.strip()] = {}

    return d


def populate_dict(dept_name, dept_dict, chrome_driver_path, url, driver):
    if dept_name not in dept_dict.keys():
        print("'{}' is not a valid department".format(dept_name))
    else:
        dd_menu = Select(driver.find_element_by_name("Dept"))
        dd_menu.select_by_value(dept_name)

        driver.find_element_by_name("Submit").click()


if __name__ == "__main__":

    dept_list_path = "data\dept_list.txt"
    dept_dict = initialize_dept_dict(dept_list_path)

    chrome_driver_path = "D:\drivers\chromedriver.exe"
    url = "https://www.reg.uci.edu/perl/WebSoc"

    driver = webdriver.Chrome(chrome_driver_path)
    driver.get(url)

    dept_name = "WRITING"
    populate_dict(dept_name, dept_dict, chrome_driver_path, url, driver)
