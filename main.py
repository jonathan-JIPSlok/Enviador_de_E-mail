import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

while True:
    print("\t\t\tSendEmails\n")
    print("Usar o Gmail (1) Usar outro (2)")
    User = '0'
    while not '1' in User and not '2' in User:
        User = input()
        
        if User == '1':
            host = 'smtp.gmail.com'
            port = 587
        elif User == '2':
            host = str(input("Host: "))
            try:
                port = int(input("Porta: "))
            except: print("Porta deve ser numerica!")
    print("Conectando ao servidor...")
    with smtplib.SMTP(host, port) as Server: #Abre o servidor.
        print("Conexão realizada")
        #Dados do usuario, email, e senha de APP
        Email = str(input("E-mail: "))
        Senha = str(input("Senha: "))
        
        #Login no servidor
        print("Indentificando...")
        Server.ehlo()
        
        print("Criptografando conexão...")
        Server.starttls()
        
        print("Fazendo Login...")
        Server.login(Email, Senha)
        
        print("Login Efetuado com sucesso!\n")
        
        #Criando Mensagem
        print("Preparando e-mail")
        while True:
            Msg = MIMEMultipart()
            Msg["From"] = input("Email: ")
            Msg["To"] = input("Destinatario: ")
            Msg["Subject"] = input("Assunto: ")
            Mensagem = input("Mensagem: ")
        
            Msg.attach(MIMEText(Mensagem, 'plain'))
            
            print(f"De: {Msg['From']}")
            print(f"Para: {Msg['To']}")
            print(f"Assunto: {Msg['Subject']}")
            print(f"\nMensagem: {Mensagem}\n")
            
            print("Continuar(1) Mudar(2)")
            if str(input()) =="1": break
            else: pass
            
        #Enviando Mensagem
        print("Enviando E-mail")
        Server.sendmail(Msg["From"], Msg["To"], Msg.as_string())
        print("E-mail enviado com sucesso")