class Human:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def output(self):
        print(f"Меня зову {self.name}, мне {self.age} лет.")

class Worker(Human):
    def __init__(self, name, age, profeshion):
        super().__init__(name, age)
        self.profeshion=profeshion

    def output(self):
        print(f"Я {self.name}, мне {self.age} лет. Я работаю {self.profeshion}")

maria=Human("Мария","18")
sergey=Worker("Сергей","35","Строитель")

maria.output()
sergey.output()
