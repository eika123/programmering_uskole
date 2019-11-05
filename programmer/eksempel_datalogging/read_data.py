import pandas as pd
from pylab import *

df = pd.read_excel('temperatur_data.xlsx')

t = df['tid']
T = df['temperatur']
N = len(T)


# regner med dette er mer aktuelt for elever.
# beregn noen statistiske størrelser
# husk! N er antall målinger!
gjennomsnitt = sum(T)/N
variasjonsbredde = max(T) - min(T)
tredje_kvartil = T[int(round(3*N/4))] 
forste_kvartil = T[int(round(N/4))]
kvartilbredde = tredje_kvartil - forste_kvartil


print('')
print("-------------------------------------------")
print('              statistikk               ')
print(f"       antall målinger:  {N:{5}}          ")
print('--------------------------------------------')
print(f"gjennomsnitt:    {gjennomsnitt:{10}.{4}}")
print(f"variasjonsbredde:  {variasjonsbredde:{10}.{4}}")
print(f"kvartilbredde:     {kvartilbredde:{10}.{4}}")

print("-------------------------------------------")

"""
for temperature in T:
    print(temperature)
"""

figure()
plot(t, T)
xlabel('t [dager]')
ylabel('Temperatur [grader celcius]')
grid()
show()

# lag boxplot
figure()
df.boxplot('temperatur')
show()


def calculate_statistics(df):
    gjennomsnitt = df.mean()[2]
    median = df.median()[2]
    max_temperatur = df.max()[2]
    min_temperatur = df.min()[2]
    tredje_kvartil = df.quantile(0.75)[2]
    forste_kvartil = df.quantile(0.25)[2]
    standardavvik = df.std()[2]
    N = df.shape[0]

    variasjonsbredde = max_temperatur - min_temperatur
    kvartilbredde = tredje_kvartil - forste_kvartil
    statistikk = {'antall målinger (N)': N,
                                'gjennomsnitt': gjennomsnitt, 
                                'median':median, 
                                'max': max_temperatur,
                                'min': min_temperatur,
                                'variasjonbredde': variasjonsbredde,
                                'kvartilbredde': kvartilbredde,
                                'første kvartil': forste_kvartil,
                                'tredje kvartil': tredje_kvartil,
                                'standardavvik': standardavvik
                            }

    return statistikk



def print_statisics(df):
    stats = calculate_statistics(df)
    for stat in stats.keys():
        value = float(stats[stat])
        print(f'{stat:{14}}     {value:{15}.{4}}')
    return
