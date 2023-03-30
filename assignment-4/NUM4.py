import numpy

def solve_upper (ad1, ad2, x):
    n = ad1.shape[0]
    y = numpy.empty(n)
    
    y[n-1] = (x[n - 1] / ad1[n - 1])
    y[n-2] = ((x[n - 2] - (y[n - 1] * ad2[n - 2])) / ad1[n - 2])

    for i in range(n - 3, -1, -1):
        y[i] = (x[i] - (y[i + 1] * ad2[i])) / ad1[i]

    return y

N = 50
A = numpy.empty((N, N))
for k in range(N):
    for j in range(N):
        A[k][j] = 1
        if k == j:
            A[k][j] = 10
        if k == j:
            A[k][j] = 8

ud1 = numpy.empty(N)
ud2 = numpy.empty(N-1)
u = numpy.empty(N)
v = numpy.empty(N)
b = numpy.empty(N)


for k in range(0, N):
    ud1[k] = 9
    u[k] = 1
    v[k] = 1
    b[k] = 5

for k in range (0, N - 1):
    ud2[k] = 7

v = v.reshape(1, N)
u = numpy.expand_dims(numpy.array(u), axis = 1)
z = solve_upper(ud1, ud2, b).reshape(N, 1)
z_prim = solve_upper(ud1, ud2, u).reshape(N, 1)
y = numpy.subtract(z, (numpy.dot(z_prim, numpy.dot(v, z)) / (1 + numpy.dot(v, z_prim)))).reshape(1, N)

print("Wektor y:")
print(y)