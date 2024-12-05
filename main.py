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
    with open('rede_INFNET_atualizado.txt', 'w', encoding='utf-8') as file:
        for usuario, dados in usuarios_dict.items():
            amigos = ','.join(dados["amigos"])
            file.write(f"{usuario},{dados['idade']},{dados['localização'][0]},{dados['localização'][1]},{amigos}\n")

# 13. Listando Usuários ⭐
def listar_usuarios():
    for usuario in usuarios_dict.keys():
        print(usuario)

# 14. Quantidade de Amigos ⭐⭐⭐
def carregar_usuarios():
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
    for usuario, dados in usuarios_dict.items():
        amigos = dados["amigos"]
        if len(amigos) > 0:
            print(f"{usuario} tem {len(amigos) - 1} amigos.")
        else:
            print(f"{usuario} tem {len(amigos)} amigos.")

# 15. Usuários Mais Populares ⭐⭐⭐
def usuarios_mais_populares():
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
    with open('INFwebNet.csv', 'r', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        dados = [linha for linha in leitor]

    with open('INFwebNET.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(dados, jsonfile, ensure_ascii=False, indent=4)

    print("Dados exportados para INFwebNET.json com sucesso!")

csv_para_json()

def cadastrar_usuario():
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
    df = pd.read_json('INFwebNET.json')

    media_idade = df['Idade'].mean()
    print(f"A média de idade dos INFNETianos é: {media_idade:.0f} anos")

def carregar_novos_usuarios():
    try:
        with open('dados_usuarios_novos.txt', 'r', encoding='utf-8') as file:
            leitor = csv.reader(file, delimiter=';')
            novos_usuarios = []
            next(leitor) 
            
            for linha in leitor:
                if len(linha) >= 5:  # Verifica se a linha tem pelo menos 5 campos
                    nome = linha[1].strip() 
                    try:
                        idade = int(float(linha[4].strip()))  # Idade está na quinta coluna
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
    dados_usuarios = []
    
    ano_atual = datetime.now().year
    
    for usuario, dados in usuarios_dict.items():
        nome = usuario
        idade = dados.get("idade", None)
        cidade, estado = dados["localização"]
        
        hobbys = ', '.join(dados.get("hobbys", [])) or 'Nenhum'
        coding = ', '.join(dados.get("coding", [])) or 'Nenhuma'
        jogos = ', '.join([f"{jogo['jogo']} ({jogo['plataforma']})" for jogo in dados.get("jogos", [])]) or 'Nenhum'
        
        # Calculando o ano de nascimento
        ano_nascimento = ano_atual - idade if idade is not None else None
        
        dados_usuarios.append({
            "Nome": nome,
            "Idade": idade,
            "Cidade": cidade if cidade else np.nan,  # Convertendo string vazia em NaN
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
    Filtra os usuários por estado e salva em arquivos CSV.
    
    Parâmetros:
    df : DataFrame
        O DataFrame contendo os dados dos INFNETianos.
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
    decisao = input("Deseja filtrar por ano de nascimento? (s/n): ")
    
    if decisao.lower() == 'n':
        return df
    
    ano_inicial = int(input("Digite o ano inicial: "))
    ano_final = int(input("Digite o ano final: "))
    
    df_filtrado = df[(df['Ano de Nascimento'] >= ano_inicial) & (df['Ano de Nascimento'] <= ano_final)]
    
    print("\n", df_filtrado)

def selecionar_infnetiano():
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
                
                # Atualizando dados
                atualizar_dados(usuario_selecionado)
            else:
                print("Seleção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    else:
        print("Nenhum INFNETiano encontrado com esse nome.")

def atualizar_dados(usuario):
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