import pandas as pd
data = pd.DataFrame([
    [90,80],
    [50,60],
    [65,70],
], index=['Mahasiswa 1','Mahasiswa 2','Mahasiswa 3'], columns=['Algoritma dan struktur Data 2','Matematika Numerik'])
print(data)
total_matkul = data.sum(axis=0)
jumlah_matkul = len(data.columns)
rata_rata_matkul = total_matkul/jumlah_matkul
print(f'=== Rata-rata Nilai Untuk Setiap Mata Kuliah ===')
print(rata_rata_matkul)
total_mahasiswa = data.sum(axis=1)
jumlah_mahasiswa = len(data.index)
rata_rata_mahasiswa = total_mahasiswa/jumlah_mahasiswa
print(f'=== Rata-rata Nilai Untuk Setiap Mahasiswa ===')
print(rata_rata_mahasiswa)