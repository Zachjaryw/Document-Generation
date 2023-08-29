from Document_Setup_Data import Setup_Data,FilePath
from Document_Template import Template

class Setup_Template:

    def document_template(report_type):
        '''
        This method creates the document template that will be run to create the full document
        @return list - this is a list of dictionaries that contain template information for the given template
        '''
        doc_template = Document.doc()
        return [doc_template]


    def create_template_from_elements(report_type):
        '''
        This method takes each of the dictionaries from the template and combines them into one large template
        @return tempalte (dict) - a dictionary with the created template
        '''
        template = Template()
        for next_template in Setup_Template.document_template(report_type):
            template.combine_templates(next_template)
        return template.get_template()
    
    def page_break():
        '''
        this method returns the template for a page break
        @return template (dict) - a dictionary for the template that will be run
        '''
        template = Template()
        template.add_line(type='Page Break')
        return template


class Document:
    
    def doc():
        template = Template()
        template.add_line("Text","Hello World",12)
        return template