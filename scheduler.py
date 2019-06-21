from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re

chrome_driver_path = "D:\drivers\chromedriver.exe"
url = "https://www.reg.uci.edu/perl/WebSoc"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

dd_menu = Select(driver.find_element_by_name("Dept"))

try:
    lt = []
    for option in dd_menu.options:
        line = option.text
        line_split = line.replace(".", " ").split()

        l = []
        if line_split[1].isupper():
            l.append(line_split[0] + " " + line_split[1])
        else:
            if line_split[0].isupper():
                l.append(line_split[0])

        lt.append(l)

    with open("course_list.txt", "w") as f:
        for course in lt:
            if (len(course) == 1):
                f.write(course[0])

                if course[0] != "WRITING":
                    f.write("\n")

finally:
    driver.quit()
    print("program finished running")
