import keepassxc_proxy_client.protocol

connection = keepassxc_proxy_client.protocol.Connection()
connection.connect()
connection.associate()  # Não precisa dar print

logins = connection.get_logins("https://matrix.org")
if logins:
    usuario = logins[0]['login']
    senha = logins[0]['password']
    # Gere comandos PowerShell:
    print(f"$Env:MATRIX_USER = '{usuario}'")
    print(f"$Env:MATRIX_PASSWORD = '{senha}'")
    print(f"$Env:MATRIX_ROOM_IDS = 'sala1, sala2'")
    print(f"$Env:MATRIX_HOST = 'https://matrix.org'")