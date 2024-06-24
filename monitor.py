import os
import psutil
import time
from datetime import datetime

def get_cpu_temp():
    try:
        temp = os.popen("sensors | grep 'Core 0' | awk '{print $3}'").readline().strip()
        return temp
    except Exception as e:
        return f"Error gettig CPU temperature: {e}"
    
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    ram = psutil.virtual_memory()
    return ram.percent

def log_performance():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu_temp = get_cpu_temp()
    cpu_usage = get_cpu_usage()
    ram_usage = get_ram_usage()
    
    log_entry = f"{now}, CPU Temp: {cpu_temp}, CPU Usage {cpu_usage}, RAM Usage: {ram_usage}%\n"
    
    with open("/logs/performance.log", "a") as log_file:
        log_file.write(log_entry)

if __name__ == "__main__":
    while True:
        log_performance()
        # Sleep for 12 hours (43200 seconds) to log twice a day
        time.sleep(43200)
    