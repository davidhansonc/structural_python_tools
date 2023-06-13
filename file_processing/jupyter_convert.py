import os
import sys
import nbformat
from nbconvert import HTMLExporter
import pdfkit


def convert_notebook_to_html(notebook_path, html_path):
    with open(notebook_path) as nb_file:
        notebook = nbformat.read(nb_file, as_version=nbformat.NO_CONVERT)

    html_exporter = HTMLExporter()
    html_exporter.template_file = 'basic'  # You can choose a different template if desired

    (body, resources) = html_exporter.from_notebook_node(notebook)

    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(body)

    print(f"Successfully converted {notebook_path} to {html_path}")


def convert_html_to_pdf(html_path, pdf_path):
    try:
        pdfkit.from_file(html_path, pdf_path)
        print(f"Successfully converted {html_path} to {pdf_path}")
    except Exception as e:
        print(f"Conversion failed for {html_path}: {str(e)}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python convert_notebooks_to_pdf.py <folder_path>")
    else:
        folder_path = sys.argv[1]

        # Convert .ipynb files to .html files
        for filename in os.listdir(folder_path):
            if filename.endswith(".ipynb"):
                notebook_path = os.path.join(folder_path, filename)
                html_path = os.path.join(
                    folder_path, f"{os.path.splitext(filename)[0]}.html")
                convert_notebook_to_html(notebook_path, html_path)

        # Convert .html files to .pdf files
        for filename in os.listdir(folder_path):
            if filename.endswith(".html"):
                html_path = os.path.join(folder_path, filename)
                pdf_path = os.path.join(
                    folder_path, f"{os.path.splitext(filename)[0]}.pdf")
                convert_html_to_pdf(html_path, pdf_path)
