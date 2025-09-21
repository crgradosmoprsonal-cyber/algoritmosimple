import time

clave_objetivo = "abc"
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=[]{};:,.<>/?|~`"

contador_intentos = 0
encontrado = False

def buscar(cadena_actual):
    global contador_intentos, encontrado

    contador_intentos += 1

    if cadena_actual == clave_objetivo:
        encontrado = True
        return cadena_actual

    if len(cadena_actual) < len(clave_objetivo):
        for caracter in alfabeto:
            if encontrado:
                break
            resultado = buscar(cadena_actual + caracter)
            if resultado:
                return resultado
    return None

inicio_tiempo = time.time()
resultado_final = buscar("")
fin_tiempo = time.time()
tiempo_total = fin_tiempo - inicio_tiempo

if resultado_final:
    print("Contraseña encontrada:", resultado_final)
else:
    print("No se encontró la contraseña")

print("Número total de intentos:", contador_intentos)
print(f"Tiempo total transcurrido: {tiempo_total:.4f}s")