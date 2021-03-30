import subprocess
import time
import concurrent.futures

# fungsi mengembalikan nilai float waktu dalam hitungan detik.
T1 = time.perf_counter()

hosts = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "8.8.8.8", "8.8.4.4"]
def check(hosts):
    status, result = subprocess.getstatusoutput("ping -c1 " + hosts)
    if (status == 0):
        return(f'Host {hosts} is UP')
    else:
        return(f'Host {hosts} is DOWN')
#ThreadPoolExecutor subclass dari kelas Executor untuk menampung untuk dijalankan
with concurrent.futures.ThreadPoolExecutor() as executor: 
    results = executor.map(check, hosts)
    for cetak in results:
        print(cetak)

T2 = time.perf_counter()

print(f"selesai dalam.. {round(T2-T1,2)} detik")

