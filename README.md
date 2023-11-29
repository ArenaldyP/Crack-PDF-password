# Pemecah PDF dengan Pemrosesan Paralel

Skrip Python ini menggunakan pustaka `pikepdf` untuk melakukan dekripsi PDF yang dilindungi kata sandi secara paralel. Skrip ini mengambil direktori kata sandi dan mencoba mendekripsi PDF menggunakan beberapa utas, meningkatkan kecepatan proses secara keseluruhan.

## Fitur:

- **Pemrosesan Paralel:** Memanfaatkan `ThreadPoolExecutor` untuk upaya dekripsi bersamaan, meningkatkan kinerja secara keseluruhan.
- **Logging:** Merekam proses dekripsi, mencatat upaya yang berhasil dan kata sandi yang salah.
- **Interaksi Pengguna:** Meminta pengguna untuk memasukkan direktori kata sandi dan file PDF, membuatnya interaktif.

## Cara Penggunaan:

1. Klona repositori: `git clone https://github.com/ArenaldyP/Crack-PDF-password.git`
2. Buka direktori proyek: `cd Crack-PDF-password`
3. Jalankan skrip: `python Crack_PDF.py`
4. Ikuti petunjuk interaktif untuk memberikan direktori kata sandi dan file PDF.

Silakan berkontribusi, laporkan isu, atau usulkan perbaikan. Selamat mendekripsi!

