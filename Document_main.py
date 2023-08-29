if __name__ == '__main__':
    from Document_Generate import Generate
    from Document_Setup_Data import FilePath
    document = Generate.generate_document()
    document.save(FilePath.document_filepath)