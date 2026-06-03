from ..database.database import get_connection
import logging

logger = logging.getLogger("BIMS.OfficialService")

class OfficialService:
    @staticmethod
    def add_official(data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO officials (name, position, term_start, term_end, contact_number) 
                VALUES (?, ?, ?, ?, ?)
            """, (data['name'], data['position'], data['term_start'], data['term_end'], data['contact_number']))
            conn.commit()
            conn.close()
            logger.info(f"Official added: {data['name']}")
            return True
        except Exception as e:
            logger.error(f"Error adding official: {e}")
            return False

    @staticmethod
    def update_official(id, data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE officials SET name=?, position=?, term_start=?, term_end=?, contact_number=? 
                WHERE id=?
            """, (data['name'], data['position'], data['term_start'], data['term_end'], data['contact_number'], id))
            conn.commit()
            conn.close()
            logger.info(f"Official updated ID: {id}")
            return True
        except Exception as e:
            logger.error(f"Error updating official: {e}")
            return False

    @staticmethod
    def delete_official(id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM officials WHERE id=?", (id,))
            conn.commit()
            conn.close()
            logger.info(f"Official deleted ID: {id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting official: {e}")
            return False

    @staticmethod
    def get_all_officials():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM officials")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def get_total_count():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM officials")
        count = cursor.fetchone()[0]
        conn.close()
        return count
