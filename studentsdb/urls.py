"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from students.views import students_view, groups_view, journal_view, contact_admin_view
from .settings import MEDIA_ROOT, DEBUG, STATIC_URL, MEDIA_URL 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

	
urlpatterns = [
	#Students urls
	url(r'^$', students_view.students_list, name='home'),
	url(r'^students/add/$', students_view.students_add, name='students_add'),
	url(r'^students/(?P<pk>\d+)/edit/$', students_view.StudentUpdateView.as_view(), name='students_edit'),
	url(r'^students/(?P<pk>\d+)/delete/$', students_view.StudentDeleteView.as_view(), name='students_delete'),
	
	# Groups urls
	url(r'^groups/$', groups_view.groups_list, name='groups'),
	url(r'^groups/add/$', groups_view.groups_add, name='groups_add'),
	url(r'^groups/(?P<gid>\d+)/edit/$', groups_view.groups_edit, name='groups_edit'),
	url(r'^groups/(?P<gid>\d+)/delete/$', groups_view.groups_delete, name='groups_delete'),
	
	# Journal urls
	url(r'^journal/(?P<pk>\d+)?/?$', journal_view.JournalView.as_view(), name='journal'),
	
    url(r'^admin/', admin.site.urls),
	url(r'^contact-admin/$', contact_admin_view.contact_admin, name='contact_admin'),
	
] + static(STATIC_URL, document_root=settings.STATIC_ROOT)

if DEBUG:
	#save files from media folder
	urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
	