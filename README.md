# AI-Image-Generator
Generate Images Using AI!
# 🎨 AI Image Generator (Python + OpenAI)

A simple **desktop application** built with **Python** and **Tkinter** that generates AI images from text prompts using the **OpenAI API**.

Type a description, generate ideas, and let the AI create images for you!

---

# 🚀 Features

✨ Generate AI image prompts from user text
🖼️ Automatically generate images from those prompts
👀 Preview generated images in the application
⬅️➡️ Navigate through images with arrow keys
💾 Images are automatically saved locally

---

# 🛠 Technologies Used

* 🐍 **Python**
* 🖥 **Tkinter** (GUI)
* 🤖 **OpenAI API**
* 🖼 **Pillow (PIL)** for image processing
* 🌐 **Requests**

---

# 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ai-image-generator.git
cd ai-image-generator
```

---

### 2️⃣ Install dependencies

```bash
pip install openai pillow requests
```

---

# 🔑 Setup API Key

You need an **OpenAI API key**.

Inside the code, find:

```python
client = openai.OpenAI(api_key="ENTER_YOUR_OWN_API_KEY")
```

Replace it with your own key:

```python
client = openai.OpenAI(api_key="sk-xxxxxxxxxxxxxxxx")
```

---

# ▶️ How to Run

Run the program with:

```bash
python main.py
```

The GUI window will open, and you can start generating images.

---

# ⚙️ How It Works

1️⃣ User enters a text prompt
2️⃣ The program generates **AI image ideas**
3️⃣ The AI creates images based on those ideas
4️⃣ Images are saved in the **outputs** folder
5️⃣ Images are displayed in the GUI

---

# 🎮 Controls

| Action         | Key            |
| -------------- | -------------- |
| Next Image     | ➡️ Right Arrow |
| Previous Image | ⬅️ Left Arrow  |

---

# 📂 Project Structure

```
project/
│
├── main.py
├── outputs/
│   └── generated images
└── README.md
```

---

# 📌 Notes

⚠️ Internet connection is required
📁 Images are automatically saved in the **outputs** folder
🔑 You must provide a valid **OpenAI API key**

