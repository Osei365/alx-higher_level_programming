#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int a;
	long int sz = PyList_Size(p);
	PyListObject *pyobj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", sz);
	printf("[*] Allocated = %li\n", pyobj->allocated);
	for (a = 0; a < sz; a++)
	{
		printf("Element %i: %s\n", a, Py_TYPE(pyobj->ob_item[a])->tp_name);
	}
}
