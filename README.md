web pws: daffa-ismail-ballknowledge.pbp.cs.ui.ac.id

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

Request Client  
️️|  
V  
urls.py (routing: URL pada request dicocokkan dengan views yang telah dibuat)  
|  
V  
views.py (menyatukan model & template, mengatur apa yang dikirim ke client)  
|--> models.py <--> Database  
|   (models adalah orm. berisi struktur tabel & query. Dapat mensuplai data ke view. Dapat akses data di db jika perlu)  
|  
|--> template (HTML yg akan menggunakan data dari view)  
|  
V  
HTTP response berupa berkas html yg sudah diproses oleh view  

3. Jelaskan peran settings.py dalam proyek Django!

Untuk konfigurasi proyek django, contohnya seperti env, database, allowed host, atau app-app yang ada dalam projek.  

4. Bagaimana cara kerja migrasi database di Django?

Semua perubahan pada models akan dibuatkan migration file oleh django. Migration file adalah file berisi kode yang memodifikasi database. Kita jalankan command untuk membikin migration file tersebut, lalu kita jalankan filenya.  
Dengan ini, perubahan pada database terlacak & mudah untuk diundo jika perlu.  

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Karena dibangun diatas python yang syntaxnya mudah dimengerti & sudah pernah diajarkan. Django juga sangat terstruktur & opinionated, mendorong pemula untuk mengikuti best practice. Banyak konsep rumit juga diabstraksi oleh django, membuatnya lebih beginner-friendly.  

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Tidak, sudah bagus.
