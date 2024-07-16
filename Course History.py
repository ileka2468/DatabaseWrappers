from AbstractTable import AbstractTable


class CourseHistory(AbstractTable):
    _table_name = "Course History"

    class Cols(AbstractTable.Cols):
        CH_ID = "ch_id"
        CH_COURSE = "course"
        CH_SECTION = "section"
        CH_TERM = "term"
        CH_START_YEAR = "start_year"
        CH_PROFESSOR_ID = "professor_id"
        CH_END_YEAR = "end_year"


def main():
    print(CourseHistory.get_all(CourseHistory.Cols.CH_COURSE, CourseHistory.Cols.CH_START_YEAR))


main()


