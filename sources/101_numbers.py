n1 = 10
n2 = 20.0
n3 = 4.323

type(n1)
type(n2)
type(n3)

n1 + n2
type(n1 + n2)
n1 * n3                 # why the last decimal case? See https://docs.python.org/2/tutorial/floatingpoint.html
n1 += 3
n1 ** 2
n1 = -n1
abs(n1)
n2 = complex(10, 20)
print n2
n2.real
n2.imag
