from django.db import models

# Create your models here.
class Operationdepartment(models.Model):
    id = models.AutoField(primary_key=True)
    oname=models.CharField(max_length=32,default=None) #运行部

class Work_area(models.Model):
    id = models.AutoField(primary_key=True)
    wname = models.CharField(max_length=32,default=None) #工区

class Instrument(models.Model):    #仪表表
    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=32,default=None) #区域
    iname=models.CharField(max_length=23,default=None) #仪表名称
    tag = models.CharField(max_length=32,default=None) #位号
    work_area = models.ForeignKey(Work_area,on_delete=models.CASCADE,default=1) #工区ID
    operation_department = models.ForeignKey(Operationdepartment,on_delete=models.CASCADE,default=1) #运行部ID
    creater = models.CharField(max_length=32,default=None) #创建人
    modifier = models.CharField(max_length=32,default=None) #修改人
    intact = models.BooleanField(default=True) #完成情况


    def __str__(self):
        return self.iname


class Instrumentfaults(models.Model): #仪表故障信息表
    id = models.AutoField(primary_key=True)
    fault_information = models.CharField(max_length=200,default=None) #故障信息
    databefore = models.DateField(default=None) #故障日期
    repairdata = models.DateField(default=None) #修复日期
    work_order_no = models.CharField(max_length=32,default=None) #工单号
    reporter = models.CharField(max_length=32,default=None) #提报人
    enforcer = models.CharField(max_length=32,default=None) #执行人
    implentention = models.CharField(max_length=4000,default=None) #执行信息
    photobefore = models.ImageField(upload_to='img',default=None)
    photoafter = models.ImageField(upload_to='img',default=None)
    cid = models.ForeignKey(Instrument,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.reporter

