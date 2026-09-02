Alcance del proyecto

El proyecto consiste en desarrollar un sistema para registrar, consultar y analizar mediciones de humedad correspondientes a distintos sectores de un campo. El sistema utilizará una matriz para almacenar los valores de humedad registrados para cada sector y cada mes del año.

El sistema permitirá registrar hasta un máximo de 50 sectores. Cada sector estará identificado mediante un ID único. En esta primera etapa, el único dato almacenado para identificar un sector será su ID.

Identificación de los sectores

Cada sector tendrá un ID único compuesto por:

Tres dígitos numéricos.
Un guion.
Tres letras correspondientes a una abreviación identificatoria.

Por ejemplo:

123-PAP

La abreviación deberá estar compuesta por exactamente tres letras y se almacenará en mayúsculas. El sistema validará que el ID cumpla con este formato y que no se encuentre registrado previamente.

El usuario podrá continuar registrando sectores mientras no se haya alcanzado el límite máximo de 50 sectores. Para finalizar la carga de sectores podrá ingresar -1.

En esta primera etapa no se almacenará información relacionada con el tipo de cultivo. La clasificación de humedad utilizará valores generales para todos los sectores. La incorporación del cultivo y de rangos específicos según cada tipo de plantación podrá considerarse en una etapa posterior.

Organización de las mediciones

Las mediciones de humedad se almacenarán en una matriz numérica donde:

Las filas representan los sectores del campo.
Las columnas representan los meses del año.
Cada posición de la matriz representa el porcentaje de humedad registrado para un determinado sector durante un determinado mes.

La relación será:

matriz[sector][mes] → porcentaje de humedad

Los meses del año serán representados mediante una tupla, conteniendo los doce meses:

("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

Para representar la ausencia de una medición se utilizará el valor -1, ya que el valor 0 representa una medición válida de humedad.

Por lo tanto:

-1 → sin medición.
0 a 100 → porcentaje de humedad registrado.

El sistema permitirá que existan sectores o meses sin mediciones. Las posiciones con valor -1 no serán consideradas para realizar cálculos.

Si no existen mediciones suficientes para realizar un determinado cálculo, el sistema informará que no hay datos disponibles y permitirá continuar utilizando el programa.

Carga y actualización de mediciones

El usuario podrá cargar o actualizar una medición indicando:

ID del sector.
Mes correspondiente.
Porcentaje de humedad.

El porcentaje de humedad deberá ser un valor numérico comprendido entre 0 % y 100 %.

Antes de registrar la medición, el sistema validará que:

El sector exista.
El mes seleccionado sea válido.
El porcentaje de humedad se encuentre entre 0 % y 100 %.
Los campos obligatorios no estén vacíos.

Si el sector y el mes seleccionados ya poseen una medición, el sistema permitirá reemplazar el valor anterior por el nuevo valor ingresado.

Si se intenta actualizar una medición que no existe, el sistema informará al usuario y permitirá continuar. En ese caso, la medición podrá registrarse como una nueva medición si corresponde a un sector y mes válidos.

Clasificación de la humedad

El sistema clasificará las mediciones según los siguientes rangos generales:

Porcentaje de humedad	Estado
0 % – 29 %	Crítico
30 % – 50 %	Bajo
51 % – 80 %	Adecuado
81 % – 100 %	Excesivo

A partir de esta clasificación, el sistema podrá determinar el estado de humedad de cada sector para un mes determinado.

Los sectores se considerarán de la siguiente manera:

Crítico: sector que necesita riego.
Bajo: sector que requiere atención.
Adecuado: sector en una situación normal.
Excesivo: posible exceso de agua.

Los estados crítico y bajo serán considerados sectores que requieren atención y aparecerán en los informes correspondientes.

El estado excesivo será mostrado como parte de la clasificación de humedad, pero no será considerado dentro de los sectores que requieren atención en esta primera etapa.

Procesamiento y análisis de los datos

El sistema permitirá realizar diferentes cálculos sobre las mediciones almacenadas.

Se podrá obtener:

Promedio de humedad de un sector, considerando todas las mediciones disponibles de dicho sector.
Promedio de humedad del campo para un mes determinado, considerando las mediciones disponibles de todos los sectores.
Promedio general de humedad del campo, considerando todas las mediciones registradas.
Mayor medición de humedad registrada.
Menor medición de humedad registrada.

En el caso de obtener la mayor o menor medición, el sistema informará:

Porcentaje de humedad.
Sector al que corresponde.
Mes en el que fue registrada.

Si existen varias mediciones que coinciden con el valor máximo o mínimo, el sistema contemplará todas las mediciones correspondientes e indicará cada sector y mes involucrado.

Cuando no existan mediciones para realizar alguno de estos cálculos, el sistema informará que no existen datos disponibles.

Además, para un mes seleccionado, el sistema podrá contabilizar cuántos sectores se encuentran en cada estado de humedad:

Cantidad de sectores en estado crítico.
Cantidad de sectores en estado bajo.
Cantidad de sectores en estado adecuado.
Cantidad de sectores en estado excesivo.

También se podrá generar un listado de los sectores que requieren atención. Este listado incluirá únicamente aquellos cuya humedad se encuentre en estado crítico o bajo durante el mes seleccionado.

Ranking de sectores

El sistema permitirá generar, para un mes determinado, un ranking de los sectores ordenados según su porcentaje de humedad, desde el menor hasta el mayor.

De esta manera:

Los primeros sectores del ranking serán los más secos.
Los últimos sectores serán los más húmedos.

El ranking se realizará únicamente considerando los sectores que tengan una medición registrada para el mes seleccionado, es decir, aquellos cuya posición correspondiente en la matriz sea diferente de -1.

Para realizar el ordenamiento se utilizará lambda como criterio de ordenamiento, tomando como referencia el porcentaje de humedad de cada sector.

También se utilizarán otras herramientas requeridas para el desarrollo del proyecto, como:

Comprensión de listas: para obtener sectores que cumplan determinadas condiciones, por ejemplo, sectores en estado crítico o bajo.
Slicing: para validar o separar partes del ID, como los tres dígitos y las tres letras de un ID con formato 123-PAP.

Estas herramientas serán utilizadas dentro de las funcionalidades existentes, sin necesidad de agregar nuevas funcionalidades al sistema.

Búsqueda y consulta de sectores

El usuario podrá buscar un sector mediante su ID.

La opción Buscar sector por ID tendrá como finalidad localizar un sector y verificar si se encuentra registrado en el sistema.

Si el ID existe, el sistema informará que el sector se encuentra registrado.

Si el ID no existe, el sistema informará al usuario y permitirá realizar una nueva búsqueda.

Por otra parte, la opción Consultar un sector permitirá consultar información más detallada del sector seleccionado, incluyendo sus mediciones registradas, el estado de humedad correspondiente y los cálculos que puedan realizarse con sus datos.

De esta manera, la búsqueda y la consulta tendrán finalidades diferentes y no representarán la misma funcionalidad.

Informes

El sistema contará con los siguientes informes:

Informe general del campo

Mostrará información general sobre el estado de los datos registrados, incluyendo:

Cantidad de sectores registrados.
Cantidad de mediciones cargadas.
Promedio general de humedad.
Mayor medición registrada, indicando sector y mes.
Menor medición registrada, indicando sector y mes.
Informe de un sector

Mostrará información correspondiente a un sector seleccionado, incluyendo:

ID del sector.
Mediciones registradas.
Meses que poseen mediciones.
Promedio de humedad del sector.
Estado de humedad de sus mediciones.
Informe mensual

Mostrará información correspondiente a un mes seleccionado, incluyendo:

Mediciones registradas de los sectores.
Promedio de humedad del campo para ese mes.
Estado de humedad de los sectores.
Informe de sectores que requieren atención

Mostrará los sectores que, durante un mes seleccionado, presenten un estado:

Crítico.
Bajo.

Los sectores con estado excesivo no serán incluidos en este informe, ya que en esta etapa serán considerados únicamente dentro de la clasificación general de humedad.

Ranking mensual de humedad

Mostrará los sectores que poseen una medición para el mes seleccionado, ordenados desde el menor hasta el mayor porcentaje de humedad.

Menú y validaciones

El sistema contará con un menú principal que permanecerá activo hasta que el usuario seleccione la opción de salida.

Desde el menú se podrá acceder a las distintas funcionalidades del sistema:

Gestión de sectores.
Gestión de mediciones.
Consultas.
Análisis de humedad.
Informes.
Salida del sistema.

Se realizarán validaciones para evitar que datos incorrectos provoquen la finalización del programa.

Entre ellas:

Validación de opciones del menú.
Validación de campos obligatorios.
Control de campos vacíos.
Validación del formato del ID.
Validación de tres dígitos, guion y tres letras en el ID.
Normalización de las letras del ID a mayúsculas.
Control de IDs repetidos.
Control de IDs inexistentes.
Validación de la cantidad máxima de 50 sectores.
Validación de meses.
Validación de valores numéricos.
Validación del porcentaje de humedad entre 0 % y 100 %.
Control de sectores sin mediciones.
Control de meses sin mediciones.
Control de actualización de mediciones inexistentes.

Ante cualquier dato inválido, el sistema mostrará un mensaje indicando el error y permitirá al usuario continuar utilizando el programa sin finalizar su ejecución.

Datos y estructuras utilizadas

La información del sistema será administrada mediante listas, matrices, tuplas y cadenas de caracteres, asignando cada estructura a la información que corresponda.

Las estructuras utilizadas serán:

Lista homogénea: almacenará los IDs de los sectores registrados.
Tupla: almacenará los doce meses del año.
Matriz numérica: almacenará los porcentajes de humedad de cada sector para cada mes. El valor -1 representará la ausencia de medición.
Cadenas de caracteres: se utilizarán para almacenar y manipular los IDs, mensajes del sistema y estados de humedad.
Variables numéricas: se utilizarán para porcentajes, promedios, cantidades, máximos y mínimos.

La matriz permitirá relacionar cada sector con sus mediciones mensuales y será la principal estructura utilizada para realizar los cálculos y análisis.

Fuera del alcance

Queda fuera del alcance del proyecto la utilización de:

Sensores físicos de humedad.
Dispositivos de riego automático.
Conexión con hardware.
Bases de datos.
Archivos o sistemas de persistencia de información.

Toda la información será almacenada únicamente en memoria durante la ejecución del programa. Al finalizar el programa, los datos se perderán.

La incorporación de cultivos y rangos de humedad específicos para cada tipo de cultivo también queda fuera del alcance de esta primera etapa y podrá ser considerada para una segunda etapa del proyecto.

## MENÚ PRINCIPAL — SISTEMA DE CONTROL DE HUMEDAD
### 1. GESTIÓN DE SECTORES
    Dar de alta un sector
    Buscar sector por ID
    Mostrar todos los sectores
    Volver al menú principal
### 2. GESTIÓN DE MEDICIONES
    Cargar / actualizar medición
    Consultar medición de un sector
    Volver al menú principal
### 3. CONSULTAS
    Consultar un sector
    Consultar mediciones de un mes
    Consultar estado de humedad de un sector
    Volver al menú principal
### 4. ANÁLISIS DE HUMEDAD
    Calcular promedio de un sector
    Calcular promedio de un mes
    Calcular promedio general del campo
    Obtener mayor medición registrada
    Obtener menor medición registrada
    Contabilizar sectores según estado de humedad
    Mostrar sectores que requieren atención
    Volver al menú principal
### 5. INFORMES
    Informe general del campo
    Informe de un sector
    Informe mensual
    Informe de sectores que requieren atención
    Ranking mensual de humedad
    Volver al menú principal
### 6. SALIR
    Confirmar salida
    Volver al menú principal