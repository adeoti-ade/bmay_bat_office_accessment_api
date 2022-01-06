from rest_framework import routers
from . import views

app_name = "repertoire"

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"files", views.FileViewset)

urlpatterns = []

urlpatterns += router.urls
