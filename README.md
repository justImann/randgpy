# 🧑‍🤝‍🧑 Group Divider CLI (Command Line Interface)

Program Python sederhana untuk membagi mahasiswa ke dalam kelompok secara adil dan interaktif, dengan mempertimbangkan ukuran kelompok dan minimal satu anggota perempuan di setiap kelompok.

## ✨ Fitur Utama

- **Interaktif**: Konfigurasi pembagian (jumlah kelompok dan ukuran) dilakukan melalui input terminal saat program dijalankan.
- **Penentuan Ketua**: Mendukung pemilihan **ketua acak** atau **ketua yang ditentukan** (dipilih dari daftar).
- **Keseimbangan Gender**: Memastikan **setiap kelompok memiliki minimal satu anggota perempuan** (jika jumlah perempuan yang tersedia mencukupi).
- **Pembagian Merata**: Mengalokasikan sisa anggota secara acak dan merata sesuai kuota yang ditentukan.
- **Output Jelas**: Menampilkan hasil pembagian dalam format tabel yang rapi menggunakan `pandas`, lengkap dengan header yang memisahkan setiap kelompok.

---

## 🚀 Cara Menjalankan Program

### 📋 Prasyarat

Pastikan Anda telah menginstal **Python 3** dan pustaka (library) yang diperlukan.

1.  **Instalasi Pustaka:**
    Anda memerlukan `pandas` untuk pemrosesan data dan tampilan output yang rapi.
    ```bash
    pip install pandas
    ```

### ▶️ Eksekusi

1.  Simpan kode program di atas sebagai file bernama `group_divider.py`.
2.  Jalankan program dari terminal:
    ```bash
    python group_divider.py
    ```
3.  Ikuti petunjuk interaktif yang muncul di terminal (UI bergaya CLI):
    - Masukkan jumlah kelompok yang diinginkan.
    - Tentukan rentang ukuran anggota per kelompok (misalnya: `4-5`).
    - Pilih apakah ketua ditentukan secara acak (`Y`) atau dipilih secara manual (`N`).

---

## 🛠️ Struktur Kode & Logika

### 💾 Data Sumber

Data mahasiswa disimpan dalam array Python bernama `data`. Setiap entri adalah tuple dengan format:
`("NIM", "Nama Lengkap", "Gender")`

**Catatan Penting**: Karena data NIM dan Nama yang Anda berikan tidak memiliki kolom gender, nilai `Gender` (`F` atau `M`) di dalam kode diasumsikan berdasarkan nama untuk memungkinkan logika keseimbangan gender berfungsi.

### 🧩 Fungsi Inti

1.  **`get_group_config()`**: Mengambil input dari pengguna untuk menentukan `leaders` (daftar nama ketua) dan `group_sizes` (ukuran final dari setiap kelompok).
2.  **`assign_groups(data, leaders, group_sizes)`**:
    - Memasukkan semua ketua ke kelompok masing-masing.
    - Memisahkan anggota yang tersisa menjadi `remaining_females` dan `remaining_males`.
    - Mengalokasikan satu anggota perempuan dari `remaining_females` ke setiap kelompok yang belum memiliki anggota perempuan.
    - Mengalokasikan sisa anggota (perempuan dan laki-laki) secara acak dan merata untuk mengisi kuota kelompok.
3.  **`print_result(groups)`**: Mencetak hasil pembagian kelompok ke terminal dalam format tabel yang jelas, memisahkan setiap kelompok dengan header berisi nama ketua.

---

## 💡 Kustomisasi

Jika Anda ingin mengubah data mahasiswa, cukup edit array `data` di awal file `group_divider.py` dengan format `("NIM", "NAMA", "GENDER")`. Pastikan kolom gender (`F` atau `M`) disertakan agar logika keseimbangan gender tetap valid.
