from ..database.database import get_connection
import logging

logger = logging.getLogger("BIMS.HouseholdService")

class HouseholdService:
    @staticmethod
    def add_household(data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO households (household_id, head_name, address, members) 
                VALUES (?, ?, ?, ?)
            """, (data['household_id'], data['head_name'], data['address'], data['members']))
            conn.commit()
            conn.close()
            logger.info(f"Household added: {data['household_id']}")
            return True
        except Exception as e:
            logger.error(f"Error adding household: {e}")
            return False

    @staticmethod
    def update_household(household_id, data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE households SET head_name=?, address=?, members=? 
                WHERE household_id=?
            """, (data['head_name'], data['address'], data['members'], household_id))
            conn.commit()
            conn.close()
            logger.info(f"Household updated: {household_id}")
            return True
        except Exception as e:
            logger.error(f"Error updating household: {e}")
            return False

    @staticmethod
    def delete_household(household_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM households WHERE household_id=?", (household_id,))
            conn.commit()
            conn.close()
            logger.info(f"Household deleted: {household_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting household: {e}")
            return False

    @staticmethod
    def get_all_households():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM households")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def search_households(query):
        conn = get_connection()
        cursor = conn.cursor()
        search_query = f"%{query}%"
        cursor.execute("""
            SELECT * FROM households 
            WHERE head_name LIKE ? OR household_id LIKE ?
        """, (search_query, search_query))
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def get_total_count():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM households")
        count = cursor.fetchone()[0]
        conn.close()
        return count
