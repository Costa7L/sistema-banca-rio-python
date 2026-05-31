saldo = 0

total_depositos = 0
total_saques = 0

quantidade_saques = 0
quantidade_depositos = 0

executando = True

while executando:

    print('\n1 - Verificar Saldo')
    print('2 - Realizar depósito')
    print('3 - Realizar Saque')
    print('4 - Ver Resumo')
    print('5 - Sair\n')

    escolha = int(input('Opção: '))

    if escolha == 1:
        print(f'Saldo atual: R$ {saldo:.2f}')

    elif escolha == 2:

        valor_deposito = float(input('Digite o valor do depósito: R$ '))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            total_depositos += valor_deposito
            quantidade_depositos += 1

            print('Depósito realizado com sucesso.')
            print(f'Saldo atual: R$ {saldo:.2f}')

        else:
            print('Valor inválido.')

    elif escolha == 3:

        valor_saque = float(input('Digite o valor do saque: R$ '))

        if valor_saque > saldo:
            print('Saldo insuficiente')

        else:
            saldo -= valor_saque
            total_saques += valor_saque
            quantidade_saques += 1

            print('Saque realizado com sucesso')
            print(f'Saldo atual: R$ {saldo:.2f}')

    elif escolha == 4:

        print('\n===== RESUMO =====')
        print(f'Saldo atual: {saldo:.2f}')
        print(f'Total depositado: R$ {total_depositos}')
        print(f'Total sacado: R$ {total_saques:.2f}')
        print(f'Quantidade de depósitos: {quantidade_depositos}')
        print(f'Quantidade de saques: {quantidade_saques}')

    elif escolha == 5:
        print('Sistema encerrado.')

        executando = False

    else:
        print('Opção inválida.') 

