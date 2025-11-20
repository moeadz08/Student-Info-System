"""
Latar Belakang Proyek
Selamat! Anda telah mencapai puncak dari perjalanan belajar Python fundamental. Ujian ini bukanlah
sekadar tugas, melainkan sebuah simulasi pengembangan perangkat lunak skala kecil. Anda akan bertindak
sebagai developer tunggal yang ditugaskan untuk membangun sebuah prototipe Sistem Informasi Siswa
(SIS).
Berbeda dengan proyek-proyek sebelumnya yang berjalan sekali dari atas ke bawah, aplikasi ini harus
persisten dan interaktif. Artinya, data yang Anda masukkan harus bisa disimpan ke file dan dimuat kembali
saat program dijalankan lagi. Pengguna akan berinteraksi dengan program melalui sebuah menu, layaknya
aplikasi Command-Line Interface (CLI) sungguhan.
Tujuan Ujian
Proyek ini dirancang untuk menguji kemampuan Anda secara holistik dalam:
Merancang struktur program yang modular menggunakan Functions.
Mengelola data aplikasi yang kompleks menggunakan Nested Dictionaries and Lists.
Mengimplementasikan siklus I/O data yang persisten (Membaca data di awal, Menulis data di akhir)
dari/ke file teks.
Membangun alur program interaktif menggunakan while loop utama dan logika kondisional.
Mem-parsing dan memformat string untuk I/O file dan tampilan antarmuka.
Menggunakan tuple untuk mengembalikan status dan data dari fungsi.
Menangani input pengguna dan potensi error dengan elegan.
Spesifikasi Detail Proyek
1. Format File Data (database_siswa.txt)
Program Anda akan bekerja dengan satu file data, database_siswa.txt. Ini adalah file teks biasa yang
akan berfungsi sebagai "database" kita.
Format Setiap Baris: NIS,NAMA LENGKAP,NILAI_1;NILAI_2;NILAI_3;...
Data utama (NIS, Nama, Kumpulan Nilai) dipisahkan oleh koma (,).
Khusus untuk kumpulan nilai, setiap nilai individu dipisahkan oleh titik koma (;).
Contoh Isi database_siswa.txt:
101,Budi Santoso,85;92;78
102,Ani Lestari,95;88;91;100
103,Charlie Wijaya,65;72
Anda harus membuat file ini secara manual untuk memulai.

2. Struktur Data Internal
Saat program berjalan, semua data dari file harus dimuat ke dalam sebuah DICTIONARY UTAMA. Struktur
data ini akan menjadi "Single Source of Truth" selama program berjalan.
Struktur yang Wajib Digunakan: Sebuah Dictionary yang key-nya adalah NIS (string), dan value-nya
adalah Dictionary lain yang berisi data siswa.
# Contoh struktur data di dalam memori
data_semua_siswa = {
 '101': {
 'nama': 'Budi Santoso',
 'nilai': [85, 92, 78]
 },
 '102': {
 'nama': 'Ani Lestari',
 'nilai': [95, 88, 91, 100]
 },
 '103': {
 'nama': 'Charlie Wijaya',
 'nilai': [65, 72]
 }
}

3. Alur Program & Fitur Wajib
Program harus berjalan dalam sebuah while True loop utama yang menampilkan menu dan menunggu
input pengguna.
Menu Utama:
--- Sistem Informasi Siswa ---
1. Lihat Daftar Siswa
2. Lihat Detail Siswa
3. Tambah Siswa Baru
4. Tambah Nilai Siswa
5. Simpan & Keluar
------------------------------
Pilih menu:
Berikut adalah detail untuk setiap fitur, yang wajib diimplementasikan dalam fungsi-fungsi terpisah:
A. Saat Program Dimulai:
Program harus secara otomatis mencari file database_siswa.txt.
Jika file ditemukan, program harus memuat datanya ke dalam Dictionary Utama.
Jika file tidak ditemukan, program harus memulai dengan Dictionary Utama yang kosong.

B. Fitur Menu (Implementasikan sebagai Fungsi):
lihat_daftar_siswa(data_siswa):
Menampilkan daftar semua siswa dengan format: NIS: Nama Lengkap.
Jika tidak ada siswa, tampilkan pesan "Belum ada data siswa."
lihat_detail_siswa(data_siswa):
Minta pengguna memasukkan NIS.
Jika NIS tidak ditemukan, tampilkan pesan error.
Jika ditemukan, tampilkan detail lengkap:
NIS dan Nama.
Daftar semua nilai yang dimiliki.
Nilai Rata-rata.
Nilai Tertinggi dan Terendah.
Grade Akhir (berdasarkan rata-rata, lihat aturan di bawah).
tambah_siswa_baru(data_siswa):
Minta pengguna memasukkan NIS baru.
Validasi: Jika NIS sudah ada, tampilkan pesan error dan batalkan.
Minta pengguna memasukkan Nama Lengkap.
Tambahkan siswa baru ke Dictionary Utama dengan daftar nilai yang masih kosong.
tambah_nilai_siswa(data_siswa):
Minta pengguna memasukkan NIS.
Validasi: Jika NIS tidak ditemukan, tampilkan pesan error dan batalkan.
Minta pengguna memasukkan nilai baru (sebuah angka).
Tambahkan nilai baru tersebut ke dalam list 'nilai' milik siswa yang bersangkutan.
simpan_dan_keluar(data_siswa):
Fungsi ini akan mengubah Dictionary Utama kembali menjadi format string yang sesuai.
Tulis (timpa / overwrite) seluruh string tersebut ke file database_siswa.txt.
Cetak pesan "Data berhasil disimpan. Program berakhir."
Hentikan program (keluar dari while loop utama).

4. Aturan Logika Tambahan
Perhitungan Rata-rata: Jika seorang siswa belum memiliki nilai, rata-ratanya adalah 0. Hindari error
pembagian dengan nol.
Penentuan Grade (berdasarkan nilai rata-rata):
>= 85: 'A'
>= 75: 'B'
>= 65: 'C'
>= 50: 'D'
< 50: 'E'
"""

import os 

# A
def load_data(file_path):
    dataSemuaSiswaa = {}
    if os.path.exists(file_path): 

        with open(file_path, 'r') as file:
            for baris in file: 
                baris = baris.strip()
                if baris: 
                    nis, nama, nilai_str = baris.split(',', 2) 
                    nilai = list(map(int, nilai_str.split(';'))) if nilai_str else [] 
                    dataSemuaSiswaa[nis] = {'nama': nama, 'nilai': nilai} 
    return dataSemuaSiswaa 

# fungsi untuk save data ke file
def save_data(file_path, dataSemuaSiswaa): 
    with open(file_path, 'w') as file:
        for nis, info in dataSemuaSiswaa.items(): 
            nilai_str = ';'.join(map(str, info['nilai'])) 
            file.write(f"{nis},{info['nama']},{nilai_str}\n")

# B 
# fungsi 1
def lihat_daftar_siswa(dataSemuaSiswaa):
    if not dataSemuaSiswaa:
        print("Data siswa masih kosong!")
    else:
        print("\nDaftar Siswa: ")
        for nis, info in dataSemuaSiswaa.items():
            print(f"{nis}: {info['nama']}") 

# fungsi 2
def lihat_detail_siswa(dataSemuaSiswaa):
    nis = input("Asupkeun NIS siswa: ").strip()
    if nis not in dataSemuaSiswaa:
        print("Mon maap, NIS gak ketemu.")
        return 
    info = dataSemuaSiswaa[nis]
    nilai = info['nilai']
    rata_rata = sum(nilai) / len(nilai) if nilai else 0
    nilai_tertinggi = max(nilai) if nilai else 0
    nilai_terendah = min(nilai) if nilai else 0
    if rata_rata >= 85:
        grade = 'A'
    elif rata_rata >= 75:
        grade = 'B'
    elif rata_rata >= 65:
        grade = 'C'
    elif rata_rata >= 50:
        grade = 'D'
    else:
        grade = 'E'
    print(f"\nDetail Siswa: ")
    print(f"NIS: {nis}")
    print(f"Nama: {info['nama']}")
    print(f"Nilai: {nilai if nilai else 'Blomm ada nilai'}")
    print(f"Rata-rata: {rata_rata:.2f}")
    print(f"Nilai Tertinggi: {nilai_tertinggi}")
    print(f"Nilai Terendah: {nilai_terendah}")
    print(f"Grade Akhir: {grade}")

# fungsi 3
def tambah_siswa_baru(dataSemuaSiswaa):
    nis = input("Asupkeun NIS baru: ").strip()
    if nis in dataSemuaSiswaa:
        print("Mon map, NIS uda ada.")
        return 
    nama = input("Masukkan Nama Lengkap: ").strip()
    dataSemuaSiswaa[nis] = {'nama': nama, 'nilai': []}
    print(f"Siswa {nama} dengan NIS {nis} udah ditambahkeun.")

# fungsi 4
def tambah_nilai_siswa(dataSemuaSiswaa):
    nis = input("Asupkeun NIS siswa: ").strip()
    if nis not in dataSemuaSiswaa:
        print("Mon map, NIS ga ketemu.")
        return
    try: 
        nilai_baru = int(input("Masukkan nilai baru (angka): ").strip())
        dataSemuaSiswaa[nis]['nilai'].append(nilai_baru)
        print(f"Nilai {nilai_baru} sudah ditambahkeun untuk siswa {dataSemuaSiswaa[nis]['nama']}.")
    except ValueError:
        print("Mon maap, Nilai must be angka.")

# fungsi 5
def simpan_dan_keluar(file_path, dataSemuaSiswaa): 
    save_data(file_path, dataSemuaSiswaa)
    print("Data berhasil disimpan. Program berakhir.")

# fungsi utama
def main():
    file_path = 'database_siswa.txt'
    dataSemuaSiswaa = load_data(file_path) 
    while True:
        print("\n--- Sistem Informasi Siswa ---")
        print("1. Lihat Daftar Siswa")
        print("2. Lihat Detail Siswa")
        print("3. Tambah Siswa Baru")
        print("4. Tambah Nilai Siswa")
        print("5. Simpan & Keluar")
        print("------------------------------")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == '1':
            lihat_daftar_siswa(dataSemuaSiswaa)
        elif pilihan == '2':
            lihat_detail_siswa(dataSemuaSiswaa)
        elif pilihan == '3':
            tambah_siswa_baru(dataSemuaSiswaa)
        elif pilihan == '4':
            tambah_nilai_siswa(dataSemuaSiswaa)
        elif pilihan == '5':
            simpan_dan_keluar(file_path, dataSemuaSiswaa)
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

main()