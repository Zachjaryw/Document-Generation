class Template:
    '''
    This class desingates a Template object
    '''

    def __init__(self):
        '''
        initialize the Template object
        '''
        self.template = {"Type":[],"Text":[],"Font Size":[],"Color":[],"Style":[],"Bold":[],"Italics":[],"Underline":[]}

    def add_line(self,type:str = 'Text',text:str=None,fontsize:int=None,color:list=[0,0,0],style=None,bold:bool = False,italics:bool = False,underline:bool = False):
        '''
        This method adds a new line to the given template object
        '''
        self.template['Type'].append(type)
        self.template['Text'].append(text)
        self.template['Font Size'].append(fontsize)
        self.template['Color'].append(color)
        self.template['Style'].append(style)
        self.template['Bold'].append(bold)
        self.template['Italics'].append(italics)
        self.template['Underline'].append(underline)
    
    def combine_templates(self,other:object):
        '''
        This method takes in another template object and combines the information into the self template
        @param object (Template) - a template object that will be added to the self template 
        '''
        other = other.get_template()
        self.template['Type'] = list(self.template['Type']) + list(other['Type'])
        self.template['Text'] = list(self.template['Text']) + list(other['Text'])
        self.template['Font Size'] = list(self.template['Font Size']) + list(other['Font Size'])
        self.template['Color'] = list(self.template['Color']) + list(other['Color'])
        self.template['Style'] = list(self.template['Style']) + list(other['Style'])
        self.template['Bold'] = list(self.template['Bold']) + list(other['Bold'])
        self.template['Italics'] = list(self.template['Italics']) + list(other['Italics'])
        self.template['Underline'] = list(self.template['Underline']) + list(other['Underline'])

    def get_template(self):
        '''
        This method returns the template as a dictionary
        @return self.template (dict) - template dict
        '''
        return self.template
