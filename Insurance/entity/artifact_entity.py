from dataclasses import dataclass

class DataIngestionArtifact:
    feature_store_file_path: str
    train_file_name: str
    test_file_name: str 
    