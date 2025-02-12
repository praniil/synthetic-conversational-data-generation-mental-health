from huggingface_hub import HfApi, HfFolder

api = HfApi()
token = HfFolder.get_token()

dataset_file = "/home/pranil/python_projects/synthetic_dataset_generation_positive_mental_health/mental_health_dataset_positive_conversations.json"
repo_id = "Pranilllllll/mental-health-positive-conversation-dataset"

api.upload_file(
    path_or_fileobj=dataset_file,
    path_in_repo=dataset_file, 
    repo_id=repo_id,
    repo_type="dataset",
    token=token
)
