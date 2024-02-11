from django.db import models
from enum import Enum
# Create your models here.
class StatusEnum(Enum):
    NOT_STARTED = 'Not Started'
    IN_PROGRESS = 'In Progress'
    HOLD = 'Hold'
    DONE = 'Done'

class Proyek(models.Model):
    nama_proyek = models.CharField(max_length=75)
    deskripsi_proyek = models.CharField(max_length=200)
    tanggal_mulai = models.DateField()
    estimasi_selesai = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[(tag.name, tag.value) for tag in StatusEnum],
        default=StatusEnum.NOT_STARTED.value  # Set the default value
    )
