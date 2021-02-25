'''
author = Zbyněk Veselka
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

jmeno = input('Zadej přihlašovací jméno: ')
heslo = input('Zadej heslo: ')

oddelovac = '-'*40

print(oddelovac)

registrovani_uzivatele = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
    }

if jmeno in registrovani_uzivatele.keys():
    if heslo == registrovani_uzivatele[jmeno]:
        print(f'Vítej v programu, {jmeno}.')
    else:
        print('Špatné heslo!')
        exit()
else:
    print('Neexistující uživatel!')
    exit()

print(f'K analyzování máme {len(TEXTS)} texty.')

print(oddelovac)

vyber_textu = input(f'Vyber text zadáním čísla od 1 do {len(TEXTS)}: ')

if vyber_textu.isdigit():
    if int(vyber_textu) not in range(1, len(TEXTS)+1):
        print(f'Text {vyber_textu} není na výběr!')
        exit()
else:
    print('Nebylo zadáno číslo!')
    exit()

print(oddelovac)

vybrany_text = TEXTS[int(vyber_textu)-1]
list_slov = vybrany_text.split(' ')
ocisteny_list_slov = []

for i in list_slov:
    ocisteny_list_slov.append(i.strip(',.\n'))

pocet_slov_zacinajicich_velkym = 0
pocet_slov_psanych_velkym = 0
pocet_slov_psanych_malym = 0
pocet_cisel = 0
soucet_cisel = 0

for j in ocisteny_list_slov:
    if j.isalpha():
        if j.istitle():
            pocet_slov_zacinajicich_velkym += 1
        elif j.isupper():
            pocet_slov_psanych_velkym += 1
            pocet_slov_zacinajicich_velkym += 1
        elif j.islower():
            pocet_slov_psanych_malym += 1
    elif j.isdigit():
        pocet_cisel += 1
        soucet_cisel += int(j)

print(f'Ve vybraném textu je {len(ocisteny_list_slov)} slov.')
print(f'V textu je {pocet_slov_zacinajicich_velkym} slov začínajících velkým písmenem.')
print(f'V textu je {pocet_slov_psanych_velkym} slov psaných velkými písmenemy.')
print(f'V textu je {pocet_slov_psanych_malym} slov psaných malými písmenemy.')
print(f'V textu je {pocet_cisel} čísel.')
print(f'Soušet čísel v textu je {soucet_cisel}.')

print(oddelovac)

slovnik_cetnosti_delek = dict()

for k in ocisteny_list_slov:
    delka_slova = len(k)
    slovnik_cetnosti_delek[delka_slova] = slovnik_cetnosti_delek.setdefault(delka_slova, 0) + 1

print('DÉL|      VÝSKYT      |POČ.')

print(oddelovac)

for delka, pocet in sorted(slovnik_cetnosti_delek.items()):
    print(f'{" " * (3-len(str(delka))) + str(delka)}|{pocet * "*" + (18-pocet) * " "}|{pocet}')
