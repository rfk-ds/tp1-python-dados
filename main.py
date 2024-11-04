from collections import Counter
import random

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
    if usuario in usuarios_dict and amigo in usuarios_dict:
        usuarios_dict[usuario]["amigos"].add(amigo)
        usuarios_dict[amigo]["amigos"].add(usuario)
        print(f"{amigo} adicionado como amigo de {usuario}.")
    else:
        print("Usuário ou amigo não encontrado.")

# 8. Verificando Conexões ⭐⭐
def verificar_popularidade(usuario):
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
        print(f"{usuario} tem {len(amigos) - 1} amigos.")

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
def main():
    global usuarios_dict
    usuarios_dict = carregar_usuarios()
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Rede INFwebNET ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    print("---------------- Lista de Usuários ---------------- ")
    listar_usuarios()
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

main()