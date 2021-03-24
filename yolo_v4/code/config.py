import os 
from pathlib import Path
PROJECT_PATH = os.path.abspath(__file__)

PROJECT_PATH = Path(PROJECT_PATH).parent.parent
CODE_PATH  = os.path.join(PROJECT_PATH,"code")
DATA_PATH  = os.path.join(PROJECT_PATH,"data")
print(DATA_PATH)
COUNT_IMAGE = 0



