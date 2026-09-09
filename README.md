# Personal Portfolio
**Nama:** Naurah Claradinda Aulia Pane
**NPM:** 2506657163
**Kelas:** PBP-A

## Deskripsi Proyek
Website portofolio pribadi yang saya buat menggunakan **Django, HTML, dan CSS** dengan Visual Studio Code sebagai code editor. Website ini berisi informasi mengenai profil, skills, project, dan experience saya.

Website dapat diakses melalui: https://naurah-claradinda-myportofolio.pws.cs.ui.ac.id/

## Konsep Ide

Saya menggunakan konsep **handmade scrapbook** untuk memberikan kesan yang lebih personal, playful, dan tidak terlalu formal. Saya juga menambahkan beberapa elemen dekoratif seperti background bergaris, efek lakban, gambar, dan floating love agar tampilannya lebih sesuai dengan konsep yang saya inginkan.

## Teknologi yang Digunakan

* Python
* Django
* HTML
* CSS
* Visual Studio Code

## Design & Resources

* W3Schools
* Inspirasi background dan photo editing dari Instagram Hiraeyq

## Cara Menjalankan Website

1. Clone repository
2. Masuk ke folder project
   cd myportofolio-naurah
3. Aktifkan virtual environment
   env\Scripts\activate
4. Install dependencies
   pip install -r requirements.txt
5. Jalankan server
   python manage.py runserver
6. Buka website melalui browser

## Struktur Halaman

* Profile
* Skills
* Projects
* Experience

## Weekly Progress

### 31 Agustus 2026

* Mengikuti Tutorial 0 sesuai langkah yang diberikan.
* Membuat project awal dan `requirements.txt`.

### 1 September 2026

* Menyelesaikan Tutorial 1.

### 3 September 2026

* Menyelesaikan beberapa bagian tutorial yang masih belum selesai.
* Memasukkan credential dari ITF.

### 5 September 2026

* Mencari konsep dan tema untuk website portofolio.
* Mulai membuat dan mengembangkan tampilan website.

### 6-7 September 2026
* Melakukan beberapa perubahan pada bio, foto, background, card, hero section, footer, responsive layout, dan menambahkan efek floating.
* Melakukan beberapa penyesuaian tampilan melalui beberapa commit di GitHub.

## AI Disclosure & Usage

Saya menggunakan **Claude** sebagai alat bantu selama proses pembuatan website. Penggunaan AI membantu saya ketika lupa atau belum memahami cara membuat suatu efek menggunakan CSS.

Contohnya, saya bertanya mengenai cara membuat **background pink stripes**, memperbesar foto, memberikan padding dan dekorasi pada bagian bio, serta membuat efek **floating love** yang bergerak di layar. Setelah mendapatkan contoh kode dari AI, saya pelajari dan sesuaikan kembali dengan struktur website yang saya buat.

AI juga membantu ketika saya membutuhkan referensi untuk beberapa bagian CSS yang sudah saya lupa.
Berikut beberapa contoh percakapan yang saya gunakan selama proses pembuatan website:
Prompt: “Bagaimana cara agar backgroundnya pink stripes?”
claude: - background-image: repeating-linear-gradient(90deg, #f5a3b8, #f5a3b8 40px, #f291a9 40px, #f291a9 80px );
Prompt: “Bagaimana agar foto saya lebih besar?”
claude: width: 65vw;
Prompt: “Cara agar di belakang bio saya ada padding, lalu luarnya ada stripes dan lakban?”
claude: .bio{  border: 2px dashed var(--teal);}, lalu di .bio::before, bagian background-color: background-color: #c5d9d8;
Prompt: “Saya mau ada efek love-love terbang di layar.”
claude: tambah menambahkan class="floating-decor" di bagian body dan menambahkan @keyframes

Namun, kode dari AI tidak selalu bisa langsung digunakan karena terkadang tidak sesuai dengan struktur kode yang saya miliki. Karena itu, saya tetap mencoba, mengecek hasilnya, dan melakukan perubahan sendiri. Salah satu contohnya adalah ketika tampilan website pada mobile mengalami masalah saat layar dimiringkan. Saya memperbaikinya sendiri dengan menyesuaikan ukuran gambar menggunakan media query.

Dari proses tersebut, saya menyadari bahwa AI lebih cocok digunakan sebagai alat bantu dan referensi. Saya tetap perlu memahami HTML dan CSS agar bisa menentukan apakah saran yang diberikan sesuai dengan kebutuhan website saya.

## Pertanyaan Reflektif

### Tugas 1

1. **Saya menggunakan elemen semantik HTML5**, seperti `<section>` dan `<article>`. Saya menggunakan `<section>` untuk memisahkan bagian utama seperti profile, skills, projects, dan experience. Di dalam beberapa section saya menggunakan `<article>`, contohnya pada bagian projects yang memiliki beberapa project berbeda. Saya tidak menggunakan `<aside>` karena tidak ada informasi tambahan yang perlu dipisahkan dari konten utama.

2. Saat membuat website responsive, tantangan yang saya temukan adalah mengatur ulang posisi dan ukuran elemen ketika berpindah dari desktop ke mobile. Misalnya, bagian skills dan experience yang awalnya terdiri dari beberapa kolom saya ubah menjadi satu kolom pada mobile. Begitu juga dengan projects yang awalnya menggunakan dua kolom menjadi satu kolom. Saya mengevaluasinya dengan melihat bagian mana yang terlalu sempit, terlalu besar, atau menyebabkan tampilan melebar. Salah satu masalah yang saya temukan adalah adanya elemen yang menyebabkan halaman bisa bergeser ke samping, sehingga saya perlu menyesuaikan ukuran beberapa elemen dan menggunakan `overflow-x: hidden`.

3. Karena website saya masih berupa static web, informasi di dalamnya masih harus diubah langsung melalui kode. Jika ingin menambahkan project atau mengubah informasi profile, saya perlu mengubah bagian HTML secara manual. Pada iterasi berikutnya, saya ingin membuat website yang lebih dinamis, misalnya dengan menggunakan database dan Django untuk menyimpan data project, skills, dan experience. Dengan begitu, informasi dapat ditambahkan atau diperbarui tanpa harus mengubah struktur halaman secara langsung.

