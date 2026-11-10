# DevOps Status API

Aplicação de monitoramento simples containerizada e integrada com GitHub Actions e Docker Hub.

## Execução Local via Docker

```bash
docker build -t seu-usuario/status-api:1.0 .
docker run -d -p 8080:8080 --name status-api-local seu-usuario/status-api:1.0
curl http://localhost:8080/hello