
# 📄 Doc Brief

**Doc Brief** is a simple yet powerful web application that summarizes academic and research PDFs using a state-of-the-art transformer model. Just upload a research paper, and Doc Brief will provide a concise summary of the content, helping you save time and grasp the core ideas quickly.

---

## 🚀 Features

* 📥 Upload any research paper in PDF format.
* 🧠 Uses `distilBART` summarization model from HuggingFace Transformers.
* ⚡ Fast and accurate summarization with just one click.
* 🌐 Web-based interface powered by Gradio.

---

## 🔧 How It Works

1. The user uploads a PDF file.
2. Text is extracted using `pdfminer`.
3. The text is summarized using the `sshleifer/distilbart-cnn-12-6` model.
4. The result is displayed in the browser.

---

## 🛠 Installation

Create a virtual environment and install the dependencies:

```bash
git clone https://github.com/Sharanya-krishnamurthi/DocBrief.git
cd DocBrief
pip install -r requirements.txt
```

---

## 📦 Requirements

Here’s what’s in `requirements.txt`:

```txt
torch
transformers
gradio
pdfminer.six
```

---

## 🖥️ Usage

To launch the app locally:

```bash
python app.py
```

Then open the Gradio interface in your browser to use the summarizer.

---

## 📚 Model Info

* 🤖 Model: `sshleifer/distilbart-cnn-12-6`
* Framework: HuggingFace Transformers
* Optimized for summarization of medium-length scientific texts.

---

## 🧑‍💻 Author

Built with ❤️ by \Sharanya

---

## DEMO
[HuggingFace Spaces](https://huggingface.co/spaces/sharanya/DocSummarizer)
