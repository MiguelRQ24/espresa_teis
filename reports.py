import datetime
from math import asinh

from PyQt6.QtGui import QFont
from PIL import Image
from reportlab.lib.utils import ImageReader

from conexion import *

from reportlab.pdfgen import canvas
class Reports:
    rootPath = ".\\reports"
    data = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    nameReportCli = data + "_reportcustomers.pdf"
    pdf_path = os.path.join(rootPath, nameReportCli)
    c = canvas.Canvas(pdf_path)

    @classmethod
    def topreport(cls):
        try:
            path_logo = os.path.join(os.path.dirname(__file__), "img", "logo.png")
            logo = Image.open(path_logo)
            if isinstance(logo, Image.Image):
                cls.c.setFont("Helvetica-Bold", 10)
                cls.c.drawString(55, 785, "EMPRESA TEIS")
                cls.c.drawCentredString(300, 675, "Report Customers")
                cls.c.line(35, 665, 550, 665)

                # dibuja el logo
                cls.c.drawImage(path_logo, 480, 745, width=40, height=40)

                # datos de la empresa
                cls.c.setFont("Helvetica", 9)
                cls.c.drawString(55, 755, "CIF: A55641214B")
                cls.c.drawString(55, 745, "28080 Vigo")
                cls.c.drawString(55, 735, "C/ A Picota, 12423")
                cls.c.drawString(55, 725, "Tel: 912345678")
                cls.c.drawString(55, 715, "Email: info@empresateis.com")

                # dibujar cuadrado en los datos de la empresa
                cls.c.line(50, 705, 50, 800)
                cls.c.line(50, 705, 180, 705)
                cls.c.line(180, 705, 180, 800)
                cls.c.line(180, 800, 50, 800)

        except Exception as e:
            print("Error en topreport", e)
    
    @classmethod
    def footer(cls):
        try:
            cls.c.line(50, 50, 525, 50)
            day = datetime.date.today()
            day = day.strftime("%d/%m/%Y %H:%M")
            cls.c.setFont('Helvetica', 7)
            cls.c.drawString(465, 40, day)
        except Exception as e:
            print(e)

    @classmethod
    def reportCustomers(cls) :
        try:
            
            records = Conexion.listCustomers(False)
            itmes = ["DNI_NIE", "SURNAME", "NAME", "MOBILE", "CITY", "INVOICE TYPE", "STATE" ]
            cls.topreport()
            cls.c.setFont("Helvetica-Bold", 10)
            cls.c.drawString(55, 650, itmes[0])
            cls.c.drawString(120, 650, itmes[1])
            cls.c.drawString(220, 650, itmes[2])
            cls.c.drawString(270, 650, itmes[3])
            cls.c.drawString(320, 650, itmes[4])
            cls.c.drawString(400, 650, itmes[5])
            cls.c.drawString(480, 650, itmes[6])
            cls.c.line(50, 695, 525, 695)
            cls.footer()
            x = 55
            y = 630
            for record in records:
                if y <= 90:
                    cls.topreport()
                    cls.c.setFont("Helvetica-Oblique", 8)
                    cls.c.drawString(450, 75, "Next page...")
                    cls.c.showPage() # Crea nueva pagina
                    cls.c.setFont("Helvetica-Bold", 10)
                    cls.c.drawString(55, 650, itmes[0])
                    cls.c.drawString(120, 650, itmes[1])
                    cls.c.drawString(220, 650, itmes[2])
                    cls.c.drawString(270, 650, itmes[3])
                    cls.c.drawString(320, 650, itmes[4])
                    cls.c.drawString(400, 650, itmes[5])
                    cls.c.drawString(480, 650, itmes[6])
                    cls.c.line(50, 695, 525, 695)
                    cls.footer()
                    x = 55
                    y = 630
                cls.c.setFont("Helvetica", 7)
                dni = '****' + record[0][4:7] + '**'
                cls.c.drawString(x, y, dni)
                cls.c.drawString(x + 65, y, record[2])
                cls.c.drawString(x + 165, y, record[3])
                cls.c.drawString(x + 215, y, record[5])
                cls.c.drawString(x + 265, y, record[8])
                cls.c.drawString(x + 345, y, record[9].capitalize())
                if record[10] == "True":
                    cls.c.drawString(x + 425, y, "Activo")
                else:
                    cls.c.drawString(x + 425, y, "Baja")
                y -= 15

            cls.c.save()
            for file in os.listdir(cls.rootPath):
                if file.endswith(cls.nameReportCli):
                    os.startfile(cls.pdf_path)
        except Exception as e:
            print("Error en reportCustomers", e)
            
            
    
