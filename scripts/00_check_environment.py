"""Check the Python environment. Reads no data and changes no files."""
import importlib
import sys

if sys.version_info < (3, 10):
    raise SystemExit("Python 3.10 or later is required.")
print(f"Python {sys.version.split()[0]}")
missing = []
for name in ["numpy", "pandas", "matplotlib", "scipy"]:
    try:
        module = importlib.import_module(name)
        print(f"{name}: {module.__version__}")
    except ImportError:
        missing.append(name)
if missing:
    raise SystemExit("Missing packages: " + ", ".join(missing) + ". See the setup prompt in README.md.")
print("Environment check passed.")
