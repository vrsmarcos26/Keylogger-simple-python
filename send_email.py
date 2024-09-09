import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time

def send_email_with_attachment(subject, body, to_email, attachment_path):
    # Informações da conta do Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'vrsmarcos26@gmail.com'
    password = 'fyom utcr lzmd udqe'  # Use a senha de aplicativo criada

    # Configuração do servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, password)

    while True:
        # Configuração do e-mail
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Adicionar corpo do e-mail
        msg.attach(MIMEText(body, 'plain'))

        # Anexar arquivo
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={attachment_path}')
            msg.attach(part)

        # Enviar e-mail
        server.send_message(msg)

        time.sleep(1800)

# Exemplo de uso
send_email_with_attachment(
    'Teste002',
    'Enviando teste002.',
    'vrsmarcos21@gmail.com',
    'Secret.zip'
)
