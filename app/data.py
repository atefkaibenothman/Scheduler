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
    soup = BeautifulSoup(content, features='lxml')
    course_titles = soup.find_all('td', {'class': 'CourseTitle'})

    for course in course_titles:
        print('Course Title: ', course.text.strip())
        print('----------')
