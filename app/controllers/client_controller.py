import psycopg2
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.client_model import Client
from fastapi.encoders import jsonable_encoder

class ClientController:

    def create_client(self, client: Client):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO cliente 
                (pn, pa, sg, sa, numero_documento, correo, telefono, id_tipo_documento)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                client.primer_nombre,
                client.primer_apellido,
                client.segundo_nombre,
                client.segundo_apellido,
                client.numero_documento,
                client.correo,
                client.telefono,
                client.tipo_documento_id
            ))
            conn.commit()
            return {"resultado": "Cliente creado"}
        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error creando cliente")
        finally:
            conn.close()

    def get_clients(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cliente")
            result = cursor.fetchall()

            payload = []
            for data in result:
                payload.append({
                    "id": data[0],
                    "pn": data[1],
                    "pa": data[2],
                    "sg": data[3],
                    "sa": data[4],
                    "tipo_documento_id": data[5],
                    "numero_documento": data[6],
                    "correo": data[7],
                    "telefono": data[8],
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error obteniendo clientes")
        finally:
            conn.close()

    def delete_client(self, client_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cliente WHERE id=%s", (client_id,))
            conn.commit()
            return {"resultado": "Cliente eliminado"}
        except psycopg2.Error:
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error eliminando cliente")
        finally:
            conn.close()