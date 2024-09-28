"""
Primera forma: nslookup {url}
Segunda forma: nslookup.io
Tercera forma: mxtoolbox.com
Cuarta forma: script pythonoso

Por que el profe nos hizo hacer este cript si ya existian otras maneras????
"""

import socket
import sys
import argparse

parse = argparse.ArgumentParser()
parse.add_argument("-t", "--target", help="Ingresa la URL sin HTTP")
parse = parse.parse_args()

def getIpLokochon(url):
    try:
        ip = socket.gethostbyname(url)
        print(f"La direccion IP de la {url} es: {ip}")

    except:
        print('No se pudo obtener la IP por...')

def main():
    if parse.target:
        getIpLokochon(parse.target)

    else:
        print('Ingrese una direccion sin HTTP')

if __name__ == "__main__":
    try:
        main()
    except keyboardInterrupt:
        sys.exit()
