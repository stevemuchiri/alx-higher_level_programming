#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints Python lists
 * @p: Pointer to a PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *obj;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: ", i);
		if (PyFloat_Check(obj))
			print_python_float(obj);
		else if (PyBytes_Check(obj))
			print_python_bytes(obj);
		else
			printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}

/**
 * print_python_bytes - Prints Python bytes objects
 * @p: Pointer to a PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; ++i)
		printf("%02x%c", string[i] & 0xFF, i == size - 1 || i == 9 ? '\n' : ' ');
}

/**
 * print_python_float - Prints Python float objects
 * @p: Pointer to a PyObject
 */
void print_python_float(PyObject *p)
{
	double val;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	val = PyFloat_AsDouble(p);
	printf("  value: %f\n", val);
}
