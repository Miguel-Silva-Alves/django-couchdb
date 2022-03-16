from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView

from papers.models import Paper, SERVER, Sensor

from papers.Utils import getTimeEditado


db = SERVER['papers']

class PaperAPI(APIView):
    def post(self, request):

        try:
            papel = Paper()
            papel.abstract = request.data["abstract"]
            papel.title = request.data["title"]
            papel.type = request.data["type"]
            papel.store(db)
        except Exception as e:
            return JsonResponse({"error":str(e)})

        return JsonResponse({"status":"Ok", "mensagem":"Cadastro Realizado"})
    def get(self, request):
        # Paper.by_name.sync(db)
        # for papel in Paper.by_name(db):
        #     print(papel._id)

        campos = ['title', 'abstract', 'type', '_id']
        retorno = []

        mango = {'selector': {'title':'bunda'}, 'fields': campos}
        for row in db.find(mango): 
            dic = {}
            for detail in campos:
                dic[detail] = row[detail]                        
            retorno.append(dic)
        return JsonResponse(
            {
                "data":"home",
                "retorno": retorno
            }
        )

# CLASS SENSORVIEW
class SensorAPI(APIView):
    def post(self, request):

        campos_request = sorted(request.data)
        campos_obrigatorios = sorted(["dado", "id_dispositivo_ip"])

        # VALIDAÇÃO
        if campos_request != campos_obrigatorios:
            return JsonResponse({"error":"ausencia de parametros"})
        
        date, timme = getTimeEditado()

        try:
            sensor = Sensor()
            sensor.dado = request.data["dado"]
            sensor.created_at_date = date
            sensor.created_at_time = timme
            sensor.id_dispositivo_ip = request.data["id_dispositivo_ip"]
            sensor.store(db)
        except Exception as e:
            return JsonResponse({"error":str(e)})

        return JsonResponse({"status":"Ok", "mensagem":"Cadastro Realizado"})
    def get(self, request):
        campos_request = sorted(request.data)
        campos_obrigatorios = sorted(["busca", "valor"])

        # VALIDAÇÃO
        if campos_request != campos_obrigatorios:
            return JsonResponse({"error":"ausencia de parametros"})

        campos = ['dado', 'created_at_date', 'created_at_time', 'id_dispositivo_ip', '_id']
        retorno = []

        mango = {'selector': {request.data['busca']:request.data['valor']}, 'fields': campos,"limit": 100}
        cont = 0
        for row in db.find(mango): 
            cont+=1
            dic = {}
            for detail in campos:
                dic[detail] = row[detail]                        
            retorno.append(dic)
        print(cont)
        return JsonResponse(
            {
                "quantidade": len(retorno),
                "retorno": retorno
            }
        )

