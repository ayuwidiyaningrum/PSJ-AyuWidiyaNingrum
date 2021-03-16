import sys
import subprocess

if(len(sys.argv) <= 1):
    sys.exit('Gagal:IP address belum diberikan')
else:
    ip = (sys.argv[1])
    status, result = subprocess.getstatusoutput("ping -c3 " + ip)
    # Status = 0 menunjukan proses berjalan dengan sukses
    if(status == 0):
        print(f'Host {ip} is UP')
    else:
        print(f'Host {ip} is DOWN')