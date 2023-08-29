if __name__ == '__main__':
    from Document_Generate import Generate
    from Document_Setup_Data import FilePath
    import argparse
    from Document_Input_Exception import InvalidReport
    report_types_list = ["All","AFI"]
    parser = argparse.ArgumentParser(
                    prog='Document Generator',
                    description='This program generates a report based on given data')
    parser.add_argument('-r','--report_type',type=str,required=True)
    args = parser.parse_args().__dict__
    report_type = args['report_type']
    
    try:
        if report_type in report_types_list:
            document = Generate.generate_document(report_type)
            document.save(FilePath.document_filepath)
        else:
            raise InvalidReport
    except InvalidReport:
        print("Exception occured: Invalid Report Type")