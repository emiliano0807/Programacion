import os
import subprocess
from graficaO import grafic_Mem

def ram_usage(opcion):
    """ Funcion que muestra las funciones de la ram"""
    print("""Memoria Ram""")

    while True:
        opcion=input("""
    I Muestra la informacion de la memoria real
    M Muestra la informacion de la memomora Cache
    E Elimina la memoria cache
    O Muestra la opciones
                    --->""")
        if opcion and opcion.upper()=="I":
            output=subprocess.getoutput('cat /proc/meminfo | grep "Mem" && cat /proc/meminfo | grep "Cache"')
            print(output)
            grafic_Mem()
            memTotal=int (subprocess.getoutput('cat /proc/meminfo | grep "MemTotal" | awk \'{print $2}\''))
            MemFree = int(subprocess.getoutput('cat /proc/meminfo | grep "MemFree" | awk \'{print $2}\''))
            MemAvailable = int(subprocess.getoutput('cat /proc/meminfo | grep "MemAvailable" | awk \'{print $2}\''))
            Cached= int(subprocess.getoutput('cat /proc/meminfo | grep "Cached" | awk \'{print $2}\' | head -n 1'))
            SwapCached = int(subprocess.getoutput('cat /proc/meminfo | grep "SwapCached" | awk \'{print $2}\''))
            #grafica_RamG(MemTotal, MemFree, MemAvailable, Cached, SwapCached)
            
        elif opcion and opcion.upper()=="M":
            os.system('sudo free -m | grep "caché" | awk \'{print$5}\' && sudo free -m | grep "Mem" | awk \'{print$6}\' ')
        elif opcion and opcion.upper()=="E":
            os.system('sudo sync && sudo sysctl vm.drop_caches=1')
        elif opcion and opcion.upper()=="0":
            print("""
                [Opciones]
        args:
                I Muestra la informacion de la memoria real
                M Muestra la  informacion de la memoria Cache
                E Elimina la memoria cache
                O Muestra la opciones
                Ej: py main.py -r i
                py main.py -r e
                py main.py-r m
                """)
        else:
            print("""
        |--------------------------|
        |(I)Informacion de la memoria RAM|
        |(M)Muestra la informacion de la memoria Cache|
        |(E)Elimina la memoria cache|
        |(S)Salir|
        |-----------------------------|
        |""")
            return
def vram_usage(opcion):
        """Funcion que muestra las opciones de la memoria virtual"""
        print("""
                """)
        while True:
            opcion=input("""
                        |-------------------------------|
                        |(I)Informacion de la memoria virtual|
                        |(S)Salir|
                        |---------------------------------|
                        --->""")
            if opcion.upper()== "I":
                os.system('cat /proc/meminfo | grep "Swap"')
            else:
                return
def iout_options(opcion):
    """Funcion para mostrar discos montados en la maquina"""
    print("""
    """)
    while True:
        opcion= input("""
        |------------|
        |(L)Listar discos|
        |(D)Desmontar discos|
        |(S)Salir|
        |---------------|
        |---->""")
        if opcion and opcion.upper()=="L":
            os.system('sblk -o NAME,TYPE,SIZE,MOUNTPOINT |grep "nvm"')
        elif opcion and opcion.upper()=="D":
            os.system('lsblk -o NAME,TYPE,SIZE,MOUNTPOINT |grep "nvm"')
            disco=input("Escriba el nombre del disco a desmontar (ej.) nvme0n1p1")
            os.system(f"sudo eject /dev/{disco}")
        elif opcion and opcion.upper()=="S":
            return
        else:
            print('Opcion incorrecta')

    