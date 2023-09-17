from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier import logger


STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==================x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare base model"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception()
    raise e