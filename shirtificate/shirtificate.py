from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")
        self.ln(20)

def main():
    name = input("Enter your name: ")
    create_shirtificate(name)

def create_shirtificate(name):
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add the header
    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")
    pdf.ln(20)

    # Add the shirt image
    pdf.image("shirtificate.png", x=pdf.w / 2 - 75, y=60, w=150)

    # Add the name on top of the shirt
    pdf.set_xy(0, 120)
    pdf.set_font("Arial", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, name, 0, 1, "C")

    # Save the PDF to a file
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
