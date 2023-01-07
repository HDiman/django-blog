#!chapter_002/src/snippet_004.py
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import PageLayout
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF


def main():
    # create Document
    doc = Document()

    # create Page
    page= Page()

    # add Page to Document
    doc.add_page(page)

    # set a PageLayout
    layout = SingleColumnLayout(page)

    # add a Paragraph
    layout.add(Paragraph("Hello World!"))


    # store
    with open("output.pdf", "wb") as pdf_file_handle:
        PDF.dumps(pdf_file_handle, doc)


if __name__ == "__main__":
    main()
