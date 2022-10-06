import pdfplumber

def ler_pdf():
    with pdfplumber.open('') as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        return text


if __name__ == '__main__':
