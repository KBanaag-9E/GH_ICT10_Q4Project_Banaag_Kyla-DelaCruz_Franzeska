from pyscript import display, document

class Classmate:
    def __init__(self, name, nickname, section, bday, interest, subject):
        self.name = name
        self.nickname = nickname
        self.section = section
        self.birthday = bday
        self.interest = interest
        self.subject = subject
    
    def introduce(self):
        display(f"Hellaur! I am {self.name.title()} from {self.section.title()}. My favorite subject is {self.favorite_subject}.", target='output', append=True)

student1 = Classmate('', '', '10-Emerald', '', '', '')
student2 = Classmate('Erin Antes', 'Rin', '10-Emerald', 'June 29', 'Monster Energy', 'VE/SS')
student3 = Classmate('', '', '10-Emerald', '', '', '')
student4 = Classmate('Kyla Banaag', 'Kyla/Limuelle', '10-Emerald', 'December 8', 'roleplaying', 'English')
student5 = Classmate('', '', '10-Emerald', '', '', '')
student6 = Classmate('', '', '10-Emerald', '', '', '')
student7 = Classmate('', '', '10-Emerald', '', '', '')
student8 = Classmate('', '', '10-Emerald', '', '', '')
student9 = Classmate('', '', '10-Emerald', '', '', '')
student10 = Classmate('', '', '10-Emerald', '', '', '')
student11 = Classmate('', '', '10-Emerald', '', '', '')
student12 = Classmate('', '', '10-Emerald', '', '', '')
student13 = Classmate('', '', '10-Emerald', '', '', '')
student14 = Classmate('', '', '10-Emerald', '', '', '')
student15 = Classmate('', '', '10-Emerald', '', '', '')
student16 = Classmate('', '', '10-Emerald', '', '', '')
student17 = Classmate('', '', '10-Emerald', '', '', '')
student18 = Classmate('', '', '10-Emerald', '', '', '')
student19 = Classmate('', '', '10-Emerald', '', '', '')
student20 = Classmate('', '', '10-Emerald', '', '', '')
student21 = Classmate('', '', '10-Emerald', '', '', '')
student22 = Classmate('', '', '10-Emerald', '', '', '')
student23 = Classmate('', '', '10-Emerald', '', '', '')
student24 = Classmate('', '', '10-Emerald', '', '', '')
student25 = Classmate('', '', '10-Emerald', '', '', '')

# adding classmate 
def add_classmate(event):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    if name and section and subject:
        new_student = Classmate(name, nickname, section, bday, interest, subject)
        classmates_list.append(new_student)
        
        document.getElementById("name").value = ""
        document.getElementById("nickname").value = ""
        document.getElementById("section").value = ""
        document.getElementById("bday").value = ""
        document.getElementById("interest").value = ""
        document.getElementById("subject").value = ""

        # display_all()

def introduce(e):
    document.getElementById('output').innerHTML = ""

    global student1, student2, student3, student4, student5, student6, student7, student8, student9, student10, student11, student12, student13, student14, student15, student16, student17, student18, student19, student20, student21, student22, student23, student24, student25

    display(f'{student1.name} is in {student1.section}. Their favorite subject is {student1.subject}.', target='output')
    display(f'{student2.name} is in {student2.section}. Their favorite subject is {student2.subject}.', target='output')
    display(f'{student3.name} is in {student3.section}. Their favorite subject is {student3.subject}.', target='output')
    display(f'{student4.name} is in {student4.section}. Their favorite subject is {student4.subject}.', target='output')
    display(f'{student5.name} is in {student5.section}. Their favorite subject is {student5.subject}.', target='output')
    display(f'{student6.name} is in {student6.section}. Their favorite subject is {student6.subject}.', target='output')
    display(f'{student7.name} is in {student7.section}. Their favorite subject is {student7.subject}.', target='output')
    display(f'{student8.name} is in {student8.section}. Their favorite subject is {student8.subject}.', target='output')
    display(f'{student9.name} is in {student9.section}. Their favorite subject is {student9.subject}.', target='output')
    display(f'{student10.name} is in {student10.section}. Their favorite subject is {student10.subject}.', target='output')
    display(f'{student11.name} is in {student11.section}. Their favorite subject is {student11.subject}.', target='output') 
    display(f'{student12.name} is in {student12.section}. Their favorite subject is {student12.subject}.', target='output')
    display(f'{student13.name} is in {student13.section}. Their favorite subject is {student13.subject}.', target='output')
    display(f'{student14.name} is in {student14.section}. Their favorite subject is {student14.subject}.', target='output')
    display(f'{student15.name} is in {student15.section}. Their favorite subject is {student15.subject}.', target='output')
    display(f'{student16.name} is in {student16.section}. Their favorite subject is {student16.subject}.', target='output')
    display(f'{student17.name} is in {student17.section}. Their favorite subject is {student17.subject}.', target='output')
    display(f'{student18.name} is in {student18.section}. Their favorite subject is {student18.subject}.', target='output')
    display(f'{student19.name} is in {student19.section}. Their favorite subject is {student19.subject}.', target='output')
    display(f'{student20.name} is in {student20.section}. Their favorite subject is {student20.subject}.', target='output')
    display(f'{student21.name} is in {student21.section}. Their favorite subject is {student21.subject}.', target='output')
    display(f'{student22.name} is in {student22.section}. Their favorite subject is {student22.subject}.', target='output')
    display(f'{student23.name} is in {student23.section}. Their favorite subject is {student23.subject}.', target='output')
    display(f'{student24.name} is in {student24.section}. Their favorite subject is {student24.subject}.', target='output')
    display(f'{student25.name} is in {student25.section}. Their favorite subject is {student25.subject}.', target='output')

    student1 = student1
    student2 = student2
    student3 = student3
    student4 = student4
    student5 = student5
    student6 = student6
    student7 = student7
    student8 = student8
    student9 = student9
    student10 = student10
    student11 = student11
    student12 = student12
    student13 = student13
    student14 = student14
    student15 = student15
    student16 = student16
    student17 = student17
    student18 = student18
    student19 = student19
    student20 = student20
    student21 = student21
    student22 = student22
    student23 = student23
    student24 = student24
    student25 = student25

# display_all()