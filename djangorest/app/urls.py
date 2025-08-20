from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('students/', views.student_view, name="Students"),
    path('students/<int:pk>', views.studentDetailView, name="StudentDetail"),
    # path('employees/', views.Employees.as_view(), name="Employees"),
    # path('employees/<int:pk>', views.Employee_detail.as_view(), name='Employee_detail')
    path('', include(router.urls)) ,  

    path('blogs/', views.BlogsView.as_view()), 
    path('comments/', views.CommentsView.as_view()), 

]