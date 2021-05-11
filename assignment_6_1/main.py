import requests #IMPORTS THE REQUETS FUNCTION (GET, POST, PUT AND DELETE)

def read_student():
    # SEND GET REQUEST AN API SERVER AND READS THE FILE(RESPONSES IN JSON)
    search = requests.get('http://localhost:5000/students/')
    users = search.json()
    for user in users: #PRINTS IN THE FUNCTION OF DICTIONARY
        print(f'id: {user["id"]}, name: {user["name"]}, email: {user["email"]}, year: {user["year"]}')
    return

def find_student(x):
    # TELLS THE STATUS CODE
    looking = requests.get(f'http://localhost:5000/students/{x}')
    bruker = looking.json()
    if looking.status_code == 200:
        print(f'{looking.status_code} OK') #TELLS THE USER THE STATUS CODE, IN THIS CASE IF IT WORKS 200
        print(f'id: {bruker["id"]}, name: {bruker["name"]}, email: {bruker["email"]}, year: {bruker["year"]}')
    else:
        print(f'{looking.status_code} Not Found') #IF IT DOESNT WORK ERROR 404
        print('Student not found')
    return


def add_student(n, e ,y):
    # ADDS THE NEW STUDENT TO THE SERVER WITH POST REQUESTS
    info = dict(id=len(requests.get('http://localhost:5000/students/').json())+1, name=str(n), email=str(e),
                year=int(y)) #FUNCTION USED TO ADD THE SPECIFIC INFORMATION INTO THE SERVER
    find = requests.post('http://localhost:5000/students/', json=info)
    if find.status_code == 201:
        info = find.json()
        print(f'Added student: id: {info["id"]}, name: {info["name"]}, email: {info["email"]}, year: {info["year"]}')
    return


def edit_student(i, n, e, y):
    # EDIT STUDENT INFO WITH PUT REQUESTS
    edit = dict(id=int(i), name=str(n), email=str(e), year=int(y)) #EDITS THE FOLLOWING INFROMATION
    edit_students = requests.put(f'http://localhost:5000/students/{i}', json=edit)
    if edit_students.status_code == 200:
        print(f'{edit_students.status_code} OK')
        print(f'Student was edited successfully')
    else:
        print(f'{edit_students.status_code} Not Found')
        print('Student not found')
    return


def delete_student(d):
    # REMOVE STUDENT WITH DELETE REQUESTS
    delete = requests.delete(f'http://localhost:5000/students/{d}')
    if delete.status_code == 204:
        print(f'{delete.status_code} OK')
        print(f'Student was removed successfully')
    else:
        print(f'{delete.status_code} Not Found')
        print('Student not found')
    return

def main():
    print("Choose a number from 1-6 (6 is exit).")
    x = 1
    while x == 1:
        choice = input()
        if choice == '1': #CHOICE 1 FOR READ
            read_student()
        elif choice == '2': #CHOICE 2 TO FIND SPECIFIC INFOMRATION
            find_student(int(input()))
        elif choice == '3': #CHOICE 3 TO INPUT DATA
            name = input()
            email = input()
            year = input()
            add_student(name, email, year)
        elif choice == '4': #CHOICE 4 TO EDIT DATA
            edit_student(int(input()), input(), input(), int(input()))
        elif choice == '5': #CHOICE 5 TO DELETE DATA
            delete_student(int(input()))
        elif choice == '6': #CHOICE 6 TO EXIT THE PROGRAM
            x = 0
    pass

if __name__ == '__main__':
    main()
