# Sockets
 Copia de arquivos via SOCKETS (CLIENT/SERVER)
 
 [![NPM](https://img.shields.io/npm/l/react)](https://github.com/EduardoGomesJr/Sockets/blob/main/LICENCE)
 
 # Projeto
 
 Aplicação para permitir copiar qualquer tipo de arquivo existente no servidor (SERVER) para qualquer máquina local. A configuração de servidor, porta e pasta de origem/destino é definida através de configurações em arquivos INIS. Tanto a aplicação SERVER como o CLIENT possuem arquivos de configuração INIS e podem ser configurados de acordo com a necessidade. Toda solicitação feita pelo CLIENT será registrada no SERVER em arquivo de LOG. Esse arquivo será usado para acompanhamento das solicitações (requisições) e tratamento de possíveis erros. Os arquivos disponíveis para copia são atualizados a cada solicitação ao SERVER e exibidas para o usuário em interface para que seja selecionado/escolhido o arquivo desejado.
 
 # Instalação
 
 ## Tecnologia Usada:
 
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

## Servidor (SERVER): na máquina que será usada como servidor criar uma pasta chamada: “Sockets_Server”
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

Para iniciar/parar o serviço basta iniciar ele normalmente usando as opções disponíveis.

![Imagem07](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura07.png)

Após o serviço iniciado a parte do servidor não precisa mais ser alterado, pode ficar rodando o tempo necessário. 

Assim que o serviço é criado/iniciado dentro da pasta Sockets_Server é criado o arquivo de LOG para monitoramento das solicitações/requisições/envio. O arquivo de LOG é gravado como Sockets-Server.LOG é um arquivo texto e pode ser visualizado com qualquer editor.

![Imagem12](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura12.png)

Caso haja necessidade de alguma alteração nas rotinas Sockets_Server.py ou Sockets_Server_Win.py para subir essas alterações para o serviço. Pasta acessar novamente a pasta do Sockets_Server como administrador e executar o comando:

			python Sockets_Server.py update <ENTER>

![Imagem08](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura08.png)

Através desse comando as alterações são enviadas para o serviço criado. 

Caso haja necessidade de excluir o serviço por algum motivo, basta usar o comando abaixo:
			
			sc delete Sockets_Server

![Imagem09](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura09.png)

Após isso o serviço é excluído do Windows.

Observações: em algumas instalações do serviço pode ocorrer erro de DLLS (bibliotecas) não encontradas. Caso ocorra esse problema pasta copiar os arquivos python310.dll e pywintypes310.dll para dentro da pasta: Python\Python310\lib\site-packages\win32 que o problema é resolvido. PYTHON310 corresponde a versão do Python instalada esse número pode mudar caso seja usado outra versão.

A DLL python310.dll fica no caminho: “\AppData\Local\Programs\Python\Python310” já a pywintypes310.dll em: \AppData\Local\Programs\Python\Python310\Lib\site-packages\pywin32_system32

![Imagem10](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura10.png)

## CLIENT (CLIENTE): para instalação do CLIENT o processo é igual ao SERVER. Deve ser criada uma pasta chamada: Sockets_Client

MD Sockets_Server (para criar a pasta)

Dentro da pasta copiar os arquivos Sockets_Client.INI e Sockets_Client.PYW

O Arquivo INI do CLIENT contém as informações do servidor que será acessado juntamente da sua porta iguais ao do SERVER. A única diferença aqui é o Directory_Files o caminho dele indica onde serão gravados os arquivos copiados do servidor.

 ![Imagem11](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura11.png)
 
 ## Execução:
 
 Com o serviço criado/iniciado, basta executar o rotina (script) Sockets_Cliente.pyw (dentro da pasta Sockets_Client) após isso é carregado a interface de seleção de arquivos.
 
![Imagem13](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura13.png)

Será aberta a tela (interface) para seleção de arquivos. Basta pressionar o COMBOBOX e todos os arquivos disponíveis no servidor são carregados para está lista. Após isso selecionar o arquivo deseja e pressionar o botçao DOWNLOAD. Com isso o arquivo selecionado é copiado do SERVIDOR para o CLIENTE (a pasta que ele irá ser salvo é a pasta informada no arquivo INI do CLIENT).

![Imagem14](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura14.png)

![Imagem15](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura15.png)

![Imagem16](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura16.png)

Após pressionar o botão DOWNLOAD o arquivo selecionado é copiado para o CLIENTE.

![Imagem17](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura17.png)

Realizando outra copia:

![Imagem18](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura18.png)

![Imagem19](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura19.png)

Consultando o arquivo de LOG do SERVIDOR, temos todas as solicitações/requisições realizadas no arquivo:

![Imagem20](https://github.com/EduardoGomesJr/Sockets/blob/main/Imagens/Figura20.png)

Quando é aberta a rotina CLIENT é enviada uma solicitação para o servidor solicitando a relação de arquivos existentes no diretório configurado para copia, após isso essa relação é atualizada no COMBOBOX da rotina, na sequencia o usuário seleciona um determinado arquivo e pede para o servidor mandar para ele, com isso o arquivo é enviado. Todas essas solicitações/requisições são gravadas no LOG do Server.

Observações: na parte do servidor é necessário ter o PYTHON instalado para poder criar/subir o serviço no Windows. Já para o CLIENTE, caso ele não queria instalar o PYTHON pode ser criado um executável da rotina Sockets_Client.PYW. Esse executável terá todas as bibliotecas básicas usadas (deve ser criado um ambiente virtual). 

Para criação do executável, precisa ser instalado o pacote: pyinstaller

pip install pyinstaller

Após isso gerar o executável: pyinstaller --onefile -w Sockets_Client.pyw









 
 
















 
