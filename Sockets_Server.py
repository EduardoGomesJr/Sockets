# Rotina: Sockets_Server
# Descrição: SERVER - Aplicativo SERVER.
# Data: 12/10/2022
# Autor: Eduardo Gomes Júnior

import socket
import os
import configparser
import logging
from Sockets_Server_Win import Sockets_Server_Win

# Classe: Start_Sockets_Server
# Descrição: Classe para iniciar serviço no Windows
# Data: 12/10/2022


class Sockets_Server(Sockets_Server_Win):
    _svc_name_ = "Sockets_Server"
    _svc_display_name_ = "Sockets_Server"
    _svc_description_ = "Serviço para Copia de arquivos via SOCKETS (CLIENT/SERVER)"

    # Rotina: start
    # Descrição: Inicia serviço
    # Data: 12/10/2022
    def start(self):
        self.isrunning = True

    # Rotina: stop
    # Descrição: Parar serviço
    # Data: 12/10/2022
    def stop(self):
        self.isrunning = False

    # Rotina: main
    # Descrição: Rotina que recebe conexões e envia arquivos solicitados
    # Data: 12/10/2022
    def main(self):

        # Criação/configuração de arquivo de LOG
        logging.basicConfig(level=logging.INFO, filename="\\Sockets_Server\\Sockets_Server.log",
                            format="%(asctime)s - %(levelname)s - %(message)s")

        # Abre arquivo de configurações (INI).
        INI = configparser.ConfigParser()

        INI.read_file(open('\\Sockets_Server\\Sockets_Server.ini'))

        # Carrega do arquivo INI informações: endereço do servidor/porta/diretório.
        SERVER = str(INI.get('Sockets_Server', 'Server'))
        PORT = INI.getint('Sockets_Server', 'Port')
        DIRATU = str(INI.get('Sockets_Server', 'Directory_Files'))

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server.bind((SERVER, PORT))
        server.listen()

        logging.info("Sockets_Server - Versão 1.0")
        logging.info("Aguardando conexões...")

        while True:

            connection, andress = server.accept()

            logging.info(f"Conectado : {andress}")

            namefile = connection.recv(1024).decode()

            if namefile == 'FILESATU':

                FILESATU = os.listdir(DIRATU)
                FILEREL = str(FILESATU)

                connection.sendall(FILEREL.encode())
            else:

                with open(DIRATU + '//' + namefile, 'rb') as file:

                    for data in file.readlines():
                        connection.send(data)

            connection.close()

            if namefile == 'FILESATU':
                logging.info(f"Relação de arquivos enviados para: {andress}")
            else:
                logging.info(f"Arquivo: {namefile} enviado para : {andress}")

            logging.info(f"Desconectando: {andress}")


if __name__ == '__main__':
    Sockets_Server.parse_command_line()
