# Dette programmet regner ut arealet A = gh/2 til en trekant 

# les inn høyden og lengden fra brukeren
h = input('Skriv inn høyden i trekanten her: ')
g = input('Skriv inn grunnlinja i pararellogrammet her: ')

# gjør strengene om til desimaltall
h = float(h)
g = float(g)


A = g*h/2.0

print('Arealet av trekanten er: ', A)