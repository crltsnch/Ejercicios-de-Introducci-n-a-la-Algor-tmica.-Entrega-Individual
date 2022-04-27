#Porcentajes, IVA e inversiones

#Parte 1: Escribir un algoritmo que calcula el precio con todos los impuestos incluidos (TII) 
#para un precio sin impuestos y un porcentaje de IVA dado.

Algoritmo calculo de impuestos

Entrada
    ci: REAL #Coste inicial
    iva: REAL #Impuesto

Resultado: REAL

Precondicion
    ci > 0
    iva > 0

Variables
    iva1: REAL #porcentaje del IVA del precio incial

Realizacion
    iva1 <- ci * (iva / 100) #cálculo del iva del producto sin impuestos
    Resultado <- ci + iva1 #coste final con iva

Poscondicion
    Resultado > ci

Fin calculo de impuesto


#Parte 2: Escribir un algoritmo que calcula el importe de los intereses generados por un capital 
#invertido a un interés dado durante un tiempo dado, expresado en meses.

Algoritmo importe

Entrada
    capi: REAL #Capital inicial
    intereses: REAL #Porcentaje de intereses
    tiempo: REAL #Tiempo en meses

Precondicion
    capi > 0
    intereses > 0
    tiempo > 0

Variables
    