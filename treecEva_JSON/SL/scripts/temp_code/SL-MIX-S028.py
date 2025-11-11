from dataclasses import dataclass
from typing import List, Union

def compute_file_hash(name: str) -> int:
    return hash(name)

def compute_folder_hash(children: List[int]) -> int:
    return sum(children)

@dataclass
class FileNode:
    name: str
    def get_hash(self) -> int:
        return compute_file_hash(self.name)

@dataclass
class FolderNode:
    name: str
    children: List[Union['FolderNode', FileNode]]
    
    def get_hash(self) -> int:
        child_hashes = [child.get_hash() for child in self.children]
        return compute_folder_hash(child_hashes)

# Directory structure:
# root/
# ├── config.txt
# ├── src/
# │   ├── main.py
# │   └── utils.py
# └── docs/
#     └── readme.md

config_file = FileNode("config.txt")
main_file = FileNode("main.py")
utils_file = FileNode("utils.py")
readme_file = FileNode("readme.md")

src_folder = FolderNode("src", [main_file, utils_file])
docs_folder = FolderNode("docs", [readme_file])
root_folder = FolderNode("root", [config_file, src_folder, docs_folder])

root_hash = root_folder.get_hash()
print(f"Result: {root_hash}")