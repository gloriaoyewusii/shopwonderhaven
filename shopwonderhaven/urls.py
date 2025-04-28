"""
URL configuration for shopwonderhaven project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import reviewer
import seller
from seller import views
from reviewer import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register-seller/', seller.views.register_seller, name='register_seller'),

    path('submit-item/', seller.views.submit_item, name='submit_item'),

    path('view-review-status/', seller.views.view_review_status, name='view_review_status'),

    path('register-reviewer/', reviewer.views.register_reviewer, name='register_reviewer'),

    path('view-pending-review-items/', reviewer.views.view_pending_review_items, name='view_pending_review_items'),

    path('approve-item/', reviewer.views.approve_item, name='approve_item'),
]
