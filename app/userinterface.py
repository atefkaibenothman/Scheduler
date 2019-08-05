# userinterface.py
#
# This module handles the CLI for
# testing the api and program.

# Files
import urlbuilder
import data
import database


def run():
    web_list = user_input()
    web_content = get_content(web_list)

    c = database.columns()
    v = database.values(web_content)
    database.insert(c, v)


def get_content(weblist: list):
    course_data_list = []
    for url in weblist:
        try:
            content = data.get_page_content(url)
            course_data = data.get_course_info(content)

            course_data_list.append(course_data)
        except IndexError:
            print("could not retrieve course data.... course removed from list")

    return course_data_list


def user_input():
    running = True
    website_list = []
    while running:
        year_term = input("Year Term [2019]: ") or "2019"
        dept_name = input("Department Name [ICS]: ") or "I&C SCI"
        show_finals = input("Show Finals [1]: ") or "1"
        show_comments = input("Show Comments [0]: ") or "0"

        url = urlbuilder.build_search_url(
            year_term,
            dept_name.upper(),
            show_finals,
            show_comments)

        print()
        print("YearTerm: {}\nDeptName: {}".format(year_term, dept_name))
        website_list.append(url)
        print("Website: ", url)
        print()

        # wish_to_quit = input("Quit [yes]: ") or "yes"
        # print()
        # if wish_to_quit == "yes":
        #     running = False

        running = False

    return website_list


if __name__ == "__main__":
    run()
