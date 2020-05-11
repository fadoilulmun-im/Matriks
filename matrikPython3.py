def matriks(x, y):
    list0 = []
    kolom = []
    for a in range(x):
        for i in range(y):
            while True:
                if (a == 0) and (i == 0):
                    print("Matrik\t[1", str(i + 1) + "]: ", end="")
                else:
                    print("\t[" + str(a + 1), str(i + 1) + "]: ", end="")
                inp = input()
                if inp.isnumeric():
                    inp = int(inp)
                    break
                else:
                    print("\033[91m{}\033[00m".format("Harus angka !"))
            kolom.append(inp)
        list0.append(kolom)
        kolom = []
    return list0


def ordo(a):
    for i in range(a):
        while True:
            print("Tentukan ordo matrik " + str(i + 1))
            inp = input('Contoh "2x3"\t: ')
            inp = inp.lower()
            inp = inp.replace("x", " ")
            inp = inp.split()
            if (len(inp) == 2) and (inp[0].isnumeric()) and (inp[1].isnumeric()):
                if (i > 0) and ((int(inp[0])) != (len(m["matrik{}".format(i - 1)][0]))):
                    print(
                        "\033[91m{}\033[00m".format(
                            "Baris matrik harus sama dengan Kolom matrik sebelumnya!"
                        )
                    )
                else:
                    m["matrik{}".format(i)] = matriks(int(inp[0]), int(inp[1]))
                    break
            else:
                print("\033[91m{}\033[00m".format("Format inputan salah !"))


def perkalianmatrik():
    hasil = []
    for i in range(len(m) - 1):
        if i == 0:
            matrik1 = m["matrik0"]
        else:
            matrik1 = hasil
        for a in range(len(matrik1)):
            baris = []
            for b in range(len(m["matrik{}".format(i + 1)][0])):
                total = 0
                for c in range(len(m["matrik{}".format(i + 1)])):
                    total = total + (matrik1[a][c] * m["matrik{}".format(i + 1)][c][b])
                baris.append(total)
            hasil.append(baris)
        if len(hasil) != len(m["matrik0"]):
            del hasil[: len(m["matrik0"])]

    return hasil


while True:
    jumlahMatrik = input("Masukkan berapa banyak matrik :")
    if jumlahMatrik.isnumeric():
        jumlahMatrik = int(jumlahMatrik)
        break
    else:
        print("\033[91m{}\033[00m".format("Harus angka !"))
m = {}

ordo(jumlahMatrik)

hasil = perkalianmatrik()

for i in range(len(m)):
    print("\nMatrik {} :".format(i + 1))
    for j in range(len(m["matrik{}".format(i)])):
        for k in range(len(m["matrik{}".format(i)][0])):
            print(m["matrik{}".format(i)][j][k], end=" ")
        print()


print(hasil)
print("\nHasil :")
for a in range(len(hasil)):
    for b in range(len(hasil[a])):
        print(hasil[a][b], end="\t")
    print()
