

class Osoba:
    def __init__(self, ime, godine, kurs):
        self.ime=ime
        self.godine=godine
        self.kurs=kurs

    def vrati_osobu(self):
        return f'{self.ime}, {self.godine},{self.kurs}' 

class Student(Osoba):
    def __init__(self, ime, godine,kurs, ocjene):
        super().__init__(ime, godine, kurs)
        self.ocjene=ocjene

    def vrati_studenta(self):
        return f' "Student:" {self.ime} "Godine:" {self.godine} "Kurs:" {self.kurs} "Ocjena:" {self.ocjene}' 

class Profesor(Osoba):
    def __init__(self, ime, godine, kurs, opterecenje):
        super().__init__(ime, godine, kurs)
        self.opterecenje=opterecenje

    def vrati_profesora(self):
        return f' "Profesor: "{self.ime} "Godine:" {self.godine} "KUrs:" {self.kurs} "Opterecenje:" {self.opterecenje}' 


student1=Student("Marko Markovic", 24, "OS",7)
print(student1.vrati_studenta())  
student2=Student("Petar Petrovic",22,"Matematika",6)
print(student2.vrati_studenta())  

profesor1=Profesor("Milos Dakovic", 55, "Baze podataka", 3)
print(profesor1.vrati_profesora())
profesor2=Profesor("Igor Djurovic", 55, "DOS", 3)
print(profesor2.vrati_profesora())

with open('newfile.txt','w') as file_object:
    file_object.writelines(student1.vrati_studenta())
    file_object.writelines(student2.vrati_studenta()), 
    file_object.writelines(profesor1.vrati_profesora()),
    file_object.writelines(profesor2.vrati_profesora()),




    