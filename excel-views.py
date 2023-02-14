import pandas as pd
from django.shortcuts import render, redirect

def upload_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']

        # read the data from the Excel file
        df = pd.read_excel(excel_file)

        return render(request, 'myapp/success.html', {'data': df.to_dict('records')})

    return render(request, 'myapp/upload_excel.html')
