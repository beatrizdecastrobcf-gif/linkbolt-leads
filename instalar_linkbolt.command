#!/bin/bash
cd "$(dirname "$0")"
echo "=== Verificando ambiente LinkBolt Leads ==="
python3 --version || echo "Python 3 nao encontrado."
docker --version || echo "Docker nao encontrado."
chmod +x *.command scripts/*.py 2>/dev/null
echo "Ambiente pronto!"
