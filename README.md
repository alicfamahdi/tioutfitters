# 
<http://aliefa-alsyafiandra-aduh.pbp.cs.ui.ac.id/>

## Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).

Mengimplementasikan checklist membutuhkan beberapa trial-and-error. Pada akhirnya, saya melakukannya sebagai berikut:
- Membuat local directory dan menginisialisasi sebagai repo git
- Membuat repo di GitHub dan menghubungkannya dengan local repo
- Mengaktifkan virtual environment pada local directory dan menginstall requirements
- Membuat proyek Django bernama "tioutfitters"
- Menambah berkas .gitignore
- Membuat aplikasi main pada directory
- Konfigurasi settings.py ALLOWED_HOSTS, INSTALLED_APPS
- Mengubah models.py dengan membuat model bernama Product dan memiliki atribut name, price, description lalu makemigrations untuk model
- Mengubah views.py untuk menambahkan context
- Membuat folder templates dan membuat main.html serta kustomisasi
- Konfigurasi routing urls
- Membuat project baru di PWS
- Menghubungkan link project PWS ke repo
- Add, commit, push ke main dan ke PWS
- Membuat README.md

## Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.



## Jelaskan fungsi `git` dalam pengembangan perangkat lunak!

Git adalah alat pengembangan perangkat lunak yang gratis dan _open-source_. Git berupa sistem kontrol versi (_version control system_) yang dapat mengelola projek secara efisien. Secara kolaboratif, git digunakan untuk melacak dan menyimpan perubahan pada _source code_, sehingga banyak _developer_ dapat bekerja sama di projek yang sama secara non-linear.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, framework Django digunakan untuk permulaan pembelajaran pengembangan perangkat lunak karena menggunakan bahasa Python yang mudah dipelajari karena kesederhanaan sintaksnya. Untuk mata kuliah PBP di Fasilkom ini, mahasiswa yang mengikutinya pasti sudah lulus mata kuliah prasyarat PBP, yaitu DDP-1 yang mengajarkan bahasa Python, dan sudah setidaknya menguasai beberapa keterampilan dalam bahasa Python.

## Mengapa model pada Django disebut sebagai *ORM*?

Django memiliki sistem ORM (_Object-Relational Mapping_) yang berfungsi sebagai jembatan antara basis data dan kode aplikasi. Dengan ORM, _developer_ dapat berinteraksi dengan basis data menggunakan bahasa Python tanpa harus menulis query SQL. ORM menyediakan abstraksi _high-level_ di atas basis data dan mempermudah pekerjaan _developer_ dengan struktur data yang kompleks.
