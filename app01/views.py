from django.shortcuts import render,redirect,HttpResponse
import os
from .models import *
# Create your views here.
def manage(request):
    return render(request,'manage.html')


def instrumentfaults_list(request): #故障仪表后台显示
    obj = Instrumentfaults.objects.all()

    return render(request,'instrumentfaults_list.html',{'obj':obj})


def instrumentfaults_listall(request): #故障仪表前端显示
    obj = Instrumentfaults.objects.all()

    return render(request,'instrumentfaults_listall.html',{'obj':obj})



def instrumentfaults_del(request,id):
    pk = request.GET.get('id')
    Instrumentfaults.objects.get(id=pk).delete()
    return redirect('/instrumentfaults_list/')



def instrument_list(request): #仪表显示
    obj = Instrument.objects.all()
    return render(request, 'instrument_list.html', {'obj': obj})


def index(request):

    return render(request,'index.html')


def instrumentfaults_edit(request):
    pk = request.GET.get('id')
    obj =Instrumentfaults.objects.get(id=pk)
    print(obj.databefore)
    if request.method == 'POST':
        databefore = request.POST.get("databefore")
        print(databefore)
        obj.databefore = databefore
        repairdata = request.POST.get('repairdata')
        obj.repairdata = repairdata
        work_order_no = request.POST.get('work_order_no')
        obj.work_order_no= work_order_no
        reporter= request.POST.get('reporter')
        obj.reporter = reporter
        fault_information = request.POST.get('fault_information')
        obj.fault_information=fault_information
        enforcer = request.POST.get('enforcer')
        obj.enforcer= enforcer
        implentention = request.POST.get('implentention')
        obj.implentention = implentention
        data = {'databefore': databefore,
                'repairdata': repairdata,
                'data_of_failure': data_of_failure,
                'work_order_no': work_order_no,
                'reporter': reporter,
                'fault_information': fault_information,
                'implentention': implentention,
                'enforcer': enforcer,
                }
        obj.save()
        return redirect("/instrumentfaults_list/")
    return render(request,'instrumentfaults_edit.html',{'obj':obj})


def instrumentfaults_add(request):
    # pk = request.GET.get('id')
    # print(pk)
    if request.method == 'POST':
        databefore = request.POST.get('databefore')
        repairdata = request.POST.get("repairdata")
        work_order_no = request.POST.get('work_order_no')
        reporter = request.POST.get('reporter')
        fault_information = request.POST.get('fault_information')
        implentention = request.POST.get('implentention')
        enforcer = request.POST.get('enforcer')
        cid_id = request.POST.get('cid')
        photobefore =request.FILES.get('photobefore','')

        data = {'repairdata': repairdata,
                'databefore': databefore,
                'work_order_no': work_order_no,
                'reporter': reporter,
                'fault_information': fault_information,
                'implentention': implentention,
                'enforcer': enforcer,
                'cid_id':cid_id,
                'photobefore':photobefore,
                }
        Instrumentfaults.objects.create(**data)
    return redirect('/instrumentfaults_list/')


def insinstrumentfaults_upload(request):
    if request.method =='GET':
        pk = request.GET.get('id')
        return render(request,'instrumentfaults_add.html',{'pk':pk})
    elif request.method =='POST':
        photobefore = request.FILES.get('photobefore', '')
        if not os.path.exists('media'):
            os.makedirs('media')
        with open(os.path.join(os.getcwd(), 'media', photobefore.name), 'wb') as fw:
            # 一次性读取
            fw.write(photobefore.read())
            # 分块读取
            # for ck in photobefore.chunks():
            # fw.write(ck)

        return HttpResponse('上传成功')
    else:
        return HttpResponse('当前访问量过大，请稍候再试！')



def insinstrumentfaults_download(request):
    photobefore = request.GET.get('photobefore','')
    filename = photobefore[photobefore.rindex('/')+1:]
    #photo[photo.rindex('/')+1:]
    path = os.path.join(os.getcwd(),'media',photobefore.replace('/','\\'))
    print(path)
    #开启一个流
    with open(path,'rb') as fr:
        response = HttpResponse(fr.read())
        response['Content-Type']='image/png'

    return response



def instrument_add(request):
    opt = Operationdepartment.objects.all()
    wpt = Work_area.objects.all()
    context = {
        'opt': opt,
        'wpt': wpt,
    }
    if request.method == 'POST':
        area = request.POST.get('area')
        creater = request.POST.get("creater")
        iname = request.POST.get('iname')
        intact = request.POST.get('intact')
        modifier = request.POST.get('modifier')
        operation_department_id = request.POST.get('operation_department')
        tag = request.POST.get('tag')
        work_area_id = request.POST.get('work_area')
        data = {'area': area,
                'creater': creater,
                'iname': iname,
                'intact': intact,
                'modifier': modifier,
                'operation_department_id': operation_department_id,
                'tag': tag,
                'work_area_id': work_area_id,
                }
        Instrument.objects.create(**data)
    return render(request, 'instrument_add.html', context)


def instrument_edit(request):
    pk = request.GET.get('id')
    obj =Instrument.objects.get(id=pk)
    if request.method == 'POST':
        area = request.POST.get('area')
        obj.area = area
        creater = request.POST.get("creater")
        obj.creater = creater
        iname = request.POST.get('iname')
        obj.iname = iname
        intact = request.POST.get('intact')
        obj.intact = intact
        modifier = request.POST.get('modifier')
        obj.modifier = modifier
        # operation_department = request.POST.get('operation_department')
        # obj.operation_department = operation_department
        tag = request.POST.get('tag')
        obj.tag = tag
        # work_area = request.POST.get('work_area')
        # obj.work_area = work_area
        obj.save()
        return redirect("/instrument_list/")
    return render(request, 'instrument_edit.html', {'obj':obj})

def instrument_del(request):
    pk = request.GET.get('id')
    Instrument.objects.get(id=pk).delete()
    return redirect('/instrument_list/')
