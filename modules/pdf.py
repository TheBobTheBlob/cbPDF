from fpdf import FPDF
from PIL import Image

image = Image.open("")

width, height = image.size

pdf = FPDF()
pdf.add_page(format=(width, height))
pdf.image(
    "",
    x=0,
    y=0,
    w=width,
    h=height,
)
pdf.output("")
