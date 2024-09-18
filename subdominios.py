import requests
from os import path
import argparse
import sys

print('Imagina programar y no hacerlo por terminal 🥱')

#conf
parser = argparse.ArgumentParser(description='Script para buscar subdominios.')
parser.add_argument('-t','--target', help='Indica el dominio objetivo', required=True)
args = parser.parse_args()

def main():
    if path.exists('subdominios.txt'):
        with open('subdominios.txt', 'r') as wordlist:
            subdominios = wordlist.read().splitlines()

        if not subdominios:
            print("El archivo subdominios.txt esta vacio.")
            return

        for subdominio in subdominios:
            url = f"http://{subdominio}.{args.target}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"[+] Subdominio valido: {url}")
                else:
                    print(f"[-] Subdominio no valido: {url}")
            except requests.exceptions.RequestException as e:
                print(f"[!] Error al conectar con {url}: {e}")
    else:
        print("No se encontro el archivo subdominios.txt con los dominios a buscar.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Script interrumpido por el usuario.")
        sys.exit()
