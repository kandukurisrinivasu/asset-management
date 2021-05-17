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
import datetime
from datetime import date
from io import BytesIO
import xlsxwriter ## This module is to wrinting files in the excel
import openpyxl # Python library to read and write an excel file.
import calendar


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

    ''' context = super().get_context_data(**kwargs)
    d = get_date(self.request.GET.get('month', None))
    cal = Calendar(d.year, d.month)
    html_cal = cal.formatmonth(withyear=True)
    context['calendar'] = mark_safe(html_cal)
    context['prev_month'] = prev_month(d)
    context['next_month'] = next_month(d)
    return context'''

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
    print("test create event \n\n\n\n")
    form = LabEventForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.method)
        event =Lab_event(
            user=request.user,
            Title=request.POST['title'],
            Description=request.POST['description'],
            Start_date=request.POST['start_date'],
            End_date=request.POST['end_date'],
            Start_time=request.POST['start_time'],
            End_time=request.POST['end_time']
        )
        event.save()
        messages.success(request, ('New Record Added Successfully...'))

        print("test create event ifififififififififi \n\n\n\n")
        Title = request.POST['title']
        Description = request.POST['description']
        Start_date = request.POST['start_date']
        End_date = request.POST['end_date']
        Start_time = request.POST['start_time']
        End_time = request.POST['end_time']
        # calendar_test(request)
        return render(request, "accounts/calendar.html", {})
    else:
        print("else part")

    return render(request, 'accounts/event.html', {'form': form})


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
        AssetNo = request.POST['AssetNo']
        Owner = request.POST['Owner']
        AssetTypeModel = request.POST['AssetTypeModel']
        Group = request.POST['Group']
        TeamName = request.POST['TeamName']
        ProductLine = request.POST['ProductLine']
        Remark = request.POST['Remark']
        # store the data in session
        request.session['AssetNo'] = request.POST['AssetNo']
        request.session['Owner'] = request.POST['Owner']
        request.session['AssetTypeModel'] = request.POST['AssetTypeModel']
        request.session['Group'] = request.POST['Group']
        request.session['TeamName'] = request.POST['TeamName']
        request.session['ProductLine'] = request.POST['ProductLine']
        request.session['Remark'] = request.POST['Remark']

        all_records=Asset_details.objects.filter(Q(Owner__contains=Owner) &
		                                             Q(AssetNo__contains=AssetNo) &
													 Q(Group__contains=Group) &
													 Q(TeamName__contains=TeamName) &
													 Q(AssetTypeModel__contains=AssetTypeModel) &
													 Q(ProductLine__contains=ProductLine)&
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
    all = Asset_details.objects.all()
    return render(request,'accounts/asset_search_display.html',{'all':all})


def add_asset(request):
    values={'form':AssetDetailsForm}
    form=AssetDetailsForm(request.POST)
    if form.is_valid():
        register=Asset_details(AssetNo = form.cleaned_data['AssetNo'],
                          Owner = form.cleaned_data['Owner'],
                          AssetTypeModel = form.cleaned_data['AssetTypeModel'],
                          Group = form.cleaned_data['Group'],
                          TeamName = form.cleaned_data['TeamName'],
                          ProductLine = form.cleaned_data['ProductLine'],
                          Remark = form.cleaned_data['Remark']
						  )
        register.save()
        messages.success(request, 'New record added sucessfully.....')
    return render(request,'accounts/add_asset.html',values)


def WriteToExcel(request, weather_data, town=None):
    AssetNo = request.session['AssetNo']
    Owner = request.session['Owner']
    AssetTypeModel = request.session['AssetTypeModel']
    Group = request.session['Group']
    TeamName = request.session['TeamName']
    ProductLine = request.session['ProductLine']
    Remark = request.session['Remark']
    all_data1 = Asset_details.objects.filter(Q(Owner__contains=Owner) &
                                                  Q(AssetNo__contains=AssetNo) &
                                                  Q(Group__contains=Group) &
                                                  Q(TeamName__contains=TeamName) &
                                                  Q(AssetTypeModel__contains=AssetTypeModel) &
                                                  Q(ProductLine__contains=ProductLine) &
                                                  Q(Remark__contains=Remark)
                                                  )
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)

    # Here we will adding the code to add data
    worksheet = workbook.add_worksheet()
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    worksheet.write(row, col, "AssetNo")
    worksheet.write(row, col + 1, "Owner")
    worksheet.write(row, col + 2, "AssetTypeModel")
    worksheet.write(row, col + 3, "Group")
    worksheet.write(row, col + 4, "TeamName")
    worksheet.write(row, col + 5, "ProductLine")
    worksheet.write(row, col + 6, "Remark")

    row = 1

    for data in all_data1:
        # print(data.AssetNo)
        worksheet.write(row, col, data.AssetNo)
        worksheet.write(row, col + 1, data.Owner)
        worksheet.write(row, col + 2, data.AssetTypeModel)
        worksheet.write(row, col + 3, data.Group)
        worksheet.write(row, col + 4, data.TeamName)
        worksheet.write(row, col + 5, data.ProductLine)
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
    return response


def export_pdf(request):
    AssetNo = request.session['AssetNo']
    Owner = request.session['Owner']
    AssetTypeModel = request.session['AssetTypeModel']
    Group = request.session['Group']
    TeamName = request.session['TeamName']
    ProductLine = request.session['ProductLine']
    Remark = request.session['Remark']
    all_data =Asset_details.objects.filter(Q(Owner__contains=Owner) &
                                                 Q(AssetNo__contains=AssetNo) &
                                                 Q(Group__contains=Group) &
                                                 Q(TeamName__contains=TeamName) &
                                                 Q(AssetTypeModel__contains=AssetTypeModel) &
                                                 Q(ProductLine__contains=ProductLine) &
                                                 Q(Remark__contains=Remark)
                                                 )

    report_name = AssetNo + "_" + Owner + "_" + AssetTypeModel + "_" + Group + "_" + TeamName + "_" + ProductLine

    data = {
        "report": report_name, "date": datetime.datetime.now(), "all": all_data,
    }
    pdf = render_to_pdf('accounts/pdf.html', data)
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
        if ("AssetNo" != data[0]):
            messages.success(request, ('AssetNo not macthed with data base field'))
            data_valid = 1
        if ("Owner" != data[1]):
            messages.success(request, ('Owner not macthed with data base field'))
            data_valid = 1
        if ("AssetTypeModel" != data[2]):
            messages.success(request, ('AssetTypeModel not macthed with data base field'))
            data_valid = 1
        if ("Group" != data[3]):
            messages.success(request, ('Group not macthed with data base field'))
            data_valid = 1
        if ("TeamName" != data[4]):
            messages.success(request, ('TeamName not macthed with data base field'))
            data_valid = 1
        if ("ProductLine" != data[5]):
            messages.success(request, ('ProductLine not macthed with data base field'))
            data_valid = all_data1 = Asset_details.objects.filter(Q(Owner__contains=Owner) &
                                                                       Q(AssetNo__contains=AssetNo) &
                                                                       Q(Group__contains=Group) &
                                                                       Q(TeamName__contains=TeamName) &
                                                                       Q(AssetTypeModel__contains=AssetTypeModel) &
                                                                       Q(ProductLine__contains=ProductLine) &
                                                                       Q(Remark__contains=Remark)
                                                                       )

        if (data_valid == 0):
            for data in excel_data[1:]:
                register =Asset_details(AssetNo=data[0],
                                              Owner=data[1],
                                              AssetTypeModel=data[2],
                                              Group=data[3],
                                              TeamName=data[4],
                                              ProductLine=data[5],
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
def index(request):
    return render(request, "index.html")



@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


def settings(request):
    return render(request,'includes/settings.html')

def setup(request):
    values = {"form":setupDetailsForm}
    form = setupDetailsForm(request.POST)
    if form.is_valid():
        register = Setup_details(Host_name=form.cleaned_data['Host_name'],
                                 FQDN=form.cleaned_data['FQDN'],
                                 OS=form.cleaned_data['OS'],
                                 COM_port_details=form.cleaned_data['COM_port_details'],
                                 Other_details=form.cleaned_data['Other_details'],
                                 )
        register.save()
    messages.success(request, 'Setup details added succesfully.....')
    return render(request, 'accounts/setup.html', values)

def setup_display(request):
    setups =Setup_details.objects.all()
    return render(request, 'accounts/table1.html', {'setups':setups})


