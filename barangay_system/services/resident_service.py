from ..database.database import get_connection
import logging

logger = logging.getLogger("BIMS.ResidentService")

class ResidentService:
    @staticmethod
    def add_resident(data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO residents (
                    resident_id, first_name, middle_name, last_name, gender, 
                    birthdate, age, civil_status, occupation, address, 
                    contact_number, voter_status, photo
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data['resident_id'], data['first_name'], data['middle_name'], 
                data['last_name'], data['gender'], data['birthdate'], data['age'], 
                data['civil_status'], data['occupation'], data['address'], 
                data['contact_number'], data['voter_status'], data.get('photo')
            ))
            conn.commit()
            conn.close()
            logger.info(f"Resident added: {data['resident_id']}")
            return True
        except Exception as e:
            logger.error(f"Error adding resident: {e}")
            return False

    @staticmethod
    def update_resident(resident_id, data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE residents SET 
                    first_name=?, middle_name=?, last_name=?, gender=?, 
                    birthdate=?, age=?, civil_status=?, occupation=?, address=?, 
                    contact_number=?, voter_status=?, photo=?
                WHERE resident_id=?
            """, (
                data['first_name'], data['middle_name'], data['last_name'], 
                data['gender'], data['birthdate'], data['age'], 
                data['civil_status'], data['occupation'], data['address'], 
                data['contact_number'], data['voter_status'], data.get('photo'),
                resident_id
            ))
            conn.commit()
            conn.close()
            logger.info(f"Resident updated: {resident_id}")
            return True
        except Exception as e:
            logger.error(f"Error updating resident: {e}")
            return False

    @staticmethod
    def delete_resident(resident_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM residents WHERE resident_id=?", (resident_id,))
            conn.commit()
            conn.close()
            logger.info(f"Resident deleted: {resident_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting resident: {e}")
            return False

    @staticmethod
    def get_all_residents():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM residents")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def search_residents(query):
        conn = get_connection()
        cursor = conn.cursor()
        search_query = f"%{query}%"
        cursor.execute("""
            SELECT * FROM residents 
            WHERE first_name LIKE ? OR last_name LIKE ? OR resident_id LIKE ?
        """, (search_query, search_query, search_query))
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def get_total_count():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM residents")
        count = cursor.fetchone()[0]
        conn.close()
        return count
