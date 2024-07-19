from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add-record/", views.add_record, name="add_record"),
    path("record-detail/<int:pk>/", views.record_detail, name="record_detail"),
    path("update-record/<int:pk>/", views.update_record, name="update_record"),
    path("delete-record/<int:pk>/", views.delete_record, name="delete_record"),
]



