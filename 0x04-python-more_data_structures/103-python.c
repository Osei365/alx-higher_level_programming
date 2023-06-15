#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	long int i = 0, a;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	string = PyBytes_AsString(p);
	printf("  size: %li\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));

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
	long int size = PyList_Size(p);
	PyListObject *pyobj = (PyListObject *)p;
	PyObject *itemobj;

	printf("[*] Python list info\n");
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
	}
}
