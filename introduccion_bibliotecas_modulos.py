# Importar una biblioteca completa:
import math
resultado = math.sqrt(16)
'''En este ejemplo, importamos la biblioteca math completa y utilizamos la
función sqrt() para calcular la raíz cuadrada de 16.'''

# Importar una biblioteca completa:
from math import sqrt
resultado = sqrt(16)
'''En este caso, importamos únicamente la función sqrt() del módulo
math. No es necesario utilizar el nombre de la biblioteca antes de la
función.'''

# Importar una biblioteca completa:
import pandas as pd # type: ignore
dataframe = pd.DataFrame()
'''En este ejemplo, importamos la biblioteca pandas y le asignamos el alias
pd. Luego, podemos utilizar pd en lugar del nombre completo de la
biblioteca para acceder a sus funcionalidades.'''