class Student():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = ['Python','C#']
        self.grades = {}

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            if course in lecturer_all_grades:
                lecturer_all_grades[course] += [grade]
            else:
                lecturer_all_grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        grades_list = list(self.grades.values())
        avg_grade = sum(grades_list[0]) / len(grades_list[0])
        return avg_grade

    def __str__(self):
        name = f"Имя: {self.name}\n"\
               f"Фамилия: {self.surname}\n"\
               f'Средняя оценка: {self.avg_grade()}\n'\
               f'Курсы в прочессе изучения: {self.courses_in_progress}\n'\
               f'Завершённые курсы: {self.finished_courses}'
        return name




class Mentor():

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = ['Python', 'C#']
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            if course in student_all_grades:
                student_all_grades[course] += [grade]
            else:
                student_all_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name = f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"
        return name

class Lecturer(Mentor):

    def __str__(self):
        n = f"Имя: {self.name}\n" \
            f"Фамилия: {self.surname}\n" \
            f'Средняя оценка: {self.avg_grade()}'
        return n

    def avg_grade(self):
        grades_list = list(self.grades.values())
        avg_grade = sum(grades_list[0])/len(grades_list[0])
        return avg_grade

def comparison(human1, human2):
    if isinstance(human1, Lecturer) and isinstance(human2, Lecturer) or isinstance(human1, Student) and isinstance(human2, Student):
        if human1.avg_grade() > human2.avg_grade():
            answer = f'Средняя ценка {human1.name} больше средней оценки {human2.name}'
        elif human2.avg_grade() > human1.avg_grade():
            answer = f'Средняя ценка {human2.name} больше средней оценки {human1.name}'
        else:
            answer = 'Средние оценки равны'
    else:
        answer = 'Ошибка'
    return print(answer)

def course_avg_grade(course, h):
    if h == 'студент':
        if course in student_all_grades:
            answer = sum(student_all_grades.get(course)) / len(student_all_grades.get(course))
    elif h == 'лектор':
        if course in lecturer_all_grades:
            answer = sum(lecturer_all_grades.get(course)) / len(lecturer_all_grades.get(course))
    else:
        answer ='Ошибка'
    return print(answer)

student_all_grades = {}

lecturer_all_grades = {}

best_student = Student('Ruoy', 'Eman', 'your_gender')

some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')
som_lecturer = Lecturer('Som', 'Budy')
some_student = Student('Ruy', 'Eman', 'q')

Reviewer.rate_hw(some_reviewer, best_student, 'Python', 10)
Reviewer.rate_hw(some_reviewer, some_student, 'Python', 9)
Reviewer.rate_hw(some_reviewer, some_student, 'Python', 9)
Reviewer.rate_hw(some_reviewer, best_student, 'Python', 9)
Reviewer.rate_hw(some_reviewer, some_student, 'C#', 9)

Student.rate_l(some_student, some_lecturer, 'Python', 9)
Student.rate_l(best_student, som_lecturer, 'Python', 10)

comparison(some_lecturer, som_lecturer)
course_avg_grade('Python', 'студент')
course_avg_grade('Python', 'лектор')