# WordPress brute force

<table>
  <tr>
    <th>Menu</th>
    <th>Available</th>
  </tr>
  <tr>
    <td>Validasi URL dan Cek Situs</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Brute Force Login</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Grabber (Domain/IP)</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Simpan Hasil dalam CSV</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>Keluar</td>
    <td>✅</td>
  </tr>
</table>

# **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/wordpress-brute-force.git
   cd wordpress
```
## Penggunaan

### Persiapan

1. Pastikan Python 3.7+ terinstal di sistem Anda.
2. Install dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

### Menjalankan Script

1. Buka terminal dan navigasi ke direktori script.
2. Jalankan script dengan perintah:
   ```bash
   python main.py
  ```


### Opsi 1: Validasi URL dan Cek Situs

- Masukkan URL login WordPress yang ingin Anda validasi.
- Script akan memeriksa apakah URL valid dan situs aktif.

### Opsi 2: Brute Force Login

- Masukkan URL login WordPress target.
- Pilih metode deteksi username atau masukkan username secara manual.
- Masukkan path ke file wordlist password.
- Script akan memulai proses brute force dan menampilkan progress.

### Opsi 3: Grabber (Domain/IP)

- Masukkan path ke file yang berisi daftar domain/IP.
- Script akan memproses file dan menyiapkan target untuk pengujian.

### Opsi 4: Simpan Hasil dalam CSV

- Hasil pengujian akan disimpan dalam file CSV.
- Anda dapat membuka file ini dengan spreadsheet editor.

### Opsi 5: Keluar

- Pilih opsi ini untuk mengakhiri program.

### Tips Penggunaan

- Gunakan wordlist yang kuat dan up-to-date untuk hasil terbaik.
- Pastikan Anda memiliki izin untuk melakukan pengujian pada target.
- Gunakan proxy untuk anonimitas tambahan jika diperlukan.
- Periksa log untuk informasi detail tentang proses pengujian.

<table>
  <tr>
    <th>Feature</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Multi-threading</td>
    <td>Mempercepat pengujian dan mendukung banyak target sekaligus.</td>
  </tr>
  <tr>
    <td>Penanganan Kesalahan</td>
    <td>Menangani kesalahan jaringan dan memberikan umpan balik jelas.</td>
  </tr>
  <tr>
    <td>Keamanan Tingkat Lanjut</td>
    <td>Rotasi User-Agent, dukungan proxy, dan pembatasan kecepatan.</td>
  </tr>
  <tr>
    <td>Deteksi Username</td>
    <td>Metode canggih untuk deteksi username valid dan multi-username.</td>
  </tr>
  <tr>
    <td>Scanning WordPress</td>
    <td>Periksa plugin, tema rentan, dan versi WordPress usang.</td>
  </tr>
  <tr>
    <td>Manajemen Sesi</td>
    <td>Simpan progres pengujian dan lanjutkan jika terhenti.</td>
  </tr>
  <tr>
    <td>Antarmuka Pengguna</td>
    <td>Progress bar real-time dan menu interaktif yang user-friendly.</td>
  </tr>
  <tr>
    <td>Logging</td>
    <td>Simpan hasil terstruktur dan ekspor ke CSV.</td>
  </tr>
  <tr>
    <td>Validasi Input</td>
    <td>Pastikan input valid dan aman.</td>
  </tr>
  <tr>
    <td>Grabber Domain/IP</td>
    <td>Uji massal daftar target.</td>
  </tr>
  <tr>
    <td>Kustomisasi Fleksibel</td>
    <td>Sesuaikan parameter dan gunakan wordlist kustom.</td>
  </tr>
</table>
