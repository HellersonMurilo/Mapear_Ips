import socket
import subprocess
import pandas as pd

def coletar_criar_ips():
    ip_local = socket.gethostbyname(socket.gethostname())

    partes_ip = ip_local.split('.')
    ultimo_digito = int(partes_ip[-1])

    if ultimo_digito != 0:
        ultimo_digito = 0
        
    ips_sucesso = []

    for incremento in range(1, 256):
        novo_ip = '.'.join(partes_ip[:-1] + [str(ultimo_digito + incremento)])

        # Executando o comando "ping" no terminal
        try:
            subprocess.run(['ping', '-n', '1', novo_ip], check=True)  # '-n' para Windows, '-c' para outros sistemas
            ips_sucesso.append(novo_ip)
        except subprocess.CalledProcessError:
            if "Host de destino inacessível.": 
                continue

    # Criando um DataFrame pandas com a lista de IPs bem-sucedidos
    df = pd.DataFrame({'IPs com sucesso': ips_sucesso})

    # Salvando o DataFrame em um arquivo CSV
    df.to_csv('ips_mapeados.csv', index=False)

    print(f'Arquivo CSV gerado com sucesso: ips_mapeados.csv')

coletar_criar_ips()
