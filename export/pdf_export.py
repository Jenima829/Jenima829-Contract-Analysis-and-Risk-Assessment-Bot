from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def export_pdf(summary, risks, alternatives):

    filename = "Legal_Report.pdf"

    # Create PDF
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()
    content = []

    # ---- Title ---- #
    content.append(
        Paragraph("GenAI Legal Risk Report", styles["Title"])
    )
    content.append(Spacer(1, 12))

    # ---- Summary ---- #
    content.append(
        Paragraph("Plain Language Summary", styles["Heading2"])
    )
    content.append(
        Paragraph(summary, styles["BodyText"])
    )
    content.append(Spacer(1, 12))

    # ---- Risks ---- #
    content.append(
        Paragraph("Risk Analysis", styles["Heading2"])
    )

    for r in risks:

        text = f"""
        <b>{r['Risk']} Risk</b> — {r['Clause Type']}<br/>
        {r['Text']}<br/>
        <i>Reason:</i> {r['Reason']}
        """

        content.append(
            Paragraph(text, styles["BodyText"])
        )
        content.append(Spacer(1, 8))

    # ---- Alternatives ---- #
    content.append(
        Paragraph("Suggested Alternatives", styles["Heading2"])
    )

    for alt in alternatives:
        content.append(
            Paragraph(alt, styles["BodyText"])
        )
        content.append(Spacer(1, 8))

    # ---- Build PDF ---- #
    doc.build(content)

    return filename