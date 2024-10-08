# # from serializers import Serializers
from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.StringRelatedField(read_only=True)
    watchlist = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"
        
class WatchlistSerializer(serializers.ModelSerializer):    
    # reviews = ReviewSerializer(many=True,read_only=True)
    reviews = serializers.SerializerMethodField()
    def get_reviews(self, obj):
        reviews= obj.reviews.all()
        return ReviewSerializer(reviews,many=True).data
    class Meta:
        model = WatchList
        fields = "__all__"

# class StreamPlatformSerializer(serializers.ModelSerializer):
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    
#     # Nested serializers
    watchlist = WatchlistSerializer(many=True,read_only = True)
#     # https://www.django-rest-framework.org/api-guide/relations/#stringrelatedfield watch this 
#     # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True,view_name='get_movie_detail',read_only = True,lookup_field='id')
#     # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        # extra_kwargs = {
        #     'url': {'view_name': 'get_stream_detail', 'lookup_field': 'id'}  # Corrected view name
        # }
        
        

    # extra_kwargs = {
    #         'url': {'view_name': 'get_stream_detail', 'lookup_field': 'id'}
    #     }


# class WatchlistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WatchList
#         fields = "__all__"

# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):  # Changed to HyperlinkedModelSerializer
#     watchlist = serializers.HyperlinkedRelatedField(
#         many=True,
#         view_name='get_movie_detail',
#         read_only=True,
#         lookup_field='id'
#     )

    # 









# # Basics
# '''
# class SeriesSerializer(serializers.ModelSerializer):
#     # Cutsom Fields
#     len_names = serializers.SerializerMethodField()
    
#     def get_len_names(self,object):
#         length = len(object.name)
#         return length
#     def validate_name(self, name):
#         if len(name) < 2:
#             raise serializers.ValidationError("Name should be at least 2 characters long")
#         return name
# #     #  Object level validation 
#     class Meta:
#         model = Series
#         fields = "__all__"
        
#         # fields = ('id','name','description','activate')
#         # exclude= ['activate']
        
# '''














# #---------------------------------------------------------------->

# # def name_length(value):
# #     if len(value) < 2:
# #         raise serializers.ValidationError("Name should be at least 2 characters long")
    
# # class SeriesSerializer(serializers.Serializer):
# #     id = serializers.IntegerField(read_only=True)
# #     #  Validator 
# #     name  = serializers.CharField(validators=[name_length])
# #     description = serializers.CharField()
# #     activate = serializers.BooleanField()
    
# #     def create(self,validated_data):
# #         return Series.objects.create(**validated_data)
    
# #     def update(self, instance, validated_data):
# #         """
# #         Update and return an existing `Series` instance, given the validated data.
# #         """
# #         instance.name = validated_data.get('name', instance.name)
# #         instance.description = validated_data.get('description', instance.description)
# #         instance.activate = validated_data.get('activate', instance.activate)
# #         instance.save()
# #         return instance
    
# #     # Filed level validation 
    
# #     # def validate_name(self, name):
# #     #     if len(name) < 2:
# #     #         raise serializers.ValidationError("Name should be at least 2 characters long")
# #     #     return name
# #     #  Object level validation 
# #     # def validate(self,data):
# #     #     if data['name'] == data['description']:
# #     #         raise serializers.ValidationError("Name and description cannot be the same")
# #     #     return data
