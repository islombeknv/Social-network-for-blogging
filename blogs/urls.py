from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('myadmin/dashboard/', include('myadmin.urls', namespace='myadmin')),
    path('accounts/', include('registration.backends.default.urls')),
    path('blog/', include('posts.urls', namespace='blog')),
    path('', include('pages.urls', namespace='pages')),
    path('contact/', include('contacts.urls', namespace='contact')),
    path('account/', include('account.urls', namespace='account')),
    path('post/send/email/', include('postemail.urls', namespace='email')),

)

handler404 = "blogs.views.page_not_found_view"

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
