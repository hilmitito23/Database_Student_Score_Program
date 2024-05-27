'''
Hilmi Tito Shalahudin
'''

# Berikut adalah Daftar Data Nilai Siswa Pelajaran Komputer di SMPIT 2 Pagi
database_siswa = [{
    'nisn' : '12345',
    'nama' : 'Hilmi',
    'gender' : 'L',
    'project_1' : 90,
    'project_2' : 90,
    'project_3' : 90,
    'kuis_1' : 90,
    'kuis_2' : 90,
    'uas' : 90,
    'nilai' : 90.0,
},{
    'nisn' : '23456',
    'nama' : 'Edith',
    'gender' : 'P',
    'project_1' : 80,
    'project_2' : 80,
    'project_3' : 80,
    'kuis_1' : 80,
    'kuis_2' : 80,
    'uas' : 80,
    'nilai' : 80.0,
},{
    'nisn' : '34567',
    'nama' : 'Zeus',
    'gender' : 'L',
    'project_1' : 70,
    'project_2' : 80,
    'project_3' : 90,
    'kuis_1' : 80,
    'kuis_2' : 80,
    'uas' : 80,
    'nilai' : 80.0,
}]

# READ
def read():
    while True:
        print("----- MENU READ DATA SISWA -----")
        print("----------------------------------")
        print("1. Tampilkan Report Seluruh Data")
        print("2. Tampilkan Report Data Tertentu")
        print("3. Kembali ke Menu Utama")
        print("----------------------------------")
        masukAngka = input("Masukkan pilihan [1-3]: ")
        if masukAngka == '1':
            if database_siswa == []:
                print("="*50)
                print('Tidak Ada Data Siswa')
                print("="*50)
                break
            else:
                allData()
                break
        elif masukAngka == '2':
            unikData()
        elif masukAngka == '3':
            main()
        else:
            print("Pilihan Anda Tidak Sesuai")
## Sub Read
def allData():
    print('''
            = = = = = = REPORT DATA SISWA = = = = = =
                    = = = = SMPIT 2 PAGI = = = =     ''')
    print('''No \t| NISN \t| Nama \t| Gender \t| Project 1 \t| Project 2 \t| Project 3 \t| Kuis 1 \t| Kuis 2 \t| UAS \t| Nilai Akhir \t''')
    for i in range(len(database_siswa)):
        print('{} \t|{} \t|{} \t|{} \t\t|{} \t\t|{} \t\t|{} \t\t|{} \t\t|{} \t\t|{} \t|{} \t'.format(i+1,database_siswa[i]['nisn'],database_siswa[i]['nama'],database_siswa[i]['gender'],database_siswa[i]['project_1'],database_siswa[i]['project_2'],database_siswa[i]['project_3'],database_siswa[i]['kuis_1'],database_siswa[i]['kuis_2'],database_siswa[i]['uas'],database_siswa[i]['nilai']))
def unikData():
    panggilnisn = input('Masukkan NISN: ')
    if panggilnisn.isnumeric():
        found = False
        for i in range(len(database_siswa)):
            if panggilnisn == database_siswa[i]['nisn']:
                found = True
                print('''
                = = = = = = REPORT DATA SISWA = = = = = =
                    = = = = SMPIT 2 PAGI = = = =     ''')
                print('''No \t| NISN \t| Nama \t| Gender \t| Project 1 \t| Project 2 \t| Project 3 \t| Kuis 1 \t| Kuis 2 \t| UAS \t| Nilai Akhir \t''')
                print('{} \t|{} \t|{} \t|{} \t\t|{} \t\t|{} \t\t|{} \t\t|{} \t\t|{} \t\t|{} \t|{} \t'.format(i+1,database_siswa[i]['nisn'],database_siswa[i]['nama'],database_siswa[i]['gender'],database_siswa[i]['project_1'],database_siswa[i]['project_2'],database_siswa[i]['project_3'],database_siswa[i]['kuis_1'],database_siswa[i]['kuis_2'],database_siswa[i]['uas'],database_siswa[i]['nilai']))
                break
        
        if not found:
            print(f'Data NISN {panggilnisn} Tidak Ada')
    else:
        print("Masukkan Angka!")

# CREATE
def create():
    while True:
        print("----- MENU UPDATE DATA SISWA -----")
        print("----------------------------------")
        print("1. Tambahkan Report Data Siswa")
        print("2. Kembali ke Menu Utama")
        print("----------------------------------")
        input_create = input("Masukkan pilihan: ")
        
        if input_create == '1':
            while True:
                allData()  
                while True:
                    nisn = input('Masukkan NISN: ')
                    if nisn.isnumeric():
                        break
                    else:
                        print("Masukkan Angka!")
                
                found = False
                for i in range(len(database_siswa)):
                    if nisn == database_siswa[i]['nisn']:
                        found = True
                        print(f"NISN Sudah Digunakan, Masukkan NISN Lainnya!")
                        break
                
                if not found:
                    nama = input('Masukkan Nama: ')
                    if not cek_huruf(nama):
                        print("Nama hanya boleh mengandung huruf alfabet.")
                        continue
                
                    gender = input('Masukkan Gender(L/P): ')
                    if not validasi_Gender(gender):
                        print("Gender tidak valid. Harus 'L' atau 'P'.")
                        continue
                
                    while True:
                        project_1 = input('Masukkan Nilai Project 1: ')
                        if validasi_nilai(project_1):
                            project_1 = int(project_1)
                            break
                        else:
                            print("Nilai tidak valid. Harus nilai diantara 0 dan 100.")

                    while True:
                        project_2 = input('Masukkan Nilai Project 2: ')
                        if validasi_nilai(project_2):
                            project_2 = int(project_2)
                            break
                        else:
                            print("Nilai tidak valid. Harus nilai diantara 0 dan 100.")

                    while True:
                        project_3 = input('Masukkan Nilai Project 3: ')
                        if validasi_nilai(project_3):
                            project_3 = int(project_3)
                            break
                        else:
                            print("Nilai tidak valid. Harus nilai diantara 0 dan 100.")

                    while True:
                        kuis_1 = input('Masukkan Nilai Kuis 1: ')
                        if validasi_nilai(kuis_1):
                            kuis_1 = int(kuis_1)
                            break
                        else:
                            print("Nilai tidak valid. Harus nilai diantara 0 dan 100.")

                    while True:
                        kuis_2 = input('Masukkan Nilai Kuis 2: ')
                        if validasi_nilai(kuis_2):
                            kuis_2 = int(kuis_2)
                            break
                        else:
                            print("Nilai tidak valid. Harus nilai diantara 0 dan 100.")

                    while True:
                        uas = input('Masukkan Nilai UAS: ')
                        if validasi_nilai(uas):
                            uas = int(uas)
                            break
                        else:
                            print("Nilai tidak valid. Harus nilai diantara 0 dan 100.")
                
                    nilai = (project_1 + project_2 + project_3 + kuis_1 + kuis_2 + uas) / 6

                
                print("Simpan Data (Y/N): ")
                save = input().lower()
                if save == 'y':
                    database_siswa.append({
                        'nisn': nisn,
                        'nama': nama,
                        'gender': gender,
                        'project_1': project_1,
                        'project_2': project_2,
                        'project_3': project_3,
                        'kuis_1': kuis_1,
                        'kuis_2': kuis_2,
                        'uas': uas,
                        'nilai': nilai
                    })
                    print("Data Siswa Berhasil Disimpan!")
                    break
                else:
                    print("Data Siswa Tidak Disimpan!")
        elif input_create == '2':
            main()
## Complimentary
def cek_huruf(string):
     return all(char.isalpha() for char in string)

def cek_digit(string):
    return string.isnumeric()

def validasi_Gender(gender):
    return gender.lower() in ["l", "p"]

def validasi_nilai(angka):
    if cek_digit(angka):
        nilai = int(angka)
        if 0 <= nilai <= 100:
            return True
    return False

#UPDATE
def update():
    while True:
        print("----- MENU UPDATE DATA SISWA -----")
        print("----------------------------------")
        print("1. Ubah Report Data Siswa")
        print("2. Kembali ke Menu Utama")
        print("----------------------------------")
        input_update = input("Masukkan pilihan [1-2]: ")

        if input_update == '1':
            allData()
            updateNISN = input('Masukkan NISN yang ingin di Ubah: ')
            if not updateNISN.isnumeric():
                print('Masukkan Angka!')
                continue

            found = False
            for i, siswa in enumerate(database_siswa):
                if updateNISN == siswa['nisn']:
                    found = True
                    updateIndex = i
                    updated_data = siswa.copy()

                    while True:
                        YesNo = input(f"Apakah Ingin Mengubah Data pada NISN {updateNISN}? [Y/N]: ")
                        if YesNo == "Y":
                            while True:
                                print("Daftar Data yang Ingin di Ubah: ")
                                print("1. Nama Siswa")
                                print("2. Gender")
                                print("3. Nilai Project 1")
                                print("4. Nilai Project 2")
                                print("5. Nilai Project 3")
                                print("6. Nilai Kuis 1")
                                print("7. Nilai Kuis 2")
                                print("8. Nilai UAS")
                                print("9. Semua Data")
                                print("10. Tampilkan Perubahan")
                                print("11. Simpan Perubahan")
                                print("12. Kembali ke Main Menu")
                                updatePilihan = input("Masukkan pilihan yang ingin dilakukan?[1-12]: ")

                                if updatePilihan == "1":
                                    updateNama = input("Masukkan Nama Siswa: ")
                                    if updateNama.isalpha():
                                        updated_data['nama'] = updateNama
                                    else:
                                        print("Nama hanya boleh mengandung huruf alfabet.")

                                elif updatePilihan == "2":
                                    updateGender = input("Masukkan Gender: ")
                                    if updateGender in ['L', 'P']:
                                        updated_data['gender'] = updateGender
                                    else:
                                        print("Gender tidak valid. Harus 'L' atau 'P'.")

                                elif updatePilihan == "3":
                                    updateProject_1 = input("Masukkan Nilai Project 1: ")
                                    if updateProject_1.isnumeric():
                                        updated_data['project_1'] = int(updateProject_1)
                                    else:
                                        print("Masukkan Angka!")

                                elif updatePilihan == "4":
                                    updateProject_2 = input("Masukkan Nilai Project 2: ")
                                    if updateProject_2.isnumeric():
                                        updated_data['project_2'] = int(updateProject_2)
                                    else:
                                        print("Masukkan Angka!")

                                elif updatePilihan == "5":
                                    updateProject_3 = input("Masukkan Nilai Project 3: ")
                                    if updateProject_3.isnumeric():
                                        updated_data['project_3'] = int(updateProject_3)
                                    else:
                                        print("Masukkan Angka!")

                                elif updatePilihan == "6":
                                    updateKuis1 = input("Masukkan Nilai Kuis 1: ")
                                    if updateKuis1.isnumeric():
                                        updated_data['kuis_1'] = int(updateKuis1)
                                    else:
                                        print("Masukkan Angka!")

                                elif updatePilihan == "7":
                                    updateKuis2 = input("Masukkan Nilai Kuis 2: ")
                                    if updateKuis2.isnumeric():
                                        updated_data['kuis_2'] = int(updateKuis2)
                                    else:
                                        print("Masukkan Angka!")

                                elif updatePilihan == "8":
                                    updateUAS = input("Masukkan Nilai UAS: ")
                                    if updateUAS.isnumeric():
                                        updated_data['uas'] = int(updateUAS)
                                    else:
                                        print("Masukkan Angka!")

                                elif updatePilihan == "9":
                                    updateNama = input("Masukkan Nama Siswa: ")
                                    if updateNama.isalpha():
                                        updated_data['nama'] = updateNama
                                    else:
                                        print("Nama hanya boleh mengandung huruf alfabet.")

                                    updateGender = input("Masukkan Gender: ")
                                    if updateGender in ['L', 'P']:
                                        updated_data['gender'] = updateGender
                                    else:
                                        print("Gender tidak valid. Harus 'L' atau 'P'.")

                                    updateProject_1 = input("Masukkan Nilai Project 1: ")
                                    if updateProject_1.isnumeric():
                                        updated_data['project_1'] = int(updateProject_1)
                                    else:
                                        print("Masukkan Angka!")

                                    updateProject_2 = input("Masukkan Nilai Project 2: ")
                                    if updateProject_2.isnumeric():
                                        updated_data['project_2'] = int(updateProject_2)
                                    else:
                                        print("Masukkan Angka!")

                                    updateProject_3 = input("Masukkan Nilai Project 3: ")
                                    if updateProject_3.isnumeric():
                                        updated_data['project_3'] = int(updateProject_3)
                                    else:
                                        print("Masukkan Angka!")

                                    updateKuis1 = input("Masukkan Nilai Kuis 1: ")
                                    if updateKuis1.isnumeric():
                                        updated_data['kuis_1'] = int(updateKuis1)
                                    else:
                                        print("Masukkan Angka!")

                                    updateKuis2 = input("Masukkan Nilai Kuis 2: ")
                                    if updateKuis2.isnumeric():
                                        updated_data['kuis_2'] = int(updateKuis2)
                                    else:
                                        print("Masukkan Angka!")

                                    updateUAS = input("Masukkan Nilai UAS: ")
                                    if updateUAS.isnumeric():
                                        updated_data['uas'] = int(updateUAS)
                                    else:
                                        print("Masukkan Angka!")

                                elif updatePilihan == "10":
                                    updateNilai = (updated_data['project_1'] + updated_data['project_2'] + updated_data['project_3'] + updated_data['kuis_1'] + updated_data['kuis_2'] + updated_data['uas']) / 6
                                    updated_data['nilai'] = updateNilai
                                    print('''
                                    = = = = = = REPORT DATA SISWA = = = = = =
                                    = = = = SMPIT 2 PAGI = = = =     ''')
                                    print('''No \t| NISN \t| Nama \t| Gender \t| Project 1 \t| Project 2 \t| Project 3 \t| Kuis 1 \t| Kuis 2 \t| UAS \t| Nilai Akhir \t''')
                                    print('{} \t|{} \t|{} \t|{} \t\t|{} \t\t|{} \t\t|{} \t\t|{} \t\t|{} \t\t|{} \t|{} \t'.format(updateIndex + 1, updateNISN, updated_data['nama'], updated_data['gender'], updated_data['project_1'], updated_data['project_2'], updated_data['project_3'], updated_data['kuis_1'], updated_data['kuis_2'], updated_data['uas'], updateNilai))

                                elif updatePilihan == "11":
                                    updateSimpan = input('Simpan Data [Y/N]: ')
                                    if updateSimpan == "Y":
                                        database_siswa[updateIndex] = updated_data
                                        # NilaiAkhir()
                                        allData()
                                    else:  
                                        print("Perubahan Tidak Disimpan")
                                    break
                                elif updatePilihan == "12":
                                    main()
                                else:
                                    print("Pilihan tidak valid. Silakan masukkan angka antara 1-12.")
                        else:
                            break                                                             
            if not found:
                print(f'Data NISN {updateNISN} Tidak Ada')           
        elif input_update == "2":
            break

# DELETE
def delete():
    while True:
        print("----- MENU DELETE DATA SISWA -----")
        print("----------------------------------")
        print("1. Hapus Report Data Siswa")
        print("2. Kembali ke Menu Utama")
        print("----------------------------------")
        input_delete = input("Masukkan pilihan: ")
        
        if input_delete == '1':
            allData()
            hapusNISN = input('Masukkan NISN yang ingin di Hapus: ')
            if not hapusNISN.isnumeric():
                print('Masukkan Angka!')
                continue
            
            found = False
            for i, siswa in enumerate(database_siswa):
                if hapusNISN == siswa['nisn']:
                    found = True
                    while True:
                        YesNo = input(f"Apakah Ingin Menghapus Data pada NISN {hapusNISN}? [Y/N]: ").upper()
                        if YesNo == "Y":
                            del database_siswa[i]
                            print(f"Data dengan NISN {hapusNISN} Berhasil Dihapus")
                            break
                        elif YesNo == "N":
                            break
                        else:
                            print("Masukkan Pilihan yang Benar!")
                    break
            if not found:
                print(f'Data NISN {hapusNISN} Tidak Ada')
        elif input_delete == '2':
            break

#MENU UTAMA + CODINGAN UTAMA
def main():
    while True:
        print("\n--- Selamat datang di Database Nilai Siswa Pelajaran Komputer!! ---")
        print("______________________________________________________")
        print("|                                                    |")
        print("|1. Melihat Report Data Siswa                        |")
        print("|2. Menambahkan Report Data Siswa                    |")
        print("|3. Mengubah Report Data Siswa                       |")
        print("|4. Menghapus Report Data Siswa                      |")
        print("|5. Exit                                             |")
        print("|                                                    |")
        print("______________________________________________________")
        choice = input("Masukkan pilihan: ")

        if choice == '1':
            read()
        elif choice == '2':
            create()
        elif choice == '3':
            update()
        elif choice == '4':
            delete()
        elif choice == '5':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan Tidak Sesuai.")


if __name__ == "__main__":
    main()