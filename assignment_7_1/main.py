from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#GET BASECLASS FOR TABLE DESCRIPTION
Base = declarative_base()

class Students(Base):
    __tablename__='students'

    #CLASS DESCRIBING OUT TABLE (METADATA(DATA THATS INSIDE A DATA))
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    year = Column(Integer)


def read_data(session):
    # QUERY FOR ALL STUDENTS
    school = session.query(Students).all()
    if not school:
        print(f'No students found')
    for student in school:
        print(f'id: {student.id}, name: {student.name}, email: {student.email}, year: {student.year}')
    return


def get_data(session):
    # QUERY FOR SPECIFIC STUDENTS
    school_student = session.query(Students).get(1)
    if school_student:
        print(f'id: {school_student.id}, name: {school_student.name}, email: {school_student.email}, '
              f'year: {school_student.year}')
    else:
        print(f'Student was not found')
    return


def add_data(session):
    new_name = input(f'name:')
    new_email = input(f'email:')
    new_year = int(input(f'year:'))
    # CREATES NEW DATA TO STUDENTS
    new_student = Students(name=f'{new_name}', email=f'{new_email}', year=f'{new_year}')
    # INSERT NEW AUTHOR IN DATABASE
    session.add(new_student)
    # SAVES THE ADDED DATA
    session.commit()
    session.close()

    more_students = session.query(Students).all()
    count = len(more_students)
    all_student = session.query(Students).filter(Students.id==count).all()
    for every_student in all_student:
        print(f'Added student: id: {every_student.id}, name: {every_student.name}, '
              f'email: {every_student.email}, year: {every_student.year}')
    return


def edit_data(session):
    edit_id = input(f'id:')
    school_student = session.query(Students).get(int(edit_id))#FINDS THE INPUTTED ID
    if school_student:
        print(f'Student was edited successfully')
    else:
        print(f'Student not found')
        return
    edit_name = input(f'name:')
    edit_email = input(f'email:')
    edit_year = input(f'year')
    school_student.name = edit_name
    school_student.email = edit_email
    school_student.year = edit_year
    session.commit()
    session.close()
    return


def remove_data(session):
    find_id = input(f'id:')
    school_delete = session.query(Students).get(find_id)
    if school_delete:
        print(f'Student was removed successfully')
    else:
        print(f'Student not found')
    session.delete(school_delete)
    session.commit()
    session.close()
    return


def search_data(session):
    find_name = input(f'name:')
    look_data = session.query(Students).filter(Students.name.like(find_name)).all()
    if not look_data:
        print(f'No students found')
    for search in look_data:
        print(f'id: {search.id}, name: {search.name}, email: {search.email}, year: {search.year}')
    return


def main():
    # ENGINE DESCRIBES DATABASE AND CONNECTION URL
    engine = create_engine(f'sqlite:///school.sqlite')
    # CREATE A SESSON MAKER (FACTORY PATTERN)
    Session = sessionmaker(bind=engine)
    # CREATING SESSION USING SESSIONMAKER
    session = Session()

    print("Choose a number from 1-7 (7 is exit).")
    x = 1
    while x == 1:
        choice = input()
        if choice == '1': #CHOICE 1 FOR READ
            read_data(session)
        elif choice == '2':
            get_data(session)
        elif choice == '3':
            add_data(session)
        elif choice == '4':
            edit_data(session)
        elif choice == '5':
            remove_data(session)
        elif choice == '6':
            search_data(session)
        elif choice == '7': #CHOICE 7 TO EXIT THE PROGRAM
            x = 0
    return

if __name__ == '__main__':
    main()


