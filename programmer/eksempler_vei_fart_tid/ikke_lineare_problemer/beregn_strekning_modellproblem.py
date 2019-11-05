from pylab import *


def modell_strekning(T, s_0):
    """
    modell-problem med konstant akselereasjon
    ball kastes i lufta fra en balkong 4 meter over bakken
    med utgangshastighet v_0


    ide: bruk sammenhengene under der s(t) er beregnet
    tidligere i programmet
    s(t + dt) = s(t) + dt*v(t)
    """

    def v(t):
        a = -9.81
        v_0 = 10
        return v_0 + a*t

    dt = 0.1 # tidssteg
    t = [0]

    s = [s_0]
    k = 0

    while t[k] < T:

        s_next = s[k] + dt*v( t[k] )
        t_next = t[k] + dt

        s.append(s_next)
        t.append(t_next)

        k = k + 1

    return t, s

t, s = modell_strekning(3, 4)



# plotting
zero = zeros(len(t))

figure()
plot(t, s)
plot(t, zeros(len(t)))
xlabel('tid [s]')
ylabel('meter [m]')
grid()
show()

