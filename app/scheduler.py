# scheduler.py
# Atef Kai Benothman 6/20/2019
#
# This module web-scrapes all the departments from UCI's schedule of classes
# wesbite (https://www.reg.uci.edu/perl/WebSoc) and writes each department
# to the dept_list.txt file
#
# IMPORTANT: this module should only be ran if a department is added/removed

# https://stackoverflow.com/questions/13555307/how-to-get-the-option-text-using-beautifulsoup/13555350
# page = driver.page_source
# https://www.reg.uci.edu/perl/WebSoc?YearTerm=2019-92&ShowFinals=1&ShowComments=1&Dept=WRITING

from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def initialize_driver(driver_path, url):
    driver = webdriver.Chrome(driver_path)
    driver.get(url)

    return driver


def get_department_list(driver):
    dd_menu = Select(driver.find_element_by_name("Dept"))

    dept_list = []
    for option in dd_menu.options:
        line = option.text.replace(".", ",").split()

        dept_name = ""
        if line[1].isupper():
            dept_name = line[0] + " " + line[1]
        else:
            if line[0].isupper():
                dept_name = line[0]

        dept_list.append(dept_name)

    return dept_list[1:]


def write_dept_to_file(dept_list, dept_list_path):
    with open(dept_list_path, "w") as file:
        for dept in dept_list:
            if (dept != "WRITING"):
                file.write(dept + "\n")
            else:
                file.write(dept)

    return


if __name__ == "__main__":
    chrome_driver_path = "D:\drivers\chromedriver.exe"
    dept_list_path = "data\dept_list.txt"
    url = "https://www.reg.uci.edu/perl/WebSoc"

    driver = initialize_driver(chrome_driver_path, url)

    try:
        dept_list = get_department_list(driver)
        write_dept_to_file(dept_list, dept_list_path)
    finally:
        driver.quit()
