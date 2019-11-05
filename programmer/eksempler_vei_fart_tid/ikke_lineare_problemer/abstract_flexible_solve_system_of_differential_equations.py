from numpy import linspace, zeros
from pyplot import plot, xlabel, ylabel, grid, show, figure

def _transform_number_to_func(func_or_number):
    """
    Undersøk om en variabel er et tall eller en funksjon
    Hvis variabelen er et tall a, returneres en konstant funksjon f(t) = 0
    Hvis variableen er en funksjon, returneres funksjonen tilbake
    Hvis variabelen er noe annet, gis det en feilmelding
    """

    if type(func_or_number) == float or type(func_or_number) == int:
        u = float(func_or_number)
        def func(*args):
            return func_or_number
        return func
    elif type(func_or_number) == type(_transform_number_to_func):
        return func_or_number
    else:
        raise ValueError('parameter v to function modell_strekning must be a number or a function')



def solve(T, RHS, dt=0.1, *args):
    """
    Solves the system of differential equations y'(t) = f(t, y),
    where RHS = f(t, y)
    using the forward Euler scheme.
    """

    # make sure RHS is a function
    RHS = _transform_number_to_func(RHS)

    U = args # tuple of initial conditions
    t = [0]
    u = [U]
    k = 0

    while t[k] < T:
        u_next = u[k] + dt*RHS(t[k], u[k])
        t_next = t[k] + dt

        t.append(t_next)
        u.append(u_next)
        k += 1
    return t, u