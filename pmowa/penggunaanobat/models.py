from django.db import models
from pengingat.models import DataPasien, DataObat

# Create your models here.
class Diagnosa(models.Model):
	diagnosa = models.CharField(max_length=20, blank=False, null=False, verbose_name="Nama Penyakit")
	def __str__(self):
		return self.diagnosa
	class Meta:
		verbose_name_plural = "Data Penyakit"

class DataKunjungan(models.Model):
	nama_pasien = models.ForeignKey(DataPasien, on_delete=models.CASCADE)
	tanggal_kunjungan = models.DateField(help_text="Tanggal pasien berobat", verbose_name="Tgl Berobat")
	no_resep = models.CharField(max_length=3, blank=False, null=False, verbose_name="Nomor Resep")
	NM_DR = (
		('nur', 'dr. Nurul Pratiwi'),
		('suz', 'dr. Suzi Leoni'),
		('dwi', 'drg. Dwi Yosta C'),
		('int', 'dr. Intan Larasati'),
		('etc', 'Lainnya')
		)
	nama_dokter = models.CharField(max_length=3, blank=False, null=False, verbose_name="Nama Dokter", choices=NM_DR)
	diagnosa = models.ForeignKey(Diagnosa, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.nama_pasien) + " | " + str(self.tanggal_kunjungan)
	class Meta:
		verbose_name_plural = "Data Kunjungan"

class Resep(models.Model):
	kunjungan_pasien = models.ForeignKey(DataKunjungan, on_delete=models.CASCADE)
	obat = models.ForeignKey(DataObat, on_delete=models.CASCADE, related_name='obat')
	jumlah_obat = models.PositiveSmallIntegerField(blank=False, null=False)
	aturan_minum = models.CharField(max_length=10, help_text="Aturan minum / pakai dalam sehari", verbose_name="Aturan minum")
	lama_pengobatan = models.PositiveSmallIntegerField(help_text="Berapa hari?")
	def __str__(self):
		return str(self.obat)
	class Meta:
		verbose_name_plural = "Resep"