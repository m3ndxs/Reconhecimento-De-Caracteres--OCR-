import pytesseract
import pdf2image
from pdf2image import convert_from_path
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def recognize_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='por')

        return text

    except Exception as e:
        return f"Erro ao carregar a Imagem: {e}"


def recognize_text_from_pdf(pdf_path):
    try:
        pdf2image.pdfinfo_from_path(
            pdf_path, poppler_path=r"C:\Program Files\poppler\Library\bin")

        pages = convert_from_path(
            pdf_path, poppler_path=r"C:\Program Files\poppler\Library\bin")
        extracted_text = ""

        for page in pages:
            text = pytesseract.image_to_string(page, lang='por')
            extracted_text += text + "\n"

        return extracted_text

    except Exception as e:
        return f"Erro ao carregar o PDF: {e}"
