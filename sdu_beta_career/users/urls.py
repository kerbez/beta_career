from django.urls import path, include

from sdu_beta_career.users.views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
    ProfileDetailView, ProfileListView)

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("profiles/", ProfileListView.as_view(), name="profile"),
    path("profiles/<int:pk>", ProfileDetailView.as_view(), name="profile_detail"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
