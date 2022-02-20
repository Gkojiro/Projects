ornek_liste = ['Berkay', 'Yargi', 'Oguzhan']

for ogrenci in ornek_liste:
    print(ogrenci, 'Derse Katildi')

for i in range(1, 51):
    i

i = 0

while i <= 10:
    print(i)
    i += 1


ornek_liste = ['ali', 'veli', 'hasan', 'huseyin']

for i in ornek_liste:
    if i == 'hasan':
        continue
    print(i)

for i in ornek_liste:
    if i == 'hasan':
        break
    print(i)
print('Döngü kırıldı')

i = 0
while True:
    if i == 5:
        break
    print(i)
    i += 1
