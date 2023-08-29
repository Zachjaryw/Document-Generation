from Document_Elements import Elements

class Run_From_Template:

    def Create_Elements(document,template):
        for row in range(len(template['Type'])):
            dictrow = {"Type":template['Type'][row],"Text":template['Text'][row],"Font Size":template['Font Size'][row],"Color":template['Color'][row],"Style":template['Style'][row],"Bold":template['Bold'][row],"Italics":template['Italics'][row],"Underline":template['Underline'][row]}
            if dictrow['Type'] == "Text":
                document = Elements.text(document,dictrow['Text'],dictrow['Font Size'],dictrow['Color'],dictrow['Bold'],dictrow['Italics'],dictrow['Underline'])
            elif dictrow['Type'] == "Table":
                document = Elements.table(document,dictrow['Text'],dictrow['Font Size'],dictrow['Color'],dictrow['Bold'])
            elif dictrow['Type'] == "Image":
                document = Elements.image(document,dictrow['Text']) #text is the filepath
            elif dictrow['Type'] == "Page Break":
                document.add_page_break()
        return document