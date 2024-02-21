import argparse as ap
from functions import ram_usage,vram_usage, iout_options

def run():
    #estableciendo los relas de los argumentos
    parser=ap.ArgumentParser(description="Aplicacion para manipular ls memoria en linux "
                        +"y dispositivos de disco")
    parser.add_argument("-r" , "--ram", action="store_true", help="Acceder a las funciones"
                        +" de la memoria ram")
    parser.add_argument("-v" , "--vram", action="store_true", help="Acceder a las funciones"
                        +" de la memoria ram virtual")
    parser.add_argument("-d" , "--device", action="store_true", help="Acceder a las funciones"
                        +" de la administracion de discos")
    parser.add_argument("-m" , "--manual", action="store_true", help="Acceder a las funciones "
                        +"de la ayuda de la aplicacion")
    parser.add_argument("Opciones",
                        nargs="?",
                        default=False,
                        help="opciones de la app como valor de entrada")
#obteniendo los argumentos de la app
    args=parser.parse_args()
    if args.ram:
        ram_usage(args.Opciones)
    elif args.vram:
        vram_usage()
    elif args.device:
        iout_options()
    else:
        print("""
[args]
args:
-r     --ram     Acceder a las opciones de memmoria
-v     --vram    Acceder a las opciones de la memoria Virtual
-d     --device  Accede a las opciones de los Discos en linux
-m     --manual  Muestra el menu de opciones de la aplicacion


            """)
        
if __name__=="__main__":
    run()