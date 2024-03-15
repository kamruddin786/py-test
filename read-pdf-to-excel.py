import pandas as pd
import tabula

# Path to the PDF file
pdf_file = "Purchaser_details Final.pdf"

# Read the PDF into a DataFrame
df = tabula.read_pdf(pdf_file, pages="all")

# Path to the Excel file where you want to write the data
excel_file = "Purchaser_details Final.xlsx"

# Write the DataFrame to an Excel file
with pd.ExcelWriter(excel_file) as writer:
    df.to_excel(writer, index=False)