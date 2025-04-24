from nikolasigmoid/py-mcp-proxy:latest

copy requirements.txt .
run pip install -r requirements.txt
copy main.py .

run echo "{\"command\": \"python\", \"args\": [\"-c\", \"from main import mcp; mcp.run()\"]}" > config.json
