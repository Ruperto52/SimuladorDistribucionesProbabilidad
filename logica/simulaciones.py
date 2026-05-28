import numpy as np
import scipy.stats as stats

def ejecutar_ley_grandes_numeros(distribucion, parametros, iteraciones_maximas=10000):
    dist_nombre = distribucion.lower()
    
    # Validar de forma flexible el nombre de la distribución
    if "uniforme" in dist_nombre:
        datos = np.random.uniform(parametros['a'], parametros['b'], iteraciones_maximas)
        valor_teorico = (parametros['a'] + parametros['b']) / 2
        
    elif "normal" in dist_nombre:
        datos = np.random.normal(parametros['mu'], parametros['sigma'], iteraciones_maximas)
        valor_teorico = parametros['mu']
        
    elif "binomial" in dist_nombre:
        datos = np.random.binomial(parametros['n'], parametros['p'], iteraciones_maximas)
        valor_teorico = parametros['n'] * parametros['p']
        
    elif "poisson" in dist_nombre:
        datos = np.random.poisson(parametros['lambda'], iteraciones_maximas)
        valor_teorico = parametros['lambda']
        
    elif "geom" in dist_nombre: 
        datos = np.random.geometric(parametros['p'], iteraciones_maximas)
        valor_teorico = 1 / parametros['p']
        
    elif "exponencial" in dist_nombre:
        datos = np.random.exponential(parametros['beta'], iteraciones_maximas)
        valor_teorico = parametros['beta']
        
    else:
        raise ValueError(f"Distribución '{distribucion}' no soportada en la simulación.")

    # Calcular la evolución de la media muestral paso a paso
    trayectoria_medias = np.cumsum(datos) / np.arange(1, iteraciones_maximas + 1)
    
    return trayectoria_medias, valor_teorico

def ejecutar_teorema_limite_central(nombre_distribucion, parametros, total_simulaciones=1000, tamano_muestra=30):
    medias_calculadas = []
    # Estandarizamos para que detecte los nombres igual que la función de arriba
    dist_nombre = nombre_distribucion.lower()
    
    for _ in range(total_simulaciones):
        if "uniforme" in dist_nombre:
            muestra = np.random.uniform(parametros['a'], parametros['b'], tamano_muestra)
        elif "exponencial" in dist_nombre:
            muestra = np.random.exponential(parametros['beta'], tamano_muestra)
        elif "geom" in dist_nombre:
            muestra = np.random.geometric(parametros['p'], tamano_muestra)
        elif "poisson" in dist_nombre:
            # CORRECCIÓN AQUÍ: Se cambió de 'lam' a 'lambda'
            muestra = np.random.poisson(parametros['lambda'], tamano_muestra)
        elif "binomial" in dist_nombre:
            muestra = np.random.binomial(parametros['n'], parametros['p'], tamano_muestra)
        elif "normal" in dist_nombre:
            muestra = np.random.normal(parametros['mu'], parametros['sigma'], tamano_muestra)
        else:
             raise ValueError(f"Distribución '{nombre_distribucion}' no soportada en la simulación TLC.")
             
        medias_calculadas.append(np.mean(muestra))
    return np.array(medias_calculadas)