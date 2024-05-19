from src.TextSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline



class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        
        
    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = self.config.model_path
        #Prediction
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
        pipe = pipeline("summarization", model= model,tokenizer=tokenizer)

        ##
        print("Dialogue:")
        print(text)
        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel summary:")
        print(output)
        return output