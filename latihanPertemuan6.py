import subprocess
import concurrent.futures
import time
import csv
from datetime import datetime

with open('hosts.cfg') as file:
    fileHosts = file.read().splitlines()

saat_ini = datetime.now() 
tgl_jam = saat_ini.strftime("%Y-%m-%d %H:%M:%S")

def check(hosts):
    status, result = subprocess.getstatusoutput("ping -c1 " + hosts)
    csvFile = open('report-monitor.csv', 'a')
    csvWriter = csv.writer(csvFile)
    if (status == 0):
        csvWriter.writerow([tgl_jam, hosts, 'UP'])
        return(f'{tgl_jam} {hosts} is UP')
    else:
        csvWriter.writerow([tgl_jam, hosts, 'DOWN'])
        return(f'{tgl_jam} {hosts} is DOWN')

while(True):
    # fungsi mengembalikan nilai float waktu dalam hitungan detik.
    T1 = time.perf_counter()
    # proses multithreading
    #ThreadPoolExecutor subclass dari kelas Executor untuk menampung untuk dijalankan
    with concurrent.futures.ThreadPoolExecutor() as executor:
        print("Mulai monitor......")
        results = executor.map(check, fileHosts)
        for cetak in results:
            print(cetak)

    T2 = time.perf_counter()
    print(f"selesai dalam : {round(T2 - T1, 2)} detik \n")
    #jeda waktu 10 detik
    time.sleep(10)