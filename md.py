from sympy import symbols, Eq, solve

# --- Definimos la ecuación ---

def resolver_mrua(arg1_dicc, arg2_variable_a_buscar):
    # Definimos los símbolos (abstracción matemática)
    # x: Posición final, x0: Posición inicial, v: Velocidad inicial, t: Tiempo, a: Aceleración
    x, x0, v, t, a = symbols('x x0 v t a')

    # Declaramos la relación, es decir, declaramos la verdad
    # Fórmula: x = x0 + v*t + (1/2)*a*t^2
    # La escribimos igualada a cero para SymPy (Lado derecho - Lado izquierdo = 0)
    EcuacionPosicion = Eq(x0 + v * t + 0.5 * a * t**2 - x, 0)

    # Solución simbólica: Le pedimos a la librería que "despeje" la variable que necesitamos
    # arg2_variable_a_buscar es el símbolo que queremos encontrar (ej. x, a, o t)
    solucion_simbolica = solve(EcuacionPosicion, arg2_variable_a_buscar)[0]

    # Sustituimos los datos numéricos (del diccionario) en la solución simbólica
    resultado = solucion_simbolica.subs(arg1_dicc)

    return resultado

# --- Prueba ---

# Paso 1: Definimos los símbolos afuera para crear nuestro diccionario de datos
x, x0, v, t, a = symbols('x x0 v t a')

# Paso 2: Datos conocidos (diccionario de contexto)
# Ejemplo: Un auto arranca desde 0m (x0=0), a 10 m/s (v=10),
# acelera a 2 m/s^2 (a=2) durante 5 segundos (t=5).
# Queremos saber la Posición Final (x).
datos = {x0: 0, v: 10, a: 2, t: 5}

# Ejecutamos la función buscando 'x'
valor_final = resolver_mrua(datos, x)

print(f"Posición final calculada: {valor_final:.2f} metros")