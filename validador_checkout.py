import re

class EmailInvalidoError(Exception):
        """DISPARADA CASO O E-MAIL NÃO SIGA O PADRÃO"""
        pass

def validar_checkout():
    print('=== SISTEMA DE CHECKOUT (VALIDAÇÃO AVANÇADA ) ===')

    try :
        email = input("Validar e-mail de usuário:").strip()

        padrao_email = r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$"

        if not re.match(padrao_email, email):
            raise EmailInvalidoError('O formato do email está incorreto !')


        valor_ingresso = float(input('Digite o valor do ingresso:'))

        if valor_ingresso <= 0:

            raise ValueError('o valor do ingresso deve ser maior que zero!')

    except EmailInvalidoError as erro_email :
        print(f'Erro de validação: {erro_email}')

    except ValueError as erro_valor :
        print(f'Erro de entrada: {erro_valor}')


    else :
        print('\n Sucesso! Dados validados com precisão cirúrgica ')
        print(f'E-mail: {email} | Valor do ingresso: {valor_ingresso:.2f}')


    finally:
            print('Conexão com o validador encerrada com segurança ! ')


validar_checkout()
