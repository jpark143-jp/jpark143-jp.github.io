import os

INPUT_DATASET = "C:/Users/JUNGHWAN PARK/Downloads/input/covid19-xray-dataset-train-test-sets/xray_dataset_covid19"

BASE_PATH = "C:/Users/JUNGHWAN PARK/Downloads/input/covid19-xray-dataset-train-test-sets/base"
TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH, "testing"])

TRAIN_SPLIT = 0.8
VAL_SPLIT = 0.1