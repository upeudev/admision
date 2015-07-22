from django.conf.urls import include, url


# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from admision_seleccion.views.PostulanteView import PostulanteViewSet, \
    ApiEndpoint


router = routers.DefaultRouter()
router.register(r'postulantes', PostulanteViewSet)


urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^api/hello', ApiEndpoint.as_view()),  # and also a resource server!

]
