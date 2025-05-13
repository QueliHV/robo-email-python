from imap_tools import MailBox
from dotenv import load_dotenv
import os
from datetime import datetime
import schedule
import time
import logging

# Configurar o log
logging.basicConfig(
    filename="execucao.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Carregar variáveis de ambiente
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER")

# Palavras-chave para filtrar no assunto
PALAVRAS_CHAVE = ["Nota Fiscal", "Cotação"]

# Caminho da pasta onde os anexos serão salvos
PASTA_ANEXOS = "anexos"

def executar():
    # Conectar à caixa de entrada
    with MailBox(IMAP_SERVER).login(EMAIL, PASSWORD, initial_folder='INBOX') as mailbox:
        print("Conectado com sucesso!")

        for msg in mailbox.fetch(limit=10, reverse=True):  # Pode ajustar o limit conforme quiser
            assunto = msg.subject or ""
            remetente = msg.from_ or "desconhecido"
            data = msg.date.strftime("%Y-%m-%d")

            # Verifica se o assunto contém alguma das palavras-chave
            if any(palavra.lower() in assunto.lower() for palavra in PALAVRAS_CHAVE):
                print(f"📩 Encontrado: {assunto}")
                logging.info(f"📩 Encontrado: {assunto}")

                if msg.attachments:
                    for anexo in msg.attachments:
                        nome_original = anexo.filename or "anexo_sem_nome"
                        nome_seguro = nome_original.replace(" ", "_")
                        nome_arquivo = f"{data}_{remetente}_{nome_seguro}"
                        
                        
                        # Criar subpasta por data, se ainda não existir
                        pasta_data = os.path.join(PASTA_ANEXOS, data)
                        os.makedirs(pasta_data, exist_ok=True)

                        # Caminho final do anexo com subpasta
                        caminho_completo = os.path.join(pasta_data, nome_arquivo)


                        # Salvar o anexo
                        with open(caminho_completo, "wb") as f:
                            f.write(anexo.payload)
                        
                        print(f"✅ Anexo salvo: {caminho_completo}")
                        logging.info(f"✅ Anexo salvo: {caminho_completo}")
                else:
                    print("⚠️ Sem anexos nesse e-mail.")
                    logging.info("⚠️ Sem anexos nesse e-mail.")


# Agendar execução a cada 30 minutos
schedule.every(30).minutes.do(executar)

print("⏳ Robô iniciado. Aguardando execuções automáticas...")

while True:
    schedule.run_pending()
    time.sleep(1)                    