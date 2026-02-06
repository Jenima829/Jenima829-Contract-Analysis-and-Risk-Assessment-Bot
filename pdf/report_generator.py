from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def export_pdf(summary, risks, alternatives):
    file_path = "Legal_Report.pdf"

    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    content = []

    # ====================================================
    # 📌 TITLE
    # ====================================================
    content.append(Paragraph("<b>Legal Contract Risk Report</b>", styles["Title"]))
    content.append(Spacer(1, 0.3 * inch))

    # ====================================================
    # 🧾 SUMMARY
    # ====================================================
    content.append(Paragraph("<b>Summary</b>", styles["Heading2"]))
    content.append(Paragraph(summary.replace("\n", "<br/>"), styles["Normal"]))
    content.append(Spacer(1, 0.3 * inch))

    # ====================================================
    # ⚠ RISK DETAILS
    # ====================================================
    content.append(Paragraph("<b>Identified Risks</b>", styles["Heading2"]))
    content.append(Spacer(1, 0.2 * inch))

    if not risks:
        content.append(Paragraph("No risks detected.", styles["Normal"]))
    else:
        for r in risks:
            content.append(
                Paragraph(
                    f"<b>Risk Level:</b> {r['Risk']}<br/>"
                    f"<b>Clause:</b> {r['Clause']}<br/>"
                    f"<b>Reason:</b> {r['Reason']}",
                    styles["Normal"]
                )
            )
            content.append(Spacer(1, 0.2 * inch))

    # ====================================================
    # 📄 BUILD PDF
    # ====================================================
    doc.build(content)

    return file_path
