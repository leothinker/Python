import pdfplumber
import re

def remove_pagenum(texts):
    pattern = r'\n\d+$'
    match = re.search(pattern, texts)
    if match:
        texts = texts[:match.start()]
    return texts

pdf_file_path = "pdf_data/policy-full_tc.pdf"
output_file_path = "output_data/policy-full.txt"

page_break_indicator = "\n--page-break--\n"

with pdfplumber.open(pdf_file_path) as pdf, open(output_file_path, "w", encoding="utf-8") as text_file:
    for page in pdf.pages:
        text = page.extract_text()
        text = remove_pagenum(text).strip('\n')
        if text:
            text += page_break_indicator
            text_file.write(text)
