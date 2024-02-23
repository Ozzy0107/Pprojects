import subprocess,os
from datetime import datetime, timedelta

os.system('clear')


def getAccs(dias):

    try:

            print("Apagando o conteudo do arquivo /tmp/contaslastlogon.txt...\n")

            with open('/tmp/contaslastlogon.txt', 'w') as file:
                pass

            print("Feito!\n")
            print("Iniciando a execucao do script que pega o ultimo login de todas as contas...\n")
            print("Executando /opt/zimbra/scripts/zimbraGetLastLogon/allaccslastlogon.sh\n")

            subprocess.call("/opt/zimbra/scripts/zimbraGetLastLogon/allaccslastlogon.sh")

            print("Feito!\n")
            print("Iniciando a tratativa dos dados, separando as contas e data de ultimo login por espaco e obtendo as contas que nao logam a X dias\n")
            print("Essas informacoes serao guardadas no arquivo temporario /tmp/accslastlogon_temp\n")

            with open('/tmp/accslastlogon_temp', 'r') as file:
                lines = file.readlines()

            users_lastlogon = []
            for line in lines:
                parts = line.strip().split(';')
                if len(parts) != 2:
                    continue

                email, date_str = parts
                if not date_str:
                    users_lastlogon.append(email)
                    continue

                if not email.count('@') == 1:
                    continue

                year = int(date_str[:4])
                month = int(date_str[4:6])
                day = int(date_str[6:8])
                login_date = datetime(year, month, day)

                if datetime.now() - login_date > timedelta(days=dias):
                    users_lastlogon.append(email)

            print("Feito!\n")
            print("Gravando o conteudo no arquivo /tmp/contaslastlogon.txt...\n")

            # Escreve o conteudo em um arquivo
            with open('/tmp/contaslastlogon.txt', 'w') as output_file:
                for user in users_lastlogon:
                    output_file.write(user + '\n')

            print("Feito!\n")
            print("Apagando o contedo do arquivo /tmp/accslastlogon_temp...\n")

            # Apaga o conteudo
            with open('/tmp/accslastlogon_temp', 'w') as file:
                pass

            print("Feito e finalizado! =]\n")
            print("O conteudo esta no arquivo /tmp/contaslastlogon.txt\n")
    except Exception as e:
        print("Erro: " + e)



if __name__ == '__main__':
    print("Obter informacoes de ultimo logon das contas\n\n")

    usrIpt = input("Informe o numero de dias para obter as contas que nao realizam logon.\nEx: Digite 50 e enter para obter contas que nao realizam logon a 50 dias.\n\n")

    usrIptInt = int(usrIpt)

    getAccs(usrIptInt)



