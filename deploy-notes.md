# Despliegue simulado - Clínica Django
1. git clone https://github.com/melanybermeo/clinica-cicd.git
2. cd clinica-cicd
3. (Opcional) docker load -i clinica-doctor.tar
4. docker compose up -d --build
5. docker ps
6. Abrir http://localhost:8000
7. docker compose down
El job "deploy" de GitHub Actions ejecuta estos pasos automáticamente.