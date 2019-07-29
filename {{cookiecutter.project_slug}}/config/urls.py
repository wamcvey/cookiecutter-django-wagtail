from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
{% if cookiecutter.use_wagtail == 'y' -%}

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
{%- endif %}

urlpatterns = [
    # Django Admin, use {% raw %}{% url 'admin:index' %}{% endraw %}
    path(settings.ADMIN_URL, admin.site.urls),
    {% if cookiecutter.use_wagtail == 'y' -%}
    path(r'cms/', include(wagtailadmin_urls)),
    path(r'documents/', include(wagtaildocs_urls)),
   
    {%- endif %}

    # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    # path(
    #    "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    # ),
    
    # User management
    path("users/", include("{{ cookiecutter.project_slug }}.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

{% if cookiecutter.use_wagtail == 'y' -%}

urlpatterns += [
    path(r'', include(wagtail_urls)),
]
{%- endif %}
