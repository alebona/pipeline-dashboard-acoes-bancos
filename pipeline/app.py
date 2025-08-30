import time
import os
from dotenv import load_dotenv
import extracao
import transformacao
from logger import get_logger

# Carrega variáveis do .env
load_dotenv()

# Intervalo entre execuções (padrão 300s = 5 min)
INTERVALO = int(os.getenv("INTERVALO_ATUALIZACAO", 300))

# Inicializa o logger
logger = get_logger(__name__)


def orquestrar():
    while True:
        try:
            logger.info("🚀 Iniciando pipeline ETL...")

            # 1. Extração
            extracao.extrair_dados()
            logger.info("✅ Extração concluída")

            # 2. Transformação
            transformacao.transformar_dados()
            logger.info("✅ Transformação concluída")

            logger.info("🏁 Pipeline finalizado com sucesso")

        except Exception as e:
            # Qualquer exceção aqui dispara um log ERROR e envia email
            logger.error(f"❌ Erro durante o pipeline: {e}")

        # Pausa antes da próxima execução
        logger.info(f"⏳ Aguardando {INTERVALO} segundos para próxima atualização...\n")
        time.sleep(INTERVALO)


if __name__ == "__main__":
    orquestrar()
