## Alcance del proyecto

El proyecto consiste en desarrollar un sistema para registrar, consultar y analizar mediciones de humedad realizadas en distintos sectores de un campo. 

El sistema permitirá registrar los diferentes sectores del campo y almacenar las mediciones de humedad correspondientes a cada uno. También permitirá buscar un sector específico y consultar las mediciones registradas por meses.

A partir de los datos ingresados, el sistema realizará diferentes cálculos y análisis, como obtener valores máximos, mínimos y promedios de humedad (promedios de un sector en especifico, promedios de una matriz entera, o promedios de un mes). Además, permitirá determinar mediante condiciones si un sector presenta un nivel de humedad que requiera atención. Y la cantidad de sectores que tengan distintos % de humedad.

El sistema contará con un menú principal desde el cual se podrá acceder a las distintas funcionalidades, controlando las entradas incorrectas para evitar que el programa finalice ante datos inválidos.

Las matrices tendran en las filas los sectores de campo y las columnas los meses, todo esto con la variacion de humedad. Siendo de 0% – 29%: Crítico → necesita riego. 30% – 50%: Bajo → requiere atención. 51% – 80%: Adecuado → humedad normal. 81% – 100%: Excesivo → posible exceso de agua. Todo esto dependiendo del tipi de cultivo que se utilice en el sector.

Tambien habra un ranking de los sectores mas secos y los mas humedos por mes VER

Se podra buscar distintos sectores por ID (validando todo)

Queda fuera del alcance la utilización de sensores físicos, dispositivos de riego automático o conexión con hardware. El sistema trabajará únicamente con las mediciones ingresadas por el usuario.


IDEAS: Tengo campos en distintas provincias. (ver mas de una matriz)