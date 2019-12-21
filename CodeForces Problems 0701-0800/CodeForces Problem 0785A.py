# Anton and Polyhedrons
n = int(input())
shapes = [input() for i in range(n)]
icos = shapes.count("Icosahedron")
dode = shapes.count("Dodecahedron")
octa = shapes.count("Octahedron")
cube = shapes.count("Cube")
tetr = shapes.count("Tetrahedron")
print(20 * icos + 12 * dode + 8 * octa + 6 * cube + tetr * 4)
