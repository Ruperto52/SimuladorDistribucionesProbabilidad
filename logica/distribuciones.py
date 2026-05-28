import numpy as np
import scipy.stats as stats
import pandas as pd

class SimuladorDistribuciones:
    def __init__(self, tamano_muestra):
        if tamano_muestra <= 0:
            raise ValueError("El tamaño de muestra debe ser un entero mayor que cero.")
        self.tamano_muestra = int(tamano_muestra)

    def _formatear_resultados(self, datos, media_teorica, varianza_teorica, tipo_distribucion):
        media_empirica = float(np.mean(datos))
        varianza_empirica = float(np.var(datos, ddof=1)) if self.tamano_muestra > 1 else 0.0
        desviacion_empirica = float(np.sqrt(varianza_empirica))
        desviacion_teorica = float(np.sqrt(varianza_teorica))
        
        df_resultados = pd.DataFrame({
            "Concepto": ["Media", "Varianza", "Desviación estándar", "Tamaño de muestra"],
            "Valor teórico": [media_teorica, varianza_teorica, desviacion_teorica, self.tamano_muestra],
            "Valor simulado": [media_empirica, varianza_empirica, desviacion_empirica, self.tamano_muestra],
            "Diferencia": [abs(media_teorica - media_empirica), abs(varianza_teorica - varianza_empirica), abs(desviacion_teorica - desviacion_empirica), 0]
        })
        
        return {
            "datos": datos,
            "tipo": tipo_distribucion,
            "estadisticas": df_resultados
        }
    
    def simular_binomial(self, ensayos_n, prob_p):
        if ensayos_n <= 0 or not isinstance(ensayos_n, int):
            raise ValueError("El número de ensayos 'n' debe ser un entero positivo.")
        if not (0 <= prob_p <= 1):
            raise ValueError("La probabilidad 'p' debe estar en el intervalo [0, 1].")
        
        datos = np.random.binomial(ensayos_n, prob_p, self.tamano_muestra)
        media_teorica, varianza_teorica = stats.binom.stats(ensayos_n, prob_p, moments='mv')
        return self._formatear_resultados(datos, float(media_teorica), float(varianza_teorica), "Discreta")

    def simular_poisson(self, parametro_lambda):
        if parametro_lambda <= 0:
            raise ValueError("El parámetro Lambda debe ser mayor que cero.")
        
        datos = np.random.poisson(parametro_lambda, self.tamano_muestra)
        media_teorica, varianza_teorica = stats.poisson.stats(parametro_lambda, moments='mv')
        return self._formatear_resultados(datos, float(media_teorica), float(varianza_teorica), "Discreta")

    def simular_geometrica(self, prob_p):
        if not (0 < prob_p <= 1):
            raise ValueError("La probabilidad de éxito 'p' para la Geométrica debe estar en (0, 1].")
        
        datos = np.random.geometric(prob_p, self.tamano_muestra)
        media_teorica, varianza_teorica = stats.geom.stats(prob_p, moments='mv')
        return self._formatear_resultados(datos, float(media_teorica), float(varianza_teorica), "Discreta")
    
    def simular_normal(self, media_mu, desviacion_sigma):
        if desviacion_sigma <= 0:
            raise ValueError("La desviación estándar debe ser estrictamente positiva.")
        
        datos = np.random.normal(media_mu, desviacion_sigma, self.tamano_muestra)
        media_teorica, varianza_teorica = stats.norm.stats(loc=media_mu, scale=desviacion_sigma, moments='mv')
        return self._formatear_resultados(datos, float(media_teorica), float(varianza_teorica), "Continua")

    def simular_uniforme(self, limite_a, limite_b):
        if limite_a >= limite_b:
            raise ValueError("El límite inferior 'a' debe ser menor que el límite superior 'b'.")
        
        datos = np.random.uniform(limite_a, limite_b, self.tamano_muestra)
        media_teorica, varianza_teorica = stats.uniform.stats(loc=limite_a, scale=limite_b-limite_a, moments='mv')
        return self._formatear_resultados(datos, float(media_teorica), float(varianza_teorica), "Continua")

    def simular_exponencial(self, parametro_beta):
        if parametro_beta <= 0:
            raise ValueError("El parámetro de escala debe ser mayor que cero.")
        
        datos = np.random.exponential(parametro_beta, self.tamano_muestra)
        media_teorica, varianza_teorica = stats.expon.stats(scale=parametro_beta, moments='mv')
        return self._formatear_resultados(datos, float(media_teorica), float(varianza_teorica), "Continua")