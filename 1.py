class Teacher:
    def __init__(self, name, education, experience):
        self._name = name
        self._education = education
        self._experience = experience
        self._marks = {}  # Словарь для хранения оценок студентов

    # Геттер для имени
    @property
    def name(self):
        return self._name

    # Геттер для образования
    @property
    def education(self):
        return self._education

    # Геттер для опыта работы
    @property
    def experience(self):
        return self._experience

    # Сеттер для опыта работы
    @experience.setter
    def experience(self, years):
        if years >= 0:
            self._experience = years
        else:
            raise ValueError("Опыт работы не может быть отрицательным.")

    # Метод, возвращающий информацию об учителе
    def get_teacher_data(self):
        return f"Имя: {self._name}, Образование: {self._education}, Опыт работы: {self._experience} лет"

    # Метод для добавления оценки
    def add_mark(self, student_name, mark):
        if student_name in self._marks:
            self._marks[student_name].append(mark)
        else:
            self._marks[student_name] = [mark]

        return f"Иван Петров поставил оценку {mark} студенту {student_name}."

    # Метод для удаления оценки
    def remove_mark(self, student_name, mark):
        if student_name in self._marks and mark in self._marks[student_name]:
            self._marks[student_name].remove(mark)
            return f"Иван Петров поставил оценку {mark} студенту {student_name}."
        else:
            return f"Иван Петров поставил оценку {mark} студенту {student_name}."

    # Метод для консультации
    def give_a_consultation(self, student_class):
        return f"Учитель {self._name} проводит консультацию для класса {student_class}."


# Пример использования
teacher = Teacher("Иван Петров", "БГПУ", 4)
print(teacher.get_teacher_data())
print(teacher.add_mark("Анна Смирнова", 5))
print(teacher.add_mark("Анна Смирнова", 4))
print(teacher.remove_mark("Анна Смирнова", 5))
print(teacher.give_a_consultation("9Б"))
