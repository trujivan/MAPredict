from rest_framework import serializers
from .utils import get_ml_predictions
from .models import MLRequest, Prediction


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['year', 'pollution',]


class MLRequestSerializer(serializers.ModelSerializer):

    predictions = PredictionSerializer(many=True, read_only=True)
    factor = serializers.ChoiceField(choices=['NO2 AQI', 'SO2 AQI', 'CO AQI','O3 AQI'])
    class Meta:
        model = MLRequest
        fields = ['start_year', 'end_year', 'state', 'factor', 'predictions']

    def create(self, validated_data, *args, **kwargs):

        predicted_data = get_ml_predictions(validated_data['state'], validated_data['factor'],validated_data['start_year'],
                                            validated_data['end_year'])
        #print(prediction)
        #print("It works")
        ml_request = MLRequest.objects.create(**validated_data)
        year = int(validated_data['start_year'])
        for prediction in predicted_data:
            Prediction.objects.create(request=ml_request, year=year, pollution=prediction)
            year += 1
        return ml_request
