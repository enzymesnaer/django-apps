from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.generic.base import RedirectView 

urlpatterns = [
    path('adminpage/', admin.site.urls),
    path('redirect/', page),
    path('home/', index),
    path('djangotutorA/', TutorialA.as_view()),
    path('djangotutorB/', RedirectView.as_view(url = 'https://google.co.in')),
    #arguments > url , pattern_name, permanent, get_redirect_url( arguments, keyword_arguments), .query_string
    # .url – If this attribute is used, then the value should be URL string which can have placeholders from python and they can be changed dynamically.

    # .pattern_name – This is the collection of URL patterns, its like urlpatterns list for redirects.

    # .permanent – This takes Boolean values of true and false. If it’s true, then the redirect becomes permanent. By default its value is false.

    # get_redirect_url( arguments, keyword_arguments) – This is a method that returns a string in the form of URL. this method is responsible for generating your URL, Django allows the developer to overwrite this method any way they want.

    # .query_string – This attribute takes values, true or false and by default it’s false. If this attribute is set to true then the view will add or append any query_string to the URL and return the same.

    # ---------------------------------------------------------------------------------------
    # infinite redirect cycle
    path('inf2', inf2),
    path('inf1', inf1),
]
