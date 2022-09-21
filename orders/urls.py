from django.urls import path
from orders import views

urlpatterns = [
    path('create/', views.CreateUserOrderView.as_view()),
    path('list/', views.UserOrderListView.as_view()),
    path('<int:id>', views.OrdersRetrieveUpdateDeleteView.as_view()),
]