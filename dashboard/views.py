# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
import pandas as pd
import numpy as np
from .models import Records, Organisation_master, Student, Teacher,Class
import plotly.express as px
import dash
from dash import dcc, html
from django_plotly_dash import DjangoDash
import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from django.contrib.auth import get_user_model
from django.contrib import messages 


def upload_marks(request):
    if request.method == "POST":
        myfile = request.FILES.get('doc')
        df = pd.read_csv(myfile)
        df.rename(columns = {'Roll No':'No','Student Name':'Name'}, inplace = True)
        try:
            cols = ['IA', 'SEE']
            df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
            df.fillna(0,inplace = True)
            df.describe(include="all")
            df['Total'] = df['IA']+df['SEE']
            vv = df.Name.value_counts().loc[lambda x: x>35].reset_index()['index']
            df2 = df[df['Name'].isin(vv)]
            list1 = df2.values.tolist()
            print(list1)
            for i in list1:
                if Records.objects.filter(No=i[0],Name = i[1], Internal = i[2], External = i[3], Subject = i[4], Semester = i[5], Total = i[6] ).exists():
                    pass
                else:
                    h = Records(No=i[0],Name = i[1], Internal = i[2], External = i[3], Subject = i[4], Semester = i[5], Total = i[6])
                    h.save()
        except:
            messages.warning(request,'The required excel is not provided. Please resubmit the proper excel.')
            return redirect('dashboard:upload_marks')
    return render(request,'upload_marks.html')




def index(request):
    stu = Records.objects.order_by().values('Name').distinct().count()
    sub = Records.objects.order_by().values('Subject').distinct().count()
    all_data = Records.objects.order_by().values('Name').distinct()
    item = Records.objects.all().values('id','No','Name','Internal','External','Subject','Semester','Total')
    df = pd.DataFrame(item)
    a =  df["Internal"].mean()
    meani = round(a, 2)
    b = df['External'].mean()
    meanx = round(b, 2)
    return render(request,'front.html',{'Student':stu,'Subjects':sub,'all':all_data,'reA':meani, 'reB': meanx})





def students(request):
    stu = Records.objects.order_by().values('Name').distinct().count()
    sub = Records.objects.order_by().values('Subject').distinct().count()
    all_data = Records.objects.order_by().values('Name').distinct()
    all_dat = Records.objects.order_by().values().distinct()
    return render(request, 'student.html',{'Student':stu,'Subjects':sub,'all':all_data})



def stud_plot(request, pk):
    print(pk)
    item = Records.objects.all().values('id','No','Name','Internal','External','Subject','Semester','Total').filter(Name = pk)
    z = pd.DataFrame(item)
    print(z.head())
    a =  z["Internal"].mean()
    meani = round(a, 2)
    b = z['External'].mean()
    meanx = round(b, 2)
    fig_graph = px.bar(z, x = "Semester", y = "Total", color = "Internal", text = "Subject",  title="Marks scored with respect to Internal marks",hover_data=['Subject', 'External'])
    fig_graph1 = px.bar(z, x = "Semester", y = "Total", color = "External", text = "Subject",title="Marks scored with respect to External marks",hover_data=['Subject', 'External','Internal'])
    fig1=fig_graph.to_html(full_html=True,config={'displayModeBar':False})
    fig2=fig_graph1.to_html(full_html=True,config={'displayModeBar':False})
    return render(request,'plot.html',{'bar':fig1,'int':meani,'ext':meanx,'bar1':fig2})



def only_stud(request):
    us = 'GAIKWAD SHUBHANGI MANSINGH SHEETAL'
    item = Records.objects.all().values('id','No','Name','Internal','External','Subject','Semester','Total').filter(Name = us)
    z = pd.DataFrame(item)
    print(z.head())
    a =  z["Internal"].mean()
    meani = round(a, 2)
    b = z['External'].mean()
    meanx = round(b, 2)
    fig_graph = px.bar(z, x = "Semester", y = "Total", color = "Internal", text = "Subject", title="Marks scored with respect to Internal marks",hover_data=['Subject', 'External'])
    fig_graph1 = px.bar(z, x = "Semester", y = "Total", color = "External", text = "Subject", title="Marks scored with respect to External marks",hover_data=['Subject', 'External','Internal'])
    fig1=fig_graph.to_html(full_html=True,config={'displayModeBar':False})
    fig2=fig_graph1.to_html(full_html=True,config={'displayModeBar':False})
    return render(request,'plot.html',{'bar':fig1,'int':meani,'ext':meanx,'bar1':fig2})




item = Records.objects.values('id','No','Name','Internal','External','Subject','Semester','Total')
df2 = pd.DataFrame(item)


r = 'SEM_VI'
z4 = df2.query('Semester == @r') 
figg = px.pie(z4, names = "Subject", values = "Total",height = 500, width = 1000, title="Marks Distribution According to Subjects in 6th Semester")




app = DjangoDash('SimpleExample')
app.layout = dbc.Container([
    dbc.Card([
            dbc.Button('🡠', id='back-button', outline=True, size="sm",
                        className='mt-2 ml-2 col-1', style={'display': 'none'}),
            dbc.Row(
                dcc.Graph(
                        id='graph',
                        figure=figg
                    ), justify='center'
            )
    ], className='mt-3')
])

#Callback
@app.callback(
    Output(component_id = 'graph',component_property =  'figure'),
    Output(component_id = 'back-button',component_property =  'style'), #to hide/unhide the back button
    Input(component_id = 'graph', component_property = 'clickData'),    #for getting the vendor name from graph
    Input(component_id = 'back-button', component_property = 'n_clicks')
)



def drilldown(click_data,n_clicks):
    ctx = dash.callback_context
    if len(ctx.triggered) !=0:
        trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if trigger_id == 'graph':
            s = click_data['points'][0]['label'] 
            print(s)
            if s in z4.Subject.unique():
                x = 'DIGITAL MEDIA'
                vendor_sales_df =z4.query('Subject == @s') 
                fig = px.bar(vendor_sales_df, x = "Name", y = "Total", color = "External",hover_data=['Internal', 'External'], height = 600, width = 1000)
                return fig, {'display':'block'}     #returning the fig and unhiding the back button
            else:
                return figg, {'display':'none'}
    return figg, {'display':'block'}  
    




def trial(request):
   
    menu_list = Records.objects.order_by().values('Subject','Semester').distinct()
    print(len(menu_list))
    if request.method == 'GET':
        menuname =request.GET.get('menuname')

        if request.GET.get('menuname') == '' :
           
            a = Records.objects.order_by().values('Subject','Semester').distinct()
            
        else:
           
             a = Records.objects.order_by().values('Subject','Semester').filter(Subject=menuname).distinct()
    return render(request,'trial_forms.html',{'menu_list':menu_list, 'ab':a})        


def teacher_specific_student(request,ak,bk):
    item = Records.objects.all().values('id','No','Name','Internal','External','Subject','Semester','Total').filter(Name = ak)
    name = ak
    print(ak)
    print(bk)
    z = pd.DataFrame(item)
    r = bk
    df = z.query('Subject == @r') 
    print(df)
    a =  df["Internal"].mean()
    meani = round(a, 2)
    b = df['External'].mean()
    meanx = round(b, 2)
    item2 = Records.objects.all().values('id','No','Name','Internal','External','Subject','Semester','Total')
    for_avg = pd.DataFrame(item2)
    a =  for_avg["Internal"].mean()
    meaniA = round(a, 2)
    b = for_avg['External'].mean()
    meanxA = round(b, 2)
    fig_graph = px.bar(df, x = "Semester", y = "Total", color = "Internal", text = "Subject", title="Marks scored with respect to Internal marks",hover_data=['Subject', 'External'])
    fig_graph1 = px.bar(df, x = "Semester", y = "Total", color = "External", text = "Subject", title="Marks scored with respect to External marks",hover_data=['Subject', 'External','Internal'])
    fig1=fig_graph.to_html(full_html=True,config={'displayModeBar':False})
    fig2=fig_graph1.to_html(full_html=True,config={'displayModeBar':False})
    return render(request, 'teacher_specific_student.html',{'bar':fig1,'int':meani,'ext':meanx,'bar1':fig2, 'reA':meaniA, 'reB': meanxA,'nam':name,'sub':r})

def teachers_view_dynamic(request,pk,jk):
    print(pk)
    print(jk)
    item = Records.objects.all().values('id','No','Name','Internal','External','Subject','Semester','Total').filter(Semester = jk)
    z = pd.DataFrame(item).sort_values('Total')
    r = pk
    df = z.query('Subject == @r') 
    top = Records.objects.values().order_by('-Total').filter(Semester = jk,Subject = r)[0:5]
    low = Records.objects.values().order_by('Total').filter(Semester = jk,Subject = r)[0:5]
    # print(df.head())
    print(low)
    all_data = Records.objects.order_by().values().distinct()
    a =  df["Internal"].mean()
    meani = round(a, 2)
    b = df['External'].mean()
    meanx = round(b, 2)
    print(df.head())
    figg1 = px.bar(df,x = 'Name',y = 'Total',color = 'External',text_auto='.2s',hover_data=['Internal', 'External'],height=600, width = 1000)
    figg1.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    figg=figg1.to_html(full_html=True,config={'displayModeBar':False})

    return render(request,'teacher_dynamic.html',{'graphh':figg,'all':all_data,'int':meani,'ext':meanx,'sub':r,'lo':low,'to':top})














































































def test_form(request):
    return render(request,'test_form.html')


# def std_form(request):
#     return render(request,'standard_form.html')

def Semester_form(request):
    return render(request,'Semester_form.html')







def org_form(request):
    if request.method == 'POST':
        name = request.POST.get('orgname')
        if Organisation_master.objects.filter(org_name = name).exists():
            pass
        else:
            z = Organisation_master(org_name = name)
            z.save()

    return render(request,'organisation_form.html')



def student_form(request):
    organisations = Organisation_master.objects.values().all()
    print(organisations)
    if request.method == 'POST':
        org = request.POST.get('org')
        id = request.POST.get('idno')
        name = request.POST.get('student_name')
        if Student.objects.filter(uid_no = id,student_name = name, Organisation = org).exists():
            pass
        else:
            z = Student(uid_no = id,student_name = name, Organisation = org)
            z.save()

    return render(request,'student_form.html',{'menu_list':organisations})

def teacher_form(request):
    organisations = Organisation_master.objects.values().all()
    print(organisations)
    if request.method == 'POST':
        org = request.POST.get('org')
        name = request.POST.get('teacher_name')
        if Teacher.objects.filter(teacher_name = name, Organisation = org).exists():
            pass
        else:
            z = Teacher(teacher_name = name, Organisation = org)
            z.save()

    return render(request,'teacher_form.html',{'menu_list':organisations})

def class_form(request):
    organisations = Organisation_master.objects.values().all()
    print(organisations)
    if request.method == 'POST':
        org = request.POST.get('org')
        name = request.POST.get('standard')
        if Class.objects.filter(class_n = name, Organisation = org).exists():
            pass
        else:
            z = Class(class_n = name, Organisation = org)
            z.save()

    return render(request,'class_form.html',{'menu_list':organisations})


def subjects_form(request):
    # organisations = Organisation_master.objects.values().all()
    # classes = Class.objects.values().all()
    # print(organisations)
    # if request.method == 'POST':
    #     org = request.POST.get('org')
    #     subject = request.POST.get('sub_n')
    #     stan = request.POST.get('std')
    #     if Subjects.objects.filter(subject_n = subject, Organisation = org, standard = stan).exists():
    #         pass
    #     else:
    #         z = Subjects(subject_n = subject, Organisation = org, standard = stan)
    #         z.save()
    return render(request,'subjects_form.html')

from .forms import SearchContactForm