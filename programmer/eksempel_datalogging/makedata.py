from pylab import *
import pandas as pd

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


# lagre t og T_noisy til fil som kommaseparert liste
savetxt("temperatur_data.csv", (t, T_noisy), delimiter=',', header='time, temperature', newline='\r')

# lagre t og T_noisy i excel-format.
with pd.ExcelWriter('temperatur_data.xlsx') as writer:
    data = {'tid': t, 'temperatur': T_noisy}
    df = pd.DataFrame(data)
    df.to_excel(writer)


