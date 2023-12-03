import numpy as np

def lagrange_poly(x_vals, y_vals):

	if len(x_vals) != len(y_vals):
		return 0

	basis_polys = []
	for i in range(len(x_vals)):
		leading_coeff = y_vals[i]

		numerator_polys = []
		denominator_vals = []
		for n, j in enumerate(x_vals):
			if i != n:
				poly = np.poly1d([1, -j])
				numerator_polys.append(poly)
				denominator_vals.append(x_vals[i] - j)

		numerator = np.poly1d([1])
		for poly in numerator_polys:
			numerator *= poly

		denominator = 1
		for val in denominator_vals:
			denominator *= val 

		basis_poly = (numerator / denominator) * leading_coeff
		basis_polys.append(basis_poly)

	output = 0
	for poly in basis_polys:
		output += poly

	return output

x_vals = [0,   0.9,  1.3,  5.7, 6,    6.5,  9.6]
y_vals = [2.9, 2.52, 2.8,  1,   1.79, .44,  0]
lst = lagrange_poly(x_vals, y_vals).c[::-1]

print('+'.join('x^{}*{}'.format(*k) for k in enumerate(lst)))