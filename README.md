Electrical Fault Detection & Classification

Tugas Besar Pengganti Ujian Akhir Semester (UAS) Genap 2025/2026  
Mata Kuliah: ABK4ABB3 - PEMBELAJARAN MESIN DAN APLIKASI  

Kelompok: [Isi Nama Kelompok, misal: Kelompok 5]
- Ahmad Zacki Habibi, [1102220076]
- Brahmandityo Imam Prasetyo, [1102223277]
- M. Isaac Umar Siddiq, [1102223208]
- Satrio Nugroho, [1102223220]

---

## 🌐 1. Tautan Sistem Deployment
Sistem Machine Learning kami telah di-deploy menggunakan Gradio (Opsi B: Web App Interaktif) dan dapat diakses secara langsung untuk pengujian melalui tautan berikut:

👉 **[KLIK DI SINI UNTUK AKSES WEB APP](https://a35eaf1cf068685c6a.gradio.live)** 👈

*(Catatan Pengujian: Dosen penguji dapat menggunakan web UI di atas, atau menguji endpoint API melalui Command Prompt menggunakan skrip cURL yang telah kami sediakan di dalam file `skrip_curl.txt` pada repositori ini).*

---

## 📊 2. Akses Dataset
Dataset yang kami gunakan untuk melatih model ini berukuran kecil (`classData.csv`). Oleh karena itu, dataset tersebut sudah kami sertakan secara langsung di dalam repositori ini agar mudah diakses dan dievaluasi.

---

## ⚙️ 3. Panduan Instalasi Lokal
Jika ingin menjalankan sistem ini di komputer lokal, ikuti langkah-langkah instalasi environment berikut:

1. **Clone repositori ini:**
   ```bash
   git clone [https://github.com/Zackk009/Tubes_PMA.git](https://github.com/Zackk009/Tubes_PMA.git)
   cd Tubes_PMA
   
2. Buat Virtual Environment (Sangat Direkomendasikan):
Agar instalasi library tidak bentrok dengan sistem utama, buat dan aktifkan virtual environment:

    Bash
    # Pengguna Windows:
    python -m venv env
    env\Scripts\activate

    # Pengguna Mac/Linux:
    python3 -m venv env
    source env/bin/activate
    
3. Install library yang dibutuhkan:
Setelah berada di dalam folder repositori dan virtual environment aktif, jalankan perintah ini untuk menginstal seluruh dependencies:

        Bash
        pip install -r requirements.txt



   
**🚀 4. Cara Menjalankan Inference Secara Lokal**
Berikut adalah cara untuk menjalankan antarmuka web app (Gradio) dan melakukan prediksi di komputer lokal:

- Pastikan seluruh instalasi pada tahap sebelumnya berhasil.
- Buka terminal/Command Prompt di dalam folder repositori ini.
- Jalankan file utama aplikasi dengan perintah:

      Bash
      python app.py
  
- Tunggu beberapa detik hingga muncul tulisan * Running on local URL:  http://127.0.0.1:7860.

- Buka browser (Chrome/Edge) dan masukkan alamat http://127.0.0.1:7860 tersebut.

- Masukkan nilai Ia, Ib, Ic, Va, Vb, Vc pada antarmuka web untuk melihat hasil deteksi dan klasifikasi gangguan jaringan listrik.
