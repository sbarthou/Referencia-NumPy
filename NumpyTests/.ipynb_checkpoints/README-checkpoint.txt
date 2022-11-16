np.array(lista) : Crea un array a partir de la lista o tupla lista.
np.empty(dimensiones) : Crea y devuelve una referencia a un array vacío con las dimensiones especificadas en la tupla dimensiones.
np.zeros(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos ceros.
np.ones(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos unos.
np.full(dimensiones, valor) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos valor.
np.identity(n) : Crea y devuelve una referencia a la matriz identidad de dimensión n.
np.arange(inicio, fin, salto) : Crea y devuelve una referencia a un array de una dimensión cuyos elementos son la secuencia desde inicio hasta fin tomando valores cada salto.
np.linspace(inicio, fin, n) : Crea y devuelve una referencia a un array de una dimensión cuyos elementos son la secuencia de n valores equidistantes desde inicio hasta fin.
np.random.random(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son aleatorios.
np.random.randint(low, high, size) : Crea y devuelve un arreglo con valores aleatorios entre low y high de size elementos.
random.randrange(low, high) : retorna un numero random entre low y high.


a.ndi : Devuelve el número de dimensiones del array a.
a.shape : Devuelve una tupla con las dimensiones del array a.
a.size : Devuelve el número de elementos del array a.
a.dtype : Devuelve el tipo de datos de los elementos del array a.
np.diag(a, k=n) : Devuelve la diagonal del array a partiendo de la columna n.
np.append(arr, value) : Agrega un valor value al final del array arr.


a[condicion] : Devuelve una lista con los elementos del array a que cumplen la condición condicion.
a*num, a+num, etc : Los operadores mamemáticos +, -, *, /, %, ** se utilizan para la realizar suma, resta, producto, cociente, resto y potencia a nivel de elemento.
matriz[i,:]*num: retorna un arreglo correspondiente a la i-ésima fila multiplicada por num.
matriz[:,i]*num: retorna un arreglo correspondiente a la i-ésima columna multiplicada por num.
np.min(): retorna el valor mínimo de un arreglo.
matriz[i,:].min(): retorna el valor mínimo de la i-ésima fila.
matriz[:,i].min(): retorna el valor mínimo de la i-ésima columna.
a.round(decimales): retorna un arreglo con todos los elementos redondeados a la cantidad de decimales pasados.
np.sum(): retorna la suma de los elementos de un arreglo.
np.mean(): retorna el promedio de los elementos de un arreglo.
np.prod(): retorna la multiplicación de los elementos de un arreglo.
np.all(): retorna verdadero si todos los elementos de un arreglo se evaluan como verdadero.
np.any(): retorna verdadero si alguno de los elementos de un arreglo se evaluan como verdadero.
np.dot(b) : Devuelve el array resultado del producto matricial de los arrays a y b siempre y cuando sus dimensiones sean compatibles.
np.linalg.inv(a) : retorna la matriz inversa.