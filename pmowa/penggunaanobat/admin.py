from django.contrib import admin
from .models import DataKunjungan, Diagnosa, Resep

# Register your models here.
class ResepInline(admin.TabularInline):
    model = Resep
    autocomplete_fields = ['obat']
    extra = 5

class KunjunganAdmin(admin.ModelAdmin):
    inlines = [
        ResepInline,
    ]
    autocomplete_fields = ['nama_pasien']
    list_filter = ['tanggal_kunjungan', 'nama_dokter']
    ordering = ['-tanggal_kunjungan']
    search_fields = ['nama_pasien__nama_pasien', 'nama_pasien__no_kartu']
    list_display = ('nama_pasien', 'tanggal_kunjungan', 'no_resep',)
    list_per_page = 20

class ResepAdmin(admin.ModelAdmin):
	search_fields = ['kunjungan_pasien__tanggal_kunjungan', 'kunjungan_pasien__diagnosa__diagnosa']
	list_display = ('kunjungan_pasien', 'get_tgl', 'get_no_resep', 'obat', 'jumlah_obat', 'aturan_minum', 'lama_pengobatan', )
	list_filter = ['kunjungan_pasien__tanggal_kunjungan', 'kunjungan_pasien__diagnosa', 'kunjungan_pasien__nama_dokter', 'obat__ab']
	list_per_page = 500
	ordering = ['obat']
	def get_no_resep(self, obj):
		return obj.kunjungan_pasien.no_resep
	get_no_resep.admin_order_field = 'kunjungan_pasien'
	get_no_resep.short_description = 'No R/'
	def get_tgl(self, obj):
		return obj.kunjungan_pasien.tanggal_kunjungan
	get_tgl.admin_order_field = 'kunjungan_pasien__tanggal_kunjungan'
	get_tgl.short_description = 'Tgl'

admin.site.register(DataKunjungan, KunjunganAdmin)
admin.site.register(Diagnosa)
admin.site.register(Resep, ResepAdmin)