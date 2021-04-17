from rest_framework import routers
from employee.api import EmployeeViewSet

router = routers.DefaultRouter()
router.register('api/employees', EmployeeViewSet, 'employees')

urlpatterns = router.urls