import subprocess
import time
from AES import*
from test import*


for i in range(1000000):
	pass


print("Starting Compression...")
start = time.time()
print(str(subprocess.run(['zstd', '-v', '--ultra', '-22', 'sensor_data2.csv'])))
end = time.time()
print("COMPRESSION: {} seconds".format(end-start))
process()
print("Compression complete...")
#encrypt_file("sensor_data0.csv.zst")
