# crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , 
# aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. 
# a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

from os import system
from sys import platform
import pandas as pd
contas = pd.read_csv('backend\contas.csv') # Abre as contas salvas


class ContaPessoal:
    def __init__(self, nome, cpf, saldo=0) -> None:
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        ContaPessoal.id += 1
        self.id = ContaPessoal.id

    id = contas['Id'].iloc[-1] # Identifica o último Id gerado

    def depositar(self, deposito):
        self.saldo += deposito
        return self.saldo
        

    def sacar(self, saque):
        if saque <= self.saldo:
            self.saldo -= saque
            print('Saque realizado com sucesso')
            return self.saldo
        else:
            print('Não há saldo suficiente')
            return self.saldo
        
def limpar_tela(arg=platform): #função que limpa o console
    if arg == "win32": 
        system('cls')
    else:
        system('clear')

limpar_tela()

encerrar = False

while not encerrar:
    
    # Menu principal
    print('*** Bem vindo ao banco Pegazus ***\n\n')
    cpf_usuario = input('Digite o seu CPF: ')
    # Tira possíveis pontos ou hífens
    cpf_usuario = int(''.join(char for char in cpf_usuario if char.isnumeric()))

    limpar_tela()
    
    # Usuário Cadastrado
    if cpf_usuario in contas['CPF'].values:
        conta = int(contas[contas['CPF'] == cpf_usuario].index[0])
        usuario = ContaPessoal(contas.loc[conta]['Nome'], contas.loc[conta]['CPF'], contas.loc[conta]['Saldo'])
        sair_conta = False
        while not sair_conta:
            print(f'*** Olá {usuario.nome} ***')
            print(f'Seu saldo atual é de: {usuario.saldo}\n')
            print(f'Para fazer um DEPÓSITO digite (1)\nPara fazer um SAQUE digite(2)\nPara SAIR digite (0)')
            op = input().upper()
            limpar_tela()

            if op == '1' or op == '(1)' or op == 'DEPÓSITO':
                contas.loc[conta, 'Saldo'] = usuario.depositar(float(input('Digite o valor do depósito: ')))


            elif op == '2' or op == '(2)' or op == 'SAQUE':
                contas.loc[conta, 'Saldo'] = usuario.sacar(float(input('Digite o valor do saque: ')))
            
            elif op == '0' or op == '(0)' or op == 'SAIR':
                sair_conta = encerrar = True
                contas.to_csv('backend\contas.csv', index=False)

            input('PRECIONE ENTER PARA CONTINUAR\n')
            limpar_tela()


    # Usuário não cadastrado
    else:
        print('Parece que você não tem uma conta')
        print('Se deseja CRIAR CONTA digite (1)\nPara tentar OUTRO CPF digite (2)\nPara ENCERRAR digite (0)')
        op = input().upper()
        limpar_tela()
        
        if op == '1' or op == '(1)':
            nome_usuario = input('Para criar uma nova conta basta apenas escrever o seu nome: ')
            nova_conta = ContaPessoal(cpf_usuario, nome_usuario)
            contas.loc[len(contas)] = [nova_conta.id, nova_conta.cpf, nova_conta.nome, nova_conta.saldo]
            contas.to_csv('backend\contas.csv', index=False)

            print('Conta criada com sucesso!\nRedirecionando para o menu principal')

        elif op == '2' or op == '(2)':
            print('Redirecionando para o menu principal')
        
        elif op == '0' or op == '(0)':
            encerrar = True
        
        input('PRECIONE ENTER PARA CONTINUAR\n')

    limpar_tela()


