import os
import yaml


class Utils:
    def __init__(self) -> None:
        pass

    def save_file(self, filename: str, data, path="output/scraped_articles"):
        with open(f"{path}/{filename}", "w", encoding="utf-8") as file:
            file.write(str(data))

    def load_file(self, filename: str, path="output/scraped_articles"):
        with open(f"{path}/{filename}", "r", encoding="utf-8") as file:
            data = file.read()
        return data

    def get_filenames_in_folder(self, path="output/scraped_articles"):
        filenames = os.listdir(path)
        return filenames

    def load_env(self):
        return os.getenv("OPENAI_API_KEY")

    def load_config(self):
        with open(f"config.yml", "r") as file:
            data = yaml.safe_load(file)
        return data
