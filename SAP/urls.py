from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project_look', views.projectlook, name='projectlook'),
    path('uab_look', views.uablook, name='uablook'),
    path('toHome', views.toHome, name='toHome'),
    path('toAddUAB', views.toAddUAB, name='toAddUAB'),
    path('rinkodaraHTML', views.rinkodaraHTML, name='rinkodaraHTML'),
    path('toAddUABinfo', views.toAddUABinfo, name='toAddUABinfo'),
    path('toSaNariai', views.toSaNariai, name='toSaNariai'),
    path('rinkodara', views.rinkodara, name='rinkodara'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('registerHtml', views.registerHtml, name='registerHtml'),
    path('disconect', views.disconect, name='disconect'),
    path('projectAdd', views.projectAdd, name='projectAdd'),
    path('uabAdd', views.uabAdd, name='uabAdd'),
    path('uabAddInfo', views.uabAddInfo, name='uabAddInfo'),
    path('projectAddHtml', views.projectAddHtml, name='projectAddHtml'),
    path('project_lookout', views.project_lookout, name='project_lookout'),
    path('uab_lookout', views.uab_lookout, name='uab_lookout'),
    path('myProjects', views.myProjects, name='myProjects'),
    path('busenos_keitimas', views.busenos_keitimas, name='busenos_keitimas'),
    path('join_project', views.join_project, name='join_project'),
    path('leave_project', views.leave_project, name='leave_project'),
    path('add_uabsToProject', views.add_uabsToProject, name='add_uabsToProject'),
    path('uab_add_project', views.uab_add_project, name='uab_add_project'),
    path('delete_project', views.delete_project, name='delete_project'),
    path('projectUab_delete', views.projectUab_delete, name='projectUab_delete'),
    path('to_edit_uab', views.to_edit_uab, name='to_edit_uab'),
    path('edit_uab', views.edit_uab, name='edit_uab'),
    path('to_code_generator', views.to_code_generator, name='to_code_generator'),
    path('code_generator', views.code_generator, name='code_generator'),
    path('delete_code', views.delete_code, name='delete_code'),
    path('uab_changeConnect', views.uab_changeConnect, name='uab_changeConnect')
]
