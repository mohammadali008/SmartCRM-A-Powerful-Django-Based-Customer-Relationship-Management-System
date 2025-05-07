from unittest import result
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO,StringIO,TextIOWrapper



# Define PDFConvertor
def pdf_convertor(template_source,context_dict = {}):
    response = HttpResponse(content_type='application/pdf')
    template = get_template(template_source)
    html = template.render(context_dict)

    # result = BytesIO()
    pdf = pisa.CreatePDF(html,dest = response)

    if pdf.err:
        return HttpResponse("Invalid PDF", status_code=400, content_type='text/plain')
    print(type(pdf))

    response['content-Disposition'] =\
    'atta'
    return response

#### Test1
# def makepdf(html):
#     """Generate a PDF file from a string of HTML."""
#     htmldoc = HTML(string=html, base_url="")
#     return htmldoc.write_pdf()

#### test2

# def index(request):
#     pdfmaker = PDFMaker()
#     res = pdfmaker.get_pdf_from_html(path='https://google.com', filename='output', write=True)
#     return HttpResponse()




