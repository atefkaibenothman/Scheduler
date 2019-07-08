# departments.py
# Atef Kai Benothman 6/25/2019
#
# This module creates a valid url based on the user input in app/userinterface.py.


import urllib.parse
import urllib.request

BASE_URL = 'https://www.reg.uci.edu/perl/WebSoc'


def build_search_url(year_term, dept_name, show_finals, show_comments):
    query_param = [('YearTerm', year_term + '-92'), ('ShowFinals', show_finals), ('ShowComments', show_comments),
                   ('Dept', dept_name)]

    return BASE_URL + '?' + urllib.parse.urlencode(query_param)
