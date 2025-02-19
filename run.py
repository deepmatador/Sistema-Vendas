import subprocess

# Executar o setup.py
setup_process = subprocess.Popen(['python', 'setup.py'])

# Executar o mainserver.py dentro do diretório 'server'
server_process = subprocess.Popen(['python', 'server/mainserver.py'])

# Esperar ambos os processos terminarem
setup_process.wait()
server_process.wait()
