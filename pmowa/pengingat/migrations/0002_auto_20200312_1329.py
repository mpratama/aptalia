# Generated by Django 3.0.3 on 2020-03-12 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pengingat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kunjungan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_kunjungan', models.DateField(help_text='Tanggal pasien berobat', verbose_name='Tgl Berobat')),
            ],
            options={
                'verbose_name_plural': 'Data Kunjungan',
            },
        ),
        migrations.AddField(
            model_name='dataobat',
            name='ab',
            field=models.BooleanField(default=0, verbose_name='Antibiotik?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataobat',
            name='nama_obat',
            field=models.CharField(help_text='Tulis nama obat dan dosisnya', max_length=50),
        ),
        migrations.AlterField(
            model_name='dataobat',
            name='satuan',
            field=models.CharField(choices=[('TAB', 'Tablet'), ('SYR', 'Sirup'), ('CAP', 'Kapsul'), ('BKS', 'Bungkus'), ('SAL', 'Salep'), ('CRM', 'Krim'), ('PCS', 'Pcs'), ('BOX', 'Kotak'), ('SET', 'Set')], help_text='Bentuk sediaan', max_length=3, verbose_name='Bentuk sediaan'),
        ),
        migrations.AlterField(
            model_name='datapasien',
            name='nama_pasien',
            field=models.CharField(help_text='Masukkan nama', max_length=30, verbose_name='Nama Pasien'),
        ),
        migrations.AlterField(
            model_name='datapasien',
            name='no_kartu',
            field=models.CharField(default='000', help_text='Masukkan no BPJS / KTP', max_length=20, verbose_name='Nomor Kartu'),
        ),
        migrations.AlterField(
            model_name='datapasien',
            name='no_whatsapp',
            field=models.CharField(help_text='masukkan dengan format +628XXXXXXXXXX', max_length=15, verbose_name='No Whatsapp'),
        ),
        migrations.AlterField(
            model_name='datapasien',
            name='usia',
            field=models.DateField(blank=True, help_text='dd-mm-yy', null=True, verbose_name='Tanggal Lahir'),
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
        migrations.AddField(
            model_name='kunjungan',
            name='nama_pasien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pengingat.DataPasien'),
        ),
    ]