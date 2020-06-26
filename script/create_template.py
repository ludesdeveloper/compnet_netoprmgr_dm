import xlsxwriter

def create_data_template():
    hostname = ['IDCR1','IDSW1','IDN3K1','IDASA1','IDWLC1',]
    ip_address = ['192.168.1.1','192.168.1.2','192.168.1.3','192.168.1.4','192.168.1.5',]
    username = ['Admin','Admin','Admin','Admin','Admin',]
    password = ['P@s4word','P@s4word','P@s4word','P@s4word','P@s4word',]
    secret = ['P@s4word','P@s4word','P@s4word','P@s4word','P@s4word',]

    wb = xlsxwriter.Workbook('template.xlsx')
    ws = wb.add_worksheet('Sheet1')

    ws.write(0,0,'hostname')
    ws.write(0,1,'ip_address')
    ws.write(0,2,'username')
    ws.write(0,3,'password')
    ws.write(0,4,'secret')

    count_row=1
    for i in hostname:
        ws.write(count_row,0,i)
        count_row+=1

    count_row=1
    for i in ip_address:
        ws.write(count_row,1,i)
        count_row+=1

    count_row=1
    for i in username:
        ws.write(count_row,2,i)
        count_row+=1

    count_row=1
    for i in password:
        ws.write(count_row,3,i)
        count_row+=1

    count_row=1
    for i in secret:
        ws.write(count_row,4,i)
        count_row+=1

    wb.close()