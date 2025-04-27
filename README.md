UTS Pemrograman sisi server 
Author
- Nama : Bernandiko Priyambodo
- NIM  : A11.2022.14673

Alur Pengerjaan Proyek

1. Inisialisasi Proyek
- Membuat folder proyek 
- Membuat environment Docker dengan `Dockerfile` dan `docker-compose.yml`.
- Menentukan struktur folder dan file utama.

2. Setup Docker & Django
- Membuat `Dockerfile` untuk Django dengan base image `python:3.11-slim`.
- Membuat file `requirements.txt` berisi:
  - Django
  - psycopg2-binary
- Membuat file `docker-compose.yml` untuk menjalankan Django dan PostgreSQL secara bersamaan.

3. Inisialisasi Project Django
- Masuk ke dalam container Django.
- Menjalankan `django-admin startproject inventory .`
- Menjalankan `python manage.py startapp core`

4. Setup Database PostgreSQL
- Mengatur koneksi database di `settings.py` agar menggunakan PostgreSQL dari service Docker Compose.

5. Membuat Model Database
- Membuat model: `Admin`, `Category`, `Supplier`, dan `Item` di `core/models.py` sesuai ERD.
- Menambahkan fungsi `__str__` pada setiap model untuk tampilan yang lebih baik di admin.

6. Migrasi dan Setup Admin
- Menjalankan `python manage.py makemigrations` dan `python manage.py migrate`.
- Mendaftarkan model ke admin Django.
- Membuat superuser untuk akses admin.

7. CRUD Data Melalui Admin
- Melakukan Create, Read, Update, Delete data melalui halaman admin Django.

 8. Membuat Fitur Laporan & Ringkasan
    Membuat view dan template untuk:
      - Ringkasan stok barang (total stok, nilai stok, rata-rata harga)
      - Daftar barang dengan stok rendah
      - Laporan barang per kategori
      - Ringkasan per kategori (jumlah barang, nilai stok, rata-rata harga)
      - Ringkasan barang per pemasok
      - Ringkasan keseluruhan sistem

9. Testing & Penyempurnaan
- Menambahkan data contoh melalui admin.
- Melakukan testing fitur melalui browser.
- Memperbaiki tampilan dan menambah filter pemisah ribuan pada angka.

10. Dokumentasi & Upload ke GitHub
- Membuat file `README.md` ini sebagai dokumentasi alur pengerjaan.
- Push seluruh project ke repository GitHub.


Struktur Folder
inventory/
├── core/
│ ├── migrations/
│ ├── templates/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ └── ...
├── inventory/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
