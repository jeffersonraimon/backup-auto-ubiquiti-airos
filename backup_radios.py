import paramiko
import os
import datetime

# Lista de rádios no formato ["IP:NOME"]
radios = [
    "10.2.100.1:AP-",
    "10.2.100.2:ESTACAO-",
]

# Credenciais SSH
USERNAME = "ubnt"
PASSWORD = "ubnt"

# Opções SSH para aceitar chaves RSA antigas
SSH_OPTIONS = "-o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa"

# Diretório de saída
OUTPUT_DIR = "/opt/backups"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_radio_config(ip, name):
    try:
        # Configurar cliente SSH
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=USERNAME, password=PASSWORD, look_for_keys=False, allow_agent=False)

        # Executar comando
        stdin, stdout, stderr = client.exec_command("cat /tmp/system.cfg")
        config_data = stdout.read().decode()
        error_data = stderr.read().decode()

        if error_data:
            print(f"Erro ao acessar {name} ({ip}): {error_data}")
            return

        # Nome do arquivo
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = f"{name}-{date_str}.cfg"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Salvar saída no arquivo
        with open(filepath, "w") as f:
            f.write(config_data)

        print(f"Configuração salva: {filepath}")
    except Exception as e:
        print(f"Erro ao conectar com {name} ({ip}): {e}")
    finally:
        client.close()

# Iterar sobre a lista de rádios
for radio in radios:
    ip, name = radio.split(":")
    get_radio_config(ip, name)
