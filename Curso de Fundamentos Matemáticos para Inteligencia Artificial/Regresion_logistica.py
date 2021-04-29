# import numpy as np
# from sklearn.linear_model import LogisticRegression
# x = np.array([0.5, 0.75, 1, 1.25, 1.5, 1.75, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 4, 4.25, 4.5,
# 4.75, 5, 5.5]).reshape(-1,1)
# y=np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

# regresion_logistica=LogisticRegression()

# regresion_logistica.fit(x,y)
# x_nuevo = np.array([1,2,3,4,5,6]).reshape(-1,1)

# prediccion = regresion_logistica.predict(x_nuevo)
# print(prediccion)

# probabilidades_prediccion = regresion_logistica.predict_proba(x_nuevo)
# print(probabilidades_prediccion)
# print(probabilidades_prediccion[:,1])
import numpy as np
from sklearn.linear_model import LogisticRegression

def regresion():
    #Datos a utilizar
    xlist = [i*0.25 for i in range(2,22)]
    horas = np.array(xlist).reshape(-1,1)
    aprobado = np.array([0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1])

    #Creamos la instancia de la regresion y le damos los datos
    regresion_logistica = LogisticRegression()
    regresion_logistica.fit(horas,aprobado)

    #Generamos una nueva lista de horas para hacer una prediccion y se ejecuta
    horas_prediccion = np.array([i for i in range(1,7)]).reshape(-1,1)
    prediccion = regresion_logistica.predict(horas_prediccion)
    probabilidad = regresion_logistica.predict_proba(horas_prediccion)

    #Se muestran los resultados
    np.set_printoptions(3)  #Ajustamos la visualizacion
    print('Datos de la prediccion realizada:')
    print('Horas:        {}'.format(horas_prediccion.reshape(1,-1)))
    print('Aprobado:     {}'.format(prediccion))
    print('Probabilidad: {}'.format(probabilidad[:,1]))

if __name__ == '__main__':
    regresion()
