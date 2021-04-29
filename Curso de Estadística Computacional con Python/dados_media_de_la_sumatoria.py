import random
import collections
from estadisticas import desviacion_estandar, media

from bokeh.plotting import figure, output_file, show

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        dado_1 = random.choice([1, 2, 3, 4, 5, 6])
        dado_2 = random.choice([1, 2, 3, 4, 5, 6])
        tiro = dado_1 + dado_2
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros

def graficar(x, y):

    plot = figure(title="Distribucion Normal")
    plot.vbar(x, top=y, width=0.5, color="#CAB2D6")
    output_file("vertical_bar.html")
    show(plot)

def estimacion(numero_de_tiros):

    estimados = tirar_dado(numero_de_tiros)

    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)

    counter = dict(collections.Counter(estimados))

    graficar(list(counter.keys()), list(counter.values()))

    return (media_estimados, sigma)

def main(numero_de_tiros):

    media, sigma = estimacion(numero_de_tiros)
    print(f'Estimados = {round(media, 5)}, sigma = {round(sigma, 5)}')

if __name__ == '__main__':
    numero_de_tiros = int(input('Diga la cantidad de tiros con los que quiere iniciar: '))
    main(numero_de_tiros)
