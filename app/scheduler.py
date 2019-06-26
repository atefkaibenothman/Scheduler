# scheduler.py
# Atef Kai Benothman 6/20/2019
#
# This module send a request to 'https://www.reg.uci.edu/perl/WebSoc' and fills
# the dept_list.txt file with a list of all the department names in order.

import requests
from bs4 import BeautifulSoup


def get_result(url):
    result = requests.get(url)
    return result


def get_status_code(result):
    return result.status_code


def get_result_content(result):
    return result.content


def get_department_names(content):
    soup = BeautifulSoup(content, features='lxml')

    options = soup.find('select', {'name': 'Dept'}).text.split('\n')
    options = options[2:]

    return(options[:-1])


def clean_department_list(dept_list):
    dept_codes = []
    dept_names = []
    for dept in dept_list:
        line = dept.replace('.', ' ').split()

        dept_code = ''
        dept_full_name = ''

        if line[1].isupper() and line[0] != 'UCDC':
            dept_code = line[0] + ' ' + line[1]

            for i in line[2:]:
                dept_full_name = dept_full_name + i + ' '
                dept_full_name.strip()
        else:
            dept_code = line[0]

            for i in line[1:]:
                dept_full_name = dept_full_name + i + ' '
                dept_full_name.strip()

        dept_codes.append(dept_code)
        dept_names.append(dept_full_name)

    return dept_codes, dept_names


def fill_dept_list_file(dept_codes, dept_list_path):
    with open(dept_list_path, 'w') as file:
        for dept in dept_codes:
            if (dept != 'WRITING'):
                file.write(dept + '\n')
            else:
                file.write(dept)
    return


def run():
    base_url = 'https://www.reg.uci.edu/perl/WebSoc'
    result = get_result(base_url)
    content = get_result_content(result)

    full_department_list = get_department_names(content)
    dept_codes, dept_names = clean_department_list(full_department_list)

    dept_list_path = 'data\dept_list.txt'
    fill_dept_list_file(dept_codes, dept_list_path)


if __name__ == '__main__':
    run()
