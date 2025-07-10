# 🧘 ZenCLI — Your Minimalist Personal CLI Assistant

ZenCLI is a customizable command-line assistant built in Python.  
It helps you stay focused and organized every day — with notes, to-dos, journal entries, weather reports, and more.

---

## ✨ Features

- 📝 Create and list personal notes
- ✅ Manage your to-do list
- 📔 Write in your daily journal
- 🌤️ Get weather info based on your city
- 🕒 Display current time with your preferred format
- ⚙️ Configure name, location, and preferences
- 📁 Stores everything locally in JSON


## ⚙️ Installation

> Requires Python 3.9+

```bash
git clone https://github.com/your-username/ZenCLI.git
cd ZenCLI
pip install -r requirements.txt
```
If requirements.txt doesn't exist, install manually:
$ pip install typer rich requests

🚀 Usage
Run the CLI:
$ python3 main.py [command]

Example:
python3 main.py note add-note "Buy groceries"
python3 main.py todo add-task "Clean the house"


For help:
    $ python3 main.py --help

🧠 Tech Highlights
- Typer for CLI interface
- JSON for local storage (no DB needed)
- requests for fetching external API data
- Fully modular and easy to extend