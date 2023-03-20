from django.urls import path
from . import views

urlpatterns = [
    # USER AUTHENTICATION PATHS
    path('register/',views.register_page, name='register'),
    path('login/',views.login_page, name='login'),
    path('logout/',views.logout_user, name='logout'),

    #MAIN PATHS
    path('',views.home, name='home'),
    path('post/<slug:slug>',views.post_detail, name='post_detail'),
    path('about_us/',views.about_us, name='about_us'),
    path('contact_us/',views.contact_us, name='contact_us'),

    #CRUD PATHS
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<slug:slug>', views.update_post, name='update_post'),
    path('delete_post/<slug:slug>', views.delete_post, name='delete_post'),

    #SEND EMAIL PATH
    path('send_email',views.send_email,name="send_email"),
]
