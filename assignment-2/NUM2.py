import numpy
import scipy.linalg
A1 = numpy.array([[2.40827208, -0.36066254, 0.80575445, 0.46309511, 1.20708553], [-0.36066254, 1.14839502, 0.02576113, 0.02672584, -1.03949556], [0.80575445, 0.02576113, 2.45964907, 0.13824088, 0.0472749], [0.46309511, 0.02672584, 0.13824088, 2.05614464, -0.9434493], [1.20708553, -1.03949556, 0.0472749, -0.9434493, 1.92753926]])
A2 = numpy.array([[2.61370745, -0.6334453, 0.76061329, 0.24938964, 0.82783473], [-0.6334453, 1.51060349, 0.08570081, 0.31048984, -0.53591589], [0.76061329, 0.08570081, 2.46956812, 0.18519926, 0.13060923], [0.24938964, 0.31048984, 0.18519926, 2.27845311, -0.54893124], [0.82783473, -0.53591589, 0.13060923, -0.54893124, 2.6276678]])

b = numpy.array([5.40780228, 3.67008677, 3.12306266, -1.11187948, 0.54437218])
b2 = numpy.array([0.00001, 0, 0, 0, 0])
bp = numpy.add(b, b2)


y11 = scipy.linalg.solve(A1, b, assume_a='pos')
print("Rozwiązaniem A1y1 = b jest wektor:")
print(y11)

y12 = scipy.linalg.solve(A1, bp, assume_a='pos')
print("Rozwiązaniem A1y1prim = bprim jest wektor:")
print(y12)

y21 = scipy.linalg.solve(A2, b, assume_a='pos')
print("Rozwiązaniem A2y2 = b jest wektor:")
print(y21)

y22 = scipy.linalg.solve(A2, bp, assume_a='pos')
print("Rozwiązaniem A2y2prim = bprim jest wektor:")
print(y22)

D1 = numpy.linalg.norm(numpy.subtract(y11, y12))
print("Delta1 jest równa:")
print(D1)

D2 = numpy.linalg.norm(numpy.subtract(y21, y22))
print("Delta2 jest równa:")
print(D2)