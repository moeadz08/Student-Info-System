import os 

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

def save_data(file_path, dataSemuaSiswaa): 
    with open(file_path, 'w') as file:
        for nis, info in dataSemuaSiswaa.items(): 
            nilai_str = ';'.join(map(str, info['nilai'])) 
            file.write(f"{nis},{info['nama']},{nilai_str}\n")

def lihat_daftar_siswa(dataSemuaSiswaa):
    if not dataSemuaSiswaa:
        print("Data siswa masih kosong!")
    else:
        print("\nDaftar Siswa: ")
        for nis, info in dataSemuaSiswaa.items():
            print(f"{nis}: {info['nama']}") 

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

def tambah_siswa_baru(dataSemuaSiswaa):
    nis = input("Asupkeun NIS baru: ").strip()
    if nis in dataSemuaSiswaa:
        print("Mon map, NIS uda ada.")
        return 
    nama = input("Masukkan Nama Lengkap: ").strip()
    dataSemuaSiswaa[nis] = {'nama': nama, 'nilai': []}
    print(f"Siswa {nama} dengan NIS {nis} udah ditambahkeun.")

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

def simpan_dan_keluar(file_path, dataSemuaSiswaa): 
    save_data(file_path, dataSemuaSiswaa)
    print("Data berhasil disimpan. Program berakhir.")

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