import json , requests

from .models          import Covid ,KoreaCovid
from django.views     import View
from django.http      import HttpResponse, JsonResponse
from django.db.models import Count, Q , Sum

class CovidApiView(View):
    def get(self , request):
        try:
            query = request.GET.get('keyword' , None) # 코로나 데이터 검색
            if query :
                world_data = Covid.objects.filter(Q(area__icontains=query) | Q(country__icontains=query)).all()
                korea_data = KoreaCovid.objects.filter(Q(area__icontains=query)).all()
                world_patient_count = world_data.count()
                korea_patient_count = korea_data.count()

                data = {
                    'country_covid_count' : world_patient_count,
                    'korea_covid_count' : korea_patient_count,
                    'world_covid_data'  : [{
                            'id'      : world.id,
                            'area'    : world.area,
                            'country' : world.country,
                            'patient' : world.patient,
                            'dead'    : world.dead,
                    } for world in world_data],
                    'korea_covid_data' : [{
                            'id'      : korea.id,
                            'area'    : korea.area,
                            'patient' : korea.patient,
                    } for korea in korea_data]
                }

                return JsonResponse({"data" : data},status=200)

            country_covid     = Covid.objects.values()
            korea_covid       = KoreaCovid.objects.values()
            korea_covid_count = KoreaCovid.objects.all().aggregate(Sum('patient'))
            country_covid_count = Covid.objects.all().aggregate(Sum('patient'))

            return JsonResponse({'data' : {
                                    'country_covid_count' : country_covid_count,
                                    'korea_covid_count'   : korea_covid_count,
                                    'world_covid_data'    : list(country_covid),
                                    'korea_covid_data'    : list(korea_covid),
                                }}, status=200)

        except Covid.DoesNotExist:
            return JsonResponse({'message': 'Not found'}, status=400)

        except TypeError:
            return JsonResponse({'message': 'error'}, status=400)
