import os
import sys
import argparse
"""
command = "nslookup google.com"
respuesta = os.system(command)
print(respuesta)
"""

parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help='Introduce la direccion ip de la victima')
parse = parse.parse_args()


def get_ip(target):
    try:
        res = os.system(f'nslookup {target}')
        print(res)
    except:
        print('[-] No se pudo obtener la ip')
        sys.exit(1)


def main():
    if parse.target:
        get_ip(parse.target)
    else:
        print('[-] Debes indicar la URL')
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except keyboardInterrupt:
        sys.exit()
