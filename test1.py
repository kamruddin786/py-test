import tabula
import pandas as pd

# Path to your file
file = "Purchaser_details Final.pdf"

# Read the PDF as DataFrame
tables = tabula.read_pdf(file, pages='all', multiple_tables=True)

# Loop to save each table into separate CSV
for i, table in enumerate(tables, start=1):
    table.to_excel(f'purchase/Purchaser_details_{i}.xlsx', index=False)