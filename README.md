# Simulador de Distribuciones de Probabilidad y Visualizaciones Gráficas
Dentro de este proyecto se explora lo que son las distribuciones de probabilidad para las variables continuas y las variables discretas, una forma de hacer un simulador de estas mismas con interfaz grafica y con las opciones de guardar los resultados obtenidos para garantizar su comprension de cada una de las distribuciones

## Información de los Integrantes
* **Institución:** Instituto Politécnico Nacional (IPN)
* **Escuela:** Escuela Superior de Cómputo (ESCOM) 
* **Unidad de Aprendizaje:** Probabilidad y Estadistica
* **Programa Académico:** Ingeniería en Sistemas Computacionales / Plan 2020 
* **Grupo:** 4CM2
* **Alumno:** 
   * Diego Ruperto Hernandez (Boleta: 2024630696)

---

## 1. Introducción

En el ámbito de la Ingeniería en Sistemas Computacionales y la Ciencia de Datos, la simulación estocástica constituye una de las metodologías más potentes para modelar, analizar y optimizar sistemas complejos cuyo comportamiento interno está regido por la incertidumbre. Fenómenos cotidianos en la infraestructura tecnológica —tales como la tasa de pérdida de paquetes en una red de comunicación, el tiempo de espera de peticiones concurrentes en un servidor web, o el volumen de transacciones por segundo en una base de datos— no pueden ser predichos mediante funciones puramente deterministas. En su lugar, requieren un tratamiento analítico basado en variables aleatorias y modelos de probabilidad.

Históricamente, el estudio de la probabilidad se ha abordado desde una perspectiva puramente analítica y deductiva, fundamentada en resolver complejas ecuaciones integrales y sumatorias en papel. Si bien este enfoque proporciona la solución formal exacta, suele abstraer al estudiante y al desarrollador de la naturaleza empírica del fenómeno. El desarrollo de este simulador interactivo surge precisamente para acortar esa brecha, transformando los modelos matemáticos abstractos en una herramienta de experimentación visual tangible y dinámica.

La construcción del software plantea un desafío de ingeniería no trivial: emular la aleatoriedad de la naturaleza dentro de una computadora, la cual es por definición una máquina determinista. Para lograrlo, el sistema explota algoritmos generadores de números pseudoaleatorios de última generación, estructurando vectores masivos de datos para recrear escenarios experimentales. Mediante un enfoque de arquitectura desacoplada, el proyecto demuestra cómo interactúan armónicamente una interfaz de usuario reactiva en el Front-End y un motor de cómputo vectorizado de alta velocidad en el Back-End, ofreciendo una plataforma interactiva capaz de validar las leyes estadísticas fundamentales en tiempo real.

---

## 2. Objetivo del Proyecto

El objetivo principal de este proyecto es diseñar, codificar e implementar un simulador computacional modular y portable que permita generar muestras aleatorias masivas a partir de diversos modelos de probabilidad discretos y continuos, facilitando la visualización de sus funciones de distribución y garantizando la validación rigurosa de sus momentos estadísticos teóricos frente a los estimadores empíricos muestrales.

### Objetivos Específicos
* **Validación Estadística Precisa:** Calcular en tiempo real la media aritmética, la varianza y la desviación estándar de los conjuntos de datos generados por simulación, confrontándolos mediante diferencias absolutas contra los valores analíticos exactos derivados de sus fórmulas poblacionales.
* **Demostración Práctica de Teoremas Asintóticos:** Proveer un entorno experimental interactivo para visualizar de forma clara la convergencia de la media muestral dictada por la Ley de los Grandes Números, así como la transformación de histogramas asimétricos hacia la simetría gaussiana descrita por el Teorema del Límite Central.
* **Desarrollo de Software Bajo Arquitectura Limpia:** Separar estrictamente la lógica de procesamiento matemático y simulación numérica del código encargado del renderizado gráfico y la interfaz de usuario, promoviendo la mantenibilidad y la escalabilidad del sistema.
* **Garantía de Portabilidad e Infraestructura Continua:** Encapsular la aplicación y todo su árbol de dependencias científicas dentro de un contenedor virtual aislado utilizando Docker, asegurando que el simulador se ejecute con idéntico rendimiento y sin errores de configuración en cualquier entorno de distribución (Ubuntu/Linux, macOS o Windows).

---

## 3. Marco Teórico Fundamental

El soporte matemático del simulador se fundamenta en la teoría clásica de la probabilidad y la inferencia estadística. Los modelos implementados se dividen rigurosamente de acuerdo con el soporte y la naturaleza del espacio muestral que barren sus variables aleatorias.

### Variables Aleatorias Discretas
Son aquellas funciones medibles cuyo soporte está compuesto por un conjunto finito o infinito numerable de valores aislados. La asignación de sus probabilidades se define mediante una **Función de Masa de Probabilidad (PMF)**, denotada como $p(x) = P(X = x)$, la cual asigna un peso específico a cada punto del soporte. El simulador integra los siguientes modelos discretos:

* **Distribución de Bernoulli:** Modela un único experimento aleatorio que posee exactamente dos resultados posibles y mutuamente excluyentes: éxito (con probabilidad $p$) o fracaso (con probabilidad $1-p$). Es la base constructiva de modelos más complejos.
  * *Ecuación PMF:* $p(x) = p^x (1-p)^{1-x}, \quad x \in \{0, 1\}$
  * *Esperanza Matemática:* $E[X] = p$
  * *Varianza:* $Var(X) = p(1-p)$
  * *Aplicación en Sistemas:* Modelado del éxito o fallo en el envío de un único bit a través de un canal con ruido.

* **Distribución Binomial:** Describe el número total de éxitos obtenidos al realizar una secuencia fija de $n$ ensayos independientes e idénticamente distribuidos de Bernoulli, manteniendo una probabilidad de éxito $p$ constante en cada uno de ellos.
  * *Ecuación PMF:* $p(x) = \binom{n}{x} p^x (1-p)^{n-x}, \quad x \in \{0, 1, \dots, n\}$
  * *Esperanza Matemática:* $E[X] = np$
  * *Varianza:* $Var(X) = np(1-p)$
  * *Aplicación en Sistemas:* Simulación de la cantidad de servidores activos dentro de un clúster de alta disponibilidad compuesto por $n$ nodos autónomos.

* **Distribución Geométrica:** Modela el número total de fallos o intentos fallidos acumulados antes de presenciar el primer éxito dentro de una secuencia infinita de ensayos independientes de Bernoulli.
  * *Ecuación PMF:* $p(x) = (1-p)^x p, \quad x \in \{0, 1, 2, \dots\}$
  * *Esperanza Matemática:* $E[X] = \frac{1-p}{p}$
  * *Varianza:* $Var(X) = \frac{1-p}{p^2}$
  * *Aplicación en Sistemas:* Cálculo del número de reintentos de conexión que debe realizar un cliente de red antes de establecer un canal de comunicación exitoso con un servidor.

* **Distribución de Poisson:** Expresa la probabilidad de que ocurra un número determinado de eventos independientes dentro de un intervalo fijo de tiempo o espacio, asumiendo que dichos eventos ocurren con una tasa media constante denotada por $\lambda$ (Lambda).
  * *Ecuación PMF:* $p(x) = \frac{\lambda^x e^{-\lambda}}{x!}, \quad x \in \{0, 1, 2, \dots\}$
  * *Esperanza Matemática:* $E[X] = \lambda$
  * *Varianza:* $Var(X) = \lambda$
  * *Aplicación en Sistemas:* Modelado del flujo de peticiones entrantes por minuto a la API de un servicio web en producción.

### Variables Aleatorias Continuas
Son aquellas definidas sobre un soporte infinito no numerable, típicamente intervalos dentro de los números reales ($\mathbb{R}$). Dado que la probabilidad de que una variable continua tome un valor exacto aislado es matemáticamente nula ($P(X = x) = 0$), su comportamiento se rige por la integral de su **Función de Densidad de Probabilidad (PDF)**, denotada como $f(x)$. Las áreas bajo esta curva representan la probabilidad de que la variable caiga dentro de un rango específico.

* **Distribución Uniforme Continua:** Modela situaciones donde todos los subintervalos de idéntica longitud dentro de un dominio acotado por un límite inferior $a$ y un límite superior $b$ poseen exactamente la misma probabilidad de ocurrencia. La densidad es completamente plana.
  * *Ecuación PDF:* $f(x) = \frac{1}{b-a}, \quad \forall x \in [a, b]$
  * *Esperanza Matemática:* $E[X] = \frac{a+b}{2}$
  * *Varianza:* $Var(X) = \frac{(b-a)^2}{12}$
  * *Aplicación en Sistemas:* Generación de claves criptográficas y distribución homogénea de cargas de direccionamiento de memoria.

* **Distribución Normal (Gaussiana):** Es el modelo continuo más importante en estadística. Su representación gráfica es una campana simétrica centrada en su media $\mu$, y su ancho o dispersión está determinado por la desviación estándar $\sigma$. Describe la distribución natural de una enorme cantidad de variables físicas y computacionales.
  * *Ecuación PDF:* $f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left( -\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2 \right), \quad x \in \mathbb{R}$
  * *Esperanza Matemática:* $E[X] = \mu$
  * *Varianza:* $Var(X) = \sigma^2$
  * *Aplicación en Sistemas:* Modelado de errores de medición de sensores en sistemas embebidos o variaciones en los tiempos de respuesta de transacciones complejas.

* **Distribución Exponencial:** Modela el tiempo o la distancia continua que transcurre entre dos eventos consecutivos pertenecientes a un proceso de Poisson. Se caracteriza por su asimetría positiva extrema y por poseer la propiedad de "falta de memoria". Está parametrizada por un factor de escala continuo $\beta$ (donde $\beta = 1/\lambda$).
  * *Ecuación PDF:* $f(x) = \frac{1}{\beta} e^{-\frac{x}{\beta}}, \quad x \ge 0$
  * *Esperanza Matemática:* $E[X] = \beta$
  * *Varianza:* $Var(X) = \beta^2$
  * *Aplicación en Sistemas:* Simulación del tiempo de vida útil o tiempo medio entre fallos (MTBF) de componentes de hardware (discos duros, fuentes de poder).

### Teoremas de Convergencia Asintótica
El simulador incorpora módulos avanzados dedicados a la visualización computacional de los dos pilares teóricos de la estadística moderna:

* **Ley de los Grandes Números (LGN):** Establece que si se extrae una muestra de observaciones independientes e idénticamente distribuidas (i.i.d.) de tamaño $n$, conforme $n$ tiende al infinito ($n \rightarrow \infty$), el promedio aritmético de dicha muestra converge de forma casi segura hacia la esperanza teórica poblacional $\mu$. Computacionalmente, esto justifica por qué al simular muestras masivas ($N \ge 10,000$), la diferencia entre el estadístico empírico y el parámetro matemático analítico tiende a colapsar a cero.
* **Teorema del Límite Central (TLC):** Dictamina que la suma o el promedio ponderado de un número suficientemente grande ($n$) de variables aleatorias independientes e idénticamente distribuidas —cada una con una media $\mu$ y una varianza $\sigma^2$ finitas— tenderá asintóticamente a aproximarse a una distribución normal estándar, sin importar cuál sea la forma, el sesgo o la asimetría de la distribución poblacional original de la cual se extrajeron las muestras. El simulador explota este principio al promediar lotes de datos de distribuciones marcadamente asimétricas (como la Exponencial o la Geométrica) para evidenciar visualmente cómo el histograma resultante adquiere la forma gaussiana perfecta a medida que se incrementa el nivel de agregación de las muestras.

## 4. Funcionalidades del Sistema

El simulador computacional ha sido diseñado como una plataforma interactiva e integral que traduce la teoría estadística en componentes de software dinámicos. A continuación, se desglosan de forma detallada las funcionalidades principales que integran el sistema, describiendo su objetivo, su comportamiento interno y su relevancia en el análisis de datos:

---

### Configuración Dinámica y Reactiva de Parámetros (Sidebar Control)
* **Descripción:** Esta funcionalidad representa el panel de control unificado de la aplicación, ubicado en la barra lateral izquierda (Sidebar). En lugar de procesar entradas estáticas o requerir reconfiguraciones desde la consola de comandos, el sistema adapta automáticamente su interfaz de entrada según la distribución probabilística seleccionada por el usuario.
* **Comportamiento Interno:** Al elegir un modelo estadístico, el sistema oculta los controles irrelevantes e inyecta dinámicamente los componentes de entrada numéricos específicos (Sliders y Inputs). Por ejemplo, si el usuario selecciona la *Distribución Binomial*, el panel despliega controles para manipular de forma segura el número de ensayos ($n$) y la probabilidad de éxito ($p$); si cambia a la *Distribución Normal*, la interfaz muta instantáneamente para solicitar la media ($\mu$) y la desviación estándar ($\sigma$). 
* **Control de Errores Integrado:** Cada componente cuenta con límites estrictos programados a nivel de interfaz para evitar estados inválidos en el motor matemático (v.g., impide configurar desviaciones estándar menores o iguales a cero, o probabilidades fuera del intervalo cerrado $[0, 1]$).

---

### Módulo de Simulación Estocástica Individual e Histogramas de Densidad
* **Descripción:** Constituye el núcleo visual de la primera pestaña del software. Su objetivo es generar un espacio muestral empírico masivo y confrontarlo directamente contra el modelo teórico ideal para evaluar el nivel de representatividad de la muestra.
* **Comportamiento Interno:** Al activarse la petición, el Back-End genera un arreglo unidimensional masivo con el tamaño de muestra ($N$) indicado por el usuario mediante algoritmos vectorizados de muestreo. Posteriormente, el sistema procesa estos datos y genera dos capas de visualización superpuestas sobre el mismo lienzo gráfico:
  1. **Para Modelos Discretos:** Genera un histograma de frecuencias relativas en formato de barras aisladas y calcula de forma paralela la Función de Masa de Probabilidad (PMF) teórica exacta de SciPy, graficándola como puntos o bastones de control para contrastar la coincidencia exacta de cada evento.
  2. **Para Modelos Continuos:** Grafica un histograma de áreas normalizadas y calcula la curva analítica de la Función de Densidad de Probabilidad (PDF). Adicionalmente, calcula y superpone una curva de Estimación de Densidad por Kernel (KDE) basada en los datos muestrales para observar el ajuste del perfil empírico frente a la curva gaussiana o exponencial de referencia.

---

### Evaluación de Momentos Estadísticos y Análisis de Error Residual
* **Descripción:** Es una herramienta analítica encargada de auditar la precisión de la simulación mediante un desglose matricial numérico comparativo. Traduce la coincidencia visual de los gráficos en métricas duras de control matemático.
* **Comportamiento Interno:** El sistema toma el vector crudo de datos simulados y calcula de forma directa sus estimadores muestrales: la media aritmética (centro de masa de los datos), la varianza muestral sesgada/insesgada (dispersión cuadrática) y la desviación estándar empírica. De forma simultánea, invoca las ecuaciones cerradas de la distribución correspondiente para extraer los parámetros analíticos exactos de la población.
* **Despliegue de Resultados:** La interfaz procesa ambos conjuntos de datos y construye una tabla comparativa estructurada que calcula de forma automática el **Error Absoluto Residual** (la diferencia absoluta entre el valor teórico y el simulado). Esta funcionalidad permite comprobar matemáticamente que, conforme aumenta el volumen de datos generados, el error residual tiende asintóticamente a cero.

---

### Visualización de la Trayectoria de Convergencia (Ley de los Grandes Números)
* **Descripción:** Una funcionalidad avanzada diseñada para demostrar el comportamiento asintótico de los promedios muestrales. Permite al usuario entender por qué las fluctuaciones caóticas iniciales de la aleatoriedad se estabilizan de forma predecible conforme se acumulan observaciones.
* **Comportamiento Interno:** El software extrae un vector secuencial de simulaciones de longitud máxima ($N = 10,000$). En lugar de calcular únicamente la media final, el Back-End ejecuta un algoritmo de suma acumulada optimizado a nivel de memoria que evalúa la media muestral paso a paso, iteración por iteración.
* **Despliegue Gráfico:** Renderiza un gráfico de líneas continuas bidimensional donde el eje horizontal representa el número de experimentos acumulados y el eje vertical denota el valor de la media calculada hasta ese instante. El sistema traza una línea horizontal fija de color contrastante (Rojo Carmín institucional) que representa el valor esperado teórico preciso. El usuario puede apreciar de forma interactiva cómo la línea de la media muestral fluctúa violentamente en las primeras iteraciones y se acopla milimétricamente a la línea teórica a medida que el número de muestras progresa.

---

### Demostración Guiada del Teorema del Límite Central (Módulo de Agregación)
* **Descripción:** Esta funcionalidad permite comprobar de manera empírica uno de los teoremas más contraintuitivos y trascendentales de la estadística: cómo la suma de variables marcadamente asimétricas o no gaussianas colapsa inevitablemente en una distribución normal.
* **Comportamiento Interno:** El simulador permite al usuario seleccionar distribuciones de base con sesgos pronunciados (como la *Distribución Exponencial* o la *Geométrica*). El motor computacional ejecuta un ciclo masivo de simulaciones paralelas donde extrae $M$ cantidad de muestras independientes de tamaño $n$. Para cada una de estas submuestras, calcula su promedio aritmético individual, construyendo un nuevo vector compuesto exclusivamente por las medias resultantes.
* **Impacto Visual:** Al graficar el histograma de este nuevo vector de medias, el sistema demuestra visualmente que, a pesar de que la distribución original tiene un perfil completamente descendente o plano, el histograma de sus promedios adopta la forma de una campana gaussiana simétrica y perfecta, permitiendo modificar el tamaño del submuestreo para observar cómo se reduce la varianza del estimador.

---

### Aislamiento e Infraestructura Desacoplada mediante Docker
* **Descripción:** Aunque se trata de una funcionalidad a nivel de infraestructura y despliegue, es una característica crítica del sistema que garantiza la portabilidad y la reproducibilidad científica del simulador sin depender de las configuraciones específicas del sistema operativo del usuario.
* **Comportamiento Interno:** Mediante una receta de construcción estructurada por capas (`Dockerfile`), el sistema crea un entorno aislado basado en una imagen ligera de Linux. Configura los directorios de trabajo, inyecta las variables de entorno necesarias, compila de forma aislada las versiones exactas de las dependencias matemáticas y expone el puerto de comunicación de red `8501`. Esta funcionalidad permite levantar y destruir instancias completas del simulador en segundos a través de la terminal de comandos, eliminando por completo el problema clásico de incompatibilidad de librerías en sistemas operativos locales.

## 5. Librerias Utilizadas y Funcionalidad del codigo
El desarrollo del simulador estadístico se apoya en el ecosistema científico y de visualización de Python. A continuación, se analiza en profundidad cada una de las librerías implementadas, justificando su integración, explicando mecánicamente cómo operan dentro del código y proveyendo los canales oficiales para la consulta de su documentación técnica.

### Streamlit (v1.57.0+)
* **¿Por qué se utilizó? (Justificación):** En el desarrollo de software científico tradicional, construir una interfaz gráfica de usuario (GUI) suele requerir frameworks complejos (como Tkinter o PyQt) o arquitecturas web acopladas de tipo Cliente-Servidor (HTML, CSS y JavaScript). Streamlit elimina esta sobrecarga de infraestructura, permitiendo transformar scripts de datos en aplicaciones web interactivas y reactivas utilizando únicamente código Python nativo. Su modelo de ejecución recarga el script de arriba a abajo cada vez que el usuario interactúa con un componente, lo que simplifica drásticamente el manejo de estados dinámicos y eventos en tiempo real.
* **¿Cómo se utilizó dentro del software?:** Se encarga por completo del Front-End del proyecto. Controla la barra lateral (`st.sidebar`) para la captura de parámetros numéricos mediante deslizadores (`st.slider`), organiza el lienzo de trabajo principal en pestañas independientes (`st.tabs`), renderiza las tablas comparativas y actúa como el contenedor donde se despliegan las figuras y lienzos interactivos de graficación (`st.pyplot`).
* **Documentación de consulta:** La documentación oficial con guías de diseño, API Reference y manejo de estados se encuentra en: [https://docs.streamlit.io](https://docs.streamlit.io)

---

### NumPy (v2.2.6+)
* **¿Por qué se utilizó? (Justificación):** Las listas nativas de Python no están diseñadas para el cómputo numérico de alta densidad, ya que almacenan referencias dispersas a objetos en memoria, lo que genera cuellos de botella críticos debido a la interpretación ciclo por ciclo (loops de CPU lentos). NumPy resuelve esto introduciendo el objeto `ndarray`, un arreglo homogéneo y contiguo en memoria gestionado directamente a nivel de lenguaje C. Esto permite realizar operaciones vectorizadas (aplicar cálculos simultáneos sobre millones de datos de un solo golpe) con un consumo mínimo de memoria RAM y tiempos de ejecución casi instantáneos, requisito indispensable para simular hasta 20,000 muestras aleatorias.
* **¿Cómo se utilizó dentro del software?:** Es el motor estocástico del Back-End. A través del submódulo `numpy.random`, el sistema genera vectores masivos de variables aleatorias puras para alimentar los experimentos. Además, se utiliza para optimizar la Ley de los Grandes Números mediante funciones de álgebra lineal y métodos vectorizados como `np.cumsum` (suma acumulada) y `np.arange`, calculando la trayectoria de la media iteración por iteración en una sola operación de CPU.
* **Documentación de consulta:** Los manuales de optimización de memoria y referencia de funciones matemáticas se localizan en: [https://numpy.org/doc/](https://numpy.org/doc/)

---

### SciPy - Submódulo `scipy.stats` (v1.15.3+)
* **¿Por qué se utilizó? (Justificación):** Mientras que NumPy destaca en la generación de datos crudos simulados a partir de la aleatoriedad, no contiene las definiciones analíticas abstractas de las curvas matemáticas de probabilidad. `scipy.stats` proporciona el marco teórico y analítico formal de control. Contiene una biblioteca exhaustiva de distribuciones continuas y discretas parametrizadas con sus ecuaciones cerradas precompiladas, permitiendo extraer valores probabilísticos exactos sin necesidad de programar integrales o sumatorias desde cero, actuando como el estándar de oro de la aplicación.
* **¿Cómo se utilizó dentro del software?:** Se utiliza de forma paralela en la validación y el control de calidad matemático. El script `logica/distribuciones.py` invoca los objetos de SciPy (como `scipy.stats.norm`, `binom`, `poisson`, etc.) para dos tareas fundamentales: extraer mediante el método `.stats(moments='mv')` el valor analítico exacto de la media y la varianza teórica de la población, y evaluar las funciones de densidad (PDF) o de masa (PMF) sobre rangos continuos y discretos para alimentar las curvas teóricas de los gráficos.
* **Documentación de consulta:** La guía detallada sobre funciones de distribución y estadística avanzada está disponible en: [https://docs.scipy.org/doc/scipy/](https://docs.scipy.org/doc/scipy/)

---

### Matplotlib - Submódulo `pyplot` (v3.10.9+)
* **¿Por qué se utilizó? (Justificación):** Es la biblioteca de visualización estándar y de bajo nivel por excelencia en el ecosistema científico de Python. Proporciona una arquitectura jerárquica orientada a objetos (Lienzo -> Figura -> Ejes -> Trazos) que otorga un control absoluto y milimétrico sobre cada elemento del gráfico. Permite manipular de forma programática las dimensiones de las imágenes, los límites de los ejes numéricos, las etiquetas técnicas, los títulos y las cuadrículas de fondo, garantizando un renderizado formal apto para documentación académica.
* **¿Cómo se utilizó dentro del software?:** Actúa como el andamiaje y la infraestructura de graficación del proyecto. Se encarga de instanciar los lienzos de dibujo mediante `plt.subplots()`, definir la disposición de las figuras, inyectar los títulos técnicos, rotular los ejes cartesianos (X e Y) y dibujar las líneas de referencia horizontales y verticales fijas que delimitan las esperanzas matemáticas teóricas.
* **Documentación de consulta:** El catálogo completo de estilos, configuración de ejes y API de control se encuentra en: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)

---

### Seaborn (v0.13.2+)
* **¿Por qué se utilizó? (Justificación):** Matplotlib es sumamente potente pero requiere muchas líneas de código para construir visualizaciones estadísticas avanzadas (como histogramas normalizados combinados con curvas de densidad). Seaborn está construido directamente sobre Matplotlib y actúa como una capa de abstracción de alto nivel. Su principal ventaja es que integra algoritmos de análisis estadístico interno directo, permitiendo trazar representaciones complejas de datos en una sola línea de código, aplicando por defecto un diseño estético sofisticado y armónico adecuado para la interpretación visual de datos.
* **¿Cómo se utilizó dentro del software?:** Se utiliza específicamente para el renderizado estético de los resultados empíricos mediante la función `sns.histplot`. En los modelos continuos, Seaborn calcula de manera automática e interna la Estimación de Densidad por Kernel (KDE), trazando una curva suave basada en los datos simulados que permite apreciar visualmente la distribución de las muestras sin sufrir el ruido visual de las barras del histograma, facilitando la comparación simulación contra teoría.
* **Documentación de consulta:** Los tutoriales y galerías de visualizaciones estadísticas estructuradas están disponibles en: [https://seaborn.pydata.org](https://seaborn.pydata.org)

### Logica de `logica/Simulaciones.py`
El script `logica/simulaciones.py` es el motor computacional estocástico del simulador. Su responsabilidad exclusiva es generar muestras pseudoaleatorias masivas y ejecutar los algoritmos necesarios para demostrar los teoremas de convergencia asintótica (Ley de los Grandes Números y Teorema del Límite Central). 

A continuación, se explica detalladamente la lógica de programación detrás de cada bloque de código.

---

### Bloque 1: Importación de Dependencias

```python
import numpy as np
import scipy.stats as stats
```
**¿Qué hace?** 
Importa las librerías científicas fundamentales de Python. numpy se carga con el alias estándar np para manejar arreglos multidimensionales y generación de números aleatorios, mientras que scipy.stats se carga como stats para proveer herramientas de análisis estadístico complementario.

**Lógica y Puntos Clave:** Eficiencia de Cómputo (NumPy): Dado que el simulador maneja miles o decenas de miles de iteraciones, usar listas estándar de Python provocaría severos cuellos de botella. NumPy resuelve esto ejecutando las operaciones matemáticas en código C precompilado bajo el capó, asegurando que el servidor responda de manera casi instantánea a las peticiones del usuario.

### Bloque 2: Función `ejecutar_ley_grandes_numeros` (Parte 1 - Muestreo)
```python

```
**¿Qué hace?** Esta primera mitad de la función recibe la instrucción de simular una distribución específica. Extrae un vector masivo de datos crudos simulados (por defecto, 10,000 datos) y calcula paralelamente el valor exacto de la esperanza matemática teórica ($E[X]$) que servirá como línea base de comparación.
**Lógica y Puntos Clave:** 
* Tolerancia a Fallos (.lower() e in): Al convertir la entrada a minúsculas (distribucion.lower()) y buscar subcadenas ("uniforme" in dist_nombre), la función se vuelve robusta contra discrepancias de formato (como diferencias en mayúsculas/minúsculas o acentos) que provengan de la interfaz de usuario en app.py.
* Contrato Estricto de Llaves: Utiliza un diccionario de parametros con llaves unificadas (e.g., 'lambda', 'mu', 'beta'). Esto garantiza que la información viaje de forma segura y estructurada desde el Front-End (Streamlit) hacia el Back-End (NumPy), previniendo excepciones de tipo KeyError.
* Paralelismo Analítico-Empírico: En una misma evaluación condicional (if/elif), se resuelve tanto la simulación física (datos) como el modelo matemático abstracto (valor_teorico), preparando todo para el cruce de variables.

### Bloque 3: Función `ejecutar_ley_grandes_numeros` (Parte 2 - Calculo vectorizado)
```python
# Calcular la evolución de la media muestral paso a paso
    trayectoria_medias = np.cumsum(datos) / np.arange(1, iteraciones_maximas + 1)
    
    return trayectoria_medias, valor_teorico
```
**¿Qué hace?** Toma el vector masivo de 10,000 datos aleatorios y calcula cómo evolucionó el promedio aritmético iteración por iteración (desde el primer dato simulado hasta el último), devolviendo la "ruta" o trayectoria completa de esa convergencia junto con el valor teórico ideal.

**Lógica y Puntos Clave:**
* Suma Acumulada Optimizada (np.cumsum): Computar un promedio en cada paso utilizando un bucle for tradicional implicaría una complejidad ineficiente ($O(n^2)$). NumPy ofrece np.cumsum(), que genera un nuevo vector donde cada posición contiene la suma
de todos los elementos anteriores en una sola pasada de memoria.
* Operaciones Indexadas Paralelas (np.arange): Se crea un arreglo secuencial de divisores: $[1, 2, 3, \dots, 10000]$. Al dividir el vector de sumas acumuladas entre este vector divisor de forma directa (operación element-wise), se obtiene la historia completa de las medias en fracción de milisegundos.

### Bloque 4: Función `ejecutar_teorema_limite_central`
```python
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
```
**¿Qué hace?** Maneja la demostración del Teorema del Límite Central. Extrae múltiples submuestras pequeñas (por defecto, 30 datos cada una) de forma repetitiva (por defecto, 1,000 veces). Calcula el promedio individual de cada submuestra y devuelve un arreglo final compuesto únicamente por esas medias.

**Lógica y Puntos Clave:** 
* Estandarización de Interfaz: Al igual que la función anterior, utiliza la conversión a minúsculas (dist_nombre = nombre_distribucion.lower()) y la búsqueda flexible de subcadenas para homologar el manejo de errores en toda la plataforma.
* Iteración Controlada: Utiliza un bucle for (ignorando el índice con el guion bajo _) para forzar la extracción independiente de nuevas muestras aleatorias en cada ciclo, imitando fielmente la naturaleza de un experimento repetitivo en campo.
* Colapso Estadístico (np.mean): La esencia del teorema radica en que no graficamos los datos crudos, sino sus promedios. La instrucción np.mean(muestra) colapsa los $n$ datos de la submuestra en un único estimador escalar, que es anexado a la lista medias_calculadas para demostrar cómo el agregado de eventos aleatorios tiende hacia la Campana de Gauss.

### Logica de `logica/Distribuciones.py`
El script `logica/distribuciones.py` opera bajo el paradigma de **Programación Orientada a Objetos (POO)**. Actúa como una capa intermedia o "controlador" que encapsula la lógica de validación matemática, genera las muestras individuales de datos y empaqueta los resultados en estructuras tabulares listas para ser renderizadas por la interfaz de usuario.

A continuación, se explica detalladamente cada fragmento de este código modular:

---

### Bloque 1: Importación de Dependencias
```python
import numpy as np
import scipy.stats as stats
import pandas as pd
```
**¿Qué hace?** Importa el tridente fundamental de la ciencia de datos en Python: NumPy para el cómputo matricial, SciPy para la extracción de métricas teóricas exactas, y Pandas para la manipulación y estructuración tabular de los resultados.

**Lógica y Puntos Clave:** 
* Integración con Pandas (pd): A diferencia del módulo de simulaciones masivas, este script se encarga de preparar la tabla comparativa ("Valor teórico" vs "Valor simulado"). Pandas proporciona el objeto DataFrame, que es la estructura de datos nativa que Streamlit utiliza internamente para dibujar tablas interactivas (st.dataframe).

### Bloque 2: Definición de la Clase y Constructor Inicial
```python
class SimuladorDistribuciones:
    def __init__(self, tamano_muestra):
        if tamano_muestra <= 0:
            raise ValueError("El tamaño de muestra debe ser un entero mayor que cero.")
        self.tamano_muestra = int(tamano_muestra)
```
**¿Qué hace?** Define la clase principal SimuladorDistribuciones. El método constructor __init__ se ejecuta automáticamente cada vez que se crea una nueva instancia de la clase, recibiendo y validando el tamaño de la muestra ($N$) con la que operarán todos los métodos subsecuentes.

**Lógica y Puntos Clave:** 
* Gestión de Estado mediante POO: Al guardar tamano_muestra como un atributo de la instancia (self.tamano_muestra), se evita tener que pasar este valor repetitivamente a cada una de las funciones de simulación (binomial, poisson, etc.), logrando un código más limpio y con menor redundancia (principio DRY - Don't Repeat Yourself).
* Validación de Integridad: La cláusula de guarda if tamano_muestra <= 0 protege al sistema desde el inicio. Impide matemáticamente que se instancie un simulador con un espacio muestral nulo o negativo, lo cual generaría errores fatales de división por cero o fallas de memoria en NumPy.

### Bloque 3:
```python
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
```
**¿Qué hace?** Es el núcleo procesador de resultados del script. Recibe el arreglo crudo de datos simulados y los momentos teóricos de SciPy. Calcula los estimadores estadísticos reales de la muestra generada, estructura una matriz comparativa usando Pandas y calcula la diferencia absoluta (error residual) entre la teoría y la práctica.

**Lógica y Puntos Clave:** 
* Encapsulamiento (_formatear_resultados): El guion bajo al inicio del nombre del método indica que es una función privada o interna. La interfaz de usuario (app.py) nunca debe llamar a esta función directamente; solo es utilizada por los otros métodos de la misma clase para evitar duplicar código.

* Grados de Libertad (ddof=1): Al calcular la varianza empírica, se introduce el parámetro ddof=1 (Delta Degrees of Freedom). Esto obliga a NumPy a dividir por $N-1$ en lugar de $N$, aplicando la Corrección de Bessel para obtener un estimador insesgado de la varianza poblacional, lo que es estadísticamente riguroso.

* Retorno de Diccionario Compuesto: Devuelve un diccionario estandarizado que contiene el vector de datos (para que la interfaz grafique), el tipo de distribución continua o discreta (para elegir entre un gráfico de barras o uno de densidad) y el DataFrame pre-calculado (para renderizar la tabla).

### Bloque 4: Métodos de Simulación Específicos (Ej. Binomial y Normal)
```python
def simular_binomial(self, ensayos_n, prob_p):
        if ensayos_n <= 0 or not isinstance(ensayos_n, int):
            raise ValueError("El número de ensayos 'n' debe ser un entero positivo.")
        if not (0 <= prob_p <= 1):
            raise ValueError("La probabilidad 'p' debe estar en el intervalo [0, 1].")
        
        datos = np.random.binomial(ensayos_n, prob_p, self.tamano_muestra)
        media_teorica, varianza_teorica = stats.binom.stats(ensayos_n, prob_p, moments='mv')
        return self._formatear_resultados(datos, float(media_teorica), float(varianza_teorica), "Discreta")

    # ... (El mismo patrón se repite para simular_poisson, simular_geometrica, etc.) ...
    
    def simular_normal(self, media_mu, desviacion_sigma):
        if desviacion_sigma <= 0:
            raise ValueError("La desviación estándar debe ser estrictamente positiva.")
        
        datos = np.random.normal(media_mu, desviacion_sigma, self.tamano_muestra)
        media_teorica, varianza_teorica = stats.norm.stats(loc=media_mu, scale=desviacion_sigma, moments='mv')
        return self._formatear_resultados(datos, float(media_teorica), float(varianza_teorica), "Continua")
```
**¿Qué hace?** Cada distribución matemática (Discreta o Continua) tiene su propio método público dedicado. Estos métodos validan los parámetros matemáticos estrictos de su modelo particular, instancian los valores aleatorios a través de numpy.random y solicitan a scipy.stats los valores teóricos correspondientes.

**Lógica y Puntos Clave:** 
* Validación de Dominio Matemático Estricto: Antes de ejecutar cualquier simulación, el código valida los axiomas de Kolmogorov. Por ejemplo, en simular_binomial, lanza una excepción si la probabilidad ($p$) es mayor a 1 o menor a 0. En simular_normal, exige que la dispersión ($\sigma$) sea estrictamente positiva. Esto previene comportamientos erráticos y el colapso de la aplicación.

* Cálculo de Momentos Multivariados (moments='mv'): El parámetro moments='mv' instruye a SciPy a devolver una tupla exacta con la Esperanza Matemática ($E[X]$ o 'm') y la Varianza ($Var(X)$ o 'v') teóricas, basadas en fórmulas algebraicas cerradas y no en simulaciones empíricas.

* Invocación del Formateador Central: Una vez obtenidos el vector simulado y los dos números teóricos exactos, se invoca a self._formatear_resultados(), delegándole todo el trabajo duro de construir el DataFrame de salida y calcular los errores residuales.

### Logica de `logica/app.py`
El script `app.py` es el punto de entrada principal (Entry Point) de la aplicación y actúa como el **Front-End** del simulador. Utiliza el framework Streamlit para orquestar la interacción del usuario, capturar los parámetros de entrada y renderizar dinámicamente las gráficas y tablas sin necesidad de recargar la página del navegador.

A continuación, se detalla la arquitectura visual y lógica de este archivo:

---

### Bloque 1: Configuración Global e Inyección de Estilos (UI/UX)

```python
import streamlit as st
# ... (otras importaciones) ...
import io

# Configuración global de colores
COLOR_PRIMARIO = "#F14AC8"
COLOR_SECUNDARIO = "#333333"
COLOR_FONDO = "#FFFFFF"

st.set_page_config(page_title="Simulador Estadistico", layout="wide")

# Inyeccion dinamica de CSS
estilos_css = f"""
    <style>
        /* ... configuraciones CSS personalizadas ... */
    </style>
"""
st.markdown(estilos_css, unsafe_allow_html=True)
```
**¿Qué hace?** Configura el entorno de la página web (definiendo un layout expandido o wide) e inyecta un bloque de código CSS personalizado para alterar la apariencia nativa de Streamlit, adaptándola a una paleta de colores institucional y moderna.

**Lógica y Puntos Clave:** 
* Renderizado unsafe_allow_html=True: Streamlit por defecto bloquea la ejecución de HTML/CSS directo por razones de seguridad (XSS). Activar esta bandera permite sobreescribir el DOM de la aplicación web, estilizando pestañas, botones y fondos para lograr un diseño pulido y profesional.

* Variables de Entorno Gráfico: Definir los colores como constantes en la cabecera (COLOR_PRIMARIO) permite que tanto el CSS de la web como las gráficas de Matplotlib utilicen exactamente la misma paleta cromática, generando cohesión visual.

### Bloque 2: Panel de Control Reactivo (Sidebar)
```python
st.sidebar.header("Configuracion General")
tamano_muestra = st.sidebar.number_input("Tamano de Muestra (N)", min_value=1, max_value=100000, value=1000)

distribucion_seleccionada = st.sidebar.selectbox("Seleccione Distribucion", opciones_distribucion)
parametros = {}

if distribucion_seleccionada == "Binomial":
    parametros['n'] = st.sidebar.number_input("Numero de ensayos (n)", min_value=1, value=10, step=1)
    parametros['p'] = st.sidebar.slider("Probabilidad de exito (p)", 0.0, 1.0, 0.5, 0.01)
# ... (elif para el resto de distribuciones con sus llaves unificadas) ...
```
**¿Qué hace?** Construye el menú de navegación lateral. Detecta qué distribución desea evaluar el usuario y, mediante una estructura condicional if/elif, despliega únicamente los controles numéricos (deslizadores o cajas de texto) pertinentes para ese modelo matemático.

**Lógica y Puntos Clave:** 
* Validación de Frontera (Front-End Validation): Al utilizar argumentos como min_value, max_value y step, el sistema impide que el usuario introduzca datos que rompan los axiomas matemáticos (como una desviación estándar de cero o una probabilidad de $1.5$). Esto protege al motor del Back-End de recibir excepciones fatales.

* Construcción del Contrato (Diccionario parametros): Este bloque empaqueta dinámicamente las entradas del usuario en un diccionario con llaves estrictas (como 'lambda', 'mu', 'a', 'b'), el cual es enviado a las funciones de simulación para garantizar la integridad de los datos.

### Bloque 3: Pestaña 1 - Simulación y Descarga en Memoria (Buffers)
```python
with pestana1:
    try:
        # ... (Invocación al SimuladorDistribuciones y renderizado de tablas) ...
        
        # Generación de exportables en memoria (CSV y PNG)
        buffer_csv = io.StringIO()
        pd.DataFrame(datos, columns=["Valores_Simulados"]).to_csv(buffer_csv, index=False)
        st.download_button(label="Exportar Datos (.CSV)", data=buffer_csv.getvalue(), ...)
        
        # ... (Renderizado de Gráficas de Matplotlib/Seaborn) ...
        
        buffer_img = io.BytesIO()
        figura.savefig(buffer_img, format='png', dpi=300, bbox_inches='tight')
        st.download_button(label="Guardar Grafica (.PNG)", data=buffer_img.getvalue(), ...)
        
    except ValueError as error_validacion:
        st.error(f"Error de validacion: {error_validacion}")
```
**¿Qué hace?** Ejecuta la simulación individual, grafica el histograma superpuesto con la curva analítica y permite al usuario descargar tanto el dataset generado como la gráfica en alta resolución.

**Lógica y Puntos Clave:**
* Buffers de Memoria Volátil (io.StringIO y io.BytesIO): En aplicaciones web desplegadas en contenedores (Docker), escribir y borrar archivos en el disco duro físico es ineficiente y puede generar errores de permisos. El código sortea este problema almacenando el archivo de texto CSV y la imagen PNG directamente en la memoria RAM (Buffers), entregándolos al navegador del usuario sin tocar el disco.

* Polimorfismo Gráfico: Mediante el condicional if resultado["tipo"] == "Discreta":, el Front-End decide si renderiza un gráfico de barras o escalones (eje.step) para variables discretas, o si utiliza estimación por densidad (sns.histplot con curvas) para variables continuas.

* Manejo de Excepciones: Todo el bloque está envuelto en un bloque try/except. Si el Back-End detecta una anomalía matemática, lanza un ValueError, el cual es capturado aquí y mostrado elegantemente en la interfaz gráfica usando st.error() sin detener la aplicación.

### Bloque 4: Pestañas de Teoremas Asintóticos (LGN y TLC)
```python
with pestana3:
    trayectoria_medias, valor_teorico = ejecutar_ley_grandes_numeros(distribucion_seleccionada, parametros)
    figura_lln, eje_lln = plt.subplots(figsize=(10, 4))
    eje_lln.plot(trayectoria_medias, color=COLOR_PRIMARIO)
    eje_lln.axhline(valor_teorico, color=COLOR_SECUNDARIO, linestyle='--')
    st.pyplot(figura_lln)

with pestana4:
    medias_tlc = ejecutar_teorema_limite_central(distribucion_seleccionada, parametros, total_simulaciones, tamano_muestra_individual)
    figura_tlc, eje_tlc = plt.subplots(figsize=(10, 4))
    sns.histplot(medias_tlc, kde=True, color=COLOR_PRIMARIO, stat="density", ax=eje_tlc)
    st.pyplot(figura_tlc)
```
**¿Qué hace?** Maneja la visualización interactiva de la Ley de los Grandes Números (LGN) y el Teorema del Límite Central (TLC), extrayendo los arreglos del Back-End y representándolos en lienzos bidimensionales.

**Lógica y Puntos Clave:**
* Desacoplamiento Total (Clean Code): Observa que dentro de estas pestañas no existe ni una sola operación matemática, sumatoria o bucle de iteración aleatoria. La capa visual se limita estrictamente a pedir datos a las funciones de simulaciones.py y dibujar (plt.plot / sns.histplot) lo que le entregan.

* Líneas de Anclaje Analítico (axhline): En la Ley de los Grandes Números, se traza una línea horizontal estática en el eje $Y$ equivalente al valor teórico ($E[X]$). Esto genera un anclaje visual dramático para que el usuario observe cómo la "serpiente" de la media empírica fluctúa al inicio pero se adhiere indisolublemente a la línea de control al llegar a $N=10,000$.

## 6. Uso del Software desarrollado
### Primeros pasos
### Dentro de la aplicacion
