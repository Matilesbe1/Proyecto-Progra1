
# Alcance del proyecto

El proyecto consiste en desarrollar un sistema para registrar, consultar y analizar mediciones de humedad correspondientes a distintos sectores de un campo, cada uno con un cultivo asignado. El sistema utilizará una matriz para almacenar los valores de humedad registrados para cada sector y cada mes del año. Los datos (usuarios, sectores con sus mediciones y rangos de humedad por cultivo) se almacenarán en archivos CSV. El acceso al sistema estará protegido mediante usuario y contraseña, validados contra el archivo de usuarios.
El sistema permitirá registrar hasta un máximo de 50 sectores. Cada sector estará identificado mediante un ID único y tendrá asociado un cultivo.
Acceso al sistema (login)
Al iniciar el programa, el usuario deberá ingresar su usuario y contraseña.
Los usuarios se almacenarán en el archivo usuarios.csv con los siguientes datos: usuario, contraseña (almacenada como hash, nunca en texto plano) y nombre completo.
El usuario deberá cumplir un formato validado con expresiones regulares: entre 4 y 15 caracteres, solo letras, números y guion bajo.
La contraseña deberá cumplir un formato validado con expresiones regulares: mínimo 6 caracteres, con al menos una letra y un número.
El usuario tendrá un máximo de 3 intentos. Si los agota, el programa finalizará.
Si el archivo de usuarios no existe, el sistema lo creará con un usuario inicial.
Todos los usuarios que inicien sesión tendrán acceso a las mismas funcionalidades. No existen roles ni permisos diferenciados.
Identificación de los sectores
Cada sector tendrá un ID único compuesto por:
Tres dígitos numéricos.
Un guion.
Tres letras correspondientes a una abreviación identificatoria.
Por ejemplo: 123-PAP
El ID se validará mediante una expresión regular (\d{3}-[A-Za-z]{3}). La abreviación deberá estar compuesta por exactamente tres letras y se almacenará en mayúsculas. El sistema validará que el ID cumpla con este formato y que no se encuentre registrado previamente.
Además del ID, cada sector tendrá asociado un cultivo, que deberá ser uno de los definidos en el archivo de rangos: soja, trigo, papa, zanahoria y batata.
El usuario podrá continuar registrando sectores mientras no se haya alcanzado el límite máximo de 50 sectores. Para finalizar la carga de sectores podrá ingresar -1.
Organización de las mediciones
Las mediciones de humedad se almacenarán en una matriz numérica donde:
Las filas representan los sectores del campo.
Las columnas representan los meses del año.
Cada posición de la matriz representa el porcentaje de humedad registrado para un determinado sector durante un determinado mes.
La relación será:
matriz[sector][mes] → porcentaje de humedad
Los meses del año serán representados mediante una lista de tuplas, conteniendo los doce meses en número y en tipo string:
[(1,"Ene"), (2,"Feb"), (3,"Mar"), (4,"Abr"), (5,"May"), (6,"Jun"), (7,"Jul"), (8,"Ago"), (9,"Sep"), (10,"Oct"), (11,"Nov"), (12,"Dic")]
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
El porcentaje de humedad deberá ser un valor numérico entero comprendido entre 0 % y 100 %, validado previamente con una expresión regular.
Antes de registrar la medición, el sistema validará que:
El sector exista.
El mes seleccionado sea válido.
El porcentaje de humedad se encuentre entre 0 % y 100 %.
Los campos obligatorios no estén vacíos.
Si el sector y el mes seleccionados ya poseen una medición, el sistema permitirá reemplazar el valor anterior por el nuevo valor ingresado.
Si se intenta actualizar una medición que no existe, el sistema informará al usuario y permitirá continuar. En ese caso, la medición podrá registrarse como una nueva medición si corresponde a un sector y mes válidos.
Clasificación de la humedad según el cultivo
Los rangos de humedad dependerán del cultivo de cada sector. Se almacenarán en el archivo rangos.csv y se cargarán al iniciar el programa en un diccionario donde la clave es el cultivo y el valor es otro diccionario con los rangos de cada estado:


RANGOS_CULTIVO = {
    "Soja":      {"Crítico": (0, 34), "Bajo": (35, 54), "Adecuado": (55, 80), "Excesivo": (81, 100)},
    "Trigo":     {"Crítico": (0, 24), "Bajo": (25, 44), "Adecuado": (45, 70), "Excesivo": (71, 100)},
    "Papa":      {"Crítico": (0, 34), "Bajo": (35, 59), "Adecuado": (60, 85), "Excesivo": (86, 100)},
    "Zanahoria": {"Crítico": (0, 39), "Bajo": (40, 59), "Adecuado": (60, 80), "Excesivo": (81, 100)},
    "Batata":    {"Crítico": (0, 29), "Bajo": (30, 49), "Adecuado": (50, 75), "Excesivo": (76, 100)},
}

Si el archivo rangos.csv no existe, el sistema lo creará con estos valores iniciales. Los rangos se modifican editando el archivo por fuera del programa. Se validará al cargarlo que los rangos de cada cultivo cubran de 0 a 100 sin superposiciones ni huecos.

A partir de esta clasificación, el sistema determinará el estado de humedad de cada sector para un mes determinado, usando los rangos del cultivo asignado a ese sector.

Los sectores se considerarán de la siguiente manera:

Crítico: sector que necesita riego.
Bajo: sector que requiere atención.
Adecuado: sector en una situación normal.
Excesivo: posible exceso de agua.

Los estados crítico y bajo serán considerados sectores que requieren atención y aparecerán en los informes correspondientes.

El estado excesivo será mostrado como parte de la clasificación de humedad, pero no será considerado dentro de los sectores que requieren atención en esta etapa.

Procesamiento y análisis de los datos

El sistema permitirá realizar diferentes cálculos sobre las mediciones almacenadas.

Se podrá obtener:

Promedio de humedad de un sector, considerando todas las mediciones disponibles de dicho sector.
Promedio de humedad del campo para un mes determinado, considerando las mediciones disponibles de todos los sectores.
Promedio general de humedad del campo, considerando todas las mediciones registradas.
Mayor medición de humedad registrada.
Menor medición de humedad registrada.

Criterio unificado para mayor y menor medición: en todas las funcionalidades del sistema (análisis de humedad e informe general) se informará una única medición para la mayor y una única medición para la menor, sin mostrar empates. Si existen varias mediciones que coinciden con el valor máximo o mínimo, se informará únicamente la primera encontrada, recorriendo los sectores en el orden en que fueron registrados y los meses de enero a diciembre. Para cada una se informará:

Porcentaje de humedad.
Sector al que corresponde.
Mes en el que fue registrada.

Cuando no existan mediciones para realizar alguno de estos cálculos, el sistema informará que no existen datos disponibles.

Además, para un mes seleccionado, el sistema podrá contabilizar cuántos sectores se encuentran en cada estado de humedad, utilizando un diccionario como acumulador:

Cantidad de sectores en estado crítico.
Cantidad de sectores en estado bajo.
Cantidad de sectores en estado adecuado.
Cantidad de sectores en estado excesivo.

También se podrá generar un listado de los sectores que requieren atención. Este listado incluirá únicamente aquellos cuya humedad se encuentre en estado crítico o bajo durante el mes seleccionado, indicando el cultivo de cada sector.

Ranking de sectores

El sistema permitirá generar, para un mes determinado, un ranking de los sectores ordenados según su porcentaje de humedad, desde el menor hasta el mayor.

De esta manera:

Los primeros sectores del ranking serán los más secos.
Los últimos sectores serán los más húmedos.

El ranking se realizará únicamente considerando los sectores que tengan una medición registrada para el mes seleccionado, es decir, aquellos cuya posición correspondiente en la matriz sea diferente de -1.

Para realizar el ordenamiento se utilizará lambda como criterio de ordenamiento, tomando como referencia el porcentaje de humedad de cada sector.

También se utilizarán otras herramientas requeridas para el desarrollo del proyecto, como:

Comprensión de listas: para obtener sectores que cumplan determinadas condiciones, por ejemplo, sectores en estado crítico o bajo.
Expresiones regulares: para validar el formato del ID de los sectores, el usuario, la contraseña y el porcentaje de humedad.

Estas herramientas serán utilizadas dentro de las funcionalidades existentes, sin necesidad de agregar nuevas funcionalidades al sistema.

Búsqueda y consulta de sectores

El usuario podrá buscar un sector mediante su ID.

La opción “Buscar sector por ID” tendrá como finalidad localizar un sector y verificar si se encuentra registrado en el sistema.

Si el ID existe, el sistema informará que el sector se encuentra registrado.

Si el ID no existe, el sistema informará al usuario y permitirá realizar una nueva búsqueda.

Por otra parte, la opción “Consultar un sector” permitirá consultar información más detallada del sector seleccionado, incluyendo su cultivo, sus mediciones registradas, el estado de humedad correspondiente y los cálculos que puedan realizarse con sus datos.

De esta manera, la búsqueda y la consulta tendrán finalidades diferentes y no representarán la misma funcionalidad.

Informes

El sistema contará con los siguientes informes:

Informe general del campo

Mostrará información general sobre el estado de los datos registrados, incluyendo:

Cantidad de sectores registrados.
Cantidad de mediciones cargadas.
Promedio general de humedad.
Mayor medición registrada, indicando sector y mes (una sola, según el criterio unificado).
Menor medición registrada, indicando sector y mes (una sola, según el criterio unificado).
Informe de un sector

Mostrará información correspondiente a un sector seleccionado, incluyendo:

ID del sector.
Cultivo del sector.
Mediciones registradas.
Meses que poseen mediciones.
Promedio de humedad del sector.
Estado de humedad de sus mediciones, según los rangos de su cultivo.
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

Antes de acceder al menú, el usuario deberá iniciar sesión. El sistema contará con un menú principal que permanecerá activo hasta que el usuario seleccione la opción de salida.

Desde el menú se podrá acceder a las distintas funcionalidades del sistema:

Gestión de sectores.
Gestión de mediciones.
Consultas.
Análisis de humedad.
Informes.
Salida del sistema.

Se realizarán validaciones para evitar que datos incorrectos provoquen la finalización del programa.

Ante cualquier dato inválido, el sistema mostrará un mensaje indicando el error y permitirá al usuario continuar utilizando el programa sin finalizar su ejecución.

Manejo de excepciones

El sistema utilizará únicamente dos excepciones estándar de Python:

ValueError: se utilizará ante cualquier dato inválido, ya sea ingresado por el usuario o leído desde un archivo. Incluye: ID con formato incorrecto, sector duplicado o inexistente, límite de sectores alcanzado, cultivo inválido, mes inválido, porcentaje vacío, no numérico o fuera de 0–100, credenciales incorrectas, y filas de los CSV con datos inválidos (la fila se ignora y se informa). Cada caso se diferencia por el mensaje que se muestra al usuario.
OSError: se utilizará ante cualquier problema con los archivos CSV. Incluye los casos de archivo inexistente (FileNotFoundError) y falta de permisos (PermissionError), que son subclases de OSError. Si falta usuarios.csv o rangos.csv, se crean con valores iniciales. Si falta mediciones.csv, el sistema inicia sin sectores. Ante un error de escritura, se informa al usuario.

Todos los errores se informarán con un mensaje claro y el programa continuará en funcionamiento, salvo el agotamiento de los 3 intentos de login.

Datos y estructuras utilizadas

La información del sistema será administrada mediante listas, matrices, tuplas, diccionarios y cadenas de caracteres, asignando cada estructura a la información que corresponda.

La matriz permitirá relacionar cada sector con sus mediciones mensuales y será la principal estructura utilizada para realizar los cálculos y análisis.

Archivos utilizados

El sistema utilizará tres archivos CSV, leídos y escritos con el módulo csv:

Archivo	Columnas	Contenido
usuarios.csv	usuario, clave_hash, nombre	Usuarios habilitados. 
rangos.csv	cultivo, estado, minimo, maximo	Rangos de humedad de cada cultivo (una fila por cultivo y estado).
mediciones.csv	id, cultivo, Ene, Feb, ..., Dic	Una fila por sector, con su cultivo y las 12 mediciones (-1 si no hay medición).

Momento de lectura y escritura:

Al iniciar el programa se leen usuarios.csv y rangos.csv para el login y la clasificación, y mediciones.csv para recuperar los sectores y mediciones guardados.
Al confirmar la salida del sistema, se guardan automáticamente los sectores y mediciones en mediciones.csv.
usuarios.csv y rangos.csv son de solo lectura para el programa.
Fuera del alcance

Queda fuera del alcance del proyecto la utilización de:

Sensores físicos de humedad.
Dispositivos de riego automático.
Conexión con hardware.
Bases de datos.
Roles y permisos diferenciados entre usuarios.
Alta, baja o modificación de usuarios y de rangos de cultivo desde el sistema (ambos archivos se administran por fuera del programa).
Excepciones propias del sistema.
Archivos JSON


## Menú principal — Sistema de Control de Humedad
Inicio de sesión (previo al menú)
Ingreso de usuario y contraseña (3 intentos).
### 1. Gestión de sectores
Dar de alta un sector (ID y cultivo).
Buscar sector por ID.
Mostrar todos los sectores.
Volver al menú principal.
### 2. Gestión de mediciones
Cargar / actualizar medición.
Volver al menú principal.
### 3. Consultas
Consultar un sector.
Consultar mediciones de un mes.
Consultar estado de humedad de un sector.
Volver al menú principal.
### 4. Análisis de humedad
Calcular promedio de un sector.
Calcular promedio de un mes.
Calcular promedio general del campo.
Obtener mayor medición registrada.
Obtener menor medición registrada.
Contabilizar sectores según estado de humedad.
Mostrar sectores que requieren atención.
Volver al menú principal.
### 5. Informes
Informe general del campo.
Informe de un sector.
Informe mensual.
Informe de sectores que requieren atención.
Ranking mensual de humedad.
Volver al menú principal.
### 6. Salir
Confirmar salida (guarda las mediciones en mediciones.csv).
Volver al menú principal.





# VER (correccion de la profe)
 
Validación del porcentaje: no hace falta usar expresión regular para validar humedad 0–100. Conviene convertir a entero, controlar ValueError y luego validar el rango.  
 
CSV → estructuras: falta indicar claramente que al leer mediciones.csv se reconstruyen la lista de IDs, la lista de cultivos y la matriz de mediciones.