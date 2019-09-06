# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers.txt").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of.txt"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

class Human:
    def __init__(self, data):
        self.name = data[0]
        self.searname = data[1]
        self.position = data[3]

    def get_profile(self):
        return f'Сотрудник: {self.searname} {self.name}\nДолжность: {self.position}'

class Worker(Human):
    def __init__(self, data, hours):
        Human.__init__(self, data)
        self.salary = int(data[2])
        # норма
        self.nrate = int(data[4])
        # зп за час работы
        self.trate = self.salary / self.nrate
        # отработанное время
        self.wrate = int(hours[0])

        # Получаем сколько необходимо выплатить сотруднику
        self.pay = self.check_work_rate()

    def check_work_rate(self):
        if self.nrate > self.wrate:
            return self.salary - (self.nrate - self.wrate) * self.trate
        elif self.nrate < self.wrate:
            return self.salary + (self.wrate - self.nrate) * self.trate
        else:
            return self.salary

def my_deco(func):
    def wrapper(*args):
        print("----------")
        func(*args)
    return wrapper

class Wages:
    def __init__(self):
        self.workers = None
        self.hours = None

        # Получаем информацию о сотрудниках и табель работы
        self.get_data()

    def __get_file_data(self, nfile):
        with open(nfile + '.txt', encoding='UTF-8') as file:
            return [x.split() for x in file]

    def get_data(self):
        self.workers = self.__get_file_data('data/workers')[1:]
        self.hours = self.__get_file_data('data/hours_of')[1:]

    def set_calculation(self):
        for itm in self.workers:
            worker = Worker(itm, [time[2] for time in self.hours if time[0] == itm[0] and time[1] == itm[1]])


            self.set_result(f"{worker.get_profile()}\nЗарплата/Н.Ч.: {worker.salary} ({worker.nrate}ч.) | Отработал: {worker.wrate}ч.\nК выдаче: {round(worker.pay)}руб.")

    @my_deco
    def set_result(self, text):
        print(text)


wage = Wages()
wage.set_calculation()