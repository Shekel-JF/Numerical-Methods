import numpy
import matplotlib.pyplot
import math

N = 100
lowerD1 = numpy.empty((N), dtype=numpy.double)
lowerD2 = numpy.empty((N), dtype=numpy.double)
upperD1 = numpy.empty((N), dtype=numpy.double)
upperD2 = numpy.empty((N), dtype=numpy.double)
Dmid = numpy.empty(N, dtype=numpy.double)
x = numpy.zeros(N)
x2 = numpy.zeros(N)
y = numpy.zeros(N)
norm = []
norm2 = []

for n in range(0, N):
    Dmid[n] = 3.0
    y[n] = n + 1

for n in range(0, N - 1):   
    lowerD1[n] = 1.0
    upperD1[n] = 1.0

for n in range(0, N - 2):
    lowerD2[n] = 0.2
    upperD2[n] = 0.2

for k in range(100):
    newX = numpy.zeros(N)
    newX[0] = (y[0] - (upperD1[0] * x[1]) - (upperD2[0] * x[2])) / Dmid[0]
    newX[1] = (y[1] - (lowerD1[0] * newX[0]) - (upperD1[1] * x[2]) - (upperD2[1] * x[3])) / Dmid[1]


    for l in range(2, N - 2):
        newX[l] = (y[l] - (lowerD2[l - 2] * newX[l - 2]) - (lowerD1[l - 1] * newX[l - 1]) - (upperD1[l] * x[l + 1]) - (upperD2[l] * x[l + 2])) / Dmid[l]

    newX[N - 2] = (y[N - 2] - (lowerD2[N - 4] * newX[N - 4]) - (lowerD1[N - 3] * newX[N - 3]) - (upperD1[N - 2] * x[N - 1])) / Dmid[N - 2]
    newX[N - 1] = (y[N - 1] - (lowerD2[N - 3] * newX[N - 3]) - (lowerD1[N - 2] * newX[N - 2])) / Dmid[N - 1]

    Norm = 0
    for m in range(0, N):
        Norm += (newX[m] - (x[m])) * (newX[m] - (x[m]))

    norm.append(math.sqrt(Norm))
    x = newX

for k in range(100):
    newX = numpy.zeros(N)
    newX[0] = (y[0] - (upperD1[0] * x2[1]) - (upperD2[0] * x2[2])) / Dmid[0]
    newX[1] = (y[1] - (lowerD1[0] * x2[0]) - (upperD1[1] * x2[2]) - (upperD2[1] * x2[3])) / Dmid[1]


    for l in range(2, N - 2):
        newX[l] = (y[l] - (lowerD2[l - 2] * x2[l - 2]) - (lowerD1[l - 1] * x2[l - 1]) - (upperD1[l] * x2[l + 1]) - (upperD2[l] * x2[l + 2])) / Dmid[l]

    newX[N - 2] = (y[N - 2] - (lowerD2[N - 4] * x2[N - 4]) - (lowerD1[N - 3] * x2[N - 3]) - (upperD1[N - 2] * x2[N - 1])) / Dmid[N - 2]
    newX[N - 1] = (y[N - 1] - (lowerD2[N - 3] * x2[N - 3]) - (lowerD1[N - 2] * x2[N - 2])) / Dmid[N - 1]

    Norm2 = 0
    for k in range(0, N):
        Norm2 += (newX[k] - x2[k]) * (newX[k] - (x2[k]))

    norm2.append(math.sqrt(Norm2))
    x2 = newX

print("x:")
print(x)
matplotlib.pyplot.yscale('log')
matplotlib.pyplot.plot(norm)
matplotlib.pyplot.plot(norm2)
matplotlib.pyplot.show()