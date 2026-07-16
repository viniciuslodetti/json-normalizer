# JSON Normalizer

> A lightweight Python tool for cleaning, standardizing, and normalizing JSON files while preserving their original structure.

🇧🇷 **Portuguese version:** [README.pt-BR.md](README.pt-BR.md)

---

## ✨ Features

- 🧹 Remove HTML tags
- 📄 Remove unnecessary whitespace
- ✍️ Normalize text
- 📅 Standardize date formats
- 📂 Preserve the original JSON structure
- ⚡ Fast and lightweight
- 🔗 Easy to integrate into other projects

---

## 📁 Input Folder

Place the JSON file(s) you want to process inside:

```text
/jsons
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/viniciuslodetti/json-normalizer.git
```

Or download the project as a ZIP file.

### Install the dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python main.py
```

---

## 📄 Output

After execution, a new JSON file will be generated using the original filename with the suffix **Tratado**.

Example:

```text
products.json
        ↓
productsTratado.json
```

---

## 📌 Notes

- The original file is never modified.
- The processed file is automatically saved.
- All input files must be placed inside the `/jsons` directory.

---

## 🤝 Contributing

Contributions, suggestions and improvements are welcome.

Feel free to open an Issue or submit a Pull Request.
