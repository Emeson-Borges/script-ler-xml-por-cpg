import os
import xml.etree.ElementTree as ET

# Caminho para a pasta contendo os XMLs
pasta_xmls = 'C:/Users/itarg/Downloads/Maracanau-Separados/S-1202 - VERIFICAR A SITUACAO'

# Lista de CPFs desejados
cpfs_desejados = ['95017917349',
'03711251382',
'05117921313',
'39241416300',
'01024125378',
'01190266350',
'02524427331',
'01531630383',
'01606676318',
'02694391370',
'03406166369',
'00026860317',
'00392967332',
'01044671343',
'71948155320',
'77420861315',
'81665024372',
'04544950309',
'23044187320',
'04612681320',
'36632724353',
'56770030349',
'62020382334',
'64148610300',
'66268095391',
'39351270300',
'76942945315',
'71449817300',
'77075412353']

# Período de apuração desejado
periodo_apuracao_desejado = '2022-08'

# Diretório para salvar o arquivo de saída único
diretorio_saida = 'D:/ProjetosPycharme/Script Python Busca XML Com CPF Aguardando/dados.txt'

# Abre o arquivo de saída
with open(diretorio_saida, 'w') as arquivo_saida:
    # Loop através de todos os CPFs na lista
    for cpf_desejado in cpfs_desejados:
        cpf_encontrado = False

        # Loop através de todos os arquivos XML na pasta
        for arquivo_xml in os.listdir(pasta_xmls):
            caminho_arquivo_xml = os.path.join(pasta_xmls, arquivo_xml)

            # Parse o XML
            tree = ET.parse(caminho_arquivo_xml)
            root = tree.getroot()

            # Verifica se o CPF está no XML
            cpf_element = root.find('.//{http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_01_00}ideTrabalhador/{http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_01_00}cpfTrab')
            if cpf_element is not None and cpf_element.text == cpf_desejado:
                # Verifica o período de apuração
                per_apur_element = root.find('.//{http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_01_00}ideEvento/{http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_01_00}perApur')
                if per_apur_element is not None and per_apur_element.text == periodo_apuracao_desejado:
                    cpf_encontrado = True

                    # Extraia os dados desejados
                    ide_evento = root.find('.//{http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_01_00}ideEvento').attrib.get('Id', 'N/A')
                    nr_recibo = root.find('.//{http://www.esocial.gov.br/schema/evt/retornoEvento/v1_2_1}nrRecibo').text
                    per_apur = per_apur_element.text

                    # Escreve os dados no arquivo de saída
                    arquivo_saida.write(f"'{ide_evento}', '{nr_recibo}', '{cpf_desejado}', '{per_apur}'\n")

        if not cpf_encontrado:
            print(f"CPF {cpf_desejado} não encontrado nos XMLs.")

print("Dados foram salvos no arquivo de saída.")
