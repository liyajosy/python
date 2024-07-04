#!/usr/bin/env python3
import shutil
import psutil
cpu_use = psutil.cpu_percent(0.5)
du = shutil.disk_usage("/")
print (du)
print(cpu_use)

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def main(): 
   
    if check_disk_full(disk="/", min_gb=2, min_percent=10):
        print("Disk full.")
        sys.exit(1)
    
    print("Everything ok")
    sys.exit(0)

main()
