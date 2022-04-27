#Media aritmética ponderada

#Parte 1: Escribir un algoritmo que calcula la media aritmética de tres números dados.
Algoritmo media aritmética

Entrada
    #Los tres numeros
    n1: REAL
    n2: REAL
    n3: REAL

Resultado: REAL

Precondicion
    n1, n2, n3 >= 0

Realizacion
    Resultado <- (n1 + n2 + n3) / 3

Poscondicion
    Resultado >= 0

Fin media aritmética

#Parte 2: La misma pregunta para una media ponderada cuando se dan los números y los coeficientes de ponderación.

Entrada
    n1: REAL
    n2: REAL
    n3: REAL
    c1, c2, c3 : REAL #coeficientes de ponderacion

Precondicion
    n1, n2, n3 >= 0
    0 < c1, c2, c3 <= 1 

Realizacion
    Resultado <- n1*c1 + n2*c2 + n3*c3

Poscondicion
    Resultado >= 0

Fin media aritmetica con coeficientes de ponderacion