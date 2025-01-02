from fpdf import FPDF
import pandas as pd

# Making our document, turning off auto page break to manipulate margins & footers
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Opening our CSV file used to make desired PDF
df = pd.read_csv("topics.csv")

# Making our PDF Based off of the CSV data
for index, row in df.iterrows():
    pdf.add_page()

    # Setting the Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)
    
    # Setting the Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Adding required amount of pages per topic
    for i in range(row["Pages"] - 1):
        pdf.add_pages()

        # Setting the Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

# Finishing our PDF
pdf.output("output.pdf")