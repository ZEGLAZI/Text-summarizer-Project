from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.components.data_transformation import DataTransformation
from src.TextSummarizer.logging import logger


class DataTransformationTraningPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformaion_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config= data_transformaion_config)
        data_transformation.convert()