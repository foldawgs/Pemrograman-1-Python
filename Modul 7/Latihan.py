#tambah data
def addMahasiswa():
    jumlah = int(input("Masukan Jumlah Mahasiswa: "))
    mahasiswa = []
    while(jumlah >0):
        nama = input("Nama mahasiswa: ")
        mahasiswa.append(nama)
        jumlah = jumlah - 1

    while(True):
        panggil(mahasiswa)
        jumlah = jumlah - 1
        if(jumlah < 0):
            break

#hapus data
def removeMahasiswa(arrayMahasiswa):
    mahasiswa = arrayMahasiswa
    print("Data mahasiswa: %s" %arrayMahasiswa)
    mahasiswa.remove(input("Hapus Mahasiswa: "))
    print("Data mahasiswa %s" %mahasiswa)
    panggil(mahasiswa)

#urut data
def ascMahasiswa(arrayMahasiswa):
    mahasiswa = arrayMahasiswa
    mahasiswa.sort()
    print(mahasiswa)
    panggil(mahasiswa)

#lihat data
def viewMahasiswa(arraymahasiswa):
    mahasiswa = arraymahasiswa
    for x in mahasiswa:
        print("Nama mahasiswa: %s" %x)
    panggil(arraymahasiswa)

#menu
def panggil(arraymahasiswa):
    print("\n===== Menu Data Mahasiswa ======")
    print("1. Tambah Data Mahasiswa")
    print("2. Hapus Data Mahasiswa")
    print("3. Urutkan Data Mahasiswa")
    print("4. Lihat Data Mahasiswa")
    print("5. Tutup")

    pilih = int(input("Pilih: "))
    if pilih == 1:
        addMahasiswa()
    elif pilih == 2:
        removeMahasiswa(arraymahasiswa)
    elif pilih == 3:
        ascMahasiswa(arraymahasiswa)
    elif pilih == 4:
        viewMahasiswa(arraymahasiswa)
    else:
        print("Selesai")

addMahasiswa()