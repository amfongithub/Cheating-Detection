import pandas as pd

# Data yang ingin ditambahkan
data_baru = {'Nama': ['fds', 'ss'],
             'Usia': [32, 45],
             'Kota': ['Semarang', 'Yogyakarta']}

# Baca file Excel yang sudah ada
nama_file_excel = 'catatLOG.xlsx'
df_lama = pd.read_excel(nama_file_excel)

# Gabungkan data baru dengan data lama
df_baru = pd.DataFrame(data_baru)
df_gabung = pd.concat([df_lama, df_baru], ignore_index=True)

# Tulis kembali ke file Excel
with pd.ExcelWriter(nama_file_excel, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    df_gabung.to_excel(writer, index=False)

print("Data baru telah berhasil ditambahkan ke", nama_file_excel)
