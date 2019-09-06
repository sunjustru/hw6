# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

class Human:
    def __init__(self, name=None, searname=None, olds=None):
        self.name = name
        self.searname = searname
        self.olds = olds

    def fio(self):
        return f'{self.searname} {self.name[0]}.'

    def set_humans(self, students):
        stude = []

        self.name = students['name']
        self.searname = students['searname']
        stude.append(self.fio())

        return stude

class Teacher(Human):
    def __init__(self, *args):
        Human.__init__(self, *args)

    # Получить учителя по классу
    def get_teacher_in_categoty(self):
        pass

class Student(Human):
    """
    Учиник привязан к классу
    """
    def __init__(self, students, *args):
        self.students = [(students[itm]['category'], students[itm]) for itm in students]

        Human.__init__(self, *args)

    # Получить родителей учиника
    def get_parents(self, student):
        student_id = [itm for itm in [itm for itm in self.students if
                    itm[1]['name'] in student.split(' ') and itm[1]['searname'] in student.split(' ')]][0][0]

        parents = [{'name': school_parent[itm]['name'], 'searname':school_parent[itm]['searname']} for itm in school_parent if student_id in school_parent[itm]['child']]

        student_item_w = []

        for b in parents:
            student_item_w.append([self.set_humans(b)])

        print(student_item_w)


    # Получить одного учиника
    def get_student(self, student):
        print(student.split(' '))
        for itm in [itm for itm in self.students if itm[1]['name'] in student.split(' ') and itm[1]['searname'] in student.split(' ')]:

            student_who = self.set_humans(itm[1])
            student_item = [{'name': school_teacher[r]['name'], 'searname': school_teacher[r]['searname'] , 'info': school_teacher[r]['info']} for r in school_teacher if itm[0] in school_teacher[r]['category']]

            student_item_w = []

            for b in student_item:
                student_item_w.append([self.set_humans(b), b['info']])

            print(student_item_w)
        pass

    # Получить всех учиников
    def get_students_category(self, category):
        return self.set_humans([[category[0][1], itm] for itm in self.students if self.students[itm][0] is category[0][0]])


class Shcool:
    def __init__(self, *args):
        self.school_category = school_category
        self.category = []
        for itm in self.school_category:
            self.category.append([itm, self.school_category[itm]['name']])

    def get_category_all(self):
        category = []
        for itm in self.category:
            category.append(f"Название класса: {itm[1]}")
        return category


    def get_students_in_category(self, category):
        """
        1. Передать в класс Student информацию с учиниками
        2. Вернуть данные по учиникам
        :return:
        """
        self.category_search = [itm for itm in self.category if itm[1] is category]
        if self.category_search:
            return True
        else:
            return False

    # TODO: Поставить отлов — фильтрацию данных
    # После получения номера класса, проверяем есть ли данные классы или нет
    # Если номер класса есть в school_category то продолжаем
    def set_category_in_search(self):
        self.category_in = input('Получить список всех учеников в указанном классе: ')
        return self.get_students_in_category

    def get_categoty_teacher(self):
        teacher = [{'name': school_teacher[itm]['name'], 'searname': school_teacher[itm]['searname']} for itm in school_teacher if self.category_search[0][0] in school_teacher[itm]['category']]

        student_item_w = []

        for b in teacher:
            #TODO: исправть!
            #student_item_w.append([Human.set_humans(b)])
            pass
        print(student_item_w)

        pass

class StartSchool:
    def __init__(self):
        pass

    def get_school_category(self):
        pass
    def get_students_in_category(self):
        pass
    def get_student_profile(self):
        pass
    def get_student_parent(self):
        pass
    def get_teacher_in_category(self):
        pass

school_category = ['А', 'B', 'C', 'D']
school_teacher = {
    0: {
        'name': "Михаил",
        'searname': 'Генадьевич',
        'info': "информатика",
        'category': [school_category[0],school_category[1]]
    },
    1: {
        'name': "Снежана Генадьевна",
        'searname': 'Генадьевич',
        'info': "история",
        'category': [school_category[0]]
    },
    2: {
        'name': "Семён",
        'searname': 'Святлоков',
        'info': "Трудовик",
        'category': [school_category[2]]
    }
}
school_student = {
    0 : {
        'name': "Андрей",
        'searname': "Фролов",
        'olds': 12,
        'category': school_category[0]
    },
    1: {
        'name': "Илья",
        'searname': "Хавкин",
        'olds': 10,
        'category': school_category[0]
    },
    2: {
        'name': "Саша",
        'olds': 12,
        'category': school_category[1]
    }
}
school_parent = {
    0 : {
        'name': "Анатолий",
        'searname': "Фролов",
        'olds': 48,
        'child': [school_student[0]]
        },
    1: {
        'name': "Маргарита",
        'searname': "Фролова",
        'olds': 48,
        'child': [school_student[0]]
    }
}

print(school_student)

# Выбранная и заполненная данными структура должна решать следующие задачи:
## 1. Получить полный список всех классов школы +
# _school = Shcool(school_category)
# print(_school.get_category_all())


# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# _school = Shcool(school_category)
# Проверяем класс такой есть или нет
# if _school.get_students_in_category('A') is True:
#     student = Student(school_student)
#     # Выводим список пользователей под определённой буквой
#     print(student.get_students_category(_school.category_search))
#
# else:
#     print('Выбран не существующий класс')


# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# student = Student(school_student)
# student_list = student.get_student('Андрей Фролов')


# 4. Узнать ФИО родителей указанного ученика
# student = Student(school_student)
# student_list = student.get_parents('Андрей Фролов')



# 5. Получить список всех Учителей, преподающих в указанном классе
# _school = Shcool(school_category)
# if _school.get_students_in_category('A') is True:
#     print(_school.get_categoty_teacher())
# else:
#     print('Нет такого класса')

#
# student = Student(school_studen)
# print(student.fio)
