meny = """ 
Hvilken størrelse skal du finne?
    1) Strekning s
    2) Fart      v
    3) Tid       t
"""


enhetsmeny = """
Hvilken enhet skal du bruke?
    1) lengde: kilometer,  tid: timer, fart: km/t
    2) lengde: meter,  tid: sekunder, fart: m/s
    3) lengde: meter,  tid: minutter, fart: m/min
"""

# les inn hvilket problem brukeren ønsker å løse
ukjent_storrelse = input(meny)
enhet = int(input(enhetsmeny)) - 1


# les av enhetene brukeren ønsker å benytte
enheter = [('km', 'timer', 'km/t'), ('m', 'min', 'm/min'), ('m', 's', 'm/s')]
strekningsenhet, tidsenhet, fartsenhet = enheter[enhet]

if ukjent_storrelse == '1':
    v = float(input(f'Skriv inn farta v [{fartsenhet}]:  '))
    t = float(input(f'Skriv inn tiden t [{tidsenhet}]:   '))
    s = v*t
    print("strekningen s: ", s, strekningsenhet)

elif ukjent_storrelse == '2':
    s = float(input(f'Skriv inn strekningen s [{strekningsenhet}]:  '))
    t = float(input(f'Skriv inn tiden t  [{tidsenhet}]:  '))
    v = s/t
    print("farte v: ", v, fartsenhet)

elif ukjent_storrelse == '3':
    s = float(input(f'Skriv inn strekningen s [{strekningsenhet}]: '))
    v = float(input(f'Skriv inn farta v [{fartsenhet}]:  '))
    t = s/v
    print('Tiden t:  ', t, tidsenhet)
