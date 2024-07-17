from AbstractTable import AbstractTable


class CoursesTaught(AbstractTable):
    _table_name = "Courses Taught"

    class Cols(AbstractTable.Cols):
        COURSES_TAUGHT_ID = "ctghtid"
        COURSE_CODE_ID = "course_code_id"
        PROFESSOR_ID = "professor_id"



