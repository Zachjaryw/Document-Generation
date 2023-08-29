from Document_Setup_Data import FilePath
from Document_Setup_Template import Setup_Template
from Document_Run_From_Template import Run_From_Template
from docx import Document

class Generate:

    def setup_document(filepath:str = None):
        '''
        This method sets up a blank document or a document from a given filepath
        @param filepath (str) - the filepath to a pre made document to add to (default - None)
        @return document (Document) - a python-docx document object
        '''
        if filepath == None:
            document = Document()
        else:
            document = Document(filepath)
        return document

    def generate_document(report_type):
        '''
        This method generates the document based on the given template and data
        @return document (Document) - a python-docs document object
        '''
        document = Generate.setup_document()
        template = Setup_Template.create_template_from_elements(report_type)
        document = Run_From_Template.Create_Elements(document,template)
        return document