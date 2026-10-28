# Plantilla de protocolo — Experimento de ubicación de producto

**Equipo:** ___ · **Integrantes:** ___ · **Fecha:** 27/10/2026

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

## 1. Pregunta e hipótesis

*Hipótesis que el experimento pueda confirmar o refutar (formúlela como una comparación medible entre los grupos).*

## 2. Unidad experimental
Semana - Tienda: (# de tiendas asociadas al experimento y # de semanas)

*¿Qué recibe el tratamiento? ¿Cuántas unidades se incluyen?*

- Unidad:
- Número de unidades y justificación:

## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada): Ubicacion
- **Niveles** (valores del factor): Pasillo y habitual
- **Tratamiento** (combinación asignada): pasillo durante una semana y ubicacvion habitual durante otra (grupo de control)

## 4. Grupo de control

*¿Cuál es la referencia sin tratamiento y qué rol cumple?*
La misma tienda pero con el producto puesto en la ubicacion habitual
## 5. Aleatorización

*¿Cómo se asignan las unidades a los grupos? ¿Por qué es necesaria?*
Seria por sorteo para poder asignar. (ej de las 40 unidades las partimos a la mitad)
Sorteo de 20 tiendas a cada grupo (paralelo)
- **Línea de código de la asignación (Python o R):** escribe el comando que asigna al azar tus N unidades a los dos grupos (tratamiento y control) y ejecútalo con semilla. Incluye el resultado de una corrida y explica por qué el sorteo reparte los factores desconocidos entre los grupos.

## 6. Respuesta y medición

- Variable respuesta: Ventas semanales en USD
- Período de medición: 4 semanas
- Quién registra y cómo (¿ciego?): Mediante el punto de venta PDS, ciego (vendedor no sabe si el producto esta en principal o habitual)

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. | Clima|
| 2. | Evento local|
| 3. | Surtido/Stock|
| 4. | Cambios en el personal|

## 8. Limitaciones del diseño

*¿Qué podría invalidar el experimento si no se controla? ¿Qué no se podrá concluir?*

* Perdida de potencia pro promociones
* Canibalizacion de las tiendas
*  

## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

- ¿Qué grupo muestra mayor venta promedio en la plantilla?
El pasillo muestra mayor venta (1335 USD) frente al habitual (1049 USD)
- ¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?
Por que no hay ninguna asignacion real aleatoria, los datos son muy pocos, no tenemos control de temporada, ni promociones en el grupo pasillo y no hay medida de variabilidad
- Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?

