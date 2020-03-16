import sys
import datetime, schedule, time
import logging
import logging.handlers
from helium import start_firefox, press, write, ENTER, TAB, kill_browser
sys.dont_write_bytecode = True
from os import stat

#memulai buka firefox via helium
start_firefox("web.whatsapp.com")
time.sleep(10)

# setting logger config
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler('prog.log', maxBytes=5*1024*1024, backupCount=5)
my_logger.addHandler(handler)

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pmoWa.settings")

import django
django.setup()
from pengingat.models import Resep

my_logger.debug("Mulai program pada {}".format(datetime.datetime.now()))

a = Resep.objects.filter(selesai_minum_obat__gte=datetime.datetime.now()).filter(mulai_minum__lte=datetime.datetime.now())
b = stat('db.sqlite3').st_mtime

def valcheck(w):
	if w:
		w = w.strftime("%H:%M")
	else:
		pass
	return w

def send_wa(d):
    skrg = datetime.datetime.now().hour
    pa_si_so_mal = ""
    if 4 <= skrg < 11:
        pa_si_so_mal = "pagi"
    elif 11 <= skrg < 15:
        pa_si_so_mal = "siang"
    elif 15 <= skrg < 18:
        pa_si_so_mal = "sore"
    else:
        pa_si_so_mal = "malam"
    pesan = "Selamat {}. Jangan lupa saatnya minum obat {} untuk Bpk/Ibu/Sdr {} sebanyak {} {}".format(pa_si_so_mal, d.nama_obat.nama_obat, d.kunjungan_pasien.nama_pasien.nama_pasien, d.jumlah_obat_minum, d.nama_obat.satuan)
    write(d.kunjungan_pasien.nama_pasien.no_whatsapp[3:], into='Search or start new chat')
    press(TAB)
    write(pesan, into='Type a message')
    press(ENTER)

def load_queries():
    global a
    global b
    if b != stat('db.sqlite3').st_mtime:
        a = Resep.objects.filter(selesai_minum_obat__gte=datetime.datetime.now()).filter(mulai_minum__lte=datetime.datetime.now())
    else:
        pass

def watcher():
    sekarang = datetime.datetime.now().strftime("%H:%M")
    for i in a:
    	w1 = i.waktu_minum0
    	w2 = i.waktu_minum1
    	w3 = i.waktu_minum2
    	w4 = i.waktu_minum3
    	w5 = i.waktu_minum4
    	w1 = valcheck(w1)
    	w2 = valcheck(w2)
    	w3 = valcheck(w3)
    	w4 = valcheck(w4)
    	w5 = valcheck(w5)
    	if sekarang == w1 or sekarang == w2 or sekarang == w3 or sekarang == w4 or sekarang == w5:
            send_wa(i)
            my_logger.debug("Pengingat minum {} dikirim ke {} no WA {} pada {}".format(i.nama_obat.nama_obat, i.kunjungan_pasien.nama_pasien.nama_pasien, i.kunjungan_pasien.nama_pasien.no_whatsapp, datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")))
    	else:
    		pass
        
#load_queries()
watcher()
schedule.every().day.at("00:00").do(load_queries)
schedule.every(1).minutes.do(watcher)

try:
    while True:
        schedule.run_pending()
        load_queries()
        time.sleep(1)
except KeyboardInterrupt:
    my_logger.debug("\nUser membatalkan pada {}\nProgram selesai\n".format(datetime.datetime.now()))
finally:
    del(a)
    kill_browser()