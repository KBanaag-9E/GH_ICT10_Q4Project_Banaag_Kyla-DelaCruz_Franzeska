from pyscript import display, document, HTML
import pandas as pd

# class and objects
class Student:
    def __init__(self, name, nickname, section, bday, interest, subject):
        self.name = name
        self.nickname = nickname
        self.section = section
        self.birthday = bday
        self.interest = interest
        self.subject = subject

# student information
students = [
    Student('Andrian Joseph Abayon', 'Joe', '10-Emerald', 'Sept 29', 'Stars, moon, night, clouds, sleep, writing, music', 'English'),
    Student('Erin Antes', 'Rin', '10-Emerald', 'June 29', 'Monster Energy', 'VE/SS'),
    Student('Caitlyn Apostol', 'Cait', '10-Emerald', 'July 9', 'games, writing, reading', 'English'),
    Student('Kyla Banaag', 'Limuelle/Kyla', '10-Emerald', 'Dec 8', 'roleplaying', 'English'),
    Student('Clarisse Casal', 'Do i make myself Clairo', '10-Emerald', 'March 20', 'Franzeska Addienna Veracion Dela Cruz & snoopy', 'SS'),
    Student('Dela Cruz Franzeska', 'Fran', '10-Emerald', 'Aug 11', 'Fleas (my favorite one is keisha) & little kids', 'Science'),
    Student('Dela Cruz Jalena', 'Lan', '10-Emerald', 'Jun 18', 'playing and drawing', 'TLE'),
    Student('Keisha Dellejero', 'Alokeisha Dihllejero', '10-Emerald', 'May 23', 'Girl love (Generation)', 'SS/VE'),
    Student('James Mamauag', 'James, Aiden, or Thunder', '10-Emerald', 'Sept 22', 'Action Shows', 'Philosophy'),
    Student('Maria Julie Ann Lozano', 'Julia', '10-Emerald', 'Sept 16', 'Romance & horror', 'Filipino & Philosophy'),
    Student('Gino Ramos', 'Gino', '10-Emerald', 'Dec 17', 'Roses that vibrate', 'SS'),
    Student('Gurnoor Sidhu', 'Gurman', '10-Emerald', 'Aug 12', 'Basketball', 'Math')
]

# adding classmate 
def add_classmate(e):
    document.getElementById('output').innerHTML = ""

    name = document.getElementById("name").value
    nickname = document.getElementById("nickname").value
    section = document.getElementById("section").value
    bday = document.getElementById("bday").value
    interest = document.getElementById("interest").value
    subject = document.getElementById("subject").value

    students.append(Student(name, nickname, section, bday, interest, subject))
    class_list(None)

# displays class list
def class_list(e):
    document.getElementById('output').innerHTML = ""

    table_data = [{
        'Name': s.name,
        'Nickname': s.nickname,
        'Section': s.section,
        'Birthday': s.birthday,
        'Interests': s.interest,
        'Favorite Subject': s.subject
    } for s in students]

    df = pd.DataFrame(table_data)
    df.index += 1
    display(df, target='output', append=False)

    display(HTML('''
        <style>
            #output table {
                width: 100%;
                max-width: 100%;
                border-collapse: collapse;
                table-layout: fixed;
                word-break: break-word;
            }
            #output th, #output td {
                border: 1px solid;
                padding: 0.5rem;
                text-align: left;
                background-color: white;
            }
            #output th {
                background-color: white;
            }
        </style>
    '''), target='output', append=True)
