# from .serializers import WatchlistSerializer,StreamPlatformSerializer
# from rest_framework.response import Response
# # from rest_framework.decorators import api_view
# from rest_framework import status
# from watchlist_app.models import WatchList,StreamPlatform
# from rest_framework.views import APIView
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from watchlist_app.models import StreamPlatform, WatchList,Review
from .serializers import StreamPlatformSerializer, WatchlistSerializer,ReviewSerializer
from rest_framework import mixins
from rest_framework import generics


# Using mixins
class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class watchStreamPlatform(APIView):
    def get(self, request):
        content = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(content, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = StreamPlatformSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchListAll(APIView):
    def get(self, request):
        content = WatchList.objects.all()
        serializer = WatchlistSerializer(content, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = WatchlistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getDetail(APIView):
    def get(self, request, id):
        try:
            watchlist = WatchList.objects.get(id=id)
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WatchlistSerializer(watchlist, context={'request': request})
        return Response(serializer.data)

class GetStream(APIView):
    def get(self, request, id):
        try:
            stream_platform = StreamPlatform.objects.get(id=id)
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(stream_platform, context={'request': request})
        return Response(serializer.data)

class Reviews(APIView):
    def get(self,request):
        content = Review.objects.all()
        serializer =  ReviewSerializer(content,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class watchStreamplatform(APIView):
#     def get(self,request):
#         content = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(content,many=True,context={'request': request})
#         return Response(serializer.data)
    
#     def post(self,request):
#         data = request.data
#         serializer = StreamPlatformSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class WatchListAll(APIView):
#     def get(self,request):
#         series = WatchList.objects.all()
#         serializer = WatchlistSerializer(series,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = WatchlistSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class GetStream(APIView):
#     def get(self,request,id):
#         try:
#             stream  = StreamPlatform.objects.get(id=id)
#             serializer = StreamPlatformSerializer(stream,context={'request': request})
#             return Response(serializer.data,status = status.HTTP_200_OK)
#         except Exception as e:
#             return Response({f"{e} ":f"{id} is not a valid stream number"},status=status.HTTP_400_BAD_REQUEST)
        
#     def put(self,request,id):
#         content = StreamPlatform.objects.get(id=id)
        
#         serializer = StreamPlatformSerializer(content,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete (self, request,id):
#         content = StreamPlatform.objects.get(id=id)
#         content.delete()
#         return Response({"NO_CONTENT":"The content here has been moved or deleted"},status=status.HTTP_204_NO_CONTENT)
            
        

# class getDetail(APIView):
#     def get(self,request,id):
#         series = WatchList.objects.get(id = id)
#         serializer = WatchlistSerializer(series)
#         return Response(serializer.data,status = status.HTTP_200_OK)
    
#     def put(self,request,id):
        
#         series = WatchList.objects.get(id= id)
#         serializer = WatchlistSerializer(series ,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id):
#         series = WatchList.objects.get(id=id)
#         series.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)












# # Basics
# '''

# class SeriesList(APIView):
#     def get(self,request):
#         series = Series.objects.all()
#         serializer = SeriesSerializer(series,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = SeriesSerializer(data = request.data)
#         # print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
# class GetSeriesDetail(APIView):
#     def get(self,request,id):
#         # print(id ,"is id ")
#         series = Series.objects.get(id = id)
#         serializer = SeriesSerializer(series)
#         return Response(serializer.data,status = status.HTTP_200_OK)
    
#     def put(self,request,id):
        
#         series = Series.objects.get(id= id)
#         serializer = SeriesSerializer(series ,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id):
#         series = Series.objects.get(id=id)
#         series.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# '''
# # @api_view(['GET', 'POST', 'PUT'])
# # def series_list(request):
# #     if request.method == 'GET':    
# #         series_list = Series.objects.all()
# #         serializer = SeriesSerializer(series_list,many=True )
# #         return Response(serializer.data)
# #     if request.method == 'POST':
# #         serializer = SeriesSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=201)
# #         return Response(serializer.errors, status=400)

# # @api_view(['GET', 'PUT','DELETE'])
# # def get_series_detail(request,id):
# #     if request.method == 'GET':
# #         try:
# #             series_list = Series.objects.get(id=id) 
# #             serializer = SeriesSerializer(series_list)
# #             return Response(serializer.data)
# #         except:
# #             return Response({'Messege' : f"there is no series for id {id}"}, status=status.HTTP_404_NOT_FOUND)

# #     if request.method == 'PUT':
# #         series = Series.objects.get(id= id)
# #         serializer = SeriesSerializer(series ,data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# #     if request.method == 'DELETE' :
# #         series = Series.objects.get(id=id)
# #         series.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)

