
from django.urls import path,re_path
from app01 import views
urlpatterns = [
    path('manage/', views.manage),
    path('instrumentfaults_del/', views.instrumentfaults_del),
    path('instrumentfaults_list/', views.instrumentfaults_list),
    path('instrumentfaults_add/', views.instrumentfaults_add),
    path('instrumentfaults_upload/', views.insinstrumentfaults_upload),
  # //  path('instrumentfaults_addphotoafter/', views.instrumentfaults_addphotoafter),
    path('insinstrumentfaults_download/', views.insinstrumentfaults_download),
    path('instrumentfaults_edit/', views.instrumentfaults_edit),
 # //   path('instrumentfaults_editphotoafter/', views.instrumentfaults_editphotoafter),
    path('instrumentfaults_listall/', views.instrumentfaults_listall),
    path('instrument_add/', views.instrument_add),
    path('instrument_edit/', views.instrument_edit),
    path('instrument_del/', views.instrument_del),
    path('instrument_list/', views.instrument_list),
    path('index/', views.index),
]
