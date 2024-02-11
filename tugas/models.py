from django.db import models
from enum import Enum
from proyek.models import Proyek

# Create your models here.
class StatusEnum(Enum):
    NOT_STARTED = 'Not Started'
    IN_PROGRESS = 'In Progress'
    HOLD = 'Hold'
    DONE = 'Done'

class Tugas(models.Model):
    nama_tugas = models.CharField(max_length=75)
    progress = models.CharField(max_length=200)
    tanggal_mulai = models.DateTimeField()
    tanggal_selesai = models.DateTimeField(null=True, blank=True)
    estimate_time = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in StatusEnum], default=StatusEnum.NOT_STARTED.value)
    proyek_id = models.ForeignKey(Proyek, on_delete=models.CASCADE, related_name='tugas', default=1)

