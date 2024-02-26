###########################################################
# PROGRAMA CALCULADOR DE PONTO VIA WEB
# INICIO DO DESENVOLVIMENTO 13/07/2023
# KAIUS DE PAULA
###########################################################

# Objetivo: Receber a batida de entrada, saída e retorno de almoço, para calcular a hora para saída. 

from datetime import datetime, timedelta
from pyweb import pydom

def get_element(element):
    time = pydom[f"#{element}"].value[0]
    if time == "":
        pydom["#hora_saida"].html = "Insira todas as marcações antes de calcular a saída!"
        return None
    return pydom[f"#{element}"].value[0]

def calcular_saida(event):
    primeira = get_element("entrada_1")
    segunda = get_element("saida_1")
    terceira = get_element("entrada_2")

    if not all([primeira, segunda, terceira]):  # Verifica se alguma das marcações está vazia
        return  # Para a execução se alguma estiver vazia

    if terceira < segunda or segunda < primeira:
        pydom["#hora_saida"].html = "Entrada de marcação inválida! Confira se o tempo de entrada e saída fazem sentido."
        return 
    
    # Coleta de inputs
    primeira = datetime.strptime(primeira, '%H:%M')
    segunda = datetime.strptime(segunda, '%H:%M')
    terceira = datetime.strptime(terceira, '%H:%M')
    expediente = timedelta(hours=int(pydom[f"#expediente"].value[0]))

    faltam_x_horas = expediente - (segunda - primeira)
    saida = terceira + faltam_x_horas
    saida = saida.strftime("%H:%M")
    pydom["#hora_saida"].html = f"Você precisa sair às {saida}."
