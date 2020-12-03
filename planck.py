import matplotlib.pyplot as plt
import numpy as np


def planck(t,lambda_):

    '''
    Calcula la distribución de Planck 

    parametros:
        t -> temperatura en Kelvin
        lamda_ -> rango de la longitud de onda 

    retorno:
        devuelve la distribución de Planck
    '''

    # Constantes de la ecuación
    h = 6.626e-34 # Js
    c = 3.0e8 # m/s
    k = 1.380649e-23 # J/K

    # Ecuación de Planck
    a = 2*h*c**2    
    b = np.exp( (h*c) / (lambda_*k*t) ) 
    return a / (lambda_**5 * (b - 1) )

# Definición del rango deseado y las temperaturas
t = np.arange(3.0,13.0)*1000 # K
lambda_ = np.arange(50e-9,1e-6,1e-9)

# Operación sobre todas las temperaturas
for t_ in t:

    p = planck(t_,lambda_)
    plt.plot(lambda_*1e9 ,p, label=str(t_) + "K")

# Ploteo de las curvas de distribución
plt.title("Distribución de Planck")
plt.ylabel("W nm^(-3)")
plt.xlabel("nm")
plt.legend( )
plt.show()
