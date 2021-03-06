# Generated by Django 3.0.3 on 2020-03-12 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pengingat', '0002_auto_20200312_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataKunjungan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_kunjungan', models.DateField(help_text='Tanggal pasien berobat', verbose_name='Tgl Berobat')),
                ('no_resep', models.CharField(max_length=3, verbose_name='Nomor Resep')),
            ],
            options={
                'verbose_name_plural': 'Data Kunjungan',
            },
        ),
        migrations.CreateModel(
            name='Diagnosa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosa', models.CharField(max_length=20, verbose_name='Nama Penyakit')),
            ],
            options={
                'verbose_name_plural': 'Data Penyakit',
            },
        ),
        migrations.CreateModel(
            name='Resep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah_obat', models.PositiveSmallIntegerField()),
                ('aturan_minum', models.CharField(help_text='Aturan minum / pakai dalam sehari', max_length=10, verbose_name='Aturan minum')),
                ('lama_pengobatan', models.PositiveSmallIntegerField(help_text='Berapa hari?')),
                ('kunjungan_pasien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='penggunaanobat.DataKunjungan')),
                ('obat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obat', to='pengingat.DataObat')),
            ],
            options={
                'verbose_name_plural': 'Resep',
            },
        ),
        migrations.AddField(
            model_name='datakunjungan',
            name='diagnosa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='penggunaanobat.Diagnosa'),
        ),
        migrations.AddField(
            model_name='datakunjungan',
            name='nama_pasien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pengingat.DataPasien'),
        ),
    ]
