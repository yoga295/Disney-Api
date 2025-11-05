# 🏰 Disney Character Finder  
Aplikasi Pencarian Karakter Disney berbasis **Python** menggunakan **PyQt5** dan **Qt Designer**.

---

## 🧾 Deskripsi Aplikasi
**Disney Character Finder** adalah aplikasi desktop yang dikembangkan dengan tujuan pembelajaran pembuatan antarmuka grafis (GUI) menggunakan **PyQt** dan **Qt Designer**.  
Aplikasi ini memungkinkan pengguna untuk mencari informasi karakter-karakter Disney berdasarkan nama, film, atau kategori tertentu.

Proyek ini dibuat untuk memahami alur kerja penggabungan antara:
- **Desain tampilan (UI)** dengan Qt Designer,  
- **Fungsi logika program (Python)**,  
- dan **Integrasi API / database sederhana** untuk menampilkan hasil pencarian karakter.

---

## 🎯 Tujuan Pembelajaran
Proyek ini dirancang untuk membantu memahami:
1. Penggunaan **Qt Designer** untuk membangun tampilan GUI secara visual.  
2. Integrasi file `.ui` hasil desain ke dalam Python.  
3. Penerapan konsep **CRUD (Read)** sederhana untuk menampilkan data karakter Disney.  
4. Penggunaan **API** (jika dihubungkan ke Disney API) atau file lokal `.json` sebagai sumber data.  
5. Pembuatan interaksi user-friendly antara form input, tombol pencarian, dan hasil pencarian.

---

## ⚙️ Teknologi yang Digunakan
| Komponen | Deskripsi |
|-----------|-----------|
| **Bahasa Pemrograman** | Python 3.x |
| **Framework GUI** | PyQt5 |
| **UI Designer** | Qt Designer |
| **Database / Data Source** | File JSON lokal atau Disney API |
| **Library Pendukung** | `requests`, `json`, `os`, `sys` |

---

## 🧩 Fitur Utama
✅ **Pencarian Karakter Disney** berdasarkan nama atau kategori  
✅ **Menampilkan detail karakter** (nama, film, gambar, deskripsi)  
✅ **Desain antarmuka interaktif** menggunakan Qt Designer  
✅ **Integrasi API** untuk mengambil data real-time (opsional)  
✅ **Pemberitahuan jika karakter tidak ditemukan**  
✅ **Tampilan dinamis dengan gambar karakter**  

---

## 🖼️ Tampilan Aplikasi
Berikut beberapa contoh tampilan aplikasi Disney Character Finder:

### 🪄 Tampilan Utama
Menampilkan kolom pencarian dan hasil karakter:
![Main UI](https://raw.githubusercontent.com/yoga295/disney-finder/main/assets/screenshots/main-ui.png)

### 📜 Hasil Pencarian
Menampilkan informasi karakter beserta gambarnya:
![Search Result](https://raw.githubusercontent.com/yoga295/disney-finder/main/assets/screenshots/result.png)

### ⚠️ Notifikasi
Menampilkan pesan jika karakter tidak ditemukan:
![Not Found](https://raw.githubusercontent.com/yoga295/disney-finder/main/assets/screenshots/notfound.png)

---

## 🧠 Cara Kerja Program

1. **User memasukkan nama karakter Disney** ke kolom pencarian.  
2. Program akan:
   - Membaca file JSON lokal **atau**
   - Mengirim request ke Disney API (jika mode online diaktifkan).
3. **Data hasil pencarian** kemudian ditampilkan dalam bentuk teks dan gambar di jendela utama.
4. Jika karakter tidak ditemukan, aplikasi akan menampilkan **pesan notifikasi.**

---

## 🛠️ Instalasi dan Cara Menjalankan

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yoga295/disney-character-finder.git
cd disney-character-finder
pip install pyqt5 requests
python main.py
