# Passo 1 - Abrir o sistema              #####CASO QUEIRA INTERROMPER A QUALQUER MOMENTO A AUTOMATIZAÇÃO, ARRASTE SEU CURSOR DO MOUSE PARA O CANTO SUPERIOR ESQUERDO!!!###

import pyautogui
import time

pyautogui.press("win")                                                      # Apertar a tecla windows do sistema operacional.(para linux e mac precisa de alterações.)

pyautogui.write("edge")                                                     # Escrever o navegador que quer ser automatizado. Edge para na busca achar o microsoft edge, poderia ser o chrome(que poderia conter usuários)

pyautogui.PAUSE = 1                                                         # Para o codigo não ficar muito rápido e atropele os processos.

pyautogui.press("enter")                                                    # Aperta a tecla "Enter".

link = "url do site que fará o preenximento do formulario"                  # Colocar o Link do site do sistema que quer trabalhar dentro.
pyautogui.write(link)                                                       # Escreve o link no navegador.

pyautogui.press("enter")

# Passo 2 - Fazer Login

pyautogui.click(x=677, y=399)                                               # Posiciona o mouse para clicar nas coordenadas XY do seu monitor/tela operacional.

email_login = "joao123@teste.com"                                           # Coloque seu e-mail/usuario(e-mail ilustrativo.)

senha_login = "123teste"                                                    # Coloque sua senha.(Senha ilustrativa.)

pyautogui.write(email_login)                                                # Escreve o Email/usuario.

pyautogui.press("tab")                                                      # Preciona a tecla "tab" que vai para o proximo campo.

pyautogui.write(senha_login)                                                # Escreve a Senha.

pyautogui.press("tab")

pyautogui.press("enter")

# Passo 3 - Acessar a tabela

import pandas as pd

tabela = pd.read_csv("seu_arquivo.csv")                                     # Ou escreva o diretório da maquina onde se encontra o arquivo. Pode ser Excel, XML ou qualquer leitor de arquivo.

print(tabela)                                                               # Faz o codigo imprimir no terminal a tabela a ser trabalhada.

time.sleep(2)                                                               # Faz o codigo esperar 2 segundos para voltar a trabalhar(tempo de load do site/servidor carregar outra pagina/etapa)

# Passo 4 - Cadastrar 1 produto

for linha in tabela.index:                                                  # Para cada Linha(index) na tabela
    pyautogui.click(x=685, y=278)

    # codigo
    codigo = tabela.loc[linha, "codigo"]                                    # Na tabela []  "[linha, "coluna"]" A caluna codigo nesse exemplo é a primeira coluna dái depende da ordem a ser preenxida para achar a coluna correta de sua tabela.
    pyautogui.write(str(codigo))                                            # Usamos para escrever o str() que é em formato string, para indicar que é um textyo, não um numero(int, inteiro)
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])                                     # Escreva a observação como string assim se tiver nada lá, apenas preencherá como vazio.

    # retirar o nan
    if obs != "nan":                                                        # Se a Observação estiver vazia, contatá para o python como "nan" = Not a Number. 
        pyautogui.write(str(obs))                                           # "Se obs for DIFERENTE de nan, escreva a observação."

    pyautogui.press("tab")

    pyautogui.press("enter")                                                # Apertar para enviar

    pyautogui.scroll(10000)                                                 # Rola o Scroll do mouse para cima. (valores positivos são para cima, e negativos para baixo.)

# Passo 5 - Repetir o passo 4 até terminar.                                 # Acoplamos no passo 4 para se repetir e automatizar.

#Ajuste o codigo que possa servir a sua automatização.