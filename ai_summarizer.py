from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text):
    result = summarizer(
        text,
        max_length=50,
        min_length=15,
        do_sample=False
    )

    return result[0]["summary_text"]