from ..database.database import get_connection
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from pathlib import Path
import datetime
import logging

logger = logging.getLogger("BIMS.CertificateService")

class CertificateService:
    @staticmethod
    def generate_certificate(resident_id, cert_type, cert_number):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM residents WHERE resident_id=?", (resident_id,))
            resident = cursor.fetchone()
            
            if not resident:
                logger.error(f"Resident not found: {resident_id}")
                return False

            issued_date = datetime.date.today().strftime("%Y-%m-%d")
            
            # Save to DB
            cursor.execute("""
                INSERT INTO certificates (certificate_number, resident_id, certificate_type, issued_date) 
                VALUES (?, ?, ?, ?)
            """, (cert_number, resident_id, cert_type, issued_date))
            conn.commit()
            conn.close()

            # Generate PDF
            export_path = Path("barangay_system/exports/pdf")
            export_path.mkdir(parents=True, exist_ok=True)
            file_name = f"{cert_type}_{cert_number}.pdf"
            full_path = export_path / file_name

            c = canvas.Canvas(str(full_path), pagesize=LETTER)
            c.setFont("Helvetica-Bold", 16)
            c.drawCentredString(300, 750, "REPUBLIC OF THE PHILIPPINES")
            c.drawCentredString(300, 730, "PROVINCE OF SAMPLE")
            c.drawCentredString(300, 710, "MUNICIPALITY OF SAMPLE")
            c.drawCentredString(300, 690, "BARANGAY SAMPLE")
            
            c.line(50, 670, 550, 670)
            
            c.setFont("Helvetica-Bold", 20)
            c.drawCentredString(300, 630, cert_type.upper())
            
            c.setFont("Helvetica", 12)
            c.drawString(50, 580, f"Certificate Number: {cert_number}")
            c.drawString(50, 560, f"Date Issued: {issued_date}")
            
            text = f"This is to certify that {resident['first_name']} {resident['middle_name'] or ''} {resident['last_name']}, "
            text += f"of legal age, {resident['gender']}, {resident['civil_status']}, is a resident of this Barangay."
            
            c.setFont("Helvetica", 12)
            c.drawString(50, 500, text)
            
            if cert_type == "Barangay Clearance":
                c.drawString(50, 480, "This clearance is issued for whatever legal purposes it may serve.")
            elif cert_type == "Certificate of Residency":
                c.drawString(50, 480, "This is issued for residency verification purposes.")
            elif cert_type == "Certificate of Indigency":
                c.drawString(50, 480, "This is issued for the purpose of availing educational/medical assistance.")

            c.drawString(350, 300, "_________________________")
            c.drawString(350, 280, "Punong Barangay")
            
            c.save()
            
            logger.info(f"Certificate generated: {cert_number} for {resident_id}")
            return str(full_path)
        except Exception as e:
            logger.error(f"Error generating certificate: {e}")
            return False

    @staticmethod
    def get_all_certificates():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM certificates")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def get_total_count():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM certificates")
        count = cursor.fetchone()[0]
        conn.close()
        return count
