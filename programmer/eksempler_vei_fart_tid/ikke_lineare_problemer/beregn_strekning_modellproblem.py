from pylab import *


def modell_strekning(T, s_0, v):
    """
    modell-problem med kjent fart

    idé: Hvis man kjenner s(t) og v(t), kan s(t + dt) tilnærmes slik:
    s(t + dt) = s(t) + dt*v(t)
    Jo mindre tidssteg dt, jo mer nøyaktig blir tilnærmingen.
    """

    dt = 0.1   # tidssteg
    t = [0]    # første tidspunkt
    s = [s_0]  # start-strekning
    k = 0      # telle-variabel

    while t[k] < T:
        s_next = s[k] + dt*v( t[k] )
        t_next = t[k] + dt

        s.append(s_next)
        t.append(t_next)
        k = k + 1

    return t, s


def v(t):
    """ modell for farten v ved konstant tyngdeakselerasjon g og utgangsfart v_0=10 """
    g = -9.81
    v_0 = 10
    return v_0 + g*t

t, s = modell_strekning(T=2.5, s_0=4, v=v)


# plotting
zero = zeros(len(t))

figure()
plot(t, s)
plot(t, zeros(len(t)))
xlabel('tid [s]', fontsize=16)
ylabel('meter [m]', fontsize=16)
title('Loddrett kast', fontsize=18)
grid()
show()

