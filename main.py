from src.TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline
from src.TextSummarizer.pipeline.stage_02_data_validation import DataValidationTraningPipeline
from src.TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTraningPipeline
from src.TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
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


STAGE_NAME = "Data Validation stage"

try :
    logger.info(f">>>>>>>> stage {STAGE_NAME} Started <<<<<<<<")
    data_validation = DataValidationTraningPipeline()
    data_validation.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<")
except Exception as e :
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"

try :
    logger.info(f">>>>>>>> stage {STAGE_NAME} Started <<<<<<<<")
    data_transformation = DataTransformationTraningPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<")
except Exception as e :
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"

try :
    logger.info(f">>>>>>>> stage {STAGE_NAME} Started <<<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<")
except Exception as e :
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation stage"

try :
    logger.info(f">>>>>>>> stage {STAGE_NAME} Started <<<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} Completed <<<<<<<<")
except Exception as e :
    logger.exception(e)
    raise e
