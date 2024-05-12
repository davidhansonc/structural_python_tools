import os
import pandas as pd
from PyPDF2 import PdfWriter, PdfReader
import sys

def combine_pdfs(excel_file):
    try:
        df_path = pd.read_excel(excel_file, header=None)
        base_path = df_path.iat[2, 1].strip()
        output_pdf = df_path.iat[3, 1].strip()

        print(f"Base path: {base_path}")
        print(f"Output PDF path: {output_pdf}")

        df = pd.read_excel(excel_file, usecols=["Select Detail", "Detail ID"], header=4)
        writer = PdfWriter()
        valid_entries = False
        total_pages = 0

        for index, row in df.iterrows():
            if pd.notna(row['Select Detail']) and 'p' in row['Select Detail'].lower():
                pdf_filename = row['Detail ID'] + ".pdf"
                pdf_path = os.path.join(base_path, "PDF", "pdf details", pdf_filename)
                print(f"Checking PDF path: {pdf_path}")  # Debug print each path checked
                if os.path.exists(pdf_path):
                    valid_entries = True
                    pdf_reader = PdfReader(pdf_path)
                    for page in pdf_reader.pages:
                        writer.add_page(page)
                        total_pages += 1

        if valid_entries:
            with open(output_pdf, 'wb') as out:
                writer.write(out)
            print(f"Combined PDF created at {output_pdf}. Total pages combined: {total_pages}")
            os.startfile(output_pdf)  # Open the PDF with the default application
        else:
            print("No valid PDFs were found to combine. No combined PDF created.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <database_path>")
        sys.exit(1)

    excel_database_path = sys.argv[1]
    print(f"Excel database path: {excel_database_path}")
    combine_pdfs(excel_database_path)
