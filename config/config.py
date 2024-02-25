from pathlib import Path

class Config:
    ROOT_PATH = Path(__file__).parent.parent
    RAW_DATA_PATH = ROOT_PATH / 'data' / 'raw'
    PROCESSED_DATA_PATH = ROOT_PATH / 'data' / 'processed'
    