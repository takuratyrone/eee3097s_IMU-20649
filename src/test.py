from processing import*

def process():
	# CPU informatiom
	CPU_temp = getCPUtemperature()
	CPU_usage = getCPUuse()

	# RAM information
	# Output is in kb, here I convert it in Mb for readability
	RAM_stats = getRAMinfo()
	RAM_total = round(int(RAM_stats[0]) / 1000,1)
	RAM_used = round(int(RAM_stats[1]) / 1000,1)
	RAM_free = round(int(RAM_stats[2]) / 1000,1)

	# Disk information

	print("Total RAM: {} MB".format(RAM_total))
	print("RAM Used: {} MB".format(RAM_used))
	print("Free RAM: {} MB".format(RAM_free))
	print("CPU Usage: {} %".format(CPU_usage))

