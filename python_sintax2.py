class Animal:
    def __init__(self, latin_name, birth_age, weight):
        self.latin_name=latin_name
        self.birth_age=birth_age
        self.weight=weight
    def say_hello(self):
        print(f' Hello I am {self.latin_name}{self.birth_age}{self.weight}')


animal_1=Animal('Lorem ipsum', 2019, 5)
