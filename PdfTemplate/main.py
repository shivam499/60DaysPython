from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # ln =1 means next string start with next line, 0 means overlap
    # border = 1 or any value create the border over the cell
    # align means how text aligned to the pdf
    # w is the width of the text takes place, 0 means full width, any value lessen the width
    # h is the height of the cell, it should be the same as font size we are using.
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
    # pdf.line(10, 21, 200, 21)

    pdf.ln(265)
    # set footer
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        pdf.ln(277)
        # set footer
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
