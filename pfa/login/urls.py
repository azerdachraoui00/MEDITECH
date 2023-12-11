from django.urls import path, include

from  . import views

urlpatterns = [
    path('', views.index, name="home" ),
    path('admin/add-listing.html', views.addlisting, name="listing" ),
    path('bookings.html', views.boukings, name="bookings" ),
    path('bookmarks.html', views.bookmarks, name="bookmarks" ),
    path('charts.html', views.charts, name="charts" ),
    path('doctor-profile.html', views.docktorprof, name="docktorprof" ),
    path('messages.html', views.messages, name="messages" ),
    path('reviews.html', views.reviews, name="reviews" ),
    path('tables.html', views.tables, name="tables" ),
    path('user-profile.html', views.user, name="user" ),









]