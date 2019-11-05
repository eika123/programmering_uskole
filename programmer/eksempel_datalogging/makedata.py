from pylab import *

# funksjon som generer "tilfeldig" temperaturdata
def generer_data():

    # alle tidspunkter med måling
    # måles 4 ganger i sekundet
    maale_intervall = 15            # antall minutter mellom hver måling
    r = 1/(60*maale_intervall)      # antall målinger per sekund
    days = 30  # antall dager

    random_noise_rate = 24/2

    n_d = int(round(r*60*60*random_noise_rate))
    N = int(round(r*60*60*24*days))

    t = linspace(0, days, N)
    T = 21 + t*0.01 + 0.2*sin(2*pi*t) + 0.05*sin(5*pi*t)

    standard_deviation = 0.02

    r = []
    for day_fraction in range(int(round(24/random_noise_rate*days))):
        random_temperature_factor = np.random.normal(scale=standard_deviation)
        r_next = list(random_temperature_factor*ones(n_d))
        r += r_next

    T_noisy = T + r
    return t, T_noisy, N



t, T_noisy, N = generer_data()

# lagre t og T_noisy til fil
savetxt("temperature_data.csv", (t, T_noisy), delimiter=',', header='time, temperature', newline='\n')


# beregn noen statistiske størrelser
# husk! N er antall målinger!
gjennomsnitt = sum(T_noisy)/N
variasjonsbredde = max(T_noisy) - min(T_noisy)
tredje_kvartil = T_noisy[int(round(3*N/4))] 
forste_kvartil = T_noisy[int(round(N/4))]
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

plot(t, T_noisy)
xlabel('t [dager]')
ylabel('Temperatur [grader celcius]')
grid()
show()
figure()