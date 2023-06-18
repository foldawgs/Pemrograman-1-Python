

jumlah_matkul = int(input("Masukan Jumlah Mata Kuliah: "))

nilai_matkul = []

for i in range(jumlah_matkul):
    nilai = float(input(f"Masukan nilai mata kuliah ke {i + 1}: "))
    nilai_matkul.append(nilai)

total_nilai = sum(nilai_matkul)
rata_rata = total_nilai / jumlah_matkul

if rata_rata >= 91 and rata_rata <= 100:
    predikat = "A"
elif rata_rata >= 71 and rata_rata <= 90:
    predikat = "B"
elif rata_rata >= 51 and rata_rata <= 70:
    predikat = "C"
elif rata_rata >= 31 and rata_rata <= 50:
    predikat = "D"
elif rata_rata >= 0 and rata_rata <= 30:
    predikat = "E"
else:
    predikat = "Tidak valid"

print("\n")
print(f"Predikat anda adalah : {predikat}")
print(f"Dengan nilai: ")
for i in range(jumlah_matkul):
    print(f"Nilai mata kuliah ke-{i + 1}: {nilai_matkul[i]}") 