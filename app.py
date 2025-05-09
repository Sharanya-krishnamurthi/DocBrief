import torch
import gradio as gr
from transformers import pipeline
from pdfminer.high_level import extract_text

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    torch_dtype=torch.float16 
)

def extract_text_from_pdf(pdf_path):
    """Extract text from uploaded PDF using pdfminer."""
    try:
        text = extract_text(pdf_path)
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {str(e)}"


def chunk_text(text, chunk_size=1024):
    """Break text into chunks suitable for summarization models."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def generate_summary(pdf_file):
    """Summarize the entire PDF document by handling long text properly."""
    text = extract_text_from_pdf(pdf_file.name)
    if "Error" in text:
        return text

    # Split text into chunks
    # chunks = chunk_text(text)

    # summaries = []
    # for chunk in chunks:
    #     summary = summarizer(chunk, max_length=300, min_length=100, do_sample=False)
    #     summaries.append(summary[0]["summary_text"])

    # # Combine all chunk summaries into a final summary
    # final_summary = "\n".join(summaries)
    # return final_summary
    return summarizer(text[:2000])[0]["summary_text"]


# Gradio App
gr.close_all()
demo = gr.Interface(
    fn=generate_summary,
    inputs=[gr.File(label="Upload PDF")],
    outputs=[gr.Textbox(label="Paper Summary", lines=10)],
    title="Research Paper Summarizer",
    description="Upload a research paper PDF to get a detailed summary.",
)

demo.launch()
