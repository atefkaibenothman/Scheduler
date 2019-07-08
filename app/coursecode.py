# coursecode.py
# Atef Kai Benothman 7/07/2019
#
# This is the CourseCode class module


class CourseCode:
    def __init__(self, course_code, c_type, sec, units, instructor, time, place, final, max_allowed, enrolled, wait_list,
                 requested, reserved, restriction, status):
        self.course_code = course_code
        self.c_type = c_type
        self.sec = sec
        self.units = units
        self.instructor = instructor
        self.time = time
        self.place = place
        self.final = final
        self.max_allowed = max_allowed
        self.enrolled = enrolled
        self.wait_list = wait_list
        self.requested = requested
        self.reserved = reserved
        self.restriction = restriction
        self.status = status

    def get_course_code(self):
        return self.course_code

    def get_ctype(self):
        return self.c_type

    def get_sec(self):
        return self.sec

    def get_units(self):
        return self.units

    def get_instructor(self):
        return self.instructor

    def get_time(self):
        return self.time

    def get_place(self):
        return self.place

    def get_final(self):
        return self.final

    def get_max_allowed(self):
        return self.max_allowed

    def get_enrolled(self):
        return self.enrolled

    def get_wait_list(self):
        return self.waitlist

    def get_requested(self):
        return self.requested

    def get_reserved(self):
        return self.reserved

    def get_restriction(self):
        return self.restriction

    def get_status(self):
        return self.status


