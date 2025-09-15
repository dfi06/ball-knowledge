web pws: daffa-ismail-ballknowledge.pbp.cs.ui.ac.id

Tugas 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

di direktori kosong, bikin virtual environment (venv) & masuk ke dalam venv dengan menjalankan

```
python3 -m venv env
source env/bin/activate
```

bikin requirements.txt, masukkan deps yg diperlukan, lalu install deps & init project django dengan

```
pip install -r requirements.txt
django-admin startproject nama_project .
```

bikin & masukkan data sensitif/environment variables (env) ke .env dan .env.prod  
pastikan django menggunakan env & membolehkan localhost di settings.py  
tambahkan juga variable PRODUCTION dari env & ubah config database utk conditionally check PRODUCTION  
jalankan migrasi (meskipun belum ada changes) utk init db sqlite3 lokal

```
python3 manage.py migrate
```

lalu jalankan projek utk memastikan semua berjalan dengan benar

```
python3 manage.py runserver
```

init awal selesai. (commit utk ngesave progress incase perlu backup)  
link repo ke github & pws & boleh push sekarang atau bisa nanti  
(utk pws, janlup isi env di websitenya, samain dgn .env.prod)  
Lanjut ke pembikinan app. bikin app main dgn

```
python manage.py startapp main
```

tambahkan main ke INSTALLED_APPS di settings.py  
bikin folder templates dalam main lalu main.html dalam templates. (setiap app mengelola templatenya masing-masing)  
isi html sesuai yang diperlukan.  
bikin models di models.py sesuai keperluan program.  
buat migration file dan jalankan (lakukan setiap ada perubahan pada models)

```
python manage.py makemigrations
python manage.py migrate
```

di main.py bikin views utk menampilkan html yg tadi.  
atur routing di file urls.py punya main dan punya root.  
commit & push.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

<img width="647" height="381" alt="Screenshot 2025-09-08 at 13 41 37" src="https://github.com/user-attachments/assets/45407a28-1be1-43d3-8407-eaa183926c05" />

3. Jelaskan peran settings.py dalam proyek Django!

Untuk konfigurasi proyek django, contohnya seperti env, database, allowed host, atau app-app yang ada dalam projek.

4. Bagaimana cara kerja migrasi database di Django?

Semua perubahan pada models akan dibuatkan migration file oleh django. Migration file adalah file berisi kode yang memodifikasi database. Kita jalankan command untuk membikin migration file tersebut, lalu kita jalankan filenya.  
Dengan ini, perubahan pada database terlacak & mudah untuk diundo jika perlu.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Karena dibangun diatas python yang syntaxnya mudah dimengerti & sudah pernah diajarkan. Django juga sangat terstruktur & opinionated, mendorong pemula untuk mengikuti best practice. Banyak konsep rumit juga diabstraksi oleh django, membuatnya lebih beginner-friendly.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Tidak, sudah bagus.

Tugas 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Karena untuk mengimplementasi platform kita perlu menyimpan dan mengirim data menggunakan data delivery.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut aku, JSON lebih baik karena data terstruktur dengan cara yang lebih mudah dibaca. JSON lebih popular karena orang-orang menganggap strukturnya lebih simpel, juga lebih kompatibel dengan berbagai bahasa karena stukturnya mirip dengan objek di javascript atau dictionary di python.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

is_valid() mengembalikan true/false berdasarkan apakah datanya aman dan sesuai models atau tidak. Kita perlu untuk aplikasi kita untuk memastikan keamanan dan validasi dari input yang kita terima.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Untuk mencegah serangan CSRF. Pengguna aplikasi kita akan berisiko terkena CSRF attack jika tidak menggunakan csrf_token. Tanpa csrf_token, penyerang bisa memanfaatkan data pengguna tanpa pengetahuan pengguna untuk melancarkan sebuah request ke situs kita seakan-akan yang request adalah pengguna.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

tambahkan 4 function di views.py, function untuk xml, json, xml_by_id, dan json_by_id  
untuk yg non-id, cukup ambil semua data, serialize data, dan return.  
untuk yg makai id, kita perlu menambah parameter id lalu kita ambil data yg punya primary key id tsb.  
selanjutnya kita bikin routing di urls.py untuk memetakan url yang akan menggunakan view function yg telah dibuat.  
Lanjut dengan membikin skeleton (just incase diperluin utk masa depan), dgn bikin base.html di dir templates di root.  
Lalu di settings.py konfigurasi BASE_DIR untuk menggunakan dir templates yg baru saja dibikin.  
Modifikasi main.html utk mengextend base.html.  
Bikin forms.py dalam main, di dalamnya bikin class ProductForm.  
Gunakan ProductForm di views.py dengan membikin view function baru untuk form bernama create_product. Buatkan juga view function untuk detail product bernama show_product yang akan mengambil data sebuah product sesuai id.  
Untuk keduanya kita akan merender sebuah berkas html sehingga buatlah 2 html di templates milik main bernama create_product.html dan product_detail.html  
Isi html create_product dengan form serta gunakan csrf_token, isi product_detail dengan data product, dan tambahkan product_list ke main.html  
Tambahkan konfigurasi CSRF_TRUSTED_ORIGINS di settings.py berisi url web pws  
Bikin routing untuk kedua views yang baru dibikin ke urls.py milik main.  
Jalankan project dan coba tambahkan sebuah product menggunakan form, product yang sudah ditambah dapat dilihat di halaman utama dan juga bisa dilihat detailnya lebih lanjut dengan mengklik tombol detail.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Tidak ada.

screenshot postman keempat url:
<img width="839" height="621" alt="Screenshot 2025-09-15 at 09 01 16" src="https://github.com/user-attachments/assets/1fa97594-ca66-4975-98c8-f40ef9b18007" />
