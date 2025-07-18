import os
import re

from mongoengine import connect

MONGODB_URI = os.getenv('MONGODB_URI')
# Atualização da regex para lidar com o formato do URI de conexão MongoDB
MONGO_CONNECTION_RE = re.compile(
    r'mongodb://'
    r'(?:(?P<username>[^:]+)(?::(?P<password>[^@]+))?@)?'   # Parte opcional de usuário e senha
    r'(?P<host>[^/]+)'
    r'(?::(?P<port>\d+))?'   # Parte opcional de porta
    r'?(/)?(?P<db>.*)'
)

def parse_mongo_connection_uri(uri):
    match = MONGO_CONNECTION_RE.match(uri)
    if match is None:
        # Se não houver correspondência, tentar um formato mais simples
        if uri.startswith('mongodb://localhost:'):
            # No formato simples, assume a porta e sem database
            parts = uri.split('/')
            host_port = parts[1].split(':')
            return {
                'host': host_port[0],
                'port': host_port[1] if len(host_port) > 1 else None,
                'db': None
            }
        else:
            # Caso não reconheça o formato, retorna um dicionário vazio
            return {}
    return match.groupdict()


if MONGODB_URI:
    print(f"Connecting to {MONGODB_URI}")
    connect(**parse_mongo_connection_uri(MONGODB_URI))
else:
    connect('dinacon')
