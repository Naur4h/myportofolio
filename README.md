# Personal Portfolio

Nama: Naurah Claradinda Aulia Pane
NPM: 2506657163
Kelas: PBP-A

Link website: https://naurah-claradinda-myportofolio.pws.cs.ui.ac.id/

---

# Tugas 1

## Deskripsi Proyek
Website portofolio pribadi yang saya buat menggunakan Django, HTML, dan CSS dengan Visual Studio Code sebagai code editor. Website ini berisi informasi mengenai profil, skills, project, dan experience saya.

## Konsep Ide
Saya menggunakan konsep handmade scrapbook untuk memberikan kesan yang lebih personal, playful, dan tidak terlalu formal. Saya juga menambahkan beberapa elemen dekoratif seperti background bergaris, efek lakban, gambar, dan floating love agar tampilannya lebih sesuai dengan konsep yang saya inginkan.

## Teknologi yang Digunakan
- Python
- Django
- HTML
- CSS
- Visual Studio Code

## Design & Resources
- W3Schools — referensi syntax HTML & CSS (https://www.w3schools.com/)
- Google Fonts (Lexend) — font utama website
- Inspirasi background dan photo editing dari Instagram Hiraeyq

## Cara Menjalankan Website
1. Clone repository
2. Masuk ke folder project: `cd myportofolio-naurah`
3. Aktifkan virtual environment: `env\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Jalankan server: `python manage.py runserver`
6. Buka website melalui browser

## Struktur Halaman
- Profile
- Skills
- Projects
- Experience

## Weekly Progress
**31 Agustus 2026**
- Mengikuti Tutorial 0 sesuai langkah yang diberikan.
- Membuat project awal dan requirements.txt.

**1 September 2026**
- Menyelesaikan Tutorial 1.

**3 September 2026**
- Menyelesaikan beberapa bagian tutorial yang masih belum selesai.
- Memasukkan credential dari ITF.

**5 September 2026**
- Mencari konsep dan tema untuk website portofolio.
- Mulai membuat dan mengembangkan tampilan website.

**6-7 September 2026**
- Melakukan beberapa perubahan pada bio, foto, background, card, hero section, footer, responsive layout, dan menambahkan efek floating.
- Melakukan beberapa penyesuaian tampilan melalui beberapa commit di GitHub.

## AI Disclosure & Usage
Saya menggunakan Claude sebagai alat bantu selama proses pembuatan website. Penggunaan AI membantu saya ketika lupa atau belum memahami cara membuat suatu efek menggunakan CSS.

Contohnya, saya bertanya mengenai cara membuat background pink stripes, memperbesar foto, memberikan padding dan dekorasi pada bagian bio, serta membuat efek floating love yang bergerak di layar. Setelah mendapatkan contoh kode dari AI, saya pelajari dan sesuaikan kembali dengan struktur website yang saya buat.

Berikut beberapa contoh percakapan yang saya gunakan selama proses pembuatan website:

**Prompt:** "Bagaimana cara agar backgroundnya pink stripes?"
**Claude:**
```css
background-image: repeating-linear-gradient(90deg, #f5a3b8, #f5a3b8 40px, #f291a9 40px, #f291a9 80px);
```

**Prompt:** "Bagaimana agar foto saya lebih besar?"
**Claude:** `width: 65vw;`

**Prompt:** "Cara agar di belakang bio saya ada padding, lalu luarnya ada stripes dan lakban?"
**Claude:** `.bio { border: 2px dashed var(--teal); }`, lalu di `.bio::before`, bagian `background-color: #c5d9d8;`

**Prompt:** "Saya mau ada efek love-love terbang di layar."
**Claude:** Menambahkan class `floating-decor` di bagian body dan menambahkan `@keyframes`.

Namun, kode dari AI tidak selalu bisa langsung digunakan karena terkadang tidak sesuai dengan struktur kode yang saya miliki. Karena itu, saya tetap mencoba, mengecek hasilnya, dan melakukan perubahan sendiri. Salah satu contohnya adalah ketika tampilan website pada mobile mengalami masalah saat layar dimiringkan. Saya memperbaikinya sendiri dengan menyesuaikan ukuran gambar menggunakan media query.

Dari proses tersebut, saya menyadari bahwa AI lebih cocok digunakan sebagai alat bantu dan referensi. Saya tetap perlu memahami HTML dan CSS agar bisa menentukan apakah saran yang diberikan sesuai dengan kebutuhan website saya.

## Pertanyaan Reflektif

1. Saya menggunakan elemen semantik HTML5, seperti `<section>` dan `<article>`. Saya menggunakan `<section>` untuk memisahkan bagian utama seperti profile, skills, projects, dan experience. Di dalam beberapa section saya menggunakan `<article>`, contohnya pada bagian projects yang memiliki beberapa project berbeda. Saya tidak menggunakan `<aside>` karena tidak ada informasi tambahan yang perlu dipisahkan dari konten utama.

2. Saat membuat website responsive, tantangan yang saya temukan adalah mengatur ulang posisi dan ukuran elemen ketika berpindah dari desktop ke mobile. Misalnya, bagian skills dan experience yang awalnya terdiri dari beberapa kolom saya ubah menjadi satu kolom pada mobile. Begitu juga dengan projects yang awalnya menggunakan dua kolom menjadi satu kolom. Saya mengevaluasinya dengan melihat bagian mana yang terlalu sempit, terlalu besar, atau menyebabkan tampilan melebar. Salah satu masalah yang saya temukan adalah adanya elemen yang menyebabkan halaman bisa bergeser ke samping, sehingga saya perlu menyesuaikan ukuran beberapa elemen dan menggunakan `overflow-x: hidden`.

3. Karena website saya masih berupa static web, informasi di dalamnya masih harus diubah langsung melalui kode. Jika ingin menambahkan project atau mengubah informasi profile, saya perlu mengubah bagian HTML secara manual. Pada iterasi berikutnya, saya ingin membuat website yang lebih dinamis, misalnya dengan menggunakan database dan Django untuk menyimpan data project, skills, dan experience. Dengan begitu, informasi dapat ditambahkan atau diperbarui tanpa harus mengubah struktur halaman secara langsung.

---

# Tugas 2

## Deskripsi Proyek
Melanjutkan proyek portofolio pada Tugas 1, saya menerapkan pola Model-View-Template (MVT) pada Django untuk menampilkan data secara dinamis. Pada Tutorial 2, saya membuat model `Experience` beserta halaman `/experience/`. Pada tugas ini, saya menambahkan model `Project` beserta halaman `/projects/`, sehingga data project yang sebelumnya statis di halaman utama kini dapat dikelola melalui Django Admin dan ditampilkan secara dinamis.

## Struktur Halaman
- Profile (statis, berisi bio, skills)
- Projects → MVT (dinamis, diambil dari model `Project`)
- Experience → MVT (dinamis, diambil dari model `Experience`)

## Weekly Progress

**9 September 2026**
- Menyelesaikan Tutorial 2 (implementasi MVT: model `Experience`, view, template, routing).
- Menurunkan versi Django ke 5.2 agar kompatibel dengan PostgreSQL di PWS.
- Membuat superuser dan mengisi data Experience melalui Django Admin di production.

**10-13 September 2026**
- Mengerjakan Individual Assignment 2 dengan menambahkan model `Project` beserta view, template, routing, dan unit test terpisah.
- Memasukkan data project (Agrifarm, NUSA-CROP, E-Learnau, dan game Godot) melalui Django Admin.
- Menyesuaikan tampilan halaman Projects dan Experience agar konsisten dengan desain di halaman Profile, termasuk background, warna tombol, dan efek floating.

## AI Disclosure & Usage
Pada Tugas 2, saya juga menggunakan Claude untuk membantu memahami alur MVT (Model-View-Template) pada Django, termasuk cara membuat model baru, menghubungkan view dengan template melalui context, serta menuliskan unit test yang sesuai. Contohnya, saya bertanya bagaimana cara membuat model `Project` dengan field yang sesuai, serta bagaimana menampilkan data tersebut menggunakan `{% for %}` dan menangani kondisi ketika data masih kosong dengan `{% empty %}`. AI juga membantu saya memahami penyebab error seperti `NoReverseMatch` dan `CSRF verification failed` yang saya temui saat proses deployment ke PWS, dengan menjelaskan penyebabnya sehingga saya bisa memperbaikinya sendiri.

Selain itu, AI membantu saya memahami perbedaan antara database lokal (SQLite) dan production (PostgreSQL), khususnya mengapa data yang saya masukkan di satu environment tidak otomatis muncul di environment lain. Pemahaman ini penting agar saya tidak bingung ketika data yang saya tambahkan di lokal tidak langsung terlihat di website production.

## Pertanyaan Reflektif

### Tugas 2

1. Ketika pengguna membuka halaman Projects, browser mengirim permintaan GET ke alamat `/projects/`. Permintaan ini pertama kali diterima oleh `urls.py` pada level proyek (`portofolio/urls.py`), yang mengarahkan semua path selain `/admin/` ke `main.urls` melalui `include()`. Selanjutnya, `main/urls.py` mencocokkan path `projects/` dengan salah satu `urlpatterns` yang sudah didaftarkan, lalu memanggil fungsi view yang bersangkutan, yaitu `show_projects`. Di dalam view, Django mengambil seluruh data dari model `Project` menggunakan `Project.objects.all()`, memasukkannya ke dalam dictionary `context`, kemudian me-render template `projects.html` dengan context tersebut. Template inilah yang menerjemahkan data dari context menjadi HTML menggunakan tag `{% for %}`, sehingga setiap objek `Project` ditampilkan sebagai satu card, dan hasil akhirnya dikirim kembali ke browser pengguna.

2. Data sebaiknya disimpan dalam model karena model merepresentasikan struktur data yang konsisten dan bisa dikelola tanpa perlu menyentuh kode HTML. Jika data ditulis langsung di template, setiap kali saya ingin menambah atau mengubah project, saya harus mengedit file HTML secara manual, sama seperti pada Tugas 1 saat website masih berupa static web. Dengan model, saya cukup menambahkan data lewat Django Admin atau shell, dan perubahan tersebut otomatis muncul di halaman tanpa perlu mengubah struktur template. Ini juga membuat aplikasi lebih mudah dikembangkan ke depannya, misalnya jika suatu saat saya ingin menambahkan fitur pencarian atau filter berdasarkan tech stack, karena data sudah terstruktur di database, bukan tersebar di berbagai bagian HTML.

3. `makemigrations` digunakan untuk membuat berkas migrasi, yaitu instruksi terjadwal yang mencatat perubahan pada model (seperti penambahan field atau model baru) tanpa langsung menerapkannya ke database. Sementara itu, `migrate` digunakan untuk benar-benar menerapkan instruksi dari berkas migrasi tersebut ke database yang sedang digunakan. Contoh nyata yang saya alami adalah ketika saya menambahkan model `Project` baru dengan field seperti `title`, `description`, `tech_stack`, `code_url`, dan `demo_url`. Setelah menuliskan model tersebut di `models.py`, saya menjalankan `python manage.py makemigrations` untuk membuat berkas migrasi yang mendeskripsikan tabel baru ini, lalu menjalankan `python manage.py migrate` agar Django benar-benar membuat tabel tersebut di database SQLite (lokal) maupun PostgreSQL (production).

---

# Tugas 3

## Deskripsi Proyek
Melanjutkan proyek portofolio pada Tugas 2, saya melakukan refactoring seluruh halaman HTML agar melakukan extend terhadap satu template dasar (`base.html`), sehingga navbar dan footer tidak perlu ditulis ulang di setiap halaman. Saya juga menerapkan mekanisme form dan data delivery penuh (create, update, delete, dan JSON) untuk bagian Experience, melengkapi fitur yang sudah lebih dulu diterapkan pada Projects di Tutorial 3.

Sebagai tambahan keamanan, saya menerapkan proteksi password sederhana pada form create, update, dan delete, setelah data project saya sempat dihapus oleh orang lain karena portofolio belum memiliki sistem autentikasi.

## Struktur Halaman
- Profile (statis, berisi bio, skills)
- Projects → MVT + Form (create, delete, search, JSON)
- Experience → MVT + Form (create, **update**, delete, JSON)

## Weekly Progress

**14-16 September 2026**
- Menyelesaikan Tutorial 3 (skeleton `base.html`, form & delete Project, JSON delivery).
- Menambahkan proteksi password sederhana untuk fitur create/delete setelah data project sempat dihapus orang lain.

**17-19 September 2026**
- Mengerjakan Individual Assignment 3 dengan menambahkan fitur create, update, dan delete untuk Experience.
- Membuat `ExperienceForm` dan halaman form terpisah untuk tambah/edit Experience.
- Menambahkan endpoint JSON untuk Experience dan menerapkan deserialize di `show_experience`.
- Menambahkan gambar (thumbnail) pada halaman Experience dan Projects melalui Google Drive.

## AI Disclosure & Usage
Pada Tugas 3, saya menggunakan Claude untuk membantu memahami konsep skeleton template (`extends base.html`), pembuatan form update yang menggunakan instance dari data yang sudah ada, serta cara kerja serialize dan deserialize JSON di Django. Saya juga bertanya bagaimana membuat modal konfirmasi sederhana menggunakan elemen HTML `<dialog>` tanpa perlu library JavaScript tambahan, serta cara menambahkan proteksi password pada form create dan delete agar tidak sembarang orang bisa mengubah data portofolio saya.
Berikut beberapa contoh percakapan yang saya gunakan selama proses pengerjaan Tugas 3:

**Prompt:** "kok abis hapus proyek malah pop up muncul disini bukan pas masukin pw"  
**Claude:** Menjelaskan cara membuat modal `<dialog>` otomatis terbuka kembali saat password salah, dengan menambahkan atribut `{% if password_error %}open{% endif %}` pada tag dialog.

**Prompt:** "gimana biar form update bisa ambil data yang udah ada buat diedit"  
**Claude:** Menjelaskan penggunaan parameter `instance=experience` saat membuat `ExperienceForm`, sehingga form otomatis terisi dengan data lama dan `form.save()` akan mengupdate data yang sama, bukan membuat baru.

**Prompt:** "kok pas tambah proyek gak ada pop up masukin password"  
**Claude:** Menemukan bahwa field password belum ditambahkan sama sekali di form Tambah Project, sehingga `request.POST.get("edit_password")` selalu bernilai kosong dan validasi selalu gagal.

Saya tetap memeriksa setiap kode yang diberikan dan menyesuaikannya dengan struktur project saya sendiri, terutama karena beberapa bagian model saya (seperti tipe `id`) berbeda dari contoh di tutorial.

## Pertanyaan Reflektif

### Tugas 3

1. Kita menggunakan `ModelForm` alih-alih form HTML manual karena `ModelForm` otomatis menghasilkan field input sesuai struktur model, termasuk validasi tipe data (misalnya `URLField` otomatis validasi format URL). Ini menghemat waktu dan mengurangi resiko kesalahan dibanding menulis validasi manual satu per satu. `{% csrf_token %}` wajib ditambahkan karena Django membutuhkan token ini untuk memverifikasi bahwa request POST benar-benar berasal dari form yang di-render oleh server, bukan dari pihak ketiga yang mencoba mengirim request palsu (Cross-Site Request Forgery). Tanpa token ini, form akan ditolak dengan error 403 Forbidden.

2. JSON lebih disukai karena strukturnya lebih ringkas dibanding XML (tidak perlu closing tag untuk setiap elemen), sehingga ukuran datanya lebih kecil dan lebih cepat diproses. JSON juga native dengan JavaScript, bahasa yang paling umum dipakai di sisi frontend, sehingga proses parsing menjadi sangat mudah. Hampir semua bahasa pemrograman modern juga sudah punya dukungan bawaan untuk JSON, membuatnya jadi pilihan standar untuk REST API saat ini.

3. Ketika fungsi view dipanggil untuk mengembalikan data dalam bentuk JSON, alurnya dimulai dari query ke database menggunakan `Model.objects.all()` atau `.filter()`, yang menghasilkan queryset berisi objek-objek Python (instance model Django). Objek-objek ini tidak bisa langsung dikirim sebagai response HTTP karena bukan format teks yang bisa dibaca browser atau aplikasi lain. Di sinilah proses serialization diperlukan: `serializers.serialize("json", queryset)` mengubah objek Python tadi menjadi string JSON yang terstruktur. Hasil string ini kemudian dibungkus dalam `HttpResponse` dengan `content_type="application/json"` supaya browser/client tahu bahwa isinya adalah data JSON, bukan HTML biasa.
