# database.py
#
# This module inserts the dictionary into a table in sql.

import json
import mysql.connector as mysql


def initial_run():

    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="password"
    )

    print(db)


def print_dict(web_content):
    for dept in web_content:
        print(json.dumps(dept, indent=3))


def columns():
    c = ["dept_name", "course_name", "course_code"]
    column = ", ".join("'" + str(i) + "'" for i in c)

    return column


def values(web_content: list):
    value_list = []
    for d in web_content:
        for dept_name in d:
            for course_name in d[dept_name]:
                for course_code in d[dept_name][course_name]:
                    l = [dept_name, course_name, course_code]
                    value = ", ".join("'" + str(i) + "'" for i in l)

                    value_list.append(value)

    return value_list


def insert(column, value_list):
    for i in value_list:
        sql_template = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("test", column, i)
        print(sql_template)


if __name__ == "__main__":
    initial_run()
