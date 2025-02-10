# Backup de Configuração de Rádios

Este script em Python acessa uma lista de rádios via SSH, obtém a configuração de cada um e salva os arquivos em `/opt/backups`.

## Instalação

1. Instale a biblioteca necessária:
   ```bash
   pip install paramiko
   ```

2. Salve o script em um diretório apropriado, por exemplo:
   ```bash
   /opt/scripts/backup_radios.py
   ```

3. Torne o script executável:
   ```bash
   chmod +x /opt/scripts/backup_radios.py
   ```

## Execução Manual

Para executar manualmente, use:
```bash
/usr/bin/python3 /opt/scripts/backup_radios.py
```

## Agendamento com Cron

Para executar automaticamente todos os dias às 1h da manhã:

1. Edite o crontab:
   ```bash
   crontab -e
   ```

2. Adicione a seguinte linha no final:
   ```bash
   0 1 * * * /usr/bin/python3 /opt/scripts/backup_radios.py >> /opt/backups/backup.log 2>&1
   ```

Isso garantirá que o backup seja feito diariamente e que a saída do script seja registrada em `/opt/backups/backup.log`.

## Logs

Os logs da execução serão salvos em:
```
/opt/backups/backup.log
```

Se precisar de ajustes, modifique o script conforme necessário.

