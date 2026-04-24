#mi primer proyecto; simple_ping.py
import os

# 1. Definimos la direccion IP a la que queremos contactar
# 8.8.8.8 es el servidor DNS de Google, casi siempre esta activo
target = "8.8.8.8" 

print(f"--- Iniciando prueba de conexion con: {target} ---")

# 2. Usamos os.system para ejecutar un comando de terminal (Ping)
# El parametro '-c 1' es para que solo mande un paquete y sea rapido
response = os.system(f"ping -c 1 {target}")

# 3. En sistemas Linux, si el resultado es 0, la conexion fue exitosa
if response == 0:
    print("==========================================")
    print(f"  SUCCESS: {target} is UP and RUNNING ")
    print("==========================================")
else:
    print("==========================================")
    print(f"  ERROR: {target} is UNREACHABLE ")
    print("==========================================")
