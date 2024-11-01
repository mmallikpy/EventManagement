from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, signup, signin, profile, logMeOut, edit, detailview, createEvent, eventDel, updateEvent, bookUserFind, EventCatorogyview

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("profile", profile, name='profile'),
    path('logout/', logMeOut, name='logout'),
    path("edit/<int:id>", edit, name='edit'),
    path('detailview/<int:id>', detailview, name='detailview'),
    path('createevent/', createEvent, name='createevent'),
    path('eventdel/<int:id>', eventDel, name='eventdel'),
    path('updateevent/<int:id>', updateEvent, name='updateevent'),
    path('book/<int:id>', bookUserFind, name='bookuser'),
    path('eventcat/', EventCatorogyview, name='eventcat'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 