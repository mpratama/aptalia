# aptalia
## Deskripsi singkat
Apt-anti-lupa-ingat-anda; adalah *AI* yang dapat mengingatkan pasien supaya tidak lupa ketika telah tiba waktunya untuk minum obat dengan cara mengirimkan pesan langsung ke nomor WhatsApp pasien.

Aptalia adalah program python yang diinstall ke dalam komputer.

## Untuk apa?
Penulis program menciptakan *software* ini berawal dari kekhawatiran kurangnya kepatuhan pasien dalam minum obat terutama obat-obatan yang aturan minumnya berdasarkan waktu-waktu tertentu (mis: antibiotik, antihipertensi, antidiabetik). Penggunaan obat-obat tersebut termasuk kontinyu dan konstan pada satu waktu minum dan ada resiko jika lupa / terlewat maka terapi menjadi terganggu dan menimbulkan efek tdk diinginkan (mis: antibiotik => resiko resistensi).

## Cara install
- Install [Python 3](https://www.python.org/downloads) 
- *Clone* repo ini dengan git:
```bash
git clone https://github.com/mpratama/aptalia.git
```
- Install *dependency*:
```bash
python -m pip install -r requirements.txt
```

## Cara kerja
*Software* ini akan bekerja pagi-siang-malam-pagi 24/7 mengirimkan pesan pengingat minum obat ke nomor *WhatsApp* pasien melalui [WhatsApp Web](https://web.whatsapp.com). Jadi, untuk menjalankan software ini membutuhkan; No.WA aktif, koneksi internet, PC aktif 24/7\*, dan tentu saja--sedikit pengetahuan tentang *how software works* & *command line*.

Directory pmowa dari repo ini adalah program [Django](https://www.djangoproject.com) dengan tambahan sebuah custom script aktifkan_pengingat.py. Siapkan 2 window command line pada directory ini. Gunakan 1 window untuk menjalankan Django `python manage.py runserver` dan 1 window lainnya untuk menjalankan custom script `python aktifkan_pengingat.py`.

Django framework berfungsi sebagai *user interface* untuk memanage data pasien (kontak WA pasien), manage data obat, dan mencatat waktu minum obat serta rentang waktu pengobatan pasien.

Ketika pertama aktif, custom script akan membuka WhatsApp Web dan kita diharuskan login dengan scan QR code dari aplikasi WhatsApp smartphone. Custom script berfungsi sebagai *watcher*--di dalam script tersebut terbagi menjadi beberapa program kecil yang bekerja secara simultan membuka halaman WhatsApp Web=>mengakses database=>memantau waktu minum setiap obat=>mengirim pesan pada pasien sesuai schedule.

\*PC yang selalu aktif 24/7 tentu tidak *cost-effective*. Terdapat cara lain menginstall software ini pada smartphone android yang sudah dimodifikasi menjadi linux computer (menggunakan Termux & Andronix). Guidenya menyusul.

![login-page](https://raw.githubusercontent.com/mpratama/aptalia/master/00-login.png) |![main-menu](https://raw.githubusercontent.com/mpratama/aptalia/master/01-main-menu.png) 
---|---

![data-pasien-menu](https://raw.githubusercontent.com/mpratama/aptalia/master/02-data-pasien.png) |![data-obat-menu](https://raw.githubusercontent.com/mpratama/aptalia/master/03-data-obat.png) |![data-kunjungan-menu](https://raw.githubusercontent.com/mpratama/aptalia/master/04-data-kunjungan.png) 
---|---|---