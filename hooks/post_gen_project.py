"""Post-generation hook para renombrar archivos dot_* a .*"""

import os
from pathlib import Path

# Archivos a renombrar
dot_files = [
    ("dot_gitignore", ".gitignore"),
    ("dot_pre-commit-config.yaml", ".pre-commit-config.yaml"),
    ("dot_env.example", ".env.example"),
    ("dot_dockerignore", ".dockerignore"),
    ("dot_github", ".github"),
]

project_dir = Path.cwd()

for old_name, new_name in dot_files:
    old_path = project_dir / old_name
    new_path = project_dir / new_name
    if old_path.exists():
        old_path.rename(new_path)
