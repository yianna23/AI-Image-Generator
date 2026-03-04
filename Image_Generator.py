from tkinter import *
from tkinter import ttk
import tkinter as tk

import requests
import openai
import os
import base64

from PIL import Image, ImageTk

client = openai.OpenAI(api_key="ENTER_YOUR_OWN_API_KEY")

cIndex = 0
image_paths = []

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

BG = "#FD96A9"
BTN_BG = "#FCF6BD"
TXT = "#2B2B2B"


def process():
    global image_paths, cIndex
    user = main_entry.get().strip()
    if rb.get() == "Choice1":
        n = 1
    else:
        n = 2

    ideas = generate_ideas(user, n)
    image_paths = generate_images_from_ideas2(ideas)
    cIndex = 0
    if image_paths:
        showImage(0)


def generate_ideas(user_text, n):
    prompt = (
        f"Generate {n} a prompt that will be given to a image generator, make it straight forward, based on: {user_text}\n"
        f"Return ONLY a numbered list from 1 to {n}. One idea per line."
    )

    resp = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )
    ideas = []
    for line in resp.choices[0].message.content.splitlines():
        line = line.strip()
        if line:
            ideas.append(line)
    return ideas[:n]


def generate_images_from_ideas(ideas):
    paths = []

    for i in range(len(ideas)):
        idea = ideas[i]

        img = client.images.generate(
            model="dall-e-3",
            prompt=idea,
            size="1024x1024",
            n=1
        )

        url = img.data[0].url
        filepath = OUTPUT_DIR + "/request" + str(i + 1) + ".jpg"
        download_image(url, filepath)
        paths.append(filepath)

    return paths


def generate_images_from_ideas2(ideas):
    paths = []

    for i in range(len(ideas)):
        idea = ideas[i]

        img = client.images.generate(
            model="gpt-image-1",
            prompt=idea,
            size="1024x1024",
            n=1,
            output_format="jpeg"
        )

        filepath = os.path.join(OUTPUT_DIR, f"request_{i+1}.jpg")
        b64 = img.data[0].b64_json

        with open(filepath, "wb") as f:
            f.write(base64.b64decode(b64))

        paths.append(filepath)

    return paths


def download_image(url, filepath):
    img_data = requests.get(url).content
    with open(filepath, "wb") as f:
        f.write(img_data)


def showImage(ind):
    global imagePreview

    if not image_paths:
        return

    img = Image.open(image_paths[ind])
    img = img.resize((200, 200), Image.Resampling.LANCZOS)
    imagePreview = ImageTk.PhotoImage(img)
    main_image.configure(image=imagePreview)


def nextImg(event=None):
    global cIndex
    if not image_paths:
        return
    cIndex = (cIndex + 1) % len(image_paths)
    showImage(cIndex)


def prevImg(event=None):
    global cIndex
    if not image_paths:
        return
    cIndex = (cIndex - 1) % len(image_paths)
    showImage(cIndex)


root = tk.Tk()

screen_width_middle = int(root.winfo_screenwidth() / 2 - 600 / 2)
screen_height_middle = int(root.winfo_screenheight() / 2 - 540 / 2)


root.geometry(f"600x610+{screen_width_middle}+{screen_height_middle}")
root.title("Image Generator")
root.configure(bg=BG)
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="AI Image Generator",
    bg=BG,
    fg=TXT,
    font=("Segoe UI", 26),
)
title_label.pack(pady=20)

radio_button_style = ttk.Style()
radio_button_style.configure(
    "TRadiobutton",
    font=("Rubik Mono One", 13),
    background=BG,
    foreground=TXT
)

radio_frame = ttk.Frame(root)
radio_frame.pack(pady=20)

rb = StringVar(value="Choice1")
rad1 = ttk.Radiobutton(
    radio_frame,
    text="Short [1 variant]",
    value="Choice1",
    variable=rb,
    style="TRadiobutton"
)
rad1.pack(padx=10)

rad2 = ttk.Radiobutton(
    radio_frame,
    text="Extended [2 Variants]",
    value="Choice3",
    variable=rb,
    style="TRadiobutton"
)
rad2.pack(padx=10)

image_frame = tk.Frame(root, bg=BG)
image_frame.pack(pady=30)

main_image = tk.Label(image_frame, bg=BG)
main_image.pack()

main_entry = ttk.Entry(root, font=("Arial", 15), width=30)
main_entry.pack(pady=20)

buttons_frame = ttk.Frame(root)
buttons_frame.pack(pady=10)

button_style = ttk.Style()
button_style.configure(
    "TButton",
    font=("Rubik Mono One", 10),
    background=BTN_BG,
    foreground=TXT
)

preview_button = ttk.Button(buttons_frame, text="Preview", style="TButton")
preview_button.pack(padx=10, side=LEFT)

generate_button = ttk.Button(
    buttons_frame,
    text="Generate",
    style="TButton",
    command=process
)
generate_button.pack(padx=10, side=LEFT)

root.bind("<Left>", prevImg)
root.bind("<Right>", nextImg)


root.mainloop()
