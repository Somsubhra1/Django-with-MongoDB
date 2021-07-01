from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('', BlogViewSet, 'blogs')

urlpatterns = router.urls
