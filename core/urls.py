from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from strawberry.django.views import AsyncGraphQLView

# from graph.schema import schema
from api.apps.flights.gql.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("graphql/v1", AsyncGraphQLView.as_view(schema=schema)),
    path("", include('api.urls')),
    path("", include("django_nextjs.urls")),
    path("", include("apps.companies.urls")),
    path("schedules/", include("apps.schedules.urls")),

    # path('companies/', include('apps.companies.urls'))
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)