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

f1 = [
	(0, 1.6),
	(.1, 1.71),
	(.2, 1.75),
	(.3,1.62),
	(.4, 1.45),
	(.5, 1.475)
]

f2 = [
	(.5, 1.475),
	(.6, 1.55),
	(.7, 1.575),
	(.8, 1.56),
	(.9, 1.51),
	(1, 1.4),
]

f3 = [
	(1, 1.4),
	(1.1, 1.27),
	(1.2, 1.19),
	(1.3, 1.15),
	(1.4, 1.05),
	# (1.43, .92),
	(1.5, .88),
]

f4 = [
	(1.5, .88),
	(1.75, .76),
	(2, .67),
	(2.25, .61),
	(2.5, .58),
	(2.75, .58),
	(3, .6),
	(3.25, .66),
	(3.5, .94),
]

f5 = [
	(3.5, .94),
	(3.6, .99),
	(3.7, .97),
	(3.8, .79),
	(3.9, .53)
]

f6 = [
	(3.9, .53),
	(4.15, .74),
	(4.4, .82),
	(4.65, .85),
	(4.9, .82),
	(5.15, .7),
	(5.4, .42),
	(5.5, 0)
]

points = f6

x_vals = []
y_vals = []
for point in points:
	x_vals.append(point[0])
	y_vals.append(point[1])

lst = lagrange_poly(x_vals, y_vals).c[::-1]
print('+'.join('x^{}*{}'.format(*k) for k in enumerate(lst)))
