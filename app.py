from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv  

# Carga las variables del archivo .env
load_dotenv()

app = Flask(__name__)

# Función para obtener los datos de conexión desde el entorno
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        port=os.getenv('DB_PORT'),
        connect_timeout=5
    )

@app.route('/transferir', methods=['POST'])
def transferir():
    datos = request.json
    monto = datos.get('monto', 0)
    origen = datos.get('origen', 'DESCONOCIDO')
    destino = datos.get('destino', 'DESCONOCIDO')

    try:
      
        conn = get_db_connection()
        cur = conn.cursor()

        sql = """INSERT INTO transacciones_spei (tipo_operacion, monto, cuenta_origen, cuenta_destino, estatus)
                 VALUES (%s, %s, %s, %s, %s)"""
        
        cur.execute(sql, ('ENVIO', monto, origen, destino, 'EXITOSO'))

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"status": "ok", "mensaje": "SPEI procesado", "monto": monto}), 201

    except Exception as e:
        
        print(f"!!! ERROR DETECTADO: {str(e)}") 
        return jsonify({"status": "error", "mensaje": str(e)}), 500

if __name__ == '__main__':
    # host 0.0.0.0 para que sea visible desde Windows a través de Docker
    app.run(host='0.0.0.0', port=5000, debug=True)
