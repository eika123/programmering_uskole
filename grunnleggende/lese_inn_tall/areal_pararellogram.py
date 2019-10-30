# Dette programmet regner ut arealet A = lh til et pararellogram

# les inn høyden og lengden fra brukeren
h = input('Skriv inn høyden i pararellogrammet her: ')
l = input('Skriv inn lengden i pararellogrammet her: ')

# gjør strengene om til desimaltall
h = float(h)
l = float(l)


A = l*h

print('Arealet av pararellogrammet er: ', A)