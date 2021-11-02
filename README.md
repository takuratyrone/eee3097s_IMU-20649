# eee3097s_IMU-20649

# The main program is run by icm-20948.py
Data is read in real time from the IMU and simultaneusly written to a csv file. After a certain period of time (set by python schedule)
the csv file is sent to the compression block and the file is compressed.

## Compression is done in huffman.py
Upon reception of the csv file, the file is compressed. After compression the compressed file is sent to the encryption block to be encrypted.

## Encryption is done in AES.py
Upon reception of the compressed file, the file is encrypted, decrypted and sent back to the compression block, (huffman.py), for decompression.

## Other source files
gzip_comp.py, zlib_comp.py, lz4_comp.py, zstd_comp.py were used to test the different compression algorithms.
test.py was used to monitor CPU and RAM usage of the different subsystems (compression and encryption)
