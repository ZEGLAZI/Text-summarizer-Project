from src.TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline
from src.TextSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

try :
    logger.info(f">>>>>>>> stage {STAGE_NAME} Started <<<<<<<<")
    data_ingestion = DataIngestionTraningPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<")
except Exception as e :
    logger.exception(e)
    raise e



