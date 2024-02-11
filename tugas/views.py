from django.shortcuts import render, get_object_or_404
from .models import Tugas, Proyek

def get_status_color(status):
    status_lower = status.lower()

    if status_lower == 'not_started' or status == 'NOT_STARTED':
        return 'bg-secondary'
    elif status_lower == 'done':
        return 'bg-success'
    elif status_lower == 'hold':
        return 'bg-warning'
    elif status_lower == 'in_progress':
        return 'bg-primary'
    else:
        return 'bg-warning'
    
def view_tugas(request, proyek_id):
    proyek = get_object_or_404(Proyek, id=proyek_id)
    tugas_list = Tugas.objects.filter(proyek_id=proyek_id)


    for tugas in tugas_list:
        tugas.status_color = get_status_color(tugas.status)

    return render(request, 'view_tugas.html', {'proyek': proyek, 'tugas_list': tugas_list})
