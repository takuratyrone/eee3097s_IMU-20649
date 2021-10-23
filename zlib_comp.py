# import zlib and decompress
import zlib
import time
from AES import*

def compress_file(filename):
	f = open(filename, "r")

	# using zlib.compress(s) method
	start = time.time()
	t = zlib.compress(f.read().encode('utf-8'))
	#print("Compressed String")
	end = time.time()
	print(f"Compression: ", end-start)
	#print(t)
	#print(str(t.decode('utf-8', 'ignore')))
	returned_data = encrypt_file(str(t))
	start2 = time.time()
	#print("\nDecompressed String")
	u = zlib.decompress(returned_data.encode('utf-8'))
	#print(t)
	end2 = time.time()
	print("Decompression: ", end2-start2)

	f1 = open("zlib_compressed.txt", "wb")
	f1.write(t)
	f1.close()
