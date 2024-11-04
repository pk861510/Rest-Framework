from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'navbar-content', views.NavbarContentViewSet)
router.register(r'our-clients', views.OurClientViewSet)
router.register(r'client-testimonials', views.ClientTestimonialsViewSet)
router.register(r'management-team', views.ManagementTeamViewSet)
router.register(r'developer-team', views.DeveloperTeamViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('add-developer', views.adddeveloper),
    path('add-management', views.addmanagement),
    path('add-client', views.addclient),
    path('add-clienttmls', views.addclienttmls),

]
