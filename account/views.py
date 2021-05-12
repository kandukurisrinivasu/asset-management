from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from django import template

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin # This is for authentication
from django.views import generic
from django.utils.safestring import mark_safe #Explicitly mark a string as safe for (HTML) output
# purposes. The returned object can be used everywhere a string or unicode object is appropriate
from .utils import render_to_pdf, Calendar
from django.db.models import Q
from .utils import *
from .forms import *
from .models import *
import calendar
import datetime
from datetime import date
from io import BytesIO
import xlsxwriter ## This module is to wrinting files in the excel
import openpyxl # Python library to read and write an excel file.


class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = 'signup'
    model = Lab_event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.date.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
def calendar_test(request):
    msg     = None
    success = False
    context =""
    #context = super().get_context_data(**kwargs)
    d = get_date(request.GET.get('month', None))
    cal = Calendar(d.year, d.month)
    #print(cal)
    html_cal = cal.formatmonth(withyear=True)
    context = mark_safe(html_cal)
    return render(request, "accounts/calendar.html", { "context" : context, "success" : success })

def create_lab_event(request):
    print("create the lab event")
    form=LabEventForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        event=Lab_event(
        user=request.user,
        Setup_name=request.POST['setup_name'],
        Title = request.POST['title'],
        Description = request.POST['description'],
        Start_date =request.POST['Start date'],
        End_date =request.POST['end date'],
        Start_time =request.POST['start time'],
        End_time =request.POST['End time'],
        created_date =request.POST['created date']
        )
        event.save()
        messages.success(request, 'New user record added successfully')
        print("test create lab event")
        Setup_name=request.POST['setup_name']
        Title=request.POST['title']
        Description=request.POST['description']
        Start_date=request.POST['Start date']
        End_date=request.POST['end date']
        Start_time=request.POST['start time']
        End_time=request.POST['End time']
        created_date=request.POST['created date']

        all_data = Lab_event.objects.filter(Q(Setup_name__contains=Setup_name) &
                                                   Q(Title__contains=Title) &
                                                   Q(Description__contains=Description) &
                                                   Q(Start_data__contains=Start_date) &
                                                   Q(End_date__contains=End_date) &
                                                   Q(Start_time__contains=Start_time) &
                                                   Q(End_time__contains=End_time) &
                                                   Q(created_date__contains=created_date)
                                                   )
        value={'all_date':all_data}

        return render(request,'accounts/calender.html',value)
    else:
        print("form is not valid")

    return render(request,'accounts/event.html')

class EventEdit(generic.UpdateView):
    model = Lab_event
    fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'event.html'

def lab_event_details(request,event_id):
    event=Lab_event.objects.get(id=event_id)
    event_member=EventMember.objects.get(event=event)
    value={
        'event':event,
        'event member':event_member
    }
    return render(request,'accounts/event_details.html',value)

def asset_search(request):
    submitted=False
    if request.method=='POST':
        print("home")
        if request.POST.get("export"):
            print("export")

        values={}
        Asset_no = request.POST['AssetNo']
        Owner = request.POST['Owner']
        Asset_type = request.POST['AssetType']
        Team_name=request.POST['TeamName']
        working_status=request.POST['working status']
        Group=request.POST['Group']
        Remark = request.POST['Remark']
        Product_line = request.POST['ProductLine']
        # storing the data in a session
        request.session['AssetNo'] = request.POST['AssetNo']
        request.session['Owner'] = request.POST['Owner']
        request.session['AssetType'] = request.POST['AssetType']
        request.session['TeamName'] = request.POST['TeamName']
        request.session['ProductLine'] = request.POST['ProductLine']
        request.session['Group'] = request.POST['Group']
        request.session['working status'] = request.POST['working status']
        request.session['Remark'] = request.POST['Remark']

        all_records=Asset_details.objects.filter(Q(Owner__contains=Owner) &
		                                             Q(Asset_no__contains=Asset_no) &
													 Q(Team_name__contains=Team_name) &
                                                     Q(Group__contains=Group) &
                                                     Q(working_status__contains=working_status) &
													 Q(Asset_type__contains=Asset_type) &
													 Q(Product_line__contains=Product_line)&
													 Q(Remark__contains=Remark)
													)
        values={'name':asset_search_display,'all':all_records}
        return render(request,'accounts/asset_search_display.html',values)
    else:
        data=Asset_details.objects.all()
        form=AssetDetailsForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'accounts/asset_search.html',{'form':form,'submitted':submitted,'data':data})

def asset_search_display(request):
    values={"form":AssetDetailsForm}
    form=AssetDetailsForm(request.POST)
    if form.is_valid():
        register=Asset_details(Asset_no = form.cleaned_data['AssetNo'],
                          Owner = form.cleaned_data['Owner'],
                          Asset_type = form.cleaned_data['AssetType'],
                          Product_line = form.cleaned_data['ProductLine'],
                          Remark = form.cleaned_data['Remark']
						  )
        data=Asset_details.objects.filter(AssetNo=register.AssetNo)
        values={"all_data":data}

    return render(request,'accounts/asset_search_display.html',values)

@login_required(login_url="/login/")
def add_asset(request):
    values={'form':AssetDetailsForm}
    form=AssetDetailsForm(request.POST)
    if form.is_valid():
        register=Asset_details(Asset_no = form.cleaned_data['AssetNo'],
                          Owner = form.cleaned_data['Owner'],
                          Asset_type = form.cleaned_data['AssetTypeModel'],
                          Group=form.cleaned_data['Group'],
                          Product_line = form.cleaned_data['ProductLine'],
                          Remark = form.cleaned_data['Remark'],
                          Team_name=form.cleaned_data['Team name']
						  )
        register.save()
        messages.success(request, 'New record added sucessfully.....')
    return render(request,'accounts/add_asset.html',values)


def WriteToExcel(request, weather_data, town=None): # This function is to load data in excel
    Asset_no = request.session['AssetNo']
    Owner = request.session['Owner']
    Asset_type = request.session['AssetTypeModel']
    Group = request.session['Group']
    Team_name = request.session['TeamName']
    Product_line = request.session['ProductLine']
    Remark = request.session['Remark']
    all_data=Asset_details.objects.filter(Q(Owner__contains=Owner) &
                                                  Q(Asset_no__contains=Asset_no) &
                                                  Q(Group__contains=Group) &
                                                  Q(Team_name__contains=Team_name) &
                                                  Q(Asset_type__contains=Asset_type) &
                                                  Q(Product_line__contains=Product_line) &
                                                  Q(Remark__contains=Remark)
                                                  )
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)

    # Here we will adding the code to add data
    worksheet = workbook.add_worksheet()
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    worksheet.write(row, col, "Asset_no")
    worksheet.write(row, col + 1, "Owner")
    worksheet.write(row, col + 2, "Asset_type")
    worksheet.write(row, col + 3, "Group")
    worksheet.write(row, col + 4, "Team_name")
    worksheet.write(row, col + 5, "Product_line")
    worksheet.write(row, col + 6, "Remark")

    row = 1

    for data in all_data:
        # print(data.AssetNo)
        worksheet.write(row, col, data.Asset_no)
        worksheet.write(row, col + 1, data.Owner)
        worksheet.write(row, col + 2, data.Asset_type)
        worksheet.write(row, col + 3, data.Group)
        worksheet.write(row, col + 4, data.Team_name)
        worksheet.write(row, col + 5, data.Product_line)
        worksheet.write(row, col + 6, data.Remark)
        row += 1
    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data

def export_xls(request):
    print("welocme to export xls_files")
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
    xlsx_data = WriteToExcel(request,"weather_period", "town")
    response.write(xlsx_data)
    return render(request,'')


def export_pdf(request):
    Owner = request.session['Owner']
    Asset_type = request.session['Asset_type']
    Group = request.session['Group']
    Team_name = request.session['Team_name']
    Product_line = request.session['Product_line']
    Remark = request.session['Remark']
    all_data = Asset_details.objects.filter(Q(Owner__contains=Owner) &
                                                 Q(Group__contains=Group) &
                                                 Q(Team_name__contains=Team_name) &
                                                 Q(Asset_type__contains=Asset_type) &
                                                 Q(Product_line__contains=Product_line) &
                                                 Q(Remark__contains=Remark)
                                                 )

    report_name = "_" + Owner + "_" + Asset_type + "_" + Group + "_" + Team_name + "_" + Product_line

    data = {
        "report": report_name, "date": datetime.datetime.now(), "all": all_data,
    }
    pdf = render_to_pdf('accounts/export_pdf.html', data)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Report.pdf'
    return response


def import_xls(request):
    print("upload xls")
    if "GET" == request.method:
        return render(request, 'accounts/import_excel.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        # you may put validations here to check extension or file size
        wb = openpyxl.load_workbook(excel_file)
        # getting all sheets
        sheets = wb.sheetnames
        # getting a particular sheet
        worksheet = wb["Sheet1"]
        # getting active sheet
        active_sheet = wb.active
        # reading a cell
        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))

            excel_data.append(row_data)
        data_valid = 0
        data = excel_data[0]
        if ("Asset_no" != data[0]):
            messages.success(request, ('AssetNo not macthed with data base field'))
            data_valid = 1
        if ("Owner" != data[1]):
            messages.success(request, ('Owner not macthed with data base field'))
            data_valid = 1
        if ("Asset_type" != data[2]):
            messages.success(request, ('AssetTypeModel not macthed with data base field'))
            data_valid = 1
        if ("Group" != data[3]):
            messages.success(request, ('Group not macthed with data base field'))
            data_valid = 1
        if ("Team_name" != data[4]):
            messages.success(request, ('TeamName not macthed with data base field'))
            data_valid = 1
        if ("Product_line" != data[5]):
            messages.success(request, ('ProductLine not macthed with data base field'))
            Asset_no = request.session['AssetNo']
            Owner = request.session['Owner']
            Asset_type = request.session['AssetTypeModel']
            Group = request.session['Group']
            Team_name = request.session['TeamName']
            Product_line = request.session['ProductLine']
            Remark = request.session['Remark']
            data_valid = all_data = Asset_details.objects.filter(Q(Owner__contains=Owner) &
                                                                       Q(Asset_no__contains=Asset_no) &
                                                                       Q(Group__contains=Group) &
                                                                       Q(Team_name__contains=Team_name) &
                                                                       Q(Asset_type__contains=Asset_type) &
                                                                       Q(Product_line__contains=Product_line) &
                                                                       Q(Remark__contains=Remark)
                                                                       )

        if (data_valid == 0):
            for data in excel_data[1:]:
                register = Asset_details(Asset_no=data[0],
                                              Owner=data[1],
                                              Asset_Type=data[2],
                                              Group=data[3],
                                              Team_name=data[4],
                                              Product_line=data[5],
                                              Remark=data[6]
                                              )
                register.save()
        else:
            excel_data = []
            messages.success(request, ('import failed '))

        return render(request, 'accounts/import_excel.html', {"excel_data": excel_data})

def feedback(request):
    return render(request, 'feedback.html')

def table(request):
    assets=Asset_details.objects.all()
    return render(request,'accounts/table.html',{'assets':assets})


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('chartjs.html')
        return HttpResponse(html_template.render(context, request))

