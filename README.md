# Sockets
 Copia de arquivos via SOCKETS (CLIENT/SERVER)
 
 Aplicação para permitir copiar qualquer tipo de arquivo existente no servidor (SERVER) para qualquer máquina local. A configuração de servidor, porta e pasta de origem/destino é definida através de configurações em arquivos INIS. Tanto a aplicação SERVER como o CLIENT possuem arquivos de configuração INIS e podem ser configurados de acordo com a necessidade. Toda solicitação feita pelo CLIENT será registrada no SERVER em arquivo de LOG. Esse arquivo será usado para acompanhamento das solicitações (requisições) e tratamento de possíveis erros. Os arquivos disponíveis para copia são atualizados a cada solicitação ao SERVER e exibidas para o usuário em interface para que seja selecionado/escolhido o arquivo desejado.
 
 # Instalação
 
 Tecnologia Usada:
 
 Tanto o BACK END como FRONT END é desenvolvido em PYTHON. A versão do PYTHON usada é a 3.10, porém o mesmo funcionou corretamente nas versões 3.9 e 3.8. Para instalação/execução será necessário a instalação do PYTHON caso não exista. 

DONWLOAD do PYTHON: https://www.python.org/downloads/

Aplicação desenvolvida para sistemas operacionais Windows. No Linux não foi testada. 

A aplicação precisa de duas bibliotecas externas para o funcionamento. 

- configparser (usada para leitura dos arquivos INIS) 
- pywin32 (usada para criação/instalação do serviço no Windows)

Detalhes no arquivo: requirements.txt

Para instalar ambas utilizar PIP: acesse o prompt de comando (como administrador) e execute os comandos abaixo:

pip install configparser 
pip install pywin32

 
