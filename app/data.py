# data.py
# Atef Kai Benothman 6/25/2019
#
# This module sends a request to the specified url and sorts the data accordingly.


import requests
from bs4 import BeautifulSoup


def get_course_page(url):
    page = requests.get(url)
    content = page.content

    return content


def get_course_info(content):
    soup = BeautifulSoup(content, features='html5lib')
    table = soup.find_all('table')
    table = table[1]
    table_rows = table.find_all('tr')

    courses = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.replace('\xa0', '').strip() for i in td]
        if len(row) >= 1:
            if row[0] != '':
                courses.append(row)

    # school_name = courses[0][0]
    courses = courses[2:]

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
            course_name_title = ' '.join(course_title[c:])

            print('DEPT: ', dept_name)
            print('COURSE: ', course_name)
            print('COURSE TITLE: ', course_name_title)

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

            print('{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(course_code, c_type, sec, units,
                                                                        instructor, time, place, final, max_seats,
                                                                        enrolled, wait_list, requested, reserved,
                                                                        restriction, status))
