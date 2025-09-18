from django.http import HttpResponse
from django.shortcuts import render

from .models import Client, Order

def get_client_orders(client_id: int):
    client = Client.objects.get(pk=client_id)
    orders = Order.objects.filter(client=client).select_related("delivery_type")

    return {
        "Client.name": client.name,
        "Order": [
            {
                "delivery_type": order.delivery_type.delivery_type if order.delivery_type else None,
                "name": order.name,
            }
            for order in orders
        ]
    }

# Create your views here.
def index(request):
    return render(request, 'CustomerStats/index.html', {
        'clients': Client.objects.all()
    })

def user_stats(request, client_id):
    return render(request, 'CustomerStats/stats.html', {
        'client_name': Client.objects.get(pk=client_id).name,
        'orders': Order.objects.filter(client_id=client_id).order_by('-time')
    })
