import logging
from email_sender import send_email

class EmailHandler(logging.Handler):
    """Handler que envia email apenas para logs de erro ou críticos"""

    def emit(self, record):
        if record.levelno >= logging.ERROR:  # ERROR ou CRITICAL
            log_entry = self.format(record)
            try:
                send_email(
                    subject=f"[Pipeline Log] {record.levelname}",
                    body=log_entry
                )
            except Exception as e:
                print(f"❌ Falha ao enviar log por email: {e}")

def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:  # evita duplicar handlers
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # Log em arquivo
        file_handler = logging.FileHandler("pipeline.log", encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        # Log no console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)

        # Handler de email para ERROR+
        email_handler = EmailHandler()
        email_handler.setLevel(logging.ERROR)
        email_handler.setFormatter(formatter)

        # Adiciona handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        logger.addHandler(email_handler)

    return logger
