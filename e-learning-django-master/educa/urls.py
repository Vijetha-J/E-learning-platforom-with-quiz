#from django.conf.urls import include, url,path
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    #url(r'^accounts/login/$', auth_views.login, name='login'),
    #url( r'^login/$',auth_views.LoginView.as_view, name="login"),
    #url(r'^accounts/logout/$', auth_views.logout, name='logout'),
   # url( r'^login/$',auth_views.LoginView.as_view, name="logout"),
   
    #url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^course/', include('courses.urls')),
    #url(r'^students/', include('students.urls')),
    #url(r'^$', CourseListView.as_view(), name='course_list'),
    #url(r'^api/', include('courses.api.urls', namespace='api')),
    
    
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('', CourseListView.as_view(), name='course_list'),
    path('students/', include('students.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('', include('quiz.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
