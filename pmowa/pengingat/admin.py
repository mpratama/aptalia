from django.contrib import admin
from .models import DataPasien, DataObat, Kunjungan, Resep
from django.contrib.auth.models import User, Group
from django.conf import settings

class ResepInline(admin.StackedInline):
    model = Resep
    autocomplete_fields = ['nama_obat']
    extra = 3
    exclude = ['selesai_minum_obat']

class KunjunganAdmin(admin.ModelAdmin):
    inlines = [
        ResepInline,
    ]
    autocomplete_fields = ['nama_pasien']
    list_filter = ['tanggal_kunjungan']
    ordering = ['-tanggal_kunjungan']
    search_fields = ['nama_pasien__nama_pasien']
    list_display = ('nama_pasien', 'tanggal_kunjungan')
    exclude = ('selesai_minum_obat',)
    list_per_page = 20

class DataObatAdmin(admin.ModelAdmin):
    search_fields = ['nama_obat']
    list_display = ('nama_obat', 'satuan')
    list_filter = ['satuan']
    ordering = ['nama_obat']
    list_per_page = 20

class DataPasienAdmin(admin.ModelAdmin):
    search_fields = ['nama_pasien', 'no_whatsapp', 'no_kartu', 'alamat']
    list_display = ('nama_pasien', 'umur', 'alamat', 'no_whatsapp')
    ordering = ['nama_pasien']
    list_per_page = 20

class ResepAdmin(admin.ModelAdmin):
    exclude = ('selesai_minum_obat',)

# Register your models here.
admin.site.register(DataPasien, DataPasienAdmin)
admin.site.register(DataObat, DataObatAdmin)
admin.site.register(Kunjungan, KunjunganAdmin)
#admin.site.register(Resep, ResepAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = settings.SITE_HEADER
admin.site.site_title = settings.SITE_TITLE
admin.site.index_title = settings.INDEX_TITLE
