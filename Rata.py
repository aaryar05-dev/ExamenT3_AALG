def imprimir(mat):
    for f in mat:
        print(f)
    print()


def quitar_vida(valor, vidas):
    if valor == -1:
        return vidas - 1
    if valor == -2:
        return vidas - 2
    return vidas


def validar(lab, f, c, res, vidas):
    if f < 0 or f >= len(lab):
        return False
    if c < 0 or c >= len(lab[0]):
        return False
    if lab[f][c] == 0:
        return False
    if res[f][c] == 1:
        return False

    vidas_restantes = quitar_vida(lab[f][c], vidas)

    if vidas_restantes < 1:
        return False

    return True


def laberinto(lab, res, f, c, vidas):
    if f == 0 and c == 0:
        if lab[f][c] != 0:
            res[f][c] = 1
            imprimir(res)
            return True
        else:
            return False
    else:
        if validar(lab, f, c, res, vidas):
            vidas = quitar_vida(lab[f][c], vidas)

            res[f][c] = 1
            print("Vidas:", vidas)
            imprimir(res)

            if laberinto(lab, res, f + 1, c, vidas):      # Abajo
                return True
            elif laberinto(lab, res, f, c + 1, vidas):    # Derecha
                return True
            elif laberinto(lab, res, f - 1, c, vidas):    # Arriba
                return True
            elif laberinto(lab, res, f, c - 1, vidas):    # Izquierda
                return True
            else:
                res[f][c] = 0
                return False
        else:
            return False


lab = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [-2, 0, 0, -1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, -1, 0, 0, 0, -1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [-1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, -1, 1, 1, 1, 0, 1, 1]
]

res = [[0 for _ in range(9)] for _ in range(9)]

print("LABERINTO ORIGINAL:")
imprimir(lab)

print("RECORRIDO PASO A PASO:")

if laberinto(lab, res, 8, 0, 3):
    print("El ratón logró salir")
    print("MATRIZ SOLUCIÓN:")
    imprimir(res)
else:
    print("SIN salida")