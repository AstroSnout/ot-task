import os

os.environ["FLASK_APP"] = "main.py"
os.system('cmd /k flask run --port=5001')