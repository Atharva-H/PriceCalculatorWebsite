from fpdf import FPDF

OurAdd = """
98, Santosh Nagar, Indore Road, Khandwa(M.P.) - 450001, India
Phone: +91-733-2243160: Email: paricott.com
GSTIN: 23AACCP0175G1ZT"""


def topdf(
    No_quote,
    Date,
    CompName,
    CompAdd,
    BuyerName,
    BuyerDet,
    productName,
    NoPacketinConatiner,
    Rate,
    Amount,
    NoBoxinConatiner,
    BoxSize,
    CBMperBox,
    CBMper40HQ,
    DecSub,
    TopDia,
    BottomDia,
    Height,
    TandC,
    Item2=False,
    Item3=False,
):
    class PDF(FPDF):
        def header(self):
            self.ln(-1)
            self.image("calculator\\assets\\logo.png", 10, 8, 25)
            self.image(
                "calculator\\assets\\website.png",
                155,
                7,
                40,
                link="https://www.paricott.com",
            )
            self.set_font("helvetica", "B", 16)
            self.cell(35)
            self.cell(
                0,
                1,
                "Paricott India Papercup Pvt. Ltd.",
                ln=1,
            )
            self.set_font("helvetica", "", 8)
            self.cell(35)
            self.multi_cell(
                105,
                4,
                OurAdd,
            )
            self.set_font("helvetica", "B", 10)
            self.cell(
                20,
                4,
                "Quotation #",
            )
            self.cell(30, 4, "PIPPL/ " + No_quote)
            self.ln()
            self.set_font("helvetica", "B", 12)
            self.cell(35)
            self.cell(105, 3, "Quotation", align="C")
            self.set_font("helvetica", "B", 10)
            self.cell(20, 4, "Date :", align="R")
            self.cell(30, 4, Date)
            self.ln(6)
            self.l_margin = 8

        def Buyer(self, CompName, CompAdd, BuyerName, BuyerDet):
            self.set_font("helvetica", "B", 10)
            self.set_fill_color(100, 110, 255)
            self.set_text_color(255, 255, 255)
            self.cell(70, 5, "BUYER", fill=1, align="C")
            self.cell(50)
            self.cell(70, 5, "Kind Attn:", fill=1, align="C")
            self.ln()
            self.set_font("helvetica", "B", 12)
            self.set_text_color(0, 0, 0)
            self.cell(
                70,
                5,
                CompName,
            )
            self.cell(50)
            self.cell(
                70,
                5,
                BuyerName,
            )
            self.ln()
            self.set_font("helvetica", "", 10)
            self.multi_cell(70, 4, CompAdd)
            self.cell(40)
            self.ln(-4 * 3)
            self.cell(120)
            self.multi_cell(70, 4, BuyerDet)
            self.ln(1)

        def TableHeader(self):
            self.set_font("helvetica", "B", 10)
            self.set_text_color(255, 255, 255)
            self.set_fill_color(100, 110, 255)
            # self.set_draw_color(255,255,255)
            self.set_line_width(0.5)
            self.cell(13, 5, "S.No.", fill=1, border=1, align="C")
            self.cell(70, 5, "Description", fill=1, border=1, align="C")
            self.cell(36, 5, "Quantity", fill=1, border=1, align="C")
            self.cell(30, 5, "Rate", fill=1, border=1, align="C")
            self.cell(45, 5, "Amount", fill=1, border=1, align="C")
            self.ln()
            self.set_font("helvetica", "", 10)
            self.set_text_color(50, 50, 50)
            self.cell(13, 5, border=1)
            self.cell(70, 5, border=1)
            self.set_draw_color(10, 10, 10)
            self.cell(36, 5, "in one 40HQ", align="C", border=1)
            self.cell(30, 5, "FOB", align="C", border=1)
            self.cell(45, 5, "USD", align="C", border=1)
            self.ln()

        def ProductDet(
            self,
            sno,
            productName,
            NoPacketinConatiner,
            Rate,
            Amount,
            NoBoxinConatiner,
            BoxSize,
            CBMperBox,
            CBMper40HQ,
            TopDia,
            BottomDia,
            Height,
            DecSub,
        ):

            self.set_font("helvetica", "B", 12)
            self.cell(13, 6 * 8, str(sno), border=1, align="C")
            self.cell(70, 12, productName, border=1, align="C")
            self.cell(36, 6, NoPacketinConatiner, border=1, align="C")
            self.cell(30, 6, Rate, border=1, align="C")
            self.cell(45, 6, Amount, border=1, align="C")
            self.ln()
            self.cell(13, 6, "", align="C")
            self.cell(70, 6, "", align="C")
            self.cell(36, 6, "Packets", border=1, align="C")
            self.cell(30, 6, "per Packet", border=1, align="C")
            self.cell(45, 6, "", border=1, align="C")
            self.ln()
            self.set_font("helvetica", "", 10)
            self.cell(13, 6, "", align="C")
            self.multi_cell(70, 6, DecSub)
            self.ln(-6 * 6)
            self.cell(83, 6, "")
            self.set_text_color(255, 255, 255)
            self.set_fill_color(100, 110, 255)
            self.cell(36, 6, "Total Boxes", border=1, align="C", fill=1)
            self.cell(30, 6, "", border=1, align="C")
            self.set_font("helvetica", "B", 10)
            self.cell(45, 6, "Box Size", border=1, align="C", fill=1)
            self.ln()
            self.set_font("helvetica", "", 10)
            self.set_text_color(0, 0, 0)
            self.cell(13, 6, "", align="C")
            # self.cell(70,6,DecSub2)
            self.cell(70, 6, "")
            self.cell(36, 6, NoBoxinConatiner, border=1, align="C")
            self.cell(30, 6, "", border=1, align="C")
            self.cell(45, 6, BoxSize, border=1, align="C")
            self.ln()
            self.set_font("helvetica", "", 10)
            self.cell(13, 6, "", align="C")
            # self.cell(70,6,DecSub3)
            self.cell(70, 6, "")
            self.cell(36, 6, "", border=1, align="C")
            self.cell(30, 6, "", border=1, align="C")
            self.set_font("helvetica", "B", 10)
            self.set_text_color(255, 255, 255)
            self.set_fill_color(100, 110, 255)
            self.cell(45, 6, "CBM per Box", border=1, align="C", fill=1)
            self.ln()
            self.set_font("helvetica", "", 10)
            self.set_text_color(0, 0, 0)
            self.cell(13, 6, "", align="C")
            # self.cell(70,6,DecSub4)
            self.cell(70, 6, "")
            self.set_font("helvetica", "B", 10)
            self.set_text_color(255, 255, 255)
            self.set_fill_color(100, 110, 255)
            self.cell(66, 6, "Dimensions of Cup / Bowl", border=1, align="C", fill=1)
            self.set_font("helvetica", "", 10)
            self.set_text_color(0, 0, 0)
            self.cell(45, 6, CBMperBox, border=1, align="C")
            self.ln()
            self.set_font("helvetica", "", 10)
            self.cell(13, 6, "", align="C")
            # self.cell(70,6,DecSub5)
            self.cell(70, 6, "")
            self.cell(22, 6, "Top Dia", border=1, align="C")
            self.cell(22, 6, "Bottom Dia", border=1, align="C")
            self.cell(22, 6, "Height", border=1, align="C")
            self.set_font("helvetica", "B", 10)
            self.set_text_color(255, 255, 255)
            self.set_fill_color(100, 110, 255)
            self.cell(45, 6, "CBM per 40HQ", border=1, align="C", fill=1)
            self.ln()
            self.set_font("helvetica", "", 10)
            self.set_text_color(0, 0, 0)
            self.cell(13, 6, "", align="C")
            # self.cell(70,6,DecSub6)
            self.cell(70, 6, "")
            self.cell(22, 6, str(TopDia) + " mm", border=1, align="C")
            self.cell(22, 6, str(BottomDia) + " mm", border=1, align="C")
            self.cell(22, 6, str(Height) + " mm", border=1, align="C")
            self.cell(45, 6, CBMper40HQ, border=1, align="C")
            self.ln()
            self.cell(194, 3, "", border=1)
            self.ln()

        def footer(self):
            self.set_y(-71)
            self.set_font("helvetica", "B", 12)
            self.cell(95, 6, "Terms & Conditions", border=1, align="C", ln=1)
            self.set_font("helvetica", "", 10)
            self.multi_cell(95, 5, TandC)
            self.ln()

            self.set_font("helvetica", "B", 12)
            self.cell(95, 6, "Note: Bank Detail", border=1, align="C")
            self.cell(
                95,
                6,
                "For Paricott India Papercup ",
                align="C",
            )
            self.ln()
            self.set_font("helvetica", "", 10)
            self.cell(95, 5, "1. Account Name: Paricott India Papercup Pvt. Ltd.", ln=1)
            self.cell(95, 5, "2. Account No.: 09128970000094", ln=1)
            self.cell(95, 5, "3. Bank: Paricott India Papercup Pvt. Ltd.", ln=1)
            self.cell(95, 5, "4. Swift Code: HDFCINBBXXX", ln=1)
            self.cell(95, 5, "5. IFSC Code: HDFC0000912")
            self.cell(85, 5, "Director", align="R")
            self.image("calculator\\assets\\Seal.png", 140, 268, 23)

    pdf = PDF("P", "mm", "A4")

    pdf.add_page()

    pdf.Buyer(
        CompName=CompName, CompAdd=CompAdd, BuyerName=BuyerName, BuyerDet=BuyerDet
    )

    pdf.TableHeader()

    pdf.ProductDet(
        sno=1,
        productName=productName[0],
        NoPacketinConatiner=NoPacketinConatiner[0],
        Rate=Rate[0],
        Amount=Amount[0],
        NoBoxinConatiner=NoBoxinConatiner[0],
        BoxSize=BoxSize[0],
        CBMperBox=CBMperBox[0],
        CBMper40HQ=CBMper40HQ[0],
        TopDia=TopDia[0],
        BottomDia=BottomDia[0],
        Height=Height[0],
        DecSub=DecSub[0],
    )
    if Item2 != False:
        pdf.ProductDet(
            sno=2,
            productName=productName[1],
            NoPacketinConatiner=NoPacketinConatiner[1],
            Rate=Rate[1],
            Amount=Amount[1],
            NoBoxinConatiner=NoBoxinConatiner[1],
            BoxSize=BoxSize[1],
            CBMperBox=CBMperBox[1],
            CBMper40HQ=CBMper40HQ[1],
            TopDia=TopDia[1],
            BottomDia=BottomDia[1],
            Height=Height[1],
            DecSub=DecSub[1],
        )
    if Item3 != False:
        pdf.ProductDet(
            sno=3,
            productName=productName[2],
            NoPacketinConatiner=NoPacketinConatiner[2],
            Rate=Rate[2],
            Amount=Amount[2],
            NoBoxinConatiner=NoBoxinConatiner[2],
            BoxSize=BoxSize[2],
            CBMperBox=CBMperBox[2],
            CBMper40HQ=CBMper40HQ[2],
            TopDia=TopDia[2],
            BottomDia=BottomDia[2],
            Height=Height[2],
            DecSub=DecSub[2],
        )

    return pdf
