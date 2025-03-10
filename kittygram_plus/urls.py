from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, OwnerViewSet, AchievementSerializer


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register('achievement', AchievementSerializer)

urlpatterns = [
    path('', include(router.urls)),
]
