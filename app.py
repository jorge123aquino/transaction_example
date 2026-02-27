from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Configuración de conexión (la misma que ya probaste)
DB_CONFIG = {
    "host": "192.168.3.118",
    "database": "spei_db",
    "user": "spei_user",
    "password": "jorge"
}

@app.route('/transferir', methods=['POST'])
def transferir():
    datos = request.json
    
    # Usamos tu lógica de seguridad .get()
    monto = datos.get('monto', 0)
    origen = datos.get('origen', 'DESCONOCIDO')
    destino = datos.get('destino', 'DESCONOCIDO')

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        sql = """INSERT INTO transacciones_spei (tipo_operacion, monto, cuenta_origen, cuenta_destino, estatus) 
                 VALUES (%s, %s, %s, %s, %s)"""
        cur.execute(sql, ('ENVIO', monto, origen, destino, 'EXITOSO'))
        
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({"status": "ok", "mensaje": "SPEI procesado", "monto": monto}), 201
    
    except Exception as e:
        return jsonify({"status": "error", "mensaje": str(e)}), 500

if __name__ == '__main__':
    # Importante: host 0.0.0.0 para que Docker sea visible
    app.run(host='0.0.0.0', port=5000)
