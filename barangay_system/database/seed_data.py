import sqlite3
import datetime
from pathlib import Path

DB_PATH = Path("barangay_system/database/barangay.db")

def seed_database():
    if not DB_PATH.exists():
        print("Database not found. Please run the application or init_db first.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Sample Residents (Philippine-based names)
    residents = [
        ('RES-001', 'Juan', 'Protasio', 'Dela Cruz', 'Male', '1985-05-15', 39, 'Married', 'Teacher', '123 Rizal St. Brgy. Sample', '09171234567', 'Voter', None),
        ('RES-002', 'Maria', 'Clara', 'Santos', 'Female', '1990-08-20', 33, 'Single', 'Nurse', '456 Mabini St. Brgy. Sample', '09187654321', 'Voter', None),
        ('RES-003', 'Jose', 'P.', 'Rizal', 'Male', '1861-06-19', 162, 'Single', 'Doctor', 'Calamba, Laguna (Honorary)', '09190000000', 'Voter', None),
        ('RES-004', 'Liza', 'Soberano', 'Esperanza', 'Female', '1998-01-04', 26, 'Single', 'Actress', '789 Quezon Ave. Brgy. Sample', '09201112222', 'Voter', None),
        ('RES-005', 'Manny', 'Dapidran', 'Pacquiao', 'Male', '1978-12-17', 45, 'Married', 'Professional Boxer', 'General Santos City', '09213334444', 'Voter', None),
        ('RES-006', 'Catriona', 'Magnayon', 'Gray', 'Female', '1994-01-06', 30, 'Single', 'Model', 'Albay, Bicol', '09225556666', 'Voter', None),
        ('RES-007', 'Antonio', 'Luna', 'Novicio', 'Male', '1866-10-29', 157, 'Single', 'General', 'Ilocos Norte', '09237778888', 'Voter', None),
        ('RES-008', 'Melchora', 'Aquino', 'de Ramos', 'Female', '1812-01-06', 212, 'Widowed', 'Tandang Sora', 'Banlat, Quezon City', '09249990000', 'Voter', None),
        ('RES-009', 'Efren', 'Penaflorida', 'Jr.', 'Male', '1981-03-05', 43, 'Single', 'Social Worker', 'Cavite City', '09251113333', 'Voter', None),
        ('RES-010', 'Lea', 'Salonga', 'Chien', 'Female', '1971-02-22', 53, 'Married', 'Singer', 'Manila', '09262224444', 'Voter', None)
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO residents (
            resident_id, first_name, middle_name, last_name, gender, 
            birthdate, age, civil_status, occupation, address, 
            contact_number, voter_status, photo
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, residents)

    # Sample Households
    households = [
        ('HH-001', 'Dela Cruz, Juan', '123 Rizal St. Brgy. Sample', '5'),
        ('HH-002', 'Santos, Maria', '456 Mabini St. Brgy. Sample', '3'),
        ('HH-003', 'Pacquiao, Manny', 'General Santos City', '8'),
        ('HH-004', 'Salonga, Lea', 'Manila', '4')
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO households (household_id, head_name, address, members) 
        VALUES (?, ?, ?, ?)
    """, households)

    # Sample Officials
    officials = [
        ('Ricardo Dalisay', 'Barangay Captain', '2023-01-01', '2026-01-01', '0917-CAPTAIN'),
        ('Cardo Dalisay Jr.', 'Barangay Kagawad', '2023-01-01', '2026-01-01', '0917-KAGAWAD1'),
        ('Niana Guerrero', 'SK Chairperson', '2023-01-01', '2026-01-01', '0917-SKCHAIR'),
        ('Vic Sotto', 'Barangay Secretary', '2023-01-01', '2026-01-01', '0917-SEC'),
        ('Pia Wurtzbach', 'Barangay Treasurer', '2023-01-01', '2026-01-01', '0917-TREAS')
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO officials (name, position, term_start, term_end, contact_number) 
        VALUES (?, ?, ?, ?, ?)
    """, officials)

    conn.commit()
    conn.close()
    print("Database seeded with Philippine-based sample data successfully.")

if __name__ == "__main__":
    seed_database()
