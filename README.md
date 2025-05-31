# Aplikasi Inventaris
Proyek ini bertujuan untuk mengoptimalkan pengisian ulang stok dan mengotomatiskan proses dengan mengintegrasikan data ERP yang terkait dengan stok dan penjualan. Data tersebut mengalami transformasi dan disimpan dalam basis data MySQL, yang berfungsi sebagai tulang punggung dasbor yang digunakan untuk melacak tingkat inventaris dan kinerja penjualan.

![image](https://github.com/user-attachments/assets/d7919644-e20f-4eb8-8949-394afd995ee3)

# Gambaran Umum
Aplikasi Inventaris memproses data stok dan penjualan yang berasal dari sistem ERP. Data diekstraksi, diubah, dan dimuat (ETL) ke dalam basis data MySQL, yang memungkinkan manajemen dan visualisasi proses pengisian ulang stok yang efisien. Dasbor yang dihasilkan memberikan wawasan waktu nyata tentang status inventaris dan kinerja penjualan, membantu pengambilan keputusan dan strategi pengoptimalan.

![2](https://github.com/user-attachments/assets/5575845d-4349-4bb3-8a9f-be493a9a8945)

# Fitur
* Ekstraksi data dari sistem ERP untuk data stok dan penjualan
* Transformasi data mentah ke dalam format terstruktur menggunakan Python (Pandas dan Numpy)
* Penyimpanan data yang diubah dalam basis data MySQL untuk memudahkan kueri dan skalabilitas
* Dasbor dinamis menggunakan Dash untuk memvisualisasikan tingkat inventaris dan kinerja penjualan
* Pembaruan waktu nyata ke dasbor saat data baru diproses

# Algoritma

Algoritma ABC Analysis adalah metode klasifikasi yang digunakan dalam manajemen persediaan untuk mengelompokkan item berdasarkan pentingnya, biasanya dari segi nilai konsumsi tahunan. Dalam aplikasi Inventaria, algoritma ini membantu memprioritaskan fokus pengelolaan stok.

Ringkasan ABC Analysis:
1. A (20% item = 80% nilai): Item paling bernilai tinggi, memerlukan pengawasan ketat dan kontrol ketat.
2. B (30% item = 15% nilai): Item dengan nilai menengah, kontrol sedang.
3. C (50% item = 5% nilai): Item bernilai rendah, bisa dikelola dengan kontrol minimal.

# Alur Pemrosesan Data
1. Ekstrak: Data stok dan penjualan diambil dari sistem ERP.
2. Transformasi: Menggunakan pustaka Python (Pandas dan Numpy), data dibersihkan, difilter, dan diagregasi untuk analisis.
3. Muat: Data yang diubah disimpan dalam basis data MySQL untuk kueri dan visualisasi.
4. Visualisasikan: Dash digunakan untuk membangun dasbor interaktif yang menampilkan data dan wawasan terkait stok dan penjualan.

# Teknologi yang Digunakan
1. Python: Untuk pemrosesan data dan logika backend.
2. Pandas: Untuk manipulasi dan transformasi data.
3. Numpy: Untuk operasi dan kalkulasi numerik.
4. Dash: Untuk membuat dasbor interaktif.
5. MySQL: Untuk menyimpan data yang ditransformasikan dan mendukung kueri yang efisien.

# Instalasi
Prasyarat
* Python 3.x
* Basis data MySQL
