import textract
import pandas as pd

def parse_resume(file_path):
    """
    Extract text from PDF or DOCX resume
    """
    text = textract.process(file_path).decode("utf-8")
    return text

def load_dataset():
    """
    Load Kaggle dataset for reference or model fine-tuning
    """
    df = pd.read_csv("data/Resume.csv")
    return df
