#include <Python.h>
#include <stdio.h>

void print_python_float(PyObject *p)
{
	double val;
	char *val_string;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	val_string = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", val_string);
}

void print_python_bytes(PyObject *p)
{
	long int i = 0, a;
	char *string;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	string = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %li\n", PyBytes_Size(p));
	printf("  trying string: %s\n", string);

	if (PyBytes_Size(p) >= 10)
	{
		i += 10;
	}
	else
		i = PyBytes_Size(p) + 1;
	printf("  first %li bytes:", i);
	for (a = 0; a < i; a++)
	{
		if (string[a] >= 0)
		{
			printf(" %02x", string[a]);
		}
		else
			printf(" %02x", 256 + string[a]);
	}
	printf("\n");
}

void print_python_list(PyObject *p)
{
	int a;
	long int size = PyList_GET_SIZE(p);
	PyListObject *pyobj = (PyListObject *)p;
	PyObject *itemobj;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", pyobj->allocated);
	for (a = 0; a < size; a++)
	{
		itemobj = ((PyListObject *)p)->ob_item[a];
		printf("Element %i: %s\n", a, ((itemobj)->ob_type)->tp_name);
		if (PyBytes_Check(itemobj))
		{
			print_python_bytes(itemobj);
		}
		else if (PyFloat_Check(itemobj))
			print_python_float(itemobj);
	}
}
