# 
<http://aliefa-alsyafiandra-tioutfitters.pbp.cs.ui.ac.id/>

# Tugas 3

## Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?

Data delivery biasanya mencakup HTTP response yang memberikan file HTML, CSS, JPG, JS, serta XML atau JSON, sesuai request browser. Data delivery diperlukan dalam pengimplementasian sebuah platform karena tanpa adanya data delivery, tampilan, data, atau bahkan logic dari suatu website tidak akan muncul sesuai request HTTP yang telah diminta oleh user via client browser.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

XML dan JSON masing-masing mempunyai kelebihan saat digunakan dalam suatu proyek. Jika ingin menyimpan beberapa tipe data dengan banyak variabel, XML adalah pilihan yang lebih cocok. XML mengecek error dalam data kompleks secara lebih efisien dibandingkan dengan JSON.
JSON lebih populer dibanding XML karena berbagai keunggulannya dibandingkan dengan XML:
- Sintaks yang digunakan lebih mudah dibuat dan dibaca.
- JSON bisa di-_parse_ dengan function JavaScript yang aksesibel.
- Transmisi data yang cepat.
- Ukuran file yang lebih kecil.
- Parsing yang lebih aman daripada XML.

## Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Fungsi `is_valid()` digunakan pada variabel `form` yang merupakan semua input yang dimasukkan user dalam form yang diberikan. `form.is_valid()` digunakan untuk memvalidasi isi input dari *form* tersebut. Tipe data fields yang ada di form sudah didefinisikan, maka perlu validasi input agar bisa diproses dan tidak terjadi error. 


## Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Cross Site Request Forgery (CSRF) adalah sebuah serangan eksploitasi web yang membuat pengguna tanpa sadar mengirim sebuah permintaan atau request ke website melalui website yang sedang digunakan saat itu. Suatu CSRF token adalah token random yang digunakan untuk mencegah serangan CSRF. Dengan menambahkan csrf_token pada form, kita bisa menghindari serangan CSRF di aplikasi kita. Jika tidak, penyerang dapat membahayakan pengguna aplikasi dengan mengarahkannya ke aplikasi yang berbahaya.

## Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Membuka folder mental-health-tracker dan folder project saya secara bersamaan agar bisa melakukan direct comparison dan bisa melihat perbedaan yang harus ditambahkan.
- Menambahkan folder .github/workflows dan membuat deploy.yml agar bisa push ke GitHub dan ke PWS sekaligus.
- Membuat direktori templates pada direktori utama (root folder) dan membuat base.html untuk menjadi kerangka app lainnya
- Menyesuaikan TEMPLATES pada settings.py
- Modifikasi main.html pada direktori main agar extend base.html
- Import UUID dalam models.py dan menambahkan atribut id, serta makemigrations setelah mengubah models.py
- Membuat file forms.py dalam direktori main, membuat subclass dari ModelForm dengan inner class Meta, import model Product dengan fields yang sesuai.
- Import model dan membuat function baru dalam views.py untuk menyimpan input dari form
- Mengubah function show_main agar memberikan data yang didapat dari input form
- Konfigurasi routing urls.py dengan import function dan menambah path ke urlpatterns
- Membuat file html untuk form yang meng-extend base.html
- Modifikasi main.html agar bisa menunjukkan data dari input forms dan menambah tombol "add entry"
- Menambah function dalam views.py yang mengembalikan data dalam bentuk XML, JSON, serta keduanya dari ID, lalu routing urls.py untuk tiap function baru
- Menggunakan Postman untuk melihat data.

http://localhost:8000/json/ :
![image](https://github.com/user-attachments/assets/68c750e1-9934-42a1-9326-dddf2feedff9)
http://localhost:8000/xml/ :
![image](https://github.com/user-attachments/assets/095a869e-a7e6-4378-ac11-1577df97728b)
http://localhost:8000/json/[id] :
![image](https://github.com/user-attachments/assets/a8e65cee-f5b2-4993-9850-45393286a170)
http://localhost:8000/xml/[id] :
![image](https://github.com/user-attachments/assets/be150890-4687-4cd5-bb6b-055e18e2086a)


---

# Tugas 2

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

![bagan](https://github.com/user-attachments/assets/e0122a73-3dc5-4b74-9855-8599fcf3b6b3)


## Jelaskan fungsi `git` dalam pengembangan perangkat lunak!

Git adalah alat pengembangan perangkat lunak yang gratis dan _open-source_. Git berupa sistem kontrol versi (_version control system_) yang dapat mengelola projek secara efisien. Secara kolaboratif, git digunakan untuk melacak dan menyimpan perubahan pada _source code_, sehingga banyak _developer_ dapat bekerja sama di proyek yang sama secara non-linear.
Adapun fitur-fitur unggul yang dapat digunakan dalam git untuk pengembangan perangkat lunak:
- Menyimpan perubahan secara lengkap
  Git melacak setiap perubahan yang dilakukan pada setiap file seiring waktu, termasuk mencatat siapa yang membuat perubahan, kapan perubahan itu dilakukan, dan mengapa. Hal ini mencakup membuat dan menghapus file, serta mengedit kontennya.
- Branching dan Merging
  Developer yang bekerja dalam satu proyek dapat membuat "branch"-nya sendiri untuk mengerjakan bagian masing-masing. Bagian-bagian terpisah ini nantinya bisa digabung menggunakan fitur "merge"
- Mudah ditelusuri
  Git juga bisa digunakan untuk melacak setiap perubahan dan menghubungkan perubahan tersebut ke tools manajemen proyek dan pelacakan bug.
- Mempercepat waktu rilis
  Metode pengembangan terdistribusi ini memungkinkan developer untuk mengerjakan dan merilis pembaruan kecil secara lebih sering. Dengan begitu, perubahan-perubahan ini dapat melewati proses peluncuran lebih cepat dibandingkan dengan merilis pembaruan besar sekaligus, yang umum terjadi pada sistem kontrol versi terpusat.
- Komunitas
  Karena gratis dan _open-source_, git telah menjadi standar untuk kontrol versi dan terdapat komunitas besar penggunanya yang dapat memberi bantuan jika ada masalah.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, framework Django digunakan untuk permulaan pembelajaran pengembangan perangkat lunak karena menggunakan bahasa Python yang mudah dipelajari karena kesederhanaan sintaksnya. Untuk mata kuliah PBP di Fasilkom ini, mahasiswa yang mengikutinya pasti sudah lulus mata kuliah prasyarat PBP, yaitu DDP-1 yang mengajarkan bahasa Python, dan sudah setidaknya menguasai beberapa keterampilan dalam bahasa Python.

## Mengapa model pada Django disebut sebagai *ORM*?

Django memiliki sistem ORM (_Object-Relational Mapping_) yang berfungsi sebagai jembatan antara basis data dan kode aplikasi. Dengan ORM, _developer_ dapat berinteraksi dengan basis data menggunakan bahasa Python tanpa harus menulis query SQL. ORM menyediakan abstraksi _high-level_ di atas basis data dan mempermudah pekerjaan _developer_ dengan struktur data yang kompleks.
