# 📊 Análisis del Impacto del Pre-procesamiento por Ventanas de Tiempo en HAR

Este repositorio contiene el código, experimentos y resultados desarrollados para mi **tesis de grado**, cuyo objetivo es analizar cómo los parámetros de **ventanas de tiempo (window size)** y **porcentaje de solapamiento (overlapping)** influyen en la precisión de modelos de *Machine Learning* aplicados al **Reconocimiento de Actividades Humanas (HAR)**.

---

## Contexto

El reconocimiento de actividades humanas (HAR) ha incrementado su relevancia en múltiples disciplinas (salud, IoT, deporte, smart cities). Sin embargo, una etapa crítica —y muchas veces poco cuestionada— es el **pre-procesamiento de datos mediante ventanas de tiempo**, utilizado para representar actividades dinámicas.

Este trabajo estudia si distintas configuraciones de:

* **Tamaño de ventana**
* **Porcentaje de solapamiento**

tienen un impacto real y estadísticamente significativo sobre:

* La **precisión del modelo**
* El **rendimiento computacional**
* La **calidad final del entrenamiento**

Spoiler: **sí, importa… y bastante**.

---

## Objetivo

Evaluar la repercusión de distintas configuraciones de ventanas de tiempo sobre la precisión de modelos HAR entrenados con **Random Forest**, identificando configuraciones óptimas y estadísticamente significativas.

---

## Dataset

Se utiliza el **MHEALTH Dataset**, seleccionado por:

* Alta confiabilidad en investigaciones previas
* Información de **12 actividades humanas**
* Registros de **3 dispositivos** ubicados en distintas partes del cuerpo
* Volumen de datos suficiente para análisis estadístico

---

## Metodología

### 1. Pre-procesamiento

* Segmentación de datos usando múltiples combinaciones de:

  * Window Size
  * Overlapping (%)
* Generación de conjuntos de entrenamiento por configuración

### 2. Modelado

* Algoritmo: **Random Forest**
* Seleccionado por su alto desempeño en problemas HAR

### 3. Evaluación

Se obtienen métricas de precisión para cada configuración y se analizan mediante:

#### Análisis estadístico

* ANOVA (con submuestreo)
* Prueba t de Student (muestras independientes)
* Pruebas de homocedasticidad
* Kruskal-Wallis
* Mann-Whitney

#### Pruebas de normalidad

* Anderson-Darling
* Kolmogorov-Smirnov
* Jarque-Bera

El objetivo es identificar **diferencias significativas** entre configuraciones y validar la influencia real del pre-procesamiento.

---

## Resultados esperados

* Evidenciar el impacto del window size y overlapping sobre la precisión
* Identificar configuraciones óptimas de ventanas de tiempo
* Demostrar que el pre-procesamiento **no es un detalle menor**
* Aportar criterios técnicos para futuros modelos HAR

---

## Tecnologías utilizadas

* Python
* Scikit-learn
* Pandas / NumPy
* SciPy / Statsmodels
* Random Forest

---

## 👤 Autor

**Nathan Hidalgo**
Bachiller en Ingeniería Industrial y de Sistemas
Intereses: Data Science, Machine Learning, HAR, IoT
