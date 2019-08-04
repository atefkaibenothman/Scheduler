import sqlite3


def run():
    conn = sqlite3.connect('schedule.db')

    c = conn.cursor()

    # c.execute("""CREATE TABLE schedule (
    #             dept_name text,
    #             course_name text,
    #             course_code text
    #             )""")



    conn.commit()

    conn.close()

run()