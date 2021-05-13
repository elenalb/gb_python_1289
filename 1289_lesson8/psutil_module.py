import psutil

# Информация о системных вызовах
print(psutil.cpu_stats())

# информация о диске
print(psutil.disk_usage("C:"))

# информация о состоянии памяти
print(psutil.virtual_memory())
