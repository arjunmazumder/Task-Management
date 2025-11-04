from django.urls import path

from users.views import Sign_Up, Log_In, Log_Out,activate_user,admin_dashboard,assign_role,create_group,group_list
urlpatterns = [
    path('sign-up/', Sign_Up, name='sing-up'),
    path('log-in/',Log_In,name='log-in'),
    path('log-out/',Log_Out, name='log-out'),
    path('activate/<int:user_id>/<str:token>/', activate_user),
    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('admin/<int:user_id>/assign-role/', assign_role, name='assign-role'),
    path('admin/create-group/', create_group, name='create-group'),
    path('admin/group-list/', group_list, name='group-list')

    
]