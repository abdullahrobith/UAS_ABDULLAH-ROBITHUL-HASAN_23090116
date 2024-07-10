data = []
while True:
    nim = int(input('Masukkan NIM : '))
    nama = input('Masukkan Nama : ').title()
    data_baru = {'NIM':nim,'Nama':nama}
    data.append(data_baru)
    tambah = input('Ingin Menambah Data Lagi [Y/T]: ').upper()
    if tambah == 'T':
        break
print('===== Data Mahasiswa ====='.upper())
for a in data:
    print('NIM :', a['NIM'])
    print('Nama :', a['Nama'])
    print()
