#import <Python.h>

static long hasher(char *a)
{
  unsigned char *p;
  long x;
  
  p = (unsigned char *)a;
  x = *p << 7;
  while (*p) {
    x = (1000003*x) ^ *p++;
    x ^= strlen(a);
  }
  if (x == -1) {
    x = -2;
  }
  return x;
}

static PyObject *
chasher_hash(PyObject *self, PyObject *args)
{
  char *value;
  static long hash;

  if (!PyArg_ParseTuple(args, "s", &value)) {
    return NULL;
  }

  hash = hasher(value);

  return Py_BuildValue("l", hash);
}

static PyMethodDef CHasherMethods[] = {
  {"hash",  chasher_hash, METH_VARARGS, "Hash a string"},
  {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
initchasher(void)
{
  (void) Py_InitModule("chasher", CHasherMethods);
}

