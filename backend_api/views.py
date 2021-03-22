from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend_api import stations_wise, json_all_data, connection_line_wise,connection_line_dist


class GetAll(APIView):
    def get(self, request):
        return Response(data=json_all_data, content_type='application/json', status=status.HTTP_200_OK)


class Search(APIView):
    def get(self, request):
        req_data = request.GET.get("station").lower().split("rs")[0].strip()
        data = stations_wise.get(req_data)
        if data:
            return Response(data=data, content_type='application/json', status=status.HTTP_200_OK)
        return Response(data={"message": "Invalid parameters"}, status=status.HTTP_400_BAD_REQUEST)


class Distance(APIView):
    def get(self, request):
        from_id = request.GET.get("from").lower()
        to_id = request.GET.get("to").lower()
        for line in connection_line_wise:
            if from_id in connection_line_wise[line] and to_id in connection_line_wise[line]:
                from_dist = connection_line_dist[line][from_id]
                to_dist = connection_line_dist[line][to_id]
                data = {"from":from_id.upper(),"to":to_id.upper(),"line":line,"distance in km": float(to_dist) - float(from_dist)}
                return Response(data=data, status=status.HTTP_200_OK)
        return Response(data={"message":"invalid from or to id"}, status=status.HTTP_400_BAD_REQUEST)

