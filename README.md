# Python para Dados | Teste de Performance (TP) 1 

## Contexto
Imagine que você é um cientista de dados trabalhando em um projeto de análise de dados de uma rede social fictícia chamada INFwebNET. O INFwebNET armazena informações sobre usuários e suas conexões em diferentes arquivos. Seu objetivo é usar seus conhecimentos de Python para processar esses dados e extrair informações relevantes.

## Níveis de Dificuldade
- **Fácil (⭐)**: Envolve conceitos básicos e aplicação direta de métodos.
- **Médio (⭐⭐)**: Requer maior compreensão dos conceitos e combinação de diferentes métodos.
- **Difícil (⭐⭐⭐)**: Exige aplicação criativa dos conceitos, resolução de problemas e otimização de código.

## Uso de IAs: Sinal Vermelho 🔴
Todas as partes deste trabalho devem ser da autoria do aluno. Qualquer uso de ferramentas generativas de IA, como ChatGPT, é proibido. O uso de IA generativa será considerado má conduta acadêmica e estará sujeito à aplicação do código disciplinar, pois as tarefas deste trabalho foram elaboradas para desafiar o aluno a desenvolver conhecimentos de base, pensamento crítico e habilidades de resolução de problemas. O uso da tecnologia de IA limitaria sua capacidade de desenvolver essas competências e de atingir os objetivos de aprendizagem desta disciplina.

## Exercícios

1. **Aquecendo os motores ⭐**
   - Crie uma lista chamada `usuarios` que contenha ao menos 5 listas. Cada lista interna deve representar um usuário do INFwebNET com as seguintes informações: nome (string), idade (inteiro), cidade (string) e estado (string).

2. **Perfil ⭐⭐**
   - Escreva um programa que leia os dados da lista `usuarios` criada no exercício anterior e crie um dicionário para cada usuário. Cada dicionário deve ter as chaves "nome" e "idade" com os respectivos valores, e a chave "localização" contendo uma tupla (cidade, estado). Armazene esses dicionários em uma nova lista chamada `perfis`.

3. **Comparando Estruturas ⭐⭐⭐**
   - Explique, em poucas palavras, as principais diferenças entre uma lista, um dicionário e uma tupla em Python. Dê exemplos de como cada estrutura pode ser usada no contexto da análise de dados do INFwebNET.

4. **Limpando o terreno ⭐⭐**
   - Alguns usuários do INFwebNET forneceram informações incompletas. Remova da lista `perfis` todos os perfis que não possuem as informações de "nome" ou "cidade". Mantenha a lista `perfis` original intacta, criando uma nova lista chamada `perfis_validos` para armazenar os perfis válidos.

5. **Carregando dados ⭐⭐⭐**
   - Crie uma implementação que leia os dados presentes no arquivo `base_inicial.txt` e os armazene na lista `perfis_validos`, criando novas palavras-chave para os dados adicionais encontrados. (O arquivo está disponível no repositório.)

6. **Concatenando dados ⭐**
   - Com os dados carregados no exercício anterior, adicione os usuários dos exercícios 1 e 2, definindo um padrão para lidar com os dados ausentes e salve estas informações em um arquivo `rede_INFNET.txt`.

7. **Adicionando Amigos ⭐**
   - Com o dicionário criado no exercício anterior, adicione um novo amigo ao set de amigos de um usuário específico.

8. **Verificando Conexões ⭐⭐**
   - Crie um programa que permita verificar se um determinado usuário foi adicionado como amigo de mais de 4 usuários. Caso tenha, exiba uma mensagem afirmando que o usuário é "popular".

9. **Amigos em Comum ⭐⭐**
   - Crie um programa que selecione dois perfis aleatórios e utilize sets para armazenar os amigos de cada um desses usuários do INFwebNET. Exiba os amigos em comum entre esses dois usuários, utilizando métodos e operação de sets.

10. **Conexões Exclusivas ⭐⭐**
    - Utilizando os sets do exercício anterior, exiba os amigos que são exclusivos de cada usuário, ou seja, aqueles que não são amigos em comum.

11. **Removendo Conexões ⭐⭐**
    - Permita que o usuário remova um amigo da lista de conexões de um membro do INFwebNET específico no dicionário criado no exercício 4.

12. **Salvando o Progresso ⭐⭐**
    - Após adicionar ou remover amigos, salve o dicionário atualizado em um novo arquivo chamado `rede_INFNET_atualizado.txt`.

13. **Listando Usuários ⭐**
    - Escreva um programa que leia o arquivo `rede_INFNET.txt` e imprima na tela a lista dos nomes de todos os usuários da rede social.

14. **Quantidade de Amigos ⭐⭐**
    - Crie uma função que leia o arquivo `rede_INFNET.txt` e mostre quantos amigos cada usuário possui, imprimindo o nome do usuário e a quantidade de amigos.

15. **Usuários Mais Populares ⭐⭐⭐**
    - Analise o arquivo `rede_INFNET_atualizado.txt` e identifique os 5 usuários que foram marcados como amigos pelo maior número de usuários cadastrados. Exiba o nome desses usuários e a quantidade de amigos que cada um possui.

16. **Lidando com arquivos ⭐⭐**
    - Explique com suas palavras a importância de utilizar o recurso `with` ao lidar com arquivos.
