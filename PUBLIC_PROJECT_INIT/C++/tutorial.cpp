// include nos dice que vamos a utilizar toda la librería iostream
#include <iostream>  // iostream: input/output stream
// Para utilizar el tipo de dato string debemos de incluirlo
#include <string>
/* 
Proporciona un alcance a los identificadores (los nombres de tipos, 
Funciones, variables, etc.) dentro de él.
Se utilizan para organizar el código en grupos lógicos y evitar 
las colisiones de nombres que pueden ocurrir
*/
using namespace std;

// En c++ se necesita una funcion principal main; sin ella, no se puede
// ejecutar el script

/*
int main()
{
	// Si no incluimos la libreria iostream no podremos utilizar el cout,
	// al igual que si no utilizamos el namespace std.
	cout << "Hola, soy nuevo aqui! :')\n";  // cout: character output
	// Si no utilizamos el namespace del tipo std, entonces tendremos que
	// utilizar el comando "std::" antes del cout y de otros identifiers
	// lo que es tedioso.
	// std::cout << "Hola, soy nuevo aqui! :')";
	cout << "--------------------------" << endl;

	// Una constante no puede cambiar de valor. Si lo haces, te dará error.
	// Tampoco se puede colocarlo sin valor: "const int gravity;"
	const int gravity = -9.8;

	// El cin toma el input del usuario
	// Si colocamos un tipo de dato diferente al asignado, nos imprime "0"
	// Esto nos indica un error y ademas las siguientes lineas no se ejecutaran
	
	int n, x;
	cout << "Enter a number: ";
	cin >> n;
	cout << "Enter next number: ";
	cin >> x;
	cout << n << endl;
	cout << x;
	

	Si queremos arreglar el error del cin, haremos lo siguiente:
	int n, x;
	cout << "Enter a number: ";
	cin >> n;
	cout << cin.fail();
	// cout << cin.fail(); Con este comando se evita que de una respuesta
	// de error grande y se simplifica a 1 y 0, donde 1 es un error y 0
	es un correcto

	Otra forma de arreglarlo:
	int n, x;
	cout << "Enter a number: ";
	cin >> n;
	cin.clear();  // Este metodo solo borra el error, pero no el texto.
	// Este si elimina el texto; para ello se le da el número de caracteres
	// a eliminar y ub salto de linea.
	cin.ignore(1000, '\n');
	cout << "Enter next number: ";
	cin >> x;
	cout << n << endl;
	cout << x;
	

	Creando una simple calculadora:
	int num1, num2;
	cout << "Enter a number: ";
	cin >> num1;
	cin.clear();
	cin.ignore(1000, '\n');
	cout << "Enter next number: ";
	cin >> num2;
	int sum = num1 + num2;
	cout << "The sum is: " << sum;
	

	int x = 8;
	// Para que el resultado de una operacion sea float, solo uno
	// de los operandos debe ser float y la tipo de dato de la variable
	// que sostiene el resultado tambien debe ser float
	// No se puede sacar el modulo con numeros flotantes.
	x++;  // El valor se incrementa en 1; x--; disminuye en 1.
	cout << x;
	// El return es una regla de c++ que debe incluir al final del codigo
	// Este retorna 0, porque el main es de tipo integer.
	return 0;
}
*/

int main()
{
	
	// Operadores de comparacion [<, <=, >, >=, ==, !=] 
	// El resultado es 1 o 0, donde 1 es true y 0 es false
	bool test = 'a' == 'A';
	cout << test << endl << endl;
	cout << "------------------------" << endl;

	int num1, num2;
	cout << "Enter a number: ";
	cin >> num1;
	cin.clear();
	cin.ignore(1000, '\n');
	cout << "Enter next number: ";
	cin >> num2;
	// Se debe colocar en parentesis la comparacion para que la maquina
	// sepa que queremos comparar esas dos variables.
	cout << "These numbers are the same?: " << (num1 == num2);

	return 0;
}
