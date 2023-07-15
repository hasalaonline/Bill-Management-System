import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CEBSerializer, NWSDBSerializer
from app.models import CEB, NWSDB

@api_view(['GET'])
def home(request):
    return Response('Hello World!')

@api_view(['GET'])
def ceb_list(request):
    ceb = CEB.objects.all()
    serializer = CEBSerializer(ceb, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ceb_bill_data(request, pk):
    ceb = CEB.objects.get(username=pk)
    serializer = CEBSerializer(ceb, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def nwsdb_bill_data(request, pk):
    nwsdb = NWSDB.objects.get(username=pk)
    serializer = NWSDBSerializer(nwsdb, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ceb_create(request):
    data = request.data
    ceb = CEB.objects.create(
        username=data['username'],
        units=data['units'],
        dues_amount=data['dues_amount'],
        payments=data['payments']
    )
    serializer = CEBSerializer(ceb, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def update(request, pk):
    data = request.data
    if data['platform'] == 'CEB':
        ceb = CEB.objects.get(username=pk)
        ceb.amount[data['month']] = data['amount']
        ceb.units[data['month']] = data['units']
        ceb.save()
        return Response('Bill Updated')
    
    else:
        nwsdb = NWSDB.objects.get(username=pk)
        nwsdb.amount[data['month']] = data['amount']
        nwsdb.units[data['month']] = data['units']
        nwsdb.save()
        return Response('Bill Updated')
    
@api_view(['GET'])
def get_average(request, pk):
    ceb_bill_data = CEB.objects.get(username=pk)
    nwsdb_bill_data = NWSDB.objects.get(username=pk)

    ceb_amount = ceb_bill_data.amount
    nwsdb_amount = nwsdb_bill_data.amount
    ceb_units = ceb_bill_data.units
    nwsdb_units = nwsdb_bill_data.units

    for i in ceb_amount.values():
        i = float(i)
    for i in nwsdb_amount.values():
        i = float(i)

    for i in ceb_units.values():
        i = float(i)
    for i in nwsdb_units.values():
        i = float(i)

    ceb_avg = sum(float(value) for value in ceb_amount.values()) / len(ceb_amount.values())
    nwsdb_avg = sum(float(value) for value in nwsdb_amount.values()) / len(nwsdb_amount.values())
    ceb_units_avg = sum(float(value) for value in ceb_units.values()) / len(ceb_units.values())
    nwsdb_units_avg = sum(float(value) for value in nwsdb_units.values()) / len(nwsdb_units.values())

    ceb_avg = round(ceb_avg, 2)
    nwsdb_avg = round(nwsdb_avg, 2)
    ceb_units_avg = round(ceb_units_avg, 2)
    nwsdb_units_avg = round(nwsdb_units_avg, 2)

    response = { 'ceb_average': ceb_avg, 'nwsdb_average': nwsdb_avg, 'ceb_units_average': ceb_units_avg, 'nwsdb_units_average': nwsdb_units_avg, 'ceb_dues_amount': ceb_bill_data.dues_amount, 'nwsdb_dues_amount': nwsdb_bill_data.dues_amount }

    return Response(response)

