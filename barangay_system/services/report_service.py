import csv
from pathlib import Path
from .resident_service import ResidentService
from .household_service import HouseholdService
from .official_service import OfficialService
from .certificate_service import CertificateService
import logging

logger = logging.getLogger("BIMS.ReportService")

class ReportService:
    @staticmethod
    def export_residents_csv():
        try:
            residents = ResidentService.get_all_residents()
            export_path = Path("barangay_system/exports/csv")
            export_path.mkdir(parents=True, exist_ok=True)
            file_path = export_path / "residents_report.csv"
            
            with open(file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Resident ID", "First Name", "Middle Name", "Last Name", 
                    "Gender", "Birthdate", "Age", "Civil Status", "Occupation", 
                    "Address", "Contact Number", "Voter Status"
                ])
                for r in residents:
                    writer.writerow([
                        r['resident_id'], r['first_name'], r['middle_name'], r['last_name'],
                        r['gender'], r['birthdate'], r['age'], r['civil_status'], r['occupation'],
                        r['address'], r['contact_number'], r['voter_status']
                    ])
            logger.info("Residents exported to CSV")
            return str(file_path)
        except Exception as e:
            logger.error(f"Error exporting residents to CSV: {e}")
            return False

    @staticmethod
    def export_households_csv():
        try:
            households = HouseholdService.get_all_households()
            export_path = Path("barangay_system/exports/csv")
            export_path.mkdir(parents=True, exist_ok=True)
            file_path = export_path / "households_report.csv"
            with open(file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Household ID", "Head Name", "Address", "Members"])
                for h in households:
                    writer.writerow([h['household_id'], h['head_name'], h['address'], h['members']])
            return str(file_path)
        except Exception as e:
            logger.error(f"Error exporting households: {e}")
            return False

    @staticmethod
    def export_officials_csv():
        try:
            officials = OfficialService.get_all_officials()
            export_path = Path("barangay_system/exports/csv")
            export_path.mkdir(parents=True, exist_ok=True)
            file_path = export_path / "officials_report.csv"
            with open(file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Name", "Position", "Term Start", "Term End", "Contact"])
                for o in officials:
                    writer.writerow([o['name'], o['position'], o['term_start'], o['term_end'], o['contact_number']])
            return str(file_path)
        except Exception as e:
            logger.error(f"Error exporting officials: {e}")
            return False

    @staticmethod
    def export_certificates_csv():
        try:
            certs = CertificateService.get_all_certificates()
            export_path = Path("barangay_system/exports/csv")
            export_path.mkdir(parents=True, exist_ok=True)
            file_path = export_path / "certificates_report.csv"
            with open(file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Cert Number", "Resident ID", "Type", "Issued Date"])
                for c in certs:
                    writer.writerow([c['certificate_number'], c['resident_id'], c['certificate_type'], c['issued_date']])
            return str(file_path)
        except Exception as e:
            logger.error(f"Error exporting certificates: {e}")
            return False

    @staticmethod
    def get_system_stats():
        return {
            "total_residents": ResidentService.get_total_count(),
            "total_households": HouseholdService.get_total_count(),
            "total_officials": OfficialService.get_total_count(),
            "total_certificates": CertificateService.get_total_count()
        }
