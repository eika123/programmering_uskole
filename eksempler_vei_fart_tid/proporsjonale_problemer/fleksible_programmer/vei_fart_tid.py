
meny = """ 
Hvilken størrelse skal du finne?
    1) Strekning s
    2) Fart      v
    3) Tid       t
"""
ukjent_storrelse = input(meny)


if ukjent_storrelse == '1':
    v = float(input(f'Skriv inn farta v:    '))
    t = float(input(f'Skriv inn tiden t:    '))
    s = v*t
    print("strekningen s: ", s)

elif ukjent_storrelse == '2':
    s = float(input(f'Skriv inn strekningen s:   '))
    t = float(input(f'Skriv inn tiden t:   '))
    v = s/t
    print("farte v: ", v, fartsenhet)

elif ukjent_storrelse == '3':
    s = float(input(f'Skriv inn strekningen s:   '))
    v = float(input(f'Skriv inn farta v :    '))
    t = s/v
    print('Tiden t:  ', t, tidsenhet)

