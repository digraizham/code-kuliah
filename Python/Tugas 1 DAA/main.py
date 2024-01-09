import matplotlib.pyplot as plt

def convex_hull(points):
    # Urutkan titik berdasarkan koordinat x, lalu koordinat y
    points = sorted(points)
    
    # Fungsi bantu untuk menghitung produk cross dari tiga titik
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    
    # Fungsi untuk menentukan apakah suatu putaran ke kiri, kanan, atau lurus
    def turn(p1, p2, p3):
        arah_garis = cross_product(p1, p2, p3)
        if arah_garis > 0:
            return 1 # Putaran ke kiri
        elif arah_garis < 0:
            return -1 # Putaran ke kanan
        else:
            return 0 # Lurus
    
    # Temukan lower hull
    lower_hull = [points[0]]
    for i in range(1, len(points)):
        while len(lower_hull) >= 2 and turn(lower_hull[-2], lower_hull[-1], points[i]) == -1:
            lower_hull.pop()
        lower_hull.append(points[i])
    
    # Temukan upper hull
    upper_hull = [points[-1]]
    for i in range(len(points)-2, -1, -1):
        while len(upper_hull) >= 2 and turn(upper_hull[-2], upper_hull[-1], points[i]) == -1:
            upper_hull.pop()
        upper_hull.append(points[i])
    
    # Gabungkan lower hull dan upper hull
    hull = lower_hull[:-1] + upper_hull[:-1]
    
    # Buat daftar garis dari titik-titik di hull
    lines = [(hull[i], hull[(i+1)%len(hull)]) for i in range(len(hull))]

    return lines

points = [(0,0), (1,1), (2,2), (3,0), (2,-2), (1,-1)]
hull = convex_hull(points)
print(hull) # Output: [((0, 0), (3, 0)), ((3, 0), (2, -2)), ((2, -2), (0, 0))]

# Membuat gambar dari convex hull
x, y = zip(*points)
plt.scatter(x, y)
for line in hull:
    x, y = zip(*line)
    plt.plot(x, y)
plt.show()