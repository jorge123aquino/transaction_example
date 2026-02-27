# SPEI Transaction Simulator (Python & Docker)

Este proyecto es una API REST robusta desarrollada en **Python/Flask** que simula el procesamiento de transferencias interbancarias (SPEI).

## 🚀 Características Técnicas

* **Arquitectura de Microservicios:** Aplicación contenerizada con **Docker** para asegurar portabilidad entre entornos (Oracle Linux/Windows).
* **Seguridad y Configuración:** Implementación de variables de entorno (`python-dotenv`) para la gestión segura de credenciales y parámetros de red.
* **Base de Datos:** Persistencia en **PostgreSQL**, utilizando consultas parametrizadas para prevenir ataques de SQL Injection.
* **Networking:** Configuración de redes en contenedores para comunicación eficiente entre subredes.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Framework:** Flask
* **Contenedores:** Docker
* **SO del Servidor:** Oracle Linux
* **Base de Datos:** PostgreSQL

## 📦 Instalación y Despliegue

1. **Clonar el repositorio:**
```bash
git clone https://github.com/jorge123aquino/transaction_example.git
```
2.Configurar variables de entorno:
Crear un archivo .env con las credenciales de la base de datos (DB_HOST, DB_NAME, DB_USER, DB_PASS).

3.Construir y ejecutar con Docker:

```bash
docker build -t spei-api .
docker run -d --name contenedor-spei -p 5000:5000 spei-api
```

4.Curl en Powershell:
```bash
PowerShell
$body = @{
    monto = 750.00
    origen = "CUENTA-NOMINA"
    destino = "CUENTA-SPEI"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://<TU_IP>:5000/transferir" -Method Post -Body $body -ContentType "application/json"
```
