from django.shortcuts import render, HttpResponse,get_object_or_404, redirect
from django.contrib import messages

from .models import Proyek
from tugas.models import Tugas
def get_status_color(status):
    status_lower = status.lower()

    if status_lower == 'not_started' or status_lower == 'NOT STARTED':
        return 'bg-secondary'
    elif status_lower == 'done':
        return 'bg-success'
    elif status_lower == 'hold':
        return 'bg-warning'
    elif status_lower == 'in_progress':
        return 'bg-primary'
    else:
        return 'bg-warning'

def home(request):
    items = Proyek.objects.all()
    for item in items:
        item.status_color = get_status_color(item.status)
    return render(request,"base.html", {'proyek_arr': items})

def tambah_proyek(request):
    return render(request,"tambah_proyek.html")

def tambah_progress(request, id):
    query = Proyek.objects.get(id=id)
    return render(request,"tambah_progress.html",{'proyek':query})

def insert_new_progress(request, id):
    if request.method =="POST":
        nama_tugas=request.POST.get('nama_tugas')
        progress=request.POST.get('progress')
        tanggal_mulai=request.POST.get('tanggal_mulai')
        estimate_time=request.POST.get('estimate_time')
        proyek_id = id
        query = Tugas(nama_tugas=nama_tugas, progress=progress,tanggal_mulai=tanggal_mulai,estimate_time=estimate_time,proyek_id=proyek_id)
        query.save()

        messages.success(request, 'New Tugas added successfully to id !')

        return redirect('home')
    
def edit_progress_tugas(request, id):
    query = Tugas.objects.get(id=id)
    formatted_tanggal_mulai = query.tanggal_mulai.strftime('%Y-%m-%d')
    
    return render(request,"edit_progress_tugas.html",{'tugas':query,'formatted_tanggal_mulai':formatted_tanggal_mulai})

def update_progress_tugas(request, id):
    if request.method =="POST":
        update_tugas = Tugas.objects.get(id=id)
        update_tugas.nama_tugas=request.POST.get('nama_tugas')
        update_tugas.progress=request.POST.get('progress')
        update_tugas.tanggal_mulai=request.POST.get('tanggal_mulai')
        update_tugas.estimate_time=request.POST.get('estimate_time')
        update_tugas.status = request.POST.get('status')
        update_tugas.save()
        messages.success(request, 'Update Tugas id '+ str(id) + ' successfully !')

        return redirect('home')
    
def edit_proyek(request, proyek_id):
    proyek = get_object_or_404(Proyek, id=proyek_id)
    formatted_tanggal_mulai = proyek.tanggal_mulai.strftime('%Y-%m-%d')
    formatted_estimasi_selesai = proyek.estimasi_selesai.strftime('%Y-%m-%d')
    return render(request, 'edit_proyek.html', {'proyek': proyek, 'formatted_estimasi_selesai': formatted_estimasi_selesai, 'formatted_tanggal_mulai':formatted_tanggal_mulai})

def insertData(request):
    if request.method =="POST":
        nama_proyek=request.POST.get('nama_proyek')
        deskripsi_proyek=request.POST.get('deskripsi_proyek')
        tanggal_mulai=request.POST.get('tanggal_mulai')
        estimasi_selesai=request.POST.get('tanggal_selesai')
        query = Proyek(nama_proyek=nama_proyek, deskripsi_proyek=deskripsi_proyek,tanggal_mulai=tanggal_mulai,estimasi_selesai=estimasi_selesai)
        query.save()

        messages.success(request, 'Proyek added successfully!')

        return redirect('home')

    return render(request, "base.html")

def delete_progress_tugas(request, id):
    
    data = Tugas.objects.get(id=id)
    data.delete()
    messages.success(request, 'Tugas deleted successfully!')
    

    return redirect('home')


def updateData(request,id):
    if request.method =="POST":
        update_query = Proyek.objects.get(id=id)
        update_query.nama_proyek = request.POST.get('nama_proyek')
        update_query.deskripsi_proyek = request.POST.get('deskripsi_proyek')
        update_query.tanggal_mulai = request.POST.get('tanggal_mulai')
        update_query.estimasi_selesai = request.POST.get('tanggal_selesai')
        update_query.save()

        messages.success(request, 'Proyek updated successfully!')

        return redirect('home')

    return render(request, "base.html")

def deleteData(request, id):
    try:
        data = Proyek.objects.get(id=id)
        data.delete()
        messages.success(request, 'Proyek deleted successfully!')
    except Proyek.DoesNotExist:
        messages.error(request, 'Proyek not found.')

    return redirect('home')

