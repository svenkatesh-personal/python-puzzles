# python-puzzles

## Setup and Usage

This project uses a shared virtual environment named `py-puzzles`.

### 1. Activate the Virtual Environment

Before running any Python scripts, you must activate the virtual environment.

**macOS/Linux:**
```bash
source py-puzzles/bin/activate
```

**Windows:**
```bash
py-puzzles\Scripts\activate
```

### 2. Running Scripts

Once the environment is activated, you can run scripts from any of the day directories.

Example:
```bash
python day-1/day_1_tuples.py
```

### 3. Deactivate

To exit the virtual environment, simply run:
```bash
deactivate
```

## Managing the Virtual Environment

### Updating Dependencies
If `requirements.txt` is updated, you can install the new dependencies by running:
```bash
pip install -r requirements.txt
```

### Re-creating the Environment
If you need to start fresh or if the virtual environment becomes corrupted:

1. **Deactivate** the current environment:
   ```bash
   deactivate
   ```

2. **Delete** the existing `py-puzzles` directory:
   ```bash
   rm -rf py-puzzles
   ```

3. **Re-create** the virtual environment:
   ```bash
   python3 -m venv py-puzzles
   ```

4. **Activate** and **Install** dependencies:
   ```bash
   source py-puzzles/bin/activate
   pip install -r requirements.txt
   ```

### VS Code Configuration
If you re-create the virtual environment with the **same name** (`py-puzzles`), no changes are needed in VS Code.

If you decide to **rename** the virtual environment folder, you must update `.vscode/settings.json`:
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/<NEW_VENV_NAME>/bin/python"
}
```