from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from services.forms import (EditProfileForm)
from django.contrib import messages
import csv
from services.s3_upload import upload
import importlib
import os

from django.conf import settings


# Create your views here.
def dashboard(request):
    return render(request, 'services/dashboard.html')

def calc(request):
    return render(request, 'services/calculator.html')


def profile(request):
    args = {'user': request.user}
    return render(request, 'services/profile.html', args)


def portfolio(request):
    return render(request, 'services/portfolio.html')


def taxauto(request):
    if request.method == 'POST' and request.FILES.get('my_file'):
        myfile = request.FILES.get('my_file')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        source_file = f"media/{filename}"
        bucket_name = "textract-console-us-east-1-6375b349-b720-4339-99ab-c4a951ea5a70"
        object_key = "test.pdf"
        upload(source_file, bucket_name, object_key)
        urlf = f"s3://{bucket_name}/{object_key}"
        command_analysis = f"python services/textractor.py --documents {urlf} --tables"
        os.system(command_analysis)
        os.system('python F16_data_extractor/F_16_extractor/pipeline.py media/{} textract-console-us-east-1-6375b349-b720-4339-99ab-c4a951ea5a70 test.pdf'.format(filename))

        filename1 = 'media/test-pdf-page-1-tables.csv'
        # initializing the titles and rows list for page 1
        fields = []
        rows = []

        # reading csv file
        with open(filename1, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

            # get total number of rows
            #print("Total no. of rows: %d" % (csvreader.line_num))

        total_gross_salary = rows[7][2]
        gross_total_income_r = rows[23][2]
        gross_total_income_l = gross_total_income_r.split(" ")
        #print(gross_total_income_l)
        gross_total_income = gross_total_income_l[-2]
        gross_total_income = 'Rs. '+gross_total_income
        #print(total_gross_salary + " " + gross_total_income)

        filename2 = 'media/test-pdf-page-2-tables.csv'
        # initializing the titles and rows list for page 2
        fields = []
        rows = []

        # reading csv file
        with open(filename2, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

            # get total number of rows
            #print("Total no. of rows: %d" % (csvreader.line_num))

        deductable_amount = rows[19][2]
        income_after_deduction = rows[21][2]
        final_payable_tax_amt = rows[29][2]
        #print(deductable_amount + " " + income_after_deduction + " " + final_payable_tax_amt)

        class tax_disp:
            def __init__(self, total_gross_salary, gross_total_income, deductable_amount, income_after_deduction,
                         final_payable_tax_amt):
                self.total_gross_salary = total_gross_salary
                self.gross_total_income = gross_total_income
                self.deductable_amount = deductable_amount
                self.income_after_deduction = income_after_deduction
                self.final_payable_tax_amt = final_payable_tax_amt

        p1 = tax_disp(total_gross_salary, gross_total_income, deductable_amount, income_after_deduction,
                      final_payable_tax_amt)
        print(p1.total_gross_salary)
        print(p1.gross_total_income)
        print(p1.deductable_amount)
        print(p1.income_after_deduction)
        print(p1.final_payable_tax_amt)
        return render(request, 'services/taxauto.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'services/taxauto.html')

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/service/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'services/edit_profile.html', args)
