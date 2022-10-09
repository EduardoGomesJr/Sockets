# Rotina: Sockets_Client
# Descrição: CLIENT - Aplicativo para selecionar/copiar arquivo com SOCKETS
# Data: 07/10/2022
# Autor: Eduardo Gomes Júnior

import socket
import time
import configparser
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

# Abre arquivo de configurações (INI).
INI = configparser.ConfigParser()

INI.read_file(open('\\Sockets_Client\\Sockets_Client.ini'))

# Carrega do arquivo INI informações: endereço do servidor/porta/diretório.
SERVER = str(INI.get('Sockets_Client', 'Server'))
PORT = INI.getint('Sockets_Client', 'Port')
DIRATU = str(INI.get('Sockets_Client', 'Directory_Files'))


# Função: listFiles
# Descrição: Retorna lista de arquivos disponíveis para copia (download).
# Data: 07/10/2022
# Autor: Eduardo Gomes Júnior

def listFiles():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((SERVER, PORT))

    namefile = 'FILESATU'

    client.send(namefile.encode())

    data = client.recv(1024)
    data = data.decode('utf-8')
    data = eval(data)

    client.close()

    return data

# Função: download
# Descrição: Realiza copia do arquivo selecionado
# Data: 07/10/2022
# Autor: Eduardo Gomes Júnior


def download():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((SERVER, PORT))

    namefile = str(logs.get())

    client.send(namefile.encode())

    PROGS = 10
    download = 0
    speed = 1

    with open(DIRATU + '//' + namefile, 'wb') as file:

        while True:

            data = client.recv(1024)

            # Atualiza barra de progresso.
            if download < PROGS:
                time.sleep(0.05)
                bar['value'] += (speed/PROGS)*100
                download += speed
                percent.set(str(int((download/PROGS)*100))+"%")
                text.set(str(download) + "/" + str(PROGS) + " Completado")
                window.update_idletasks()

            if not data:
                break
            file.write(data)

        client.close()
        window.destroy()


# Cria interface (tela) para seleção de arquivo que será copiado
window = Tk()
window.title("Copia de Arquivos via Socket - Versão 1.0")

percent = StringVar()
text = StringVar()
logs = StringVar()

label = Label(text="Selecione o arquivo:").pack()

LOGSBox = Combobox(window, textvariable=logs)
LOGSBox['values'] = listFiles()

LOGSBox['state'] = 'readonly'

LOGSBox.bind('<<ComboboxSelected>>')
LOGSBox.pack(fill=X, padx=5, pady=5)

bar = Progressbar(window, orient=HORIZONTAL, length=400)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
GBLabel = Label(window, textvariable=text).pack()
button1 = Button(window, text="Download", command=download).pack()

window.mainloop()
