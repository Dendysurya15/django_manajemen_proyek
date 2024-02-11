## Tahapan Instalasi
- Run environment python 
- tambahkan database baru di PostgreSql serta sesuaikan konfigurasi di setting.py di kelas App project
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

## Testing Feature
### - Dashboard
- Terdapat button untuk tambah proyek baru dengan route /tambah_proyek
- Terdapat list proyek dalam bentuk card dengan fitur view, edit dan delete

### - Halaman Tugas(per proyek)
- Terdapat button untuk tambah tugas baru 
- List daftar tugas dalam sebuah proyek dilengkapi dengan button untuk edit dan delete


## Stack Tech
- Django
- Bootstrap
- PostgreSql
