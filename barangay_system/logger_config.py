import logging
import os
from pathlib import Path

def setup_logging():
    log_dir = Path("barangay_system/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    
    log_file = log_dir / "app.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("BIMS")

logger = setup_logging()
