from fpdf import FPDF
import glob
from pathlib import Path

files = glob.glob("files/*txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for file in files:
    with open(file,"r") as data:
        content = data.read()
    pdf.add_page()
    title = Path(file).stem
    pdf.set_font(family="Times", style="B", size=18)
    pdf.cell(w=0, h=10, txt=title.title(), ln=1)
    pdf.set_font(family="Times", style="", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output.pdf")
