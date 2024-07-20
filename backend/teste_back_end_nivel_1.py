#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

# Será necessário passar por todos os produtos para verificar 1 a 1
# A maneira mais direta de fazer isso é com um nested loop para cada "profundida"
# Até chegar no preço
for loja in response:
    for produto in loja["produtos"]:
        if produto["preço"] > 30:
            print(produto)





#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

# Conhecendo o json de antemão é uma questão trivial de acessar a variável
print(responsejson["produtos"][1]["preço"])

# Se o json fosse desconhecido e eu precisasse buscar o produto, modificaria o código da questão
# Anterior da seguinte forma:
for produto in responsejson["produtos"]:
    if produto["nome"] == "Produto B":
        print(produto["preço"])
        break
else: # Prefiro a estrutura for-else a criar uma variável booleana para salvar o achado por ser mais concisa.
    print("Não há produto com o nome procurado")



#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

# Certamente o jeito mais prático é usar o método python sort
# Afinal, por ser uma otimização de um mergesort é muito escalável
lista.sort()
print(lista)

# Agora, se precisasse escrever do zero usari um bubble sort com sentinela
# Pela praticidade, é ineficiente, mas isso é pouco relevante para uma lista 
# Deste tamanho
lista = [5,8,3,0,8,1,9,10,20,30]


for i in range(len(lista)-1):
    sorted = True # Sentinela
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
            sorted = False
    if sorted:
        break
print(lista)




#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela

# O método strip() tira os espaços automaticamente, então é apenas uma
# Questão de usar list comprehension
lista = ["   joao   ","   maria   ","  joana  "]
print([x.strip() for x in lista])



#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]
del lista[1] # Imagino que a pegadinha era o segundo item ser o index 1
print(lista)


#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]
def callback(nome): # Callback para o map
    if nome == "joao":
        return "maria"
    return nome

lista = map(callback, lista) # usei mapa para demonstrar versatilidade, mas o mesmo efeito teria um loop
print(list(lista)) # Transformação de novo em lista

#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra
lista = [x for x in range(10, 0, -1)] # Fiz assim mais para mostrrar versatilidade
cont = 0
while cont <= 5:
    print(lista[cont]) # Usei o próprio contador por me parecer a solução mais sucinta e clara
    cont += 1



#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra
import requests
def task_8(data):
    completed = 0
    for item in data:
        if item['completed']: #Verifica o valor booleano
            completed += 1

    return (completed, len(data)-completed) #retornei uma tupla por me parecer um item de natureza imutável
    # decidi salvar apenas os completos para economizar processos
try:
    request = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = request.json()

    resposta_8 = task_8(data)
    print(f'{resposta_8[0]} tarefas completas \n{resposta_8[1]} tarefas pendentes')
except:
    print('Houve alguma falha no processo')

#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra
request = requests.get('https://jsonplaceholder.typicode.com/users')
required_data = [] # Escolhi salvar em um dicionário pela natureza categóriga dos dados
for item in request.json():
    new_dict = {}
    new_dict['nome'] = item["name"]
    new_dict['username'] = item['username']
    new_dict['email'] = item["email"]
    new_dict['rua'] = item['address']['street'] 
    new_dict['número'] = item['phone']
    required_data.append(new_dict)

# Para ser honesto não entendi exatamente o que seria "retirar" mas acredito que ir chave a chave é o método mais simples

#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO
lista = [x for x in range(10)]
lista.append(10)
print(lista)



#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO
lista = [x for x in range(10)]
lista.insert(0, -1)
print(lista)

#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta


# Adoraria fazer, mas infelizmente não tive o tempo essa semana. Mas eu fiz um trabalho bem parecido com isso no primeiro semeste da faculdade, apenas sem as partes POO








