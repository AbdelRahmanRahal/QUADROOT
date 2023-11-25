print("\n~~Quadratic Solver~~")
print("Enter your terms in")
print("quadratic form:")
print("aX^2 + bX + c = 0\n")

# Get inputs for coefficients a, b, and c
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Calculate the discriminant
d = b**2 - 4*a*c

# Calculate the two solutions
if d > 0:
# If the discriminant is positive, the solutions are real and different
	sol1 = (-b - d**0.5) / (2*a)
	sol2 = (-b + d**0.5) / (2*a)
	print('\nX = {}\nX = {}'.format(sol1, sol2))
elif d == 0:
	# If the discriminant is zero, the solutions are real and the same
	sol = -b / (2*a)
	print('\nX = {}  x2'.format(sol))
else:
	# If the discriminant is negative, the solutions are imaginary
	sol = (-b / (2*a), -d / (4*a))
	print('\nX = {} + sqrt({})i\nX = {} - sqrt({})i'.format(sol[0], sol[1], sol[0], sol[1]))

	get_root = int(input("Calc root? 1 | 0\n> "))
	if get_root:
		from math import sqrt
		print('sqrt({}) = {}'.format(sol[1], sqrt(sol[1])))