# 🤖 Robô de E-mails com Python – Automação com IMAP

Este projeto é um robô simples e eficiente que se conecta a uma conta Gmail via IMAP, filtra e-mails por assunto (ex: "Nota Fiscal", "Cotação") e salva automaticamente os anexos em pastas organizadas por data. Também registra logs de execução e roda automaticamente a cada 30 minutos usando a biblioteca `schedule`.

## ✨ Funcionalidades

- Conexão segura com conta Gmail via senha de app
- Filtro de e-mails com palavras-chave definidas
- Download automático de anexos
- Organização por data em subpastas
- Log de execução com status das ações
- Execução automática com agendamento interno (usando `schedule`)

## 🛠️ Tecnologias utilizadas

- Python 3
- imap-tools
- python-dotenv
- schedule
- logging

## 🧪 Como rodar o projeto

1. Clone o repositório e acesse a pasta:

```bash
git clone https://github.com/QueliHV/robo-email-python.git
cd robo-email-python
```

2. Crie o ambiente virtual e ative:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Copie o arquivo `.env.example` para `.env` e preencha com suas credenciais:

```env
EMAIL=seu_email@gmail.com
PASSWORD=sua_senha_de_app
IMAP_SERVER=imap.gmail.com
```

> Lembre-se de ativar o IMAP nas configurações do Gmail e usar uma senha de app.

5. Execute o robô:

```bash
python main.py
```

Você verá no terminal:

```
⏳ Robô iniciado. Aguardando execuções automáticas...
📩 Encontrado: Cotação Cliente XPTO
✅ Anexo salvo: anexos/2024-05-14/2024-05-14_remetente_arquivo.pdf
```

## 📂 Estrutura de pastas

```
robo-email-python/
├── .venv/
├── anexos/
│   └── 2024-05-14/
├── main.py
├── .env.example
├── requirements.txt
├── execucao.log
└── README.md
```

## 📌 Observações

- Este projeto usa `schedule` para agendamento simples. Para produção, recomenda-se usar `cron`, `systemd` ou serviços de nuvem.
- O arquivo `.env` nunca deve ser enviado ao GitHub.

## 👤 Contato

Desenvolvido por **Queli Hesper** – [LinkedIn](https://www.linkedin.com/in/quelihesper/)
