# Alcance del proyecto

El proyecto consiste en desarrollar un sistema para registrar, consultar y analizar mediciones de humedad de distintos sectores de un campo, utilizando una matriz para almacenar los valores correspondientes a cada sector y mes.

El sistema permitirá registrar sectores del campo. Cada sector estará identificado mediante un ID único, compuesto por tres dígitos numéricos y una abreviación que permita identificarlo. Por ejemplo: 123-PAP. El sistema tendrá una cantidad máxima de sectores definida, y cada ID deberá ser único.

Por el momento, el tipo de cultivo no formará parte del sistema, ya que la clasificación de humedad utilizará valores generales. La incorporación del cultivo y de rangos específicos según cada tipo de plantación podrá considerarse en una etapa posterior.

Organización de las mediciones

Las mediciones de humedad se almacenarán en una matriz donde:

Las filas representan los sectores del campo.
Las columnas representan los meses del año.
Cada posición de la matriz representa el porcentaje de humedad registrado para un determinado sector durante un determinado mes.

Por ejemplo:

matriz[sector][mes] → porcentaje de humedad

El usuario podrá cargar las mediciones correspondientes a los meses del año. Si un sector todavía no posee una medición para determinado mes, dicha posición se considerará sin medición y no será utilizada para realizar los cálculos correspondientes.

El sistema permitirá que existan meses sin mediciones. En estos casos, los cálculos se realizarán únicamente sobre los datos disponibles. Si no existen mediciones suficientes para realizar un determinado cálculo, el sistema informará que no hay datos disponibles.

Carga y actualización de mediciones

El usuario podrá ingresar una medición indicando:

ID del sector.
Mes correspondiente.
Porcentaje de humedad.

El porcentaje de humedad deberá ser un valor numérico comprendido entre 0 % y 100 %.

Si ya existe una medición para el sector y mes seleccionados, el sistema permitirá reemplazar el valor anterior por el nuevo valor ingresado.

También se validará que el sector exista y que el mes seleccionado sea válido.

Clasificación de la humedad

El sistema clasificará las mediciones según los siguientes rangos generales:

Porcentaje de humedad	Estado
0 % – 29 %	Crítico
30 % – 50 %	Bajo
51 % – 80 %	Adecuado
81 % – 100 %	Excesivo

A partir de esta clasificación, el sistema podrá determinar el estado de humedad de cada sector para un mes determinado.

Los sectores con humedad crítica serán considerados sectores que necesitan riego, mientras que los sectores con humedad baja requerirán atención. Los sectores con humedad adecuada se encontrarán en una situación normal y los sectores con humedad excesiva serán identificados como posibles casos de exceso de agua.

Procesamiento y análisis de los datos

El sistema permitirá realizar diferentes cálculos sobre las mediciones almacenadas.

Se podrá obtener:

Promedio de humedad de un sector, considerando todas las mediciones disponibles de ese sector.
Promedio de humedad del campo para un mes determinado, considerando las mediciones disponibles de todos los sectores.
Promedio general de humedad del campo, considerando todas las mediciones registradas.
Mayor medición de humedad registrada.
Menor medición de humedad registrada.

Cuando no existan mediciones para realizar alguno de estos cálculos, el sistema informará que no existen datos disponibles.

Además, para un mes seleccionado, el sistema podrá contabilizar cuántos sectores se encuentran en cada estado de humedad:

Cantidad de sectores en estado crítico.
Cantidad de sectores en estado bajo.
Cantidad de sectores en estado adecuado.
Cantidad de sectores en estado excesivo.

También se podrá generar un informe de los sectores que requieren atención, identificando aquellos cuya humedad se encuentre en estado crítico o bajo durante el mes seleccionado.

Ranking de sectores

El sistema permitirá generar, para un mes determinado, un ranking de los sectores ordenados según su porcentaje de humedad, desde el menor hasta el mayor.

De esta manera, los primeros sectores del ranking serán los más secos y los últimos serán los más húmedos.

El ranking se realizará únicamente considerando los sectores que tengan una medición registrada para el mes seleccionado.

Búsqueda de sectores

El usuario podrá buscar un sector mediante su ID.

Si el ID existe, el sistema mostrará la información correspondiente al sector, incluyendo sus mediciones registradas y los cálculos que puedan realizarse con ellas.

Si el ID no existe, el sistema informará al usuario y permitirá realizar una nueva búsqueda.

Informes

El sistema contará con al menos los siguientes informes:

Informe general del campo: mostrará información general sobre las mediciones registradas y los valores calculados.
Informe de un sector: mostrará las mediciones y el promedio correspondiente a un sector seleccionado.
Informe mensual: mostrará las mediciones y el promedio de humedad del campo para un mes determinado.
Informe de sectores que requieren atención: mostrará los sectores que se encuentren en estado crítico o bajo durante un mes seleccionado.
Ranking mensual de humedad: mostrará los sectores ordenados desde el menor hasta el mayor porcentaje de humedad.
Menú y validaciones

El sistema contará con un menú principal que permanecerá activo hasta que el usuario seleccione la opción de salida.

Desde el menú se podrá acceder a las distintas funcionalidades del sistema, como carga, actualización, búsqueda, cálculos, clasificación, generación de informes y ranking.

Se realizarán validaciones para evitar que datos incorrectos provoquen la finalización del programa. Entre ellas:

Validación de opciones del menú.
Validación del formato del ID.
Control de IDs repetidos.
Control de IDs inexistentes.
Validación de meses.
Validación de valores numéricos.
Validación del porcentaje de humedad entre 0 % y 100 %.
Control de sectores sin mediciones.
Control de meses sin mediciones.
Datos y estructuras utilizadas

La información del sistema será administrada mediante listas, matrices, tuplas y cadenas de caracteres, de acuerdo con las necesidades de cada funcionalidad.

La matriz será utilizada principalmente para relacionar sectores, meses y porcentajes de humedad, mientras que las demás estructuras permitirán almacenar y organizar información necesaria para las búsquedas, cálculos e informes.

Fuera del alcance

Queda fuera del alcance del proyecto la utilización de:

Sensores físicos de humedad.
Dispositivos de riego automático.
Conexión con hardware.
Bases de datos.
Archivos o sistemas de persistencia de información.

Toda la información será almacenada únicamente en memoria durante la ejecución del programa. Al finalizar el programa, los datos se perderán.

La incorporación de cultivos y rangos de humedad específicos para cada tipo de cultivo también queda fuera del alcance de esta primera etapa y podrá ser considerada para una segunda etapa del proyecto.

## MENÚ PRINCIPAL - SISTEMA DE CONTROL DE HUMEDAD

### 1. GESTIÓN DE SECTORES

1. Dar de alta un sector
2. Buscar sector por ID
3. Mostrar todos los sectores
4. Volver al menú principal


### 2. GESTIÓN DE MEDICIONES

1. Cargar/actualizar medición
2. Consultar medición de un sector
3. Volver al menú principal


### 3. CONSULTAS

1. Consultar un sector
2. Consultar mediciones de un mes
3. Consultar estado de humedad de un sector
4. Volver al menú principal


### 4. ANÁLISIS DE HUMEDAD

1. Calcular promedio de un sector
2. Calcular promedio de un mes
3. Calcular promedio general del campo
4. Obtener mayor medición registrada
5. Obtener menor medición registrada
6. Contabilizar sectores según estado de humedad
7. Mostrar sectores que requieren atención
8. Volver al menú principal


### 5. INFORMES

1. Informe general del campo
2. Informe de un sector
3. Informe mensual
4. Informe de sectores que requieren atención
5. Ranking mensual de humedad
6. Volver al menú principal


### 6. SALIR

1. Confirmar salida
2. Volver al menú principal