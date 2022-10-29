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

![Imagem01](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura01.png)

Após os pré-requisitos acima realizar o clone do repositório: https://github.com/EduardoGomesJr/Sockets

Como a aplicação é divida em duas partes: SERVIDOR e CLIENTE após descompactar o arquivo serão necessários realizar a instalação/configuração em duas etapas.

1-	Servidor (SERVER): na máquina que será usada como servidor criar uma pasta chamada: “Sockets_Server”
MD Sockets_Server (para criar a pasta)

Dentro da pasta copiar os arquivos Sockets_Server.INI, Sockets_Server.PY e Sockets_Server_Win.PY

![Imagem02](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura02.png)

Arquivos:

Sockets_Server.INI: contém a configuração de IP, porta do servidor e pasta (diretório) que contém os arquivos permitidos para copia através do CLIENT. Para os testes apresentados aqui o nome do Server está como LOCALHOST, pois os testes são em ambientes locais. Num ambiente oficial, basta trocar esse nome pelo IP do servidor e porta que será liberada. Exemplo 172.16.0.10 e porta 7070 e indicar um local valido para o DIRECTORY_FILES (pasta que contém os arquivos liberados para copia).

![Imagem03](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura03.png)

A rotina (script) Sockets_Server.py é a rotina usada como servidor (fica rodando (LOOP) em modo serviço aguardando a conexão de algum CLIENT e envia a informação/arquivo solicitada. 
O Sockets_Server_Win.py é uma rotina responsável por criar um serviço PYTHON dentro do Windows.

Para criar/subir o serviço é necessário executar os passos abaixo:

- Acessar o PROMPT de comando como administrador.
- Acessar a pasta criada do Sockets_Server e dentro dela digitar o comando: 

python Sockets_Server.py install <ENTER>

![Imagem04](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura04.png)

			Através do comando acima será criado no serviço do Windows um serviço chamado Sockets_Server o nome e informações exibidas nesse serviço ficam dentro da rotina Sockets_Server.py

			Para conferir o serviço gerado, basta abrir o serviço do Windows e procurar o serviço criado:
   
![Imagem05](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura05.png)

![Imagem06](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura06.png)

Para iniciar/parar o serviço pasta iniciar ele normalmente usando as opções disponíveis.

![Imagem07](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura07.png)

Após o serviço iniciado a parte do servidor não precisa mais ser alterado, pode ficar rodando o tempo necessário. Caso haja necessidade de alguma alteração nas rotinas Sockets_Server.py ou Sockets_Server_Win.py para subir essas alterações para o serviço. Pasta acessar novamente a pasta do Sockets_Server como administrador e executar o comando:

			python Sockets_Server.py update <ENTER>

![Imagem08](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura08.png)

Através desse comando as alterações são enviadas para o serviço criado. 

Caso haja necessidade de excluir o serviço por algum motivo, basta usar o comando abaixo:
			
			sc delete Sockets_Server

![Imagem09](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura09.png)
 
















 
