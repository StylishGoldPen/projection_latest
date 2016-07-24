from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^posts/', include("openedprojects.urls", namespace = 'posts')),
    url(r'^comments/', include("comments.urls", namespace = 'comments')),
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'src.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^categories/', 'openedprojects.views.categories', name = 'categories'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/', "openedprojects.views.show_category", name = 'posts'),

    url(r'^openedprojects/','openedprojects.views.openedgenres', name='openedgenres'),
    url(r'^opened_subcategories/','openedprojects.views.opened_subcategories', name='opened_subcategories'),
    
    url(r'^closedprojects/','closedprojects.views.closedgenres', name='closedgenres'),
    url(r'^closed_subcategories/','closedprojects.views.closed_subcategories', name='closed_subcategories'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
