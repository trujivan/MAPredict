from django.urls import path, include
from .views import main_view, PredictionView

#router = routers.DefaultRouter(trailing_slash=False)
#router.register('years', YearView, basename='years')
#router.register('predict', PredictionView, basename='predict')


urlpatterns = [
    #path('api/', get_dummy_data),
    #path('pollution/predict', get_prediction, name='test_predict'),
    #path('myform/', api_form_view, name='year_form'),
    #path('api/', include(router.urls)),
    path(r'', main_view, name="main"),
    path(r'api/v1/predict', PredictionView.as_view(), name='predict')
]