import pygame
import math
import numpy as np

WINDOW_SIZE = (1000, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)

graph_bounds = ((-3, 3), (-3, 3))
graph_detail = .5
graph_center = (WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2)
x_range = graph_bounds[0][1] - graph_bounds[0][0]
y_range = graph_bounds[1][1] - graph_bounds[1][0]
sample_num = int(x_range / graph_detail)

lagrange_points = [(-1, 2), (0, 0), (1, -1), (2, 2)]

x_scale_factor = WINDOW_SIZE[0] / x_range 
y_scale_factor = WINDOW_SIZE[1] / y_range 
print(x_scale_factor, y_scale_factor)

graph_points = []
pixel_points = []

def graph_to_pixel(point, x_scale, y_scale, center):
    pixel_x = point[0] * x_scale + center[0]
    pixel_y = point[1] * y_scale + center[1]
    return (pixel_x, pixel_y)

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

def f(x):
    x_vals = []
    y_vals = []
    for point in lagrange_points:
          x_vals.append(point[0])
          y_vals.append(point[1])

    return np.polyval(lagrange_poly(x_vals, y_vals), x)

for i in range(graph_bounds[0][0]*sample_num, graph_bounds[0][1]*sample_num, 1):
    x = i / sample_num
    y = -f(x)
    graph_points.append((x, y))

for point in graph_points:
    pixel_point = graph_to_pixel(point, x_scale_factor, y_scale_factor, graph_center)
    pixel_points.append(pixel_point)

def draw(display):
    display.fill('white')

    for n, i in enumerate(pixel_points):
        if n + 1 != len(pixel_points):
            pygame.draw.line(display, 'black', i, pixel_points[n+1], 3)

    for point in lagrange_points:
        pixel_point = graph_to_pixel(point, x_scale_factor, y_scale_factor, graph_center)
        pygame.draw.circle(display, 'black', pixel_point, 5)

    pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw(screen)