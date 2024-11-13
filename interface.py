import tkinter as tk
import textwrap
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document


def recognize_image():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur eleifend purus in turpis facilisis convallis. Curabitur nec consectetur felis. Aliquam.'

    display_result(text)


def save_text(text, file_format):
    wrapped_text = '\n'.join(textwrap.wrap(text, width=80))

    save_path = filedialog.asksaveasfilename(defaultextension=f".{file_format}", filetypes=[
        (f"{file_format.upper()} Files", f"*.{file_format}")])
    if not save_path:
        return
    try:
        if file_format == "txt":
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(text)
        elif file_format == "pdf":
            c = canvas.Canvas(save_path, pagesize=letter)
            lines = wrapped_text.split("\n")
            y = 750
            for line in lines:
                c.drawString(100, y, line)
                y -= 15
            c.save()
        elif file_format == "docx":
            doc = Document()
            for line in wrapped_text.split("\n"):
                doc.add_paragraph(line)
            doc.save(save_path)
        elif file_format == "html":
            with open(save_path, "w", encoding="utf-8") as file:
                file.write(f"<html><body><pre>{text}</pre></body></html>")
        messagebox.showinfo("Sucesso", f"Arquivo salvo em {
                            file_format.upper()} com sucesso!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save the file: {e}")


def display_result(text):
    result_window = tk.Toplevel(root)
    result_window.title('Texto Reconhecido')

    text_box = tk.Text(result_window, wrap=tk.WORD, height=15, width=50)
    text_box.insert(tk.END, text)
    text_box.pack(expand=True, fill=tk.BOTH)

    export_frame = tk.Frame(result_window)
    export_frame.pack(pady=10)

    btn_txt = tk.Button(export_frame, text="Salvar em .txt",
                        command=lambda: save_text(text, "txt"))
    btn_txt.grid(row=0, column=0, padx=10)

    btn_pdf = tk.Button(export_frame, text="Salvar em .pdf",
                        command=lambda: save_text(text, "pdf"))
    btn_pdf.grid(row=0, column=1, padx=10)

    btn_docx = tk.Button(export_frame, text="Salvar em .docx",
                         command=lambda: save_text(text, "docx"))
    btn_docx.grid(row=0, column=2, padx=10)

    btn_html = tk.Button(export_frame, text="Salvar em .html",
                         command=lambda: save_text(text, "html"))
    btn_html.grid(row=0, column=3, padx=10)


root = tk.Tk()
root.title('Reconhecimento de Caracteres OCR')

root.geometry('400x300')

button_frame = tk.Frame(root)
button_frame.pack(expand=True)

btn_image = tk.Button(button_frame, text='Imagem', command=recognize_image,
                      bg='skyblue', fg='white', font=('Arial', 12, 'bold'))
btn_image.grid(padx=20, pady=10)

btn_pdf = tk.Button(button_frame, text='PDF', command=recognize_image,
                    bg='lightgreen', fg='black', font=('Arial', 12, 'bold'))
btn_pdf.grid(padx=20, pady=10)

root.mainloop()
