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
2. **Configurar variables de entorno:**
Crear un archivo .env con las credenciales de la base de datos (DB_HOST, DB_NAME, DB_USER, DB_PASS).

3. **Construir y ejecutar con Docker:**

```bash
docker build -t spei-api .
docker run -d --name contenedor-spei -p 5000:5000 spei-api
```

4. **Curl en Powershell:**
```bash
PowerShell
$body = @{
    monto = 750.00
    origen = "CUENTA-NOMINA"
    destino = "CUENTA-SPEI"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://<TU_IP>:5000/transferir" -Method Post -Body $body -ContentType "application/json"
```

graph TD
    %% Define los estilos para los diferentes componentes
    classDef client fill:#f9f,stroke:#333,stroke-width:2px,color:black;
    classDef host fill:#bbf,stroke:#333,stroke-width:2px,color:black;
    classDef container fill:#dfd,stroke:#333,stroke-width:2px,color:black;
    classDef database fill:#fdd,stroke:#333,stroke-width:2px,color:black;

    %% Define los nodos y sus etiquetas
    subgraph Client_Network [Red del Cliente (Segmento .3)]
        PowerShell_Client[Cliente Windows (PowerShell/Curl)]:::client
    end

    subgraph Oracle_Linux_Host [Oracle Linux Host (192.168.3.118)]:::host
        Docker_Engine[Docker Engine]:::host
        PostgreSQL_DB[(PostgreSQL DB: postgres)]:::database
        
        subgraph Docker_Network [Red de Docker Bridge]:::container
            SPEI_API_Container[Contenedor spei-api (Flask)]:::container
        end
    end

    %% Define las conexiones y sus etiquetas (flujo de red)
    PowerShell_Client -- "POST /transferir (Puerto 5000)" --> Oracle_Linux_Host
    Oracle_Linux_Host -- "Port Forwarding (5000:5000)" --> SPEI_API_Container
    SPEI_API_Container -- "Conexión a la DB (Host: 192.168.3.118, Puerto 5432)" --> PostgreSQL_DB
