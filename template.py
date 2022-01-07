import os

#create the directories required

directories=[
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "src",
    "saved_models",
    "notebooks"
]
for dir_ in directories:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]

for file_ in files:
    with open(file_, "w") as f:
        pass