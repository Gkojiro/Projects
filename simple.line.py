class Kedi:
    """
    def __init__(self, name, gender, age, colors):
        self.name = name
        self.gender = gender
        self.age = age
        self.colors = colors
    """
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.gender = kwargs['gender']
        self.age = kwargs['age']
        self.colors = kwargs['colors']

a = ['ali', 'veli', 'hasan', 'huseyin']
b, c, d, e = a
print(b, c, d, e)


print(*a)
print(a[0], a[1], a[2], a[3])

a_d = {'name': 'Mahmut', 'surname': 'Tuncer'}

def deneme_dict(name):
    print(a_d['name'], a_d['surname'])

deneme_dict(**a_d)
deneme_dict(name='Mahmut', surname='Tuncer')
    
def cok_ciktili_fonksiyon(nesne):
    
    sayi_mi = nesne.isdigit()
    return sayi_mi, nesne

result, nesne = cok_ciktili_fonksiyon('444')

ornek_dict_list = [
    {'name': 'Mahmut', 'surname': 'Tuncer'},
    {'name': 'Ibrahim', 'surname': 'Tatlises'},
    {'name': 'Mustafa', 'surname': 'Sandal'},
    {'name': 'Yildiz', 'surname': 'Tilbe'},
]

output = []
for i in ornek_dict_list:
    output.append(f"{i['name']} {i['surname']}")

output = [f"{i['name']} {i['surname']}" for i in ornek_dict_list]

for i in range(1, 10):
    if i % 2 == 0:
        print(i)
    else:
        print('Tek')

for i in range(1, 10):
    print(i if i % 2 == 0 else 'Tek')
