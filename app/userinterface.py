# userinterface.py
# Atef Kai Benothman 6/25/2019
#
# This module handles the simple (temporary) user interface for
# testing the program.


import urlbuilder
import data
import json


def get_dept_url():
    year_term = input('Enter the year term [2019]: ') or '2019'
    dept_name = input('Enter the department name [I&C SCI]: ') or 'I&C SCI'
    show_finals = input('Show finals? [1]: ') or '1'
    show_comments = input('Show comments? [0]: ') or '0'
    print()

    return(urlbuilder.build_search_url(
        year_term, dept_name.upper(), show_finals, show_comments))


def run(url):
    content = data.get_course_page(url)
    course_info = data.get_course_info(content)

    with open("course_data.json", "w") as json_file:
        json.dump(course_info, json_file)





if __name__ == '__main__':
    url = get_dept_url()
    run(url)
