class Student:
    instances = []
    generalis_album = {}
    def __init__(self, name, surname, gender):
        self.instances.append(self)
        self.name = name 
        self.surname = surname
        self.gender = gender 
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def estimation(self, courses_name, lectors_name, estim):
        if isinstance(lectors_name, Lecturer) and courses_name in self.courses_in_progress and courses_name in lectors_name.courses_attached:
            if courses_name in lectors_name.ratings:
                lectors_name.ratings [courses_name] += [estim]
                Lecturer.generalis_album[courses_name] +=[estim]
            else:
                lectors_name.ratings[courses_name] =[estim]
                Lecturer.generalis_album[courses_name] =[estim]
        else:
            return 'ошибка'

    def ave_score(self):
        for v in self.grades.values():
            average=sum(v)/len(v)
            return average
    def comparison(self, student2):
        if self.ave_score() > student2.ave_score():
            print(f"Ср балл студента {self.name} {self.surname} выше чем у {student2.name} {student2.surname}")
        elif self.ave_score() < student2.ave_score():
            print(f"Ср балл студента {self.name} {self.surname} ниже чем у {student2.name} {student2.surname}")
        else:
            print ('Они равны')
    
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка: {self.ave_score()}\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.ratings = {}
        if isinstance(self, Lecturer):
            Lecturer.instances +=[self]
        
class Lecturer(Mentor):
    instances = []

    generalis_album = {}
    def ave_score(self):
        for v in self.ratings.values():
            average=sum(v)/len(v)
            return average
            
    def comparison(self, lector2):
        if self.ave_score() > lector2.ave_score():
            print(f"Ср балл лектора {self.name} {self.surname} выше чем у {lector2.name} {lector2.surname}")
        elif self.ave_score() < lector2.ave_score():
            print(f"Ср балл лектора {self.name} {self.surname} ниже чем у {lector2.name} {lector2.surname}")
        else:
            print ('Они равны')

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка: {self.ave_score()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):  
        if isinstance(student, Student) and self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                Student.generalis_album[course] +=[grade]
            else:
                student.grades[course] = [grade]
                Student.generalis_album[course] =[grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def grades_students(students_list, course):
    mid_sum_grades = 0
    lectors = 0
    for stud in students_list:
        if course in stud.grades.keys():
            stud_sum_grades = 0
            for grades in stud.grades[course]:
                stud_sum_grades += grades
            mid_stud_sum_grades = stud_sum_grades / len(stud.grades[course])
            mid_sum_grades += mid_stud_sum_grades
            lectors += 1
    if mid_sum_grades == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{mid_sum_grades / lectors:.2f}'


def grades_lecturers(lecturer_list, course):
    mid_sum_rates = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.ratings.keys():
            lecturer_sum_rates = 0
            for rate in lecturer.ratings[course]:
                lecturer_sum_rates += rate
            mid_lecturer_sum_rates = lecturer_sum_rates / len(lecturer.ratings[course])
            mid_sum_rates += mid_lecturer_sum_rates
            b += 1
    if mid_sum_rates == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{mid_sum_rates / b:.2f}'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')

low_student = Student ('Иван', 'Абрамов', 'м')

best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ["Введение в програмирование"]
low_student.courses_in_progress += ['Java']
low_student.finished_courses = "Введение в програмирование"


lector_boris = Lecturer('Борис', 'Просто')
lector_thor = Lecturer('Тор', 'бог')

lector_boris.courses_attached += ['Python', 'Git']
lector_thor.courses_attached += ['Java']

cool_mentor = Mentor('Some', 'Buddy') 
cool_mentor.courses_attached += ['Python'] 
 
cool_reviewer = Reviewer('Александр', 'Овечкин')
low_reviewer = Reviewer ('Егор', 'Летов')
cool_reviewer.courses_attached += ['Python']
low_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 7)
low_reviewer.rate_hw(low_student, 'Java', 5)
best_student.estimation('Python', lector_boris, 10)
best_student.estimation('Git', lector_boris, 9)
low_student.estimation('Java', lector_thor, 5)
low_student.estimation('Java', lector_thor, 4)


print(f"на курсе учатся {len(Student.instances)} студента(ов)")
print(f"на курсе учатся {len(Lecturer.instances)} студента(ов)")
print()
print(low_reviewer.__str__())
print()
print(lector_thor.__str__())
print()
print(best_student.__str__())
print()
best_student.comparison(low_student)
lector_boris.comparison(lector_thor)

print(f'Средняя оценка студентов по курсу "Git": {grades_students(Student.instances, "Git")}')
print(f'Средняя оценка студентов по курсу "Java": {grades_students(Student.instances, "Java")}')
print(f'Средняя оценка студентов по курсу "Python": {grades_students(Student.instances, "Python")}')

print(f'Средняя оценка лекторов по курсу "Git": {grades_lecturers(Lecturer.instances, "Git")}')
print(f'Средняя оценка лекторов по курсу "Java": {grades_lecturers(Lecturer.instances, "Java")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(Lecturer.instances, "Python")}')
