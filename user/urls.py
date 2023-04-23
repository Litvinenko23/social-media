from django.urls import path


from user.views import CreateUserView, CreateTokenView, ManageUserView, UserViewSet, LogoutView, SubscribeUserView, \
    UnsubscribeUserView, UserFollowingListView, UserFollowersListView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="token"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("users/", UserViewSet.as_view({"get": "list"}), name="users"),


    path("subscribe/", SubscribeUserView.as_view(), name="subscribe"),
    path("unsubscribe/<int:pk>/", UnsubscribeUserView.as_view(), name="unsubscribe"),
    path("following/", UserFollowingListView.as_view(), name="following"),
    path("followers/", UserFollowersListView.as_view(), name="followers"),
]

app_name = "user"
