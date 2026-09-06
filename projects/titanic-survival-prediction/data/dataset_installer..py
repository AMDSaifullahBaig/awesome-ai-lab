import kagglehub
import shutil
from pathlib import Path

# Folder where this loader.py exists
data_folder = Path(__file__).parent

# Download Titanic competition files
download_path = kagglehub.competition_download("titanic")

print("Downloaded to:", download_path)

# Copy files into the data folder
for file in Path(download_path).iterdir():
    if file.is_file():
        destination = data_folder / file.name
        shutil.copy2(file, destination)
        print(f"Copied: {file.name}")

print("Dataset setup complete.")