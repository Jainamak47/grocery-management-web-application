from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Product, Order, OrderDetail, Customer, UOM

@require_http_methods(["GET"])
def get_uom(request):
    uoms = UOM.objects.values('uom_id', 'uom_name')
    return JsonResponse(list(uoms), safe=False)

@require_http_methods(["GET"])
def get_products(request):
    products = Product.objects.select_related('uom').all()
    result = [{
        'product_id': p.product_id,
        'name': p.name,
        'uom_id': p.uom_id,
        'price_per_unit': float(p.price_per_unit),
        'uom_name': p.uom.uom_name
    } for p in products]
    return JsonResponse(result, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def insert_product(request):
    if request.POST.get('data'):
        data = json.loads(request.POST.get('data'))
    else:
        data = json.loads(request.body)
    
    product = Product.objects.create(
        name=data['product_name'],
        uom_id=data['uom_id'],
        price_per_unit=data['price_per_unit']
    )
    return JsonResponse({"product_id": product.product_id})

@csrf_exempt
@require_http_methods(["POST"])
def delete_product(request):
    if request.POST.get('product_id'):
        product_id = request.POST.get('product_id')
    else:
        data = json.loads(request.body)
        product_id = data['product_id']
    
    Product.objects.filter(product_id=product_id).delete()
    return JsonResponse({"status": "success"})

@require_http_methods(["GET"])
def get_all_orders(request):
    orders = Order.objects.select_related('customer').values(
        'order_id', 'total', 'datetime', 
        'customer__name', 'customer__phone'
    ).order_by('-order_id')
    
    result = [{
        'order_id': o['order_id'],
        'total': float(o['total']),
        'datetime': o['datetime'].strftime('%Y-%m-%d %H:%M:%S'),
        'customer_name': o['customer__name'],
        'customer_phone': o['customer__phone']
    } for o in orders]
    
    return JsonResponse(result, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def insert_order(request):
    if request.POST.get('data'):
        data = json.loads(request.POST.get('data'))
    else:
        data = json.loads(request.body)
    
    customer, _ = Customer.objects.get_or_create(
        name=data['customer_name'],
        phone=data['customer_phone']
    )
    
    order = Order.objects.create(
        customer=customer,
        total=data['grand_total']
    )
    
    for item in data['order_details']:
        OrderDetail.objects.create(
            order=order,
            product_id=item['product_id'],
            quantity=item['quantity']
        )
    
    return JsonResponse({"order_id": order.order_id})
