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
            if (row[0] != ''):
                courses.append(row)

    school_name = courses[0][0]
    courses = courses[2:]

    print('School: ', school_name)
    print('{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format('Code', 'Type', 'Sec', 'Units',
                                                                'Instructor', 'Time', 'Place', 'Final', 'Max', 'Enr', 'WL', 'Req', 'Nor', 'Rstr', 'Status'))
    print('==========================================================================')
    for course in courses:
        if len(course) == 1 and course[0][0] != '(':
            course_name = course[0]
            print('Course Name: ', course_name)
        elif course[0][0] == '(':
            continue
        else:
            course_code = course[0]
            type = course[1]
            sec = course[2]
            units = course[3]
            instructor = course[4]
            time = course[5]
            place = course[6]
            final = course[7]
            max_seats = course[8]
            enrolled = course[9]
            waitlist = course[10]
            requested = course[11]
            reserved = course[12]
            restriction = course[13]
            status = course[16]

            print('{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format(course_code, type, sec, units,
                                                                        instructor, time, place, final, max_seats, enrolled, waitlist, requested, reserved, restriction, status))
