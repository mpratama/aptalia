# Generated by Django 2.2.10 on 2020-03-16 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataObat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_obat', models.CharField(help_text='Tulis nama obat dan dosisnya', max_length=50)),
                ('satuan', models.CharField(choices=[('TAB', 'Tablet'), ('CAP', 'Kapsul'), ('BKS', 'Bungkus')], help_text='Bentuk sediaan', max_length=3, verbose_name='Bentuk sediaan')),
            ],
            options={
                'verbose_name_plural': 'Data Obat',
            },
        ),
        migrations.CreateModel(
            name='DataPasien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_kartu', models.CharField(default='000', help_text='Masukkan no BPJS / KTP', max_length=20, verbose_name='Nomor Kartu')),
                ('nama_pasien', models.CharField(help_text='Masukkan nama', max_length=30, verbose_name='Nama Pasien')),
                ('alamat', models.CharField(help_text='Masukkan alamat', max_length=50)),
                ('usia', models.DateField(blank=True, help_text='dd-mm-yy', null=True, verbose_name='Tanggal Lahir')),
                ('no_whatsapp', models.CharField(help_text='masukkan dengan format +628XXXXXXXXXX', max_length=15, verbose_name='No Whatsapp')),
            ],
            options={
                'verbose_name_plural': 'Data Pasien',
            },
        ),
        migrations.CreateModel(
            name='Kunjungan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_kunjungan', models.DateField(help_text='Tanggal pasien berobat', verbose_name='Tgl Berobat')),
                ('nama_pasien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pengingat.DataPasien')),
            ],
            options={
                'verbose_name_plural': 'Data Kunjungan',
            },
        ),
        migrations.CreateModel(
            name='Resep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah_obat', models.PositiveSmallIntegerField()),
                ('mulai_minum', models.DateField()),
                ('waktu_minum0', models.TimeField(verbose_name='Waktu minum 1')),
                ('waktu_minum1', models.TimeField(blank=True, null=True, verbose_name='Waktu minum 2')),
                ('waktu_minum2', models.TimeField(blank=True, null=True, verbose_name='Waktu minum 3')),
                ('waktu_minum3', models.TimeField(blank=True, null=True, verbose_name='Waktu minum 4')),
                ('waktu_minum4', models.TimeField(blank=True, null=True, verbose_name='Waktu minum 5')),
                ('jumlah_obat_minum', models.PositiveSmallIntegerField()),
                ('selesai_minum_obat', models.DateField(blank=True, null=True)),
                ('kunjungan_pasien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pengingat.Kunjungan')),
                ('nama_obat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pengingat.DataObat')),
            ],
            options={
                'verbose_name_plural': 'Resep',
            },
        ),
    ]
