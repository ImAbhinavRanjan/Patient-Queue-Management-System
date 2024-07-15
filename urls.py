from django.urls import path
from . import views

urlpatterns= [
    
    path("", views.main, name="main"),
    path("login",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout"),
    path("logged",views.logged,name="logged"),
    path("book",views.book,name="book"),
    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path("index",views.index,name="index"),
    path("doc1",views.doc1, name="doc1"),
    path("doc2",views.doc2, name="doc2"),
    path("doc1/<int:doctor_id>/",views.doc1inc,name="doc1inc"),
    path("doc2/<int:doctor_id>/",views.doc2inc,name="doc2inc"),
    path("doc1Reset",views.doc1Reset, name="doc1Reset"),
    path("doc2Reset",views.doc2Reset, name="doc2Reset"),
]