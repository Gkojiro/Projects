class Hayvan:
    ad = None
    tur = None
    yas = None
    cinsiyet = None

    def __str__(self):
        return f'{self.tur} - {self.ad}'

    def add_age(self):
        self.yas += 1


pacchi = Hayvan()
pacchi.ad = 'Pacchi'
pacchi.tur = 'Kedi'
pacchi.yas = 2
pacchi.cinsiyet = 'Disi'

print(pacchi)
print(pacchi.ad)
print(pacchi.tur)
print(pacchi.yas)
pacchi.add_age()
print(pacchi.yas)


class Insan:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.name} {self.surname}'


bg = Insan(
    name='Batuhan',
    surname='Günaydın',
    age=27,
    gender='Male'
)


class Dikdortgen:
    def __init__(self, en, boy):
        self.en = en
        self.boy = boy

    def get_alan(self):
        return self.en * self.boy


d1 = Dikdortgen(10, 20)

print(d1.get_alan())


class Ogrenci(Insan):
    def __init__(self, name, surname, age, gender, classroom, gpa):
        super().__init__(name, surname, age, gender)
        self.classroom = classroom
        self.gpa = gpa

mt = Ogrenci(
    name='Mahmut',
    surname='Tuncer',
    age='Sonsuz',
    gender='Halay',
    classroom='C305',
    gpa=10
)

print(mt)
print(mt.classroom)
print(mt.gpa)
print(mt.gender)
