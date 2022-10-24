def createClassificationTable(connection):
    # recorremos la base de datos con el objeto de conexión
    cursorObj = connection.cursor()
    STUDENT_ID = "student_id INTEGER"
    NAME = "name TEXT"
    LAST_NAME = "lastName TEXT"
    AMOUNT_SUBJECTS = "amountSubjects INTEGER"
    CREDIT_SUM = "creditSum INTEGER"
    AVERAGE = "average INTEGER"
    CREATE_STATEMENT = f"CREATE TABLE IF NOT EXISTS classification({STUDENT_ID},{NAME},{LAST_NAME},{AMOUNT_SUBJECTS},{CREDIT_SUM},{AVERAGE})"
    cursorObj.execute(CREATE_STATEMENT)  # creamos la tabla materias
    connection.commit()  # aseguramos la persistencia guardando la tabla en el disco
def getstudentinfo(connection): #tomamos la información relevante de la tabla students y la pasamos a la tabla clasificación
    cursorObj = connection.cursor()
    joinStatement = "INSERT INTO classification (student_id,name,lastname) SELECT id,name,lastname FROM students WHERE id NOT IN(SELECT student_id FROM classification)"
    cursorObj.execute(joinStatement)
    connection.commit()
def selectClassificationByID(connection, student_id): #permite seleccionar la clasificación de un estudiante mediante su ID
    """Select a classification by the student id in the database:

    Args:
        connection (object): Connection to sqlite3.
        student_id (int): Id of the student.
    Returns:
        list<tuple>: List of tuples with the data of the students that contains the id.
    """
    CURSOR_OBJ = connection.cursor()
    SELECT_STATEMENT = "SELECT * FROM Classification WHERE student_id = ?"
    CURSOR_OBJ.execute(SELECT_STATEMENT, (student_id,))
    return CURSOR_OBJ.fetchall()
def GetSubjectAmount(connection): #recorre la tabla de academicHistory y cuenta cuantas materias concuerdan con cada ID del estudiante
        cursorObj = connection.cursor()
        UPDATE_STATEMENT = "UPDATE classification SET amountSubjects = (SELECT COUNT(id) FROM academicHistory WHERE id IN(SELECT id FROM academicHistory)) WHERE student_id = (SELECT id FROM academicHistory)"
        cursorObj.execute(UPDATE_STATEMENT)
        connection.commit()