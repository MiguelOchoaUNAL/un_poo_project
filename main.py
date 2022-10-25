from unicodedata import name
import modules.connect_db as CONNECT_DB
import modules.students as STUDENTS
import modules.subjects as SUBJECTS
import modules.classification as CLASSIFY
import modules.academic_history as ACADEMIC_HISTORY
import modules.menu_students as MENU_STUDENTS
import modules.main_menu as MENU

def main():

    my_connection = CONNECT_DB.connectionToDB()
    STUDENTS.createStudentTable(my_connection)
    SUBJECTS.createSubjectsTable(my_connection)
    CLASSIFY.createClassificationTable(my_connection)
    ACADEMIC_HISTORY.createAcademicHistoryTable(my_connection)
    #ACADEMIC_HISTORY.addSubject(my_connection)
    #MENU_STUDENTS.mainMenuStudents(my_connection)
    # STUDENTS.selectStudentByID(my_connection, 1)
    MENU.mainMenu(my_connection)
    CLASSIFY.getstudentinfo(my_connection)
    CLASSIFY.UpdateClassification(my_connection)
    MAIN

if __name__ == "__main__":
    main()
