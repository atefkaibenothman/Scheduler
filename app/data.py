# data.py
#
# This module sends a request to the specified url and sorts the data accordingly.


import requests
from bs4 import BeautifulSoup
from collections import defaultdict


def get_page_content(url):
    page = requests.get(url)
    content = page.content

    return content


def get_course_info(content):
    soup = BeautifulSoup(content, features='html5lib')
    table = soup.find_all('table')
    table = table[1]
    table_rows = table.find_all('tr')

    data = scrape_data(table_rows)

    return data


def scrape_data(table_rows):
    courses = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.replace('\xa0', '').strip() for i in td]
        if len(row) >= 1:
            if row[0] != '':
                courses.append(row)

    courses = courses[2:]

    d = defaultdict()
    for course in courses:
        if len(course) == 1 and course[0][0] != '(':
            course_title = course[0].split()

            dept_name = []
            c = 0
            for i in course_title:
                try:
                    if int(i[0]):
                        course_name = i
                        c += 1
                    break
                except ValueError:
                    dept_name.append(i)
                    c += 1

            dept_name = ' '.join(dept_name)
            # course_name_title = ' '.join(course_title[c:])

            if dept_name not in d.keys():
                d[dept_name] = {}

            d[dept_name].update({course_name:{}})

        elif course[0][0] == '(':
            continue
        else:
            course_code = course[0]
            c_type = course[1]
            sec = course[2]
            units = course[3]
            instructor = course[4]
            time = course[5]
            place = course[6]
            final = course[7]
            max_seats = course[8]
            enrolled = course[9]
            wait_list = course[10]
            requested = course[11]
            reserved = course[12]
            restriction = course[13]
            status = course[16]

            d[dept_name][course_name].update({course_code:{}})

            d[dept_name][course_name][course_code].update({"type": c_type})
            d[dept_name][course_name][course_code].update({"sec": sec})
            d[dept_name][course_name][course_code].update({"units": units})
            d[dept_name][course_name][course_code].update({"instructor": instructor})
            d[dept_name][course_name][course_code].update({"time": time})
            d[dept_name][course_name][course_code].update({"place": place})
            d[dept_name][course_name][course_code].update({"final": final})
            d[dept_name][course_name][course_code].update({"max_seats": max_seats})
            d[dept_name][course_name][course_code].update({"enrolled": enrolled})
            d[dept_name][course_name][course_code].update({"wait_list": wait_list})
            d[dept_name][course_name][course_code].update({"requested": requested})
            d[dept_name][course_name][course_code].update({"reserved": reserved})
            d[dept_name][course_name][course_code].update({"restriction": restriction})
            d[dept_name][course_name][course_code].update({"status": status})

    return d
