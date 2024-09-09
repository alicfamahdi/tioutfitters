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


## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django digunakan untuk permulaan pembelajaran pengembangan perangkat lunak karena menggunakan bahasa python yang mudah dipelajari karena kesederhanaan sintaksnya.

## Mengapa model pada Django disebut sebagai *ORM*?

Django's Object-Relational Mapping (ORM) is a powerful tool that allows developers to interact with a relational database using Python code, without writing raw SQL queries. The ORM provides a high-level abstraction layer over the database, making it easier for developers to work with complex data structures.
