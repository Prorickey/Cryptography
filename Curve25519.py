import matplotlib.pyplot as plt

# Small prime field (just for visualization)
p = 2**255 - 19

# Curve25519-like constants
A = 486662

# Storage for valid points
points = []

# Try all x in the field
for x in range(p):
    # Curve25519-like equation: y^2 = x^3 + A*x^2 + x mod p
    rhs = (x**3 + A * x**2 + x) % p

    # Find all y such that y^2 ≡ rhs (mod p)
    for y in range(p):
        if (y * y) % p == rhs:
            points.append((x, y))

# Split into x and y for plotting
x_vals, y_vals = zip(*points)

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(x_vals, y_vals, s=10)
plt.title("Montgomery Curve (small-scale Curve25519)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
