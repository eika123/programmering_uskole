from pylab import *


def strekning(T, a, v_0, t_0=0, s_0=0, dt=0.1):

    """
    beregn strekningen et objekt har tilbakelagt fra posisjonen t_0
    etter tiden T med en variabel, kjent akselerasjon a(t, v, s)

    input:
    T - endetidspunkt på simuleringen
    a - akselerasjonen. Funksjon av tre parametere
    t_0 - starttidspunkt
    s_0 - strekning ved tiden t=t_0
    dt - størrelsen på tidssteget
    """

    t = [0]
    v = [v_0]
    s = [s_0]
    k = 0

    while t[k] < T:
        v_next = v[k] + dt*a(t[k], v[k], s[k])
        s_next = s[k] + dt*v[k]
        t_next = t[k] + dt

        v.append(v_next)
        s.append(s_next)
        t.append(t_next)
        k = k + 1

    return t, v, s    


def distance_linear_acceleration_max_four_g():
    T = 5
    dt = 0.5
    v_0 = 0
    
    def a(t, v, s):
        return max(0.7*t + 9.81, 9.81*4)

    t, v, s = strekning(T, a, v_0, dt=dt)

    return t, v, s


def linear_spring(stiffness=1.0, mass=1.0):
    """
    demonstrerer problem med "forlengs differanseskjema"
    da amplituden i svingningene øker over tid. Løsningen er
    dermed en perpetuum mobile da ingen ytre krefter virker på systemet.
    """

    T = 20
    dt = 0.001
    v_0 = 0
    s_0 = 1

    # enklere matematisk notasjon
    k = stiffness   
    m = mass

    def a(t, v, x):
        return -k*x/m
    
    t, v, s = strekning(T, a, v_0, s_0=s_0, dt=dt)

    return t, v, s


if __name__ == '__main__':

    #t, v, s = distance_linear_acceleration_max_four_g()
    t, v, s = linear_spring()

    figure()
    plot(t, s)
    xlabel('tid [sek]')
    ylabel('høyde [m]')
    grid()
    show()

        
    "I wonder how the mx-red and mx-blue feels like"