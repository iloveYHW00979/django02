from rest_framework import serializers
from .models import *


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class Team_RankingSerializers(serializers.ModelSerializer):
    team_type = serializers.SerializerMethodField()
    class Meta:
        model = TeamRanking
        fields = '__all__'

    def get_team_type(self, obj):
        team = obj
        print(team.group_type_id)
        team_type = GroupDict.objects.filter(group_id=team.group_type_id)[0].group_type
        return team_type

class All_imgsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AllImg
        fields = '__all__'

class Inc_introduceSerializers(serializers.ModelSerializer):
    class Meta:
        model = IncIntroduce
        fields = '__all__'

class CultureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'

class EquipmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

