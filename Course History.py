from AbstractTable import AbstractTable


class CourseHistory(AbstractTable):
    _table_name = "Course History"

    class Cols(AbstractTable.Cols):
        PROFESSOR_ID = "ch_id"
        PROFESSOR_NAME = "course"
        PROFESSOR_EMAIL = "section"
        PROFESSOR_POSITION = "term"
        PROFESSOR_SCHOOL = "term"
        RMP_PROFESSOR_DEPARTMENT = "term"
        RMP_PROFILE_NAME = "end_year"
        RMP_PROFILE_ID = "rmp_profile_id"
        PROFILE_PICTURE = "profile_piture"
        FACULTY_ID = "faculty_id"
        RMP_RATING_DISTRO = "rmp_rating_distro"


def main():
    print(Professors.get_multiple_records( {Professors.Cols.PROFESSOR_POSITION: "Professor"}, Professors.Cols.PROFESSOR_NAME, Professors.Cols.PROFESSOR_ID))


main()
