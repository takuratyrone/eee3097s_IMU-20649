import subprocess
import time
from AES import*
from test import*

print("Starting Compression...")
start = time.time()
print(str(subprocess.run(['lz4', '-kv', '--fast', 'sensor_data2.csv'])))
end = time.time()
print("COMPRESSION: {} seconds".format(end-start))
print("Compression complete...")
process()
