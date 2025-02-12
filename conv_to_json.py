import pandas as pd
import json

df = pd.read_csv("/home/pranil/python_projects/synthetic_dataset_generation_positive_mental_health/mental_health_dataset_positive_conversations.csv")

dataset = df.to_dict(orient="records")

# Save as a JSON file
with open('mental_health_dataset_positive_conversations.json', 'w') as json_file:
    json.dump(dataset, json_file, indent=4)
