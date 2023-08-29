from pathlib import Path                #defining all the constants in this file and they will be used in every other file

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAM_FILE_PATH = Path("params.yaml")
# config = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, param_filepath=PARAM_FILE_PATH)
# data_ingestion_config = config.get_data_ingestion_config()
# data_ingestion = DataIngestion(config=data_ingestion_config)