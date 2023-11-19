from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Domain

def index(request):
    message = ''
    if request.POST:
        
        name = request.POST.get('name')
        
        if name == 'test':
                
                return HttpResponse('test not allowed')
            
        else:
            number_client = Client.objects.count() + 1
            tenant = Client.objects.create(name=name, schema_name='tenant{}'.format(number_client))
            
            dom = "{}.{}".format(tenant.schema_name, request.get_host().split(':')[0])
            domain = Domain()
            domain.domain = dom
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()
            
            # messages success
            
            host = request.get_host()
            
            http_protocol = request.scheme
            
            connection_url = f'{http_protocol}://{tenant.schema_name}.{host}'
            
            message = f'Your connection url is: {connection_url}'
    
    return render(request, 'index.html', {'message': message})
    