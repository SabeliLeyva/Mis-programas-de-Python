/*
 Complementos para VS-Code
 1. Jupyter
 2. Python IntelliSense
*/

--Nombre de la carpeta: Notebooksipynb
--Nombre del Notebook: ship-manual.ipynb

--MARKDOWN
# Manual de la nave

--TERMINAL
pip install ipywidgets
--Actualizar después

--CODE
import ipywidgets as widgets

ignition = widgets.ToggleButton(
    value=False,
    description='Iniciar Launch',
    button_style='success',
    tooltip='Engage your Launch',
    icon='rocket'
)

output = widgets.Output()

display(ignition, output)

def on_value_change(change):
    with output:
        if change['new'] == True:
            print("Nave Iniciada!")
        else:   
            print("Nave Detenida")

ignition.observe(on_value_change, names='value')

--MARKDOWN
## Niveles de oxigeno
Muestra 10 minutos de niveles de oxigeno en tu nave

--CODE
%pip install matplotlib
%pip install numpy

--TERMINAL
pip install matplotlib
pip install numpy
--Actualizar después

--CODE
import numpy as np
import matplotlib.pyplot as plt

data = np.random.default_rng(12345)
oxy_nums = data.integers(low=0, high=10, size=10)

plt.bar(range(len(oxy_nums)), oxy_nums)
plt.show()

--MARKDOWN
## Velocidad de la nave
Muestra los segundos necesarios para pasar de 0 a 11200 metros por segundo, dada la aceleración de la nave en metros por segundo.

--CODE
endVelocity = 11200
startVelocity = 0
acceleration = 9.8

time = (endVelocity - startVelocity) / acceleration
print("Tiempo para alcanzar la velocidad deseada = ", time)