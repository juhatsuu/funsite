from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import math

def index(request):
    return render(request, 'main/index.html')

@ensure_csrf_cookie
def process_function(request):
    print(request)
    if request.method == 'POST':

        function = request.POST.get('function')


        def func(x, function):
            return eval(function)

        xmin = -100.0
        xmax = 100.0
        count = 200
        lol = np.linspace(xmin, xmax, count)
        ylist = [func(x, function) for x in lol]
        plt.plot(lol, ylist)
        fig = plt.gcf()
        buf = BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        data = base64.b64encode(buf.read())
        plt.show()
        plt.close()
        context = {'image': data.decode('utf8')}

        return render(request, 'index.html', context)
    else:
        return HttpResponse('Неверный метод запроса')
