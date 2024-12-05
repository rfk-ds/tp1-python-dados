from collections import Counter
import random
import csv
import json
import pandas as pd
from datetime import datetime
import numpy as np

# 1. Aquecendo os motores ⭐
usuarios = [
    ["Rafiki", 25, "Rio de Janeiro", "RJ"],
    ["Olivia", 22, "São Paulo", "SP"],
    ["Beatriz", 30, "Belo Horizonte", "MG"],
    ["Angelo", 28, "Curitiba", "PR"],
    ["Leonardo", 27, "Porto Alegre", "RS"],
]

# 2. Perfil ⭐⭐
perfis = []
for usuario in usuarios:
    nome, idade, cidade, estado = usuario
    perfil = {
        "nome": nome,
        "idade": idade,
        "localização": (cidade, estado)
    }
    perfis.append(perfil)
    
# 3. Comparando estruturas
"""
Lista: ordernada e mútavel. Utiliza colchetes. Exemplo: [Rafiki, Olivia, Beatriz, Angelo, Leonardo]
Dicionário: não-ordenado e mutável. Utiliza Chaves. Exemplo: {"nome": "Rafiki", "idade": 25, "localização": ("Rio de Janeiro", "RJ")}
Tuple: ordenada e imutável. Utiliza parentesês. Exemplo: ("Rafiki", 25, "Rio de Janeiro", "RJ")
"""

# 4. Limpando o terreno ⭐⭐
perfis_validos = []
for perfil in perfis:
    if perfil["nome"] and perfil["localização"][0]:
        perfis_validos.append(perfil)

# 5. Carregando dados ⭐⭐⭐
arquivo_base = 'base_inicial.txt'
with open(arquivo_base, 'r', encoding='utf-8') as file:
    next(file)
    for line in file:
        dados = line.strip().split('?')
        if len(dados) >= 4 and dados[0]:
            nome, idade, cidade, estado = dados[:4]
            amigos = set(dados[4:])
            perfil = {
                "nome": nome,
                "idade": int(idade),
                "localização": (cidade, estado),
                "amigos": amigos
            }
            perfis_validos.append(perfil)

# 6. Concatenando dados ⭐
with open('rede_INFNET.txt', 'w', encoding='utf-8') as file:
    for perfil in perfis_validos:
        nome = perfil.get("nome")
        idade = perfil.get("idade", "N/A")
        cidade, estado = perfil["localização"]
        amigos = perfil.get("amigos", set())
        
        nome = nome if nome else "Nome Desconhecido"
        cidade = cidade if cidade else "Cidade Desconhecida"
        estado = estado if estado else "Estado Desconhecido"
        
        file.write(f"{nome},{idade},{cidade},{estado},{','.join(amigos)}\n")

# 7. Adicionando Amigos ⭐
usuarios_dict = {
    perfil["nome"]: {
        "idade": perfil["idade"],
        "localização": perfil["localização"],
        "amigos": set()
    } 
    for perfil in perfis_validos
}

def adicionar_amigo(usuario, amigo):
    """
    Adiciona um amigo à lista de amigos de um usuário.

    Parâmetros:
    usuario (str): O nome do usuário que está adicionando um amigo.
    amigo (str): O nome do amigo a ser adicionado.

    Se o usuário e o amigo existirem no dicionário de usuários,
    o amigo será adicionado à lista de amigos do usuário e vice-versa.
    Caso contrário, uma mensagem de erro será exibida.
    """
    if usuario in usuarios_dict and amigo in usuarios_dict:
        usuarios_dict[usuario]["amigos"].add(amigo)
        usuarios_dict[amigo]["amigos"].add(usuario)
        print(f"{amigo} adicionado como amigo de {usuario}.")
    else:
        print("Usuário ou amigo não encontrado.")

# 8. Verificando Conexões ⭐⭐
def verificar_popularidade(usuario):
    """
    Verifica a popularidade de um usuário com base no número de amigos.

    Parâmetros:
    usuario (str): O nome do usuário a ser verificado.

    A função conta quantos usuários têm o usuário especificado em sua lista de amigos.
    Se o número de amigos for maior que 4, o usuário é considerado popular.
    Caso contrário, é considerado não popular.
    Uma mensagem é exibida indicando a popularidade do usuário.
    """
    contagem = 0
    for perfil in usuarios_dict.values():
        if usuario in perfil["amigos"]:
            contagem += 1
    if contagem > 4:
        print(f"{usuario} é popular! Adicionado como amigo por {contagem} usuários.")
    else:
        print(f"{usuario} não é popular. Adicionado como amigo por apenas {contagem} usuários.")

# 9. Amigos em Comum ⭐⭐
def amigos_em_comum():
    """
    Seleciona aleatoriamente dois usuários e verifica se eles têm amigos em comum.

    A função obtém uma lista de usuários do dicionário global e seleciona
    aleatoriamente dois deles. Em seguida, verifica se esses usuários compartilham
    algum amigo e exibe os amigos em comum, se houver.

    Se não houver amigos em comum, uma mensagem informando isso será exibida.
    """
    usuarios = list(usuarios_dict.keys())
    usuario1, usuario2 = random.sample(usuarios, 2)
    amigos_usuario1 = usuarios_dict[usuario1]["amigos"]
    amigos_usuario2 = usuarios_dict[usuario2]["amigos"]
    amigos_comum = amigos_usuario1.intersection(amigos_usuario2)
    print(f"Usuário 1: {usuario1}")
    print(f"Usuário 2: {usuario2}")
    if amigos_comum:
        print("Amigos em comum:", amigos_comum)
    else:
        print("Não há amigos em comum.")

# 10. Conexões Exclusivas ⭐⭐
def conexoes_exclusivas():
    """
    Seleciona aleatoriamente dois usuários e exibe seus amigos exclusivos.

    A função escolhe aleatoriamente dois usuários do dicionário global e
    determina quais amigos cada um deles possui que não são amigos do outro.
    Os amigos exclusivos de cada usuário são exibidos. Se um usuário não tiver
    amigos exclusivos, uma mensagem informando isso será exibida.

    Amigos em comum são identificados e excluídos da lista de amigos de cada usuário.
    """
    usuario1, usuario2 = random.sample(list(usuarios_dict.keys()), 2)
    amigos_usuario1 = usuarios_dict[usuario1]["amigos"]
    amigos_usuario2 = usuarios_dict[usuario2]["amigos"]

    amigos_comum = amigos_usuario1 & amigos_usuario2
    amigos_exclusivos = {
        usuario1: amigos_usuario1 - amigos_comum,
        usuario2: amigos_usuario2 - amigos_comum
    }
    
    for usuario, amigos in amigos_exclusivos.items():
        if amigos:
            print(f"Usuário: {usuario}")
            print("Amigos exclusivos:", amigos)
        else:
            print(f"Usuário: {usuario}")
            print("Amigos exclusivos: Nenhum")

# 11. Removendo Conexões ⭐⭐
def remover_amigo(usuario, amigo):
    """
    Remove um amigo da lista de amigos de um usuário.

    Parâmetros:
    usuario (str): O nome do usuário que deseja remover um amigo.
    amigo (str): O nome do amigo a ser removido.

    A função verifica se o usuário existe e se o amigo está na lista de amigos do usuário.
    Se ambos existirem, o amigo é removido da lista de amigos do usuário e vice-versa.
    Caso contrário, mensagens apropriadas são exibidas.
    """
    if usuario in usuarios_dict:
        if amigo in usuarios_dict[usuario]["amigos"]:
            usuarios_dict[usuario]["amigos"].remove(amigo)
            usuarios_dict[amigo]["amigos"].remove(usuario)
            print(f"{amigo} foi removido da lista de amigos de {usuario}.")
        else:
            print(f"{amigo} não é amigo de {usuario}.")
    else:
        print("Usuário não encontrado.")

# 12. Salvando o Progresso ⭐⭐
def salvar_progresso():
    """
    Salva o progresso dos usuários em um arquivo de texto.

    A função grava as informações de cada usuário, incluindo nome, idade,
    localização (latitude e longitude) e lista de amigos, em um arquivo chamado
    'rede_INFNET_atualizado.txt'. Cada linha do arquivo contém os dados de um usuário,
    separados por vírgulas.

    O arquivo é criado ou sobrescrito se já existir.
    """
    with open('rede_INFNET_atualizado.txt', 'w', encoding='utf-8') as file:
        for usuario, dados in usuarios_dict.items():
            amigos = ','.join(dados["amigos"])
            file.write(f"{usuario},{dados['idade']},{dados['localização'][0]},{dados['localização'][1]},{amigos}\n")

# 13. Listando Usuários ⭐
def listar_usuarios():
    """
    Lista todos os usuários presentes no dicionário de usuários.

    A função percorre o dicionário global de usuários e imprime o nome de cada usuário.
    Não retorna nenhum valor, apenas exibe os nomes no console.
    """
    for usuario in usuarios_dict.keys():
        print(usuario)

# 14. Quantidade de Amigos ⭐⭐⭐
def carregar_usuarios():
    """
    Carrega os usuários de um arquivo de texto para um dicionário.

    A função lê os dados de usuários do arquivo 'rede_INFNET.txt', onde cada linha contém
    informações sobre um usuário, incluindo nome, idade, localização (latitude e longitude)
    e uma lista de amigos. Os dados são armazenados em um dicionário, onde a chave é o nome
    do usuário e o valor é outro dicionário com detalhes do usuário.

    Retorna:
        dict: Um dicionário contendo os usuários e suas informações.
    """
    usuarios_dict = {}
    with open('rede_INFNET.txt', 'r', encoding='utf-8') as file:
        for line in file:
            partes = line.strip().split(',')
            nome = partes[0]
            idade = int(partes[1])
            localizacao = (partes[2], partes[3])
            
            if len(partes) > 4:
                amigos = set(partes[4:])
            else:
                amigos = set()
            
            usuarios_dict[nome] = {
                "idade": idade,
                "localização": localizacao,
                "amigos": amigos
            }
    
    return usuarios_dict

def quantidade_amigos(usuarios_dict):
    """
    Exibe a quantidade de amigos de cada usuário no dicionário.

    A função percorre o dicionário de usuários e imprime o número de amigos de cada um.
    Se o usuário tiver amigos, o número é exibido. Caso contrário, é informado que o usuário
    não possui amigos.

    Parâmetros:
        usuarios_dict (dict): O dicionário contendo os usuários e suas informações.
    """
    for usuario, dados in usuarios_dict.items():
        amigos = dados["amigos"]
        if len(amigos) > 0:
            print(f"{usuario} tem {len(amigos) - 1} amigos.")
        else:
            print(f"{usuario} tem {len(amigos)} amigos.")

# 15. Usuários Mais Populares ⭐⭐⭐
def usuarios_mais_populares():
    """
    Exibe os cinco usuários mais populares com base na quantidade de amigos.

    A função conta quantas vezes cada usuário é mencionado como amigo por outros usuários
    e exibe os cinco usuários que têm o maior número de amigos. 

    Utiliza a classe Counter do módulo collections para facilitar a contagem.
    """
    contador = Counter()
    
    for dados in usuarios_dict.values():
        amigos = dados.get("amigos", [])
        for amigo in amigos:
            contador[amigo] += 1
            
    populares = contador.most_common(5)
    
    for usuario, quantidade in populares:
        print(f"{usuario} é amigo de {quantidade} usuários.")

# 16. Lidando com arquivos ⭐⭐
"""
Resposta:
'with' é importante pois facilita a abertura e fechamento de arquivos,
de forma que não é necessário se preocupar em fechar o arquivo manualmente,
evitando assim possíveis erros e problemas de memória.
"""

def txt_para_csv():
    """
    Converte um arquivo de texto com dados de usuários para um formato CSV.

    A função lê os dados do arquivo 'rede_INFNET_atualizado.txt', onde cada linha contém
    informações sobre um usuário (nome, idade, cidade e estado). Os dados são extraídos e
    salvos em um novo arquivo chamado 'INFwebNet.csv'.

    O arquivo CSV resultante contém um cabeçalho com os campos 'Nome', 'Idade', 'Cidade' e 'Estado'.
    """
    with open('rede_INFNET_atualizado.txt', 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    dados = []
    for linha in linhas:
        partes = linha.strip().split(',')
        if len(partes) >= 4:
            nome = partes[0]
            idade = partes[1]
            cidade = partes[2]
            estado = partes[3]
            dados.append([nome, idade, cidade, estado])

    with open('INFwebNet.csv', 'w', newline='', encoding='utf-8') as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(['Nome', 'Idade', 'Cidade', 'Estado'])
        escritor.writerows(dados)

    print("Dados exportados para INFwebNet.csv com sucesso!")

txt_para_csv()

def csv_para_json():
    """
    Converte um arquivo CSV com dados de usuários para um formato JSON.

    A função lê os dados do arquivo 'INFwebNet.csv' usando um leitor de dicionário e
    converte essas informações para um formato JSON, que é salvo em um novo arquivo chamado
    'INFwebNET.json'.

    O arquivo JSON resultante contém uma lista de dicionários, onde cada dicionário representa
    um usuário e suas informações.
    """
    with open('INFwebNet.csv', 'r', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        dados = [linha for linha in leitor]

    with open('INFwebNET.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(dados, jsonfile, ensure_ascii=False, indent=4)

    print("Dados exportados para INFwebNET.json com sucesso!")

csv_para_json()

def cadastrar_usuario():
    """
    Cadastra um novo usuário no sistema INFNET.

    A função solicita informações do usuário, incluindo nome, idade, cidade, estado,
    hobbys, linguagens de programação e jogos. Os dados são salvos em um arquivo JSON
    chamado 'INFwebNET.json'.

    Se o arquivo não existir, ele será criado. A função também atualiza a lista de usuários
    carregando os dados existentes após o cadastro.
    """
    decisao = input("Deseja cadastrar um novo INFNETiano? (s/n): ")
    
    if decisao.lower() == 's':
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        cidade = input("Digite a cidade: ")
        estado = input("Digite o estado: ")
        
        hobbys = input("Digite os hobbys (separados por vírgula): ").split(',')
        hobbys = [hobby.strip() for hobby in hobbys]

        coding = input("Digite as linguagens de programação (separadas por vírgula): ").split(',')
        coding = [lang.strip() for lang in coding]
        
        jogos = []
        while True:
            jogo = input("Digite o nome do jogo (ou 'sair' para finalizar): ")
            if jogo.lower() == 'sair':
                break
            plataforma = input("Digite a plataforma do jogo: ")
            jogos.append({"jogo": jogo, "plataforma": plataforma})

        novo_usuario = {
            "nome": nome,
            "idade": int(idade),
            "localização": (cidade, estado),
            "hobbys": hobbys,
            "coding": coding,
            "jogos": jogos
        }

        try:
            with open('INFwebNET.json', 'r', encoding='utf-8') as jsonfile:
                dados_existentes = json.load(jsonfile)
        except FileNotFoundError:
            dados_existentes = []

        dados_existentes.append(novo_usuario)

        with open('INFwebNET.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(dados_existentes, jsonfile, ensure_ascii=False, indent=4)

        print("Novo INFNETiano cadastrado com sucesso!\n")
        
        print("Atualizando lista de usuários...\n")
        global usuarios_dict
        usuarios_dict = carregar_usuarios()
        
        print("Lista de usuários atualizada:\n")
        listar_usuarios()
    else:
        print("Prosseguindo...\n")


def calcular_media_idade():
    """
    Calcula e exibe a média de idade dos usuários cadastrados no sistema INFNET.

    A função lê os dados do arquivo 'INFwebNET.json', calcula a média das idades
    dos usuários e imprime o resultado. É esperado que o arquivo JSON contenha um
    campo chamado 'Idade'.
    """
    df = pd.read_json('INFwebNET.json')

    media_idade = df['Idade'].mean()
    print(f"A média de idade dos INFNETianos é: {media_idade:.0f} anos")

def carregar_novos_usuarios():
    """
    Carrega novos usuários a partir de um arquivo de texto e os adiciona ao dicionário global de usuários.

    A função lê o arquivo 'dados_usuarios_novos.txt', que deve conter informações sobre novos usuários,
    e converte essas informações em dicionários. Os dados são armazenados em um dicionário global chamado
    `usuarios_dict`. Cada usuário é representado por um dicionário que inclui nome, idade, localização,
    hobbys, linguagens de programação e jogos.

    O arquivo deve ter campos separados por ponto e vírgula e a função lida com possíveis erros de
    formatação, como idades inválidas. Se o arquivo não for encontrado, uma mensagem de erro será exibida.
    """
    try:
        with open('dados_usuarios_novos.txt', 'r', encoding='utf-8') as file:
            leitor = csv.reader(file, delimiter=';')
            novos_usuarios = []
            next(leitor) 
            
            for linha in leitor:
                if len(linha) >= 5:
                    nome = linha[1].strip() 
                    try:
                        idade = int(float(linha[4].strip()))
                    except ValueError:
                        print(f"Idade inválida para o usuário {nome}. Ignorando...")
                        continue
                    
                    cidade = linha[6].strip()
                    estado = linha[7].strip()
                    
                    hobbys = linha[8].strip().strip("[]").split(',') if len(linha) > 8 else []
                    coding = linha[9].strip().strip("[]").split(',') if len(linha) > 9 else []
                    
                    jogos = []
                    if len(linha) > 10:
                        for jogo_info in linha[10:]:
                            jogo_dados = jogo_info.strip().split(',')
                            if len(jogo_dados) == 2:
                                jogos.append({"jogo": jogo_dados[0].strip(), "plataforma": jogo_dados[1].strip()})
                    
                    novo_usuario = {
                        "nome": nome,
                        "idade": idade,
                        "localização": (cidade, estado),
                        "hobbys": hobbys,
                        "coding": coding,
                        "jogos": jogos
                    }
                    novos_usuarios.append(novo_usuario)
                    
            global usuarios_dict
            for usuario in novos_usuarios:
                usuarios_dict[usuario["nome"]] = {
                    "idade": usuario["idade"],
                    "localização": usuario["localização"],
                    "hobbys": usuario["hobbys"],
                    "coding": usuario["coding"],
                    "jogos": usuario["jogos"],
                    "amigos": set()
                }
                
            print(f"{len(novos_usuarios)} novos usuários carregados com sucesso!")
            
    except FileNotFoundError:
        print("Arquivo 'dados_usuarios_novos.txt' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def organizar_dados_em_dataframe():
    """
    Organiza os dados dos usuários em um DataFrame do Pandas.

    A função coleta informações dos usuários armazenados no dicionário global `usuarios_dict`,
    calcula o ano de nascimento com base na idade e cria um DataFrame com as seguintes colunas:
    Nome, Idade, Cidade, Estado, Hobbys, Linguagens de Programação, Jogos e Ano de Nascimento.

    A função também trata valores ausentes, preenchendo a idade média para idades ausentes e utilizando
    a moda da coluna 'Cidade' para preencher valores vazios. O DataFrame resultante é impresso e retornado.
    
    Pelo menos era a intenção...

    Returns:
        pd.DataFrame: DataFrame contendo as informações organizadas dos usuários.
    """
    dados_usuarios = []
    
    ano_atual = datetime.now().year
    
    for usuario, dados in usuarios_dict.items():
        nome = usuario
        idade = dados.get("idade", None)
        cidade, estado = dados["localização"]
        
        hobbys = ', '.join(dados.get("hobbys", [])) or 'Nenhum'
        coding = ', '.join(dados.get("coding", [])) or 'Nenhuma'
        jogos = ', '.join([f"{jogo['jogo']} ({jogo['plataforma']})" for jogo in dados.get("jogos", [])]) or 'Nenhum'
        
        ano_nascimento = ano_atual - idade if idade is not None else None
        
        dados_usuarios.append({
            "Nome": nome,
            "Idade": idade,
            "Cidade": cidade if cidade else np.nan,
            "Estado": estado,
            "Hobbys": hobbys,
            "Linguagens de Programação": coding,
            "Jogos": jogos,
            "Ano de Nascimento": ano_nascimento
        })
    
    df = pd.DataFrame(dados_usuarios)
    
    media_idade = df['Idade'].mean()
    df['Idade'] = df['Idade'].fillna(media_idade)
    
    if df['Cidade'].isnull().all():
        print("Todos os valores da coluna 'Cidade' estão ausentes. Não é possível preencher.")
    else:
        modo_cidade = df['Cidade'].mode()[0] if not df['Cidade'].mode().empty else 'Desconhecida'
        df['Cidade'] = df['Cidade'].fillna(modo_cidade)
    
    df['Ano de Nascimento'] = ano_atual - df['Idade']
    
    print(df)
    
    return df

    """
    Explicação campos com valores ausentes e critério utilizados para preenchimento:
    
    Campo: idade

    Critério: Preencher valores ausentes com a média das idades.

    Justificativa: A média é uma boa escolha para dados numéricos, pois fornece um valor
    central que representa bem o conjunto de dados como um todo.
    
    Campo: cidade
    
    Critério: Preencher valores ausentes com o valor mais frequente das cidades.
    
    Justificativa: O valor mais frequente é uma boa escolha para dados categóricos, pois fornece o valor
    mais frequente, que é uma boa representação da maioria dos dados.
    """
    
def salvar_grupos_por_estado(df):
    """
    Salva os usuários em arquivos CSV separados por estado.

    A função recebe um DataFrame que contém informações dos usuários e cria arquivos CSV
    para cada estado único presente na coluna 'Estado'. Cada arquivo contém os dados dos usuários
    correspondentes ao estado específico.

    Parâmetros:
        df (pd.DataFrame): DataFrame contendo os dados dos usuários, incluindo a coluna 'Estado'.

    A função não retorna nenhum valor, mas imprime uma mensagem indicando que os dados foram salvos.
    """
    estados_unicos = df['Estado'].unique()
    for estado in estados_unicos:
        if pd.notna(estado):
            df_estado = df[df['Estado'] == estado]
            
            sigla_estado = estado.upper()
            nome_arquivo = f"grupo_{sigla_estado}.csv"
            
            df_estado.to_csv(nome_arquivo, index=False)
            print(f"Usuários do estado {estado} salvos em {nome_arquivo}.")


def filtrar_por_ano_nascimento(df):
    """
    Filtra o DataFrame de usuários com base no ano de nascimento.

    A função solicita ao usuário se deseja filtrar os dados por ano de nascimento. Se a resposta for 'n',
    o DataFrame original é retornado. Caso contrário, o usuário deve inserir um ano inicial e um ano final,
    e a função retorna um novo DataFrame contendo apenas os usuários cujo ano de nascimento está dentro
    do intervalo especificado.

    Parâmetros:
        df (pd.DataFrame): DataFrame contendo os dados dos usuários, incluindo a coluna 'Ano de Nascimento'.

    Returns:
        pd.DataFrame: DataFrame filtrado com os usuários que atendem ao critério de ano de nascimento.
    """
    decisao = input("Deseja filtrar por ano de nascimento? (s/n): ")
    
    if decisao.lower() == 'n':
        return df
    
    ano_inicial = int(input("Digite o ano inicial: "))
    ano_final = int(input("Digite o ano final: "))
    
    df_filtrado = df[(df['Ano de Nascimento'] >= ano_inicial) & (df['Ano de Nascimento'] <= ano_final)]
    
    print("\n", df_filtrado)

def selecionar_infnetiano():
    """
    Permite ao usuário buscar e selecionar um INFNETiano pelo nome.

    A função solicita ao usuário que insira o nome de um INFNETiano e busca no dicionário global
    `usuarios_dict`. Se encontrar usuários correspondentes, exibe uma lista numerada. O usuário pode
    então selecionar um INFNETiano pelo número correspondente. Se a seleção for válida, a função
    chama a função `atualizar_dados` para atualizar os dados do usuário selecionado.

    A função não retorna nenhum valor, mas imprime mensagens informativas sobre o processo de busca e seleção.
    """
    nome_busca = input("Digite o nome do INFNETiano que deseja buscar: ").strip()
    
    usuarios_encontrados = [usuario for usuario in usuarios_dict.keys() if nome_busca.lower() in usuario.lower()]
    
    if usuarios_encontrados:
        print("INFNETiano(s) encontrado(s):")
        for i, usuario in enumerate(usuarios_encontrados):
            print(f"{i + 1}. {usuario}")
        
        escolha = input("Digite o número do INFNETiano que deseja selecionar: ")
        
        try:
            indice = int(escolha) - 1
            if 0 <= indice < len(usuarios_encontrados):
                usuario_selecionado = usuarios_encontrados[indice]
                print(f"Você selecionou: {usuario_selecionado}")
                
                atualizar_dados(usuario_selecionado)
            else:
                print("Seleção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    else:
        print("Nenhum INFNETiano encontrado com esse nome.")

def atualizar_dados(usuario):
    """
    Atualiza os dados de um INFNETiano.

    A função permite que o usuário atualize informações pessoais de um INFNETiano, como idade,
    localização (cidade e estado), hobbies e jogos. O usuário pode optar por manter os valores atuais
    pressionando Enter. As atualizações são salvas no dicionário global `usuarios_dict`.

    Parâmetros:
        usuario (str): O nome do INFNETiano cujos dados serão atualizados.

    A função não retorna nenhum valor, mas imprime mensagens informativas sobre o processo de atualização.
    """
    print(f"\nAtualizando dados para: {usuario}")
    
    dados_usuario = usuarios_dict[usuario]
    
    nova_idade = input(f"Idade atual: {dados_usuario['idade']}. Digite a nova idade (ou pressione Enter para manter): ")
    if nova_idade:
        dados_usuario['idade'] = int(nova_idade)
    
    nova_cidade = input(f"Cidade atual: {dados_usuario['localização'][0]}. Digite a nova cidade (ou pressione Enter para manter): ")
    nova_estado = input(f"Estado atual: {dados_usuario['localização'][1]}. Digite o novo estado (ou pressione Enter para manter): ")
    
    if nova_cidade or nova_estado:
        cidade_atual = dados_usuario['localização'][0] if nova_cidade == '' else nova_cidade
        estado_atual = dados_usuario['localização'][1] if nova_estado == '' else nova_estado
        dados_usuario['localização'] = (cidade_atual, estado_atual)

    print(f"Hobbies atuais: {', '.join(dados_usuario.get('hobbys', []))}")
    novos_hobbys = input("Digite até 5 novos hobbys (separados por vírgula): ").split(',')
    novos_hobbys = [hobby.strip() for hobby in novos_hobbys][:5] 
    dados_usuario['hobbys'] = novos_hobbys

    print(f"Jogos atuais: {', '.join([jogo['jogo'] for jogo in dados_usuario.get('jogos', [])])}")
    novos_jogos = []
    while len(novos_jogos) < 5:
        jogo = input("Digite o nome do jogo (ou 'sair' para finalizar): ")
        if jogo.lower() == 'sair':
            break
        plataforma = input("Digite a plataforma do jogo: ")
        novos_jogos.append({"jogo": jogo.strip(), "plataforma": plataforma.strip()})

    dados_usuario['jogos'] = novos_jogos[:5] 

    usuarios_dict[usuario] = dados_usuario
    print("Dados atualizados com sucesso!")
    
def linguagens_mais_citadas():
    """
    Exibe as 5 linguagens de programação mais citadas entre os INFNETianos.

    A função percorre o dicionário global `usuarios_dict`, contando a frequência das linguagens
    de programação mencionadas na chave "coding" de cada usuário. Em seguida, exibe as 5 linguagens
    mais populares e suas respectivas quantidades.

    A função não recebe parâmetros e não retorna nenhum valor, mas imprime os resultados diretamente.
    """
    contador = Counter()

    for dados in usuarios_dict.values():
        linguagens = dados.get("coding", [])
        contador.update(linguagens)

    populares = contador.most_common(5)

    if populares:
        print("\nAs 5 linguagens de programação mais citadas entre os INFNETianos:")
        for linguagem, quantidade in populares:
            print(f"{linguagem}: {quantidade} vez(es)")
    else:
        print("Nenhuma linguagem de programação foi citada.")

def main():
    """
    Função principal do programa que gerencia a rede INFwebNET.

    A função executa uma série de operações relacionadas ao gerenciamento de usuários na rede,
    incluindo o carregamento de dados, cadastro de usuários, adição e remoção de amigos,
    verificação de popularidade, cálculo de média de idade, e organização de dados em um DataFrame.

    O fluxo de execução inclui:
    - Carregar usuários existentes.
    - Listar usuários cadastrados.
    - Cadastrar novos usuários.
    - Calcular a quantidade de amigos.
    - Adicionar e remover amigos.
    - Verificar a popularidade de usuários.
    - Identificar amigos em comum e conexões exclusivas.
    - Salvar o progresso em um arquivo.
    - Organizar dados em um DataFrame e salvar em formato JSON.
    - Filtrar dados por ano de nascimento e selecionar um INFNETiano específico.
    - Exibir as linguagens de programação mais citadas.

    A função não recebe parâmetros e não retorna valores.
    """
    global usuarios_dict
    usuarios_dict = carregar_usuarios()
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Rede INFwebNET ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    carregar_novos_usuarios()
    print("\n")
    
    print("---------------- Lista de Usuários ---------------- ")
    listar_usuarios()
    print("\n")
    
    cadastrar_usuario()
    print("\n")
    
    print("---------------- Quantidade de amigos ---------------- ")
    quantidade_amigos(usuarios_dict)
    print("\n")

    print("---------------- Adicionando amigos ---------------- ")
    adicionar_amigo("Rafiki", "Olivia")
    adicionar_amigo("Rafiki", "Beatriz")
    adicionar_amigo("Rafiki", "Angelo")
    adicionar_amigo("Rafiki", "Leonardo")
    adicionar_amigo("Rafiki", "Carlos")
    adicionar_amigo("Rafiki", "Renata")
    adicionar_amigo("Rafiki", "Daniel")
    adicionar_amigo("Rafiki", "Felipe")
    print("\n")
    
    print("---------------- Verificando popularidade ---------------- ")
    verificar_popularidade("Rafiki")
    verificar_popularidade("Leonardo")
    print("\n")
    
    print("---------------- Amigos em comum ---------------- ")
    amigos_em_comum()
    print("\n")
    
    print("---------------- Conexões exclusivas ---------------- ")
    conexoes_exclusivas()
    print("\n")
    
    print("---------------- Removendo amigos ---------------- ")
    remover_amigo("Rafiki", "Olivia")
    print("\n")
    
    print("Salvando progresso...")
    salvar_progresso()
    print("\n")
    
    print("---------------- Quantidade de Amigos ---------------- ")
    quantidade_amigos(usuarios_dict)
    print("\n")
    
    print("---------------- Usuários mais populares ---------------- ")
    usuarios_mais_populares()
    print("\n")
    
    print("---------------- Média de idade dos usuários ---------------- ")
    calcular_media_idade()
    print("\n")

    print("---------------- Organizando dados em DataFrame ---------------- ")
    df_informacoes = organizar_dados_em_dataframe()
    df_informacoes.to_json("INFwebNet_Data.json", orient="records", lines=True)
    salvar_grupos_por_estado(df_informacoes)
    filtrar_por_ano_nascimento(df_informacoes)
    print("\n")
    
    print("---------------- Selecionando INFNETiano ---------------- ")
    selecionar_infnetiano()
    print("\n")
    
    print("---------------- Linguagens mais citadas ---------------- ")
    linguagens_mais_citadas()
    print("\n")
    
main()