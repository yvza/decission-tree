from sklearn import tree
#datasets
#waktu = 0 pendek, 1 panjang
#paket = 0 kecil, 1 besar
#frekwensi = 0 rendah, 1 sedang, 2, tinggi
#prioritas = 0 rendah, 1 tinggi
#waktu #paket #frekwensi #prioritas
x = [
 [0, 1, 1, 0],
 [0, 0, 0, 1],
 [1, 1, 1, 1],
 [1, 0, 2, 0],
 [0, 1, 2, 1],
 [1, 0, 0, 1],
 [1, 0, 2, 0],
 [1, 0, 1, 0],
 [1, 1, 2, 1],
 [1, 0, 1, 0],
 [0, 1, 1, 1],
 [1, 1, 0, 1],
]
y = [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

def prog() :
	waktu = int(input("Waktu? (0 pendek, 1 panjang) : "))
	paket = int(input("Paket? (0 kecil, 1 besar) : "))
	frekwensi = int(input("Frekwensi? (0 rendah, 1 sedang, 2, tinggi) : "))
	prioritas = int(input("Prioritas? (0 rendah, 1 tinggi) : "))

	if clf.predict([[waktu, paket, frekwensi, prioritas]]):
		print("\nJarigan sedang gangguan")
	else:
		print("\nJaringan sedang lancar")

prog()
