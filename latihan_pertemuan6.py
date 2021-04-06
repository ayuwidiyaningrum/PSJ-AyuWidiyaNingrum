import subprocess
import time
import concurrent.futures
from datetime import datetime

print("Mulai monitor.....")

T1 = time.perf_counter()

saat_ini = datetime.now() 

tgl_jam = saat_ini.strftime("%Y-%m-%d %H:%M:%S")

hosts = open("hosts.cfg", 'r')
def check(hosts):
    status, result = subprocess.getstatusoutput("ping -c1 " + hosts )
    if (status == 0):
        return(f'Host {hosts} is UP')
    else:
        return(f'Host {hosts} is DOWN')

with concurrent.futures.ThreadPoolExecutor() as executor: 

    results = executor.map(check, hosts)
    for cetak in results:
        print(tgl_jam , cetak)

T2 = time.perf_counter()

print(f"selesai dalam.. {round(T2-T1,2)} detik")


