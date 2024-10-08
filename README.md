# 
<http://aliefa-alsyafiandra-tioutfitters.pbp.cs.ui.ac.id/>

# Tugas 6

## Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

JavaScript adalah bahasa pemrograman yang digunakan developer untuk membuat halaman web yang interaktif. Dengan JavaScript, browser dapat merespons interaksi pengguna dan mengubah tata letak konten di halaman web.

Manfaat dari JavaScript, di antaranya:
- Mudah dipelajari dan digunakan
Sintaks JavaScript terinspirasi oleh bahasa pemrograman Java serta mudah dipelajari dan dikodekan. Node.js juga mendapatkan popularitas yang signifikan untuk pengkodean backend.

- Mendapatkan independensi platform
Tidak seperti bahasa pemrograman lain, JavaScript dapat dimasukkan ke halaman web mana pun serta dapat digunakan dengan banyak kerangka kerja dan bahasa pengembangan web lainnya. Setelah ditulis, kode JavaScript dapat dijalankan di mesin apa pun. 

- Mengurangi beban server
JavaScript dapat digunakan untuk mengurangi beban server dan kemacetan jaringan karena dapat menjalankan operasi logis serta melakukan banyak pekerjaan server pada klien itu sendiri.

- Meningkatkan antarmuka pengguna
JavaScript membuat pencarian dan pemrosesan informasi yang kompleks lebih mudah. Developer menerapkan JavaScript untuk memperluas fungsionalitas dan keterbacaan serta membuat interaksi pengguna situs web lebih efisien.

- Mendukung konkurensi
JavaScript dapat menjalankan beberapa set instruksi yang berbeda secara paralel. Di backend, Node.js dapat menangani dan memproses respons server yang skalanya dinaikkan dengan sangat tinggi tanpa menghabiskan jumlah bandwidth yang sama.

## Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?

`fetch` adalah suatu function built-in JavaScript untuk membuat request HTTP. Ketika digunakan dengan `async/await`, kode asinkronus
untuk meng-*handle* response dapat dibuat.
Jika mendapat suatu exception yang di-*raise* pada method, tanpa `await`, exception tersebut akan hilang. Jika `await` digunakan, 
exception akan di-*rethrow*. Sebagai *best practice*, sebaiknya menggunakan `await` dalam function.

## Mengapa kita perlu menggunakan *decorator* `csrf_exempt` pada *view* yang akan digunakan untuk AJAX `POST`?

Ketika menggunakan CSRF token, token unik akan dibuat secara otomatis untuk tiap update halaman. Akan tetapi, jika menggunakan AJAX, halaman tidak akan diupdate, dan tidak akan mendapat token baru. Maka `csrf_exempt` digunakan agar CSRF token tidak dibuat untuk view AJAX POST.

## Pada tutorial PBP minggu ini, pembersihan data *input* pengguna dilakukan di belakang (*backend*) juga. Mengapa hal tersebut tidak dilakukan di *frontend* saja?

Data difilter di *frontend* karena data input masuk melalui layer *frontend* terlebih dahulu, lalu di *backend* data tersebut akan difilter lagi agar tidak terjadi error.
Ketika data difilter di *frontend*, seluruh dataset harus diambil, dan akibatnya menggunakan jumlah bandwidth yang lebih signifikan, terlebih ketika datasetnya besar. Filter data pada *backend* mengurangi penggunaan bandwidth tersebut dengan mentransfer data yang dibutuhkan saja ke *frontend*.

## Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)!

- Modifikasi views.py agar menunjukkan error message pada login jika gagal.
- Membuat function baru dalam views.py yaitu create_product_entry_ajax lalu routing function tersebut ke path /create-ajax/
- Modifikasi agar bisa menunjukkan data product entry dengan fetch() API
- Modifikasi main.html dengan menggantikan block conditional dengan div product_entry_cards serta menambahkan async function script
- Membuat function JavaScript untuk add, get, refresh entries
- Membuat modal untuk menambah product dengan AJAX
- Melindungi app dari XSS dengan clean_data, strip_tags, dan DOMPurify

---

# Tugas 5

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Jika ada dua atau lebih CSS selector yang ditetapkan ke satu elemen yang sama, *style* selector dengan level spesifikasi yang paling tinggi akan dipilih untuk elemen tersebut. Terdapat hirarki spesifikasi:
1. Inline styles - Contoh: `<h1 style="color: pink;">`
2. IDs - Contoh: #navbar
3. Classes, pseudo-classes, attribute selectors - Contoh: .test, :hover, [href]
4. Elements dan pseudo-elements - Contoh: h1, ::before

Cara menghitung spesifikasi: mulai dari 0, tambahkan 100 untuk tiap ID value, tambahkan 10 untuk tiap class value (atau pseudo-class atau attribute selector), tambahkan 1 untuk tiap element selector atau pseudo-element.

Note:
- Inline style memiliki nilai spesifikasi 1000, dan selalu diberikan prioritas tertinggi,
- Kecuali jika menggunakan !important, maka inline style tersebut juga akan di-*override*

## Mengapa *responsive design* menjadi konsep yang penting dalam pengembangan aplikasi *web*? Berikan contoh aplikasi yang sudah dan belum menerapkan *responsive design*!

Responsive design adalah suatu cara menyusun website sedemikian sehingga bisa menyesuaikan skala content dan elementnya ke ukuran layar yang digunakan untuk melihat website tersebut. Responsive design penting dalam pengembangan aplikasi karena dapat mempermudah pengguna dalam menggunakan aplikasi buatan kita. Dengan responsive design, diharapkannya pengguna tidak perlu melakukan resize, scroll, zoom, atau pan yang tidak dibutuhkan.
Tanpa responsive design, akan sulit untuk menavigasi aplikasi, dan secara keuntungan, bisa merugikan karena ada kemungkinan pelanggan akan menyerah sebelum bisa melakukan apapun dalam aplikasi. 
Contoh aplikasi yang sudah menerapkan responsive design: Twitter, YouTube
Contoh aplikasi yang belum menerapkan responsive design: SIAK-NG, https://dequeuniversity.com/library/responsive/1-non-responsive

## Jelaskan perbedaan antara *margin*, *border*, dan *padding*, serta cara untuk mengimplementasikan ketiga hal tersebut!

Dalam CSS Box Model, terdapat elemen-elemen ini:
1. Content - isi dari box, seperti text atau image
2. Padding - memberikan ruang di sekitar content, padding transparan
3. Border - garis batas yang mengelilingi padding dan content
4. Margin - memberikan ruang di luar border, margin transparan
![alt text](tugas-5-boxmodel.png)

- Cara mengimplementasikan padding dengan tailwind:
`<div class="p-8 ...">p-8</div>`
dengan p-8 memberikan padding ke semua sisi content. padding juga bisa diberikan secara vertikal (py-8) dan horizontal (px-8) ataupun dari sisi spesifik (pt-8 untuk atas, pb-8 untuk bawah, pl-8 untuk kiri, dan pr-8 untuk kanan)
- Cara mengimplementasikan border dengan tailwind:
border memiliki lebih banyak spesifikasi dibandingkan dengan padding, beberapa di antaranya adalah set warna, radius, dan ketebalan border.
- Cara mengimplementasikan margin dengan tailwind:
mirip seperti padding, margin juga bisa diberikan dari sisi spesifik, horizontal, vertikal, ataupun semua sisi.

## Jelaskan konsep *flex box* dan *grid layout* beserta kegunaannya!

Flex box adalah layout yang berupa suatu flex container yang berisi flex items. Flex container ini dapat berubah-ubah ukurannya, dan flex items menyesuaikan (sesuai setting) akan berpindah, mengecil, atau membesar untuk mengisi space yang ada pada container secara efektif dan fleksibel. Flex box mungkin lebih cocok untuk komponen aplikasi dan layout skala kecil.
Di sisi lain, grid layout lebih cocok untuk layout skala besar. Grid layout adalah layout yang berupa tabel dengan baris dan kolom. Item di dalam grid layout posisi dan ukurannya akan lebih rigid dibandingkan dengan di dalam flex box karena tidak bertujuan untuk mengisi semua space yang ada.

## Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)!

- Membuka folder mental-health-tracker dan folder project secara bersamaan agar bisa membandingkan perbedaan.
- Menambahkan Tailwind ke aplikasi dengan modifikasi base.html, konfigurasi static files dengan modifikasi MIDDLEWARE & STATIC_URLS settings.py, lalu membuat folder untuk static files seperti global.css atau folder untuk image.
- Membuat function baru edit_product dan delete_product di views.py lalu routing functions di urls.py.
- Membuat navbar.html di folder templates pada root directory, dan set styling navbar.
- Kustomisasi page aplikasi (login, register, main, edit mood, product card, dsb.) semenarik mungkin dan menerapkan responsive design.

---

# Tugas 4

## Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`

HttpResponseRedirect adalah sebuah subclass dari HttpResponse. HttpResponseRedirect() merupakan constructor dari class tersebut yang membutuhkan argument berupa path tujuan redirect, hanya bisa berupa full URL ('https://www.yahoo.com/search/'), path tanpa domain ('/search/'), atau relative path ('search/'). redirect() adalah sebuah function yang akan me-return HttpResponseRedirect dan dapat menerima model, view, atau url sebagai argument tujuan redirect, membuatnya lebih fleksibel dibandingkan dengan HttpResponseRedirect().

##  Jelaskan cara kerja penghubungan model `Product` dengan `User`!

Pada models.py, ditambahkan atribut user ke model Product dengan models.ForeignKey yang akan mendefinisikan many-to-one relationship antara Product dan User; satu User bisa memiliki multiple Product, tetapi suatu Product hanya bisa memiliki satu User. Pada views.py, product_entries diubah agar menunjukkan product yang diinput oleh user yang sedang login saja.

##  Apa perbedaan antara *authentication* dan *authorization*, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Authentication adalah metode verifikasi identitas pengguna atau sistem yang mengecek kredensial seperti username, password, atau informasi biometrik. Authentication penting untuk mengamankan akses ke sistem, program, atau informasi sensitif.
Authorization adalah langkah setelah authentication yang menetapkan dan memberikan izin ke pengguna, memberi spesifikasi apa saja yang dapat diakses oleh pengguna dan aksi apa saja yang dapat dilakukan.
Sistem authentication Django menghandle kedua authentication dan authorization. Sistem authnya terdiri dari:
- Users
- Permissions: flag biner (yes/no) yang menentukan apakah suatu user bisa melakukan task tertentu.
- Groups: memberi label dan permissions ke lebih dari 1 user.
- Sistem password yang bisa dikonfigurasi
- Form untuk user login, atau mambatasi konten
- Sistem backend

##  Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari *cookies* dan apakah semua cookies aman digunakan?

Django bisa mengingat pengguna yang sudah login dengan proses holding state. Salah satu cara yang paling banyak digunakan untuk melakukan holding state adalah dengan menggunakan session ID yang disimpan sebagai cookie pada komputer klien. Session ID dapat dianggap sebagai suatu token (barisan karakter) untuk mengenali session yang unik pada aplikasi web tertentu. Daripada menyimpan semua jenis informasi sebagai cookies pada klien seperti username, nama, dan password, hanya Session ID yang disimpan, lalu dipetakan ke data di sisi web server.


##  Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).

- Mengubah views.py: import messages dan UserCreationForm agar bisa menggunakan form pendaftaran pengguna bawaan.
- Menambahkan function register dalam views.py yang menggunakan UserCreationForm, memasukkan QueryDict berdasarkan input dari user pada request.POST, serta return redirect ke page login jika berhasil register.
- Membuat register.html untuk tampilan page register serta menambah routing path register ke urls.py.
- Menambahkan function login dalam views.py: import AuthenticationForm, authenticate, login, HttpResponseRedirect, reverse, dan datetime, lalu buat function login_user. AuthenticationForm akan dimasukkan data dari request.POST. Jika user valid, akan diredirect ke main page dan set cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login.
- Membuat login.html untuk tampilan page login serta menambah routing path login ke urls.py.
- Menambahkan function logout dalam views.py: import logout, lalu buat function logout_user yang akan menghapus cookies last login dan redirect ke page login.
- Menambahkan tombol untuk logout dan menunjukkan kapan user terakhir login di main.html dan routing path logout ke urls.py.
- Memodifikasi views.py agar main page hanya bisa muncul jika sudah login dengan menambahkan line @login_required(login_url='/login') di atas function show_main.
- Membuat account pada localhost.
- Menghubungkan Product dengan User: memodifikasi models.py untuk import User dan menambahkan atribut user pada model Product, dengan relationship ForeignKey (satu user bisa memiliki multiple product, tetapi suatu product hanya memiliki satu user)
- Mengubah function product_entry: form.save(commit=False) agar objek Product yang dibuat tidak langsung disimpan ke database, karena field user perlu diisi dengan objek User dari return value request.user.
- Mengubah function show_main agar menunjukkan Product yang dibuat oleh User yang sedang login saja.
- Menyimpan perubahan pada models dan makemigrations.
- Memodifikasi settings.py untuk import os dan set PRODUCTION dan DEBUG.
- Membuat dua user dan membuat tiga product untuk tiap user.
![alt text](tugas-4-user-1.png)
![alt text](tugas-4-user-2.png)

---

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
