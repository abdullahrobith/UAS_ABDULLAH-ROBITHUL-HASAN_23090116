from Soal_3 import Antrian
antrian = Antrian()
def tambah_Antrian():
    pelanggan = input('Masukkan Nama Pelanggan : ')
    antrian.enqueue(pelanggan)
    print(f'{pelanggan} Berhasil Ditambahkan Kedalam Antrian')
    print(35 * '=')
def hapus_Antrian():
    if len(antrian) == 0:
        print('Data Kosong : Tidak Bisa Dihapus')
    else:
        pelanggan_dihapus = antrian.dequeue()
        if len(antrian) > 0:
            print(f'Pelanggan Selanjutnya : {antrian.antrian[0]}')
        else:
            print('Antrian Sekarang Kosong')
    print(35 * '=')
while True:
    print('''Pilihan
    1. Tambah Antrian
    2. Antrian Selanjutnya''')
    pilihan = input('Masukkan Pilihan : ')
    
    if pilihan == '1':
        tambah_Antrian()
    elif pilihan == '2':
        hapus_Antrian()
    elif pilihan == '4':
        print('Terima kasih! Program selesai.')
        break
    else:
        print('Pilihan tidak valid, silakan coba lagi.')
        print(35 * '=')