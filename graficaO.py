import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import subprocess

def grafic_Mem():
    inicio = time.time()
    etiquetas = ['Total','Libre', 'Disponible', 'Cached','Swap Usada']
    valores = [0, 0, 0, 0, 0] 
    fig, ax = plt.subplots()
    def actualizar_grafica(i):
        ax.clear()
        valores[0] = int(subprocess.getoutput('cat /proc/meminfo | grep MemTotal: | awk \'{print$2}\'').replace('\n', ''))  
        valores[1] = int(subprocess.getoutput('cat /proc/meminfo | grep MemFree: | awk \'{print$2}\'').replace('\n', ''))  
        valores[2] = int(subprocess.getoutput('cat /proc/meminfo | grep MemAvailable: | awk \'{print$2}\'').replace('\n', ''))  
        valores[3] = int(subprocess.getoutput('cat /proc/meminfo | grep Cached: | awk \'{print$2}\' | head -n 1').replace('\n', ''))  
        valores[4] = int(subprocess.getoutput('cat /proc/meminfo | grep SwapCached: | awk \'{print$2}\'').replace('\n', '')) 
        

        colores = ax.bar(etiquetas, valores, color=['brown', 'gray', 'blue', 'pink', 'green'])

        for bar, valor in zip(colores, valores):
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, yval, round(valor, 2), ha='center', va='bottom')
        
        ax.set_title('Uso de Memoria RAM')
        ax.set_ylabel('Cantidad de uso en KB')
        plt.pause(0.001)

    ani=FuncAnimation(fig, actualizar_grafica, interval=1000, save_count=10)
    plt.show()
    fin = time.time()
    print("Tiempo de visualizacion: ", fin - inicio)