from django.contrib import admin
from recommendation.models import Recommendation

# Recommendatin details in admin pannel
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['id','Product_id','User_id']
admin.site.register(Recommendation,RecommendationAdmin)
