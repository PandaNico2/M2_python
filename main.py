import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np


caminho_arquivo = 'banco/Transit Incidents Brazil/Dados_PRF_23.csv'

dados = pd.read_csv(caminho_arquivo, encoding='ISO-8859-1', sep=';')
# print(dados.dtypes)


def aplicar_filtro_simples(dados, data_inicio, output_filename):
    filtro_simples = dados[dados['data_inversa'] > data_inicio]
    filtro_simples.to_csv(output_filename, index=False)
    # print(filtro_simples)
    print('Filtro simples OK')


def aplicar_filtro_composto(dados, feridos_leves, ilesos, output_filename):
    filtro_composto = dados[(dados['feridos_leves'] == feridos_leves) & (dados['ilesos'] == ilesos)]
    filtro_composto.to_csv(output_filename, index=False)
    # print(filtro_composto)
    print('Filtro composto OK')


def gravidade_ferimentos(dados, filename):
    filtro_idade = dados['pessoas'] <= 20
    pessoas_filtradas = dados[filtro_idade]

    feridos_1 = pessoas_filtradas['ilesos']
    feridos_2 = pessoas_filtradas['feridos']
    feridos_3 = pessoas_filtradas['mortos']
    pessoas = pessoas_filtradas['pessoas']

    plt.title('Gravidade dos ferimentos em pessoas de até 20 anos')
    plt.plot(pessoas, feridos_1, color="red", marker="+")
    plt.plot(pessoas, feridos_2, color="green", marker="*")
    plt.plot(pessoas, feridos_3, color="blue", marker=".")
    plt.legend(['ilesos', 'Feridos', 'Mortos'], shadow=True)
    plt.xlabel('Idade')
    plt.ylabel('Pessoas')
    
    # Salvar o gráfico em um arquivo
    plt.savefig(filename)
    plt.show()
    print('Grafico 1 OK')

def pessoas_envolvidas(dados, filename):
    ignorados = dados['pessoas']
    
    media = dados['pessoas'].mean()
    # print(f'A média de pessoa é: {media}')
    
    # Bolinha
    plt.plot(ignorados, "o", label="Pessoas")
    
    # Linha
    plt.axhline(y=media, color='red', linestyle='--', label="Média")
    
    plt.axis(xmin=0, xmax=len(ignorados) - 1)
    plt.title('Média de pessoas envolvidas em acidentes')
    plt.axis(ymin=0, ymax=100)
    plt.legend()
    
    plt.savefig(filename)
    plt.show()
    print('Grafico 2 OK')

def porcentagem_ignorados(dados, filename):
    num_ids = len(dados['id'])
    # print(f'O número de IDs cadastrados é: {num_ids}')

    ignorados = sum(dados['ignorados'])
    # print(f'O número de ignorados cadastrados é: {ignorados}')

    categorias = ['Casos', 'Ignorados']
    porcentagens = [num_ids, ignorados]

    # Crie o gráfico de pizza
    plt.figure(figsize=(6, 6))  # Tamanho da figura
    plt.pie(porcentagens, labels=categorias, autopct='%1.1f%%', startangle=140)
    plt.title('Porcentagem de casos ignorados')

    plt.show()
    plt.savefig(filename)
    print('Grafico 3 OK')


aplicar_filtro_simples(dados, '2023-01-01', 'filtro_simples.csv')
aplicar_filtro_composto(dados, 1, 2, 'filtro_composto.csv')

gravidade_ferimentos(dados, 'gravidade_ferimentos.pdf')
pessoas_envolvidas(dados, 'pessoas_envolvidas.pdf')
porcentagem_ignorados(dados, 'porcentagem_ignorados.pdf')