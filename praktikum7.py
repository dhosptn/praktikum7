data_mahasiswa = []

def tambah(nama, nilai):
    data_mahasiswa.append({'nama': nama, 'nilai': nilai})
    print(f"Data mahasiswa {nama} berhasil ditambahkan.")

def tampilkan():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa.")
    else:
        print("Daftar Nilai Mahasiswa:")
        print("="*23)
        for mahasiswa in data_mahasiswa:
           print(f"Nama : {mahasiswa['nama']}") 
           print(f"Nilai: {mahasiswa['nilai']}")
            
            

def hapus(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'] == nama:
            data_mahasiswa.remove(mahasiswa)
            print(f"Data mahasiswa {nama} berhasil dihapus.")
            return
    print(f"Data mahasiswa {nama} tidak ditemukan.")

def ubah(nama, nilai_baru):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'] == nama:
            mahasiswa['nilai'] = nilai_baru
            print(f"Data mahasiswa {nama} berhasil diubah.")
            return
    print(f"Data mahasiswa {nama} tidak ditemukan.")


tambah("Ardho", 90)
tambah("Ridho", 85)
tambah("Septian", 95)
print("")

tampilkan()

print("")
print("-"*40)
hapus("Ardho")
print("-"*40)
print("")

tampilkan()
print("")
print("-"*40)
ubah("Septian", 92)
print("-"*40)
print("")

tampilkan()
