from django.shortcuts import render, HttpResponse
from panel.models import Proceso, Evaluaciones
from django.db import connection

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (Métodos)
# MVT = Modelo Template Vista -> Acciones (Métodos)

layout = """
    <h1>Sitio web con Django | Gestión Municipal </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a> 
        </li>
        <li>
            <a href="/diagnostico">Diagnóstico de los 8 Pilares</a> 
        </li>                
        <li>
            <a href="/resumen">Resumen del Diagnóstico</a> 
        </li>                        
    </ul>
    <hr/>
"""

def hola_mundo(request):
    return HttpResponse(layout + "Hola mundo !!...")

def index(request):
    return render(request, 'index.html')

def diagnostico(request):
    return render(request, 'diagnostico.html')

def personas(request):

    if request.method == 'GET':

        var_unidad = request.GET['unidad']

        proceso = Proceso(
            unidad = var_unidad
        )
        objeto = proceso.save()

        print(proceso.pk) #ultimo id ingresado .

    else:
        return HttpResponse ("<h2>No se ha podido crear el proceso</h2>")

    return render(request, '1_personas.html', {'id_proceso': proceso.pk})
#    return HttpResponse (f"Proceso creado: {proceso.unidad}")

def cultura(request):

    if request.method == 'GET':

        var_idproceso = request.GET['id_proceso']
        e1 = request.GET['eva1.1']
        e2 = request.GET['eva1.2']
        e3 = request.GET['eva1.3']
        e4 = request.GET['eva1.4']
        e5 = request.GET['eva1.5']
        e6 = request.GET['eva1.6']
        e7 = request.GET['eva1.7']
        e8 = request.GET['eva1.8']
        e9 = request.GET['eva1.9']
        e10 = request.GET['eva1.10']
        
        evaluaciones = Evaluaciones(
            id_proceso = var_idproceso,
            nro_pilar = 1,
            p1 = e1,
            p2 = e2,
            p3 = e3,                       
            p4 = e4,
            p5 = e5,
            p6 = e6,
            p7 = e7,
            p8 = e8,
            p9 = e9,
            p10 = e10
        )
        objeto = evaluaciones.save()        

    else:
        return HttpResponse ("<h2>No se ha podido obtener el id del proceso</h2>")

    return render(request, '2_cultura.html', {'id_proceso': var_idproceso})

def liderazgo(request):

    if request.method == 'GET':

        var_idproceso = request.GET['id_proceso']
        e1 = request.GET['eva2.1']
        e2 = request.GET['eva2.2']
        e3 = request.GET['eva2.3']
        e4 = request.GET['eva2.4']
        e5 = request.GET['eva2.5']
        e6 = request.GET['eva2.6']
        e7 = request.GET['eva2.7']
        e8 = request.GET['eva2.8']
        e9 = request.GET['eva2.9']
        e10 = request.GET['eva2.10']
        
        evaluaciones = Evaluaciones(
            id_proceso = var_idproceso,
            nro_pilar = 2,
            p1 = e1,
            p2 = e2,
            p3 = e3,                       
            p4 = e4,
            p5 = e5,
            p6 = e6,
            p7 = e7,
            p8 = e8,
            p9 = e9,
            p10 = e10
        )
        objeto = evaluaciones.save()        

    else:
        return HttpResponse ("<h2>No se ha podido obtener el id del proceso</h2>")

    return render(request, '3_liderazgo.html', {'id_proceso': var_idproceso})

def estrategia(request):

    if request.method == 'GET':

        var_idproceso = request.GET['id_proceso']
        e1 = request.GET['eva3.1']
        e2 = request.GET['eva3.2']
        e3 = request.GET['eva3.3']
        e4 = request.GET['eva3.4']
        e5 = request.GET['eva3.5']
        e6 = request.GET['eva3.6']
        e7 = request.GET['eva3.7']
        e8 = request.GET['eva3.8']
        e9 = request.GET['eva3.9']
        e10 = request.GET['eva3.10']
        
        evaluaciones = Evaluaciones(
            id_proceso = var_idproceso,
            nro_pilar = 3,
            p1 = e1,
            p2 = e2,
            p3 = e3,                       
            p4 = e4,
            p5 = e5,
            p6 = e6,
            p7 = e7,
            p8 = e8,
            p9 = e9,
            p10 = e10
        )
        objeto = evaluaciones.save()        

    else:
        return HttpResponse ("<h2>No se ha podido obtener el id del proceso</h2>")

    return render(request, '4_estrategia.html', {'id_proceso': var_idproceso})

def estructura(request):

    if request.method == 'GET':

        var_idproceso = request.GET['id_proceso']
        e1 = request.GET['eva4.1']
        e2 = request.GET['eva4.2']
        e3 = request.GET['eva4.3']
        e4 = request.GET['eva4.4']
        e5 = request.GET['eva4.5']
        e6 = request.GET['eva4.6']
        e7 = request.GET['eva4.7']
        e8 = request.GET['eva4.8']
        e9 = request.GET['eva4.9']
        e10 = request.GET['eva4.10']
        
        evaluaciones = Evaluaciones(
            id_proceso = var_idproceso,
            nro_pilar = 4,
            p1 = e1,
            p2 = e2,
            p3 = e3,                       
            p4 = e4,
            p5 = e5,
            p6 = e6,
            p7 = e7,
            p8 = e8,
            p9 = e9,
            p10 = e10
        )
        objeto = evaluaciones.save()        

    else:
        return HttpResponse ("<h2>No se ha podido obtener el id del proceso</h2>")

    return render(request, '5_estructura.html', {'id_proceso': var_idproceso})

def operaciones(request):

    if request.method == 'GET':

        var_idproceso = request.GET['id_proceso']
        e1 = request.GET['eva5.1']
        e2 = request.GET['eva5.2']
        e3 = request.GET['eva5.3']
        e4 = request.GET['eva5.4']
        e5 = request.GET['eva5.5']
        e6 = request.GET['eva5.6']
        e7 = request.GET['eva5.7']
        e8 = request.GET['eva5.8']
        e9 = request.GET['eva5.9']
        e10 = request.GET['eva5.10']
        
        evaluaciones = Evaluaciones(
            id_proceso = var_idproceso,
            nro_pilar = 5,
            p1 = e1,
            p2 = e2,
            p3 = e3,                       
            p4 = e4,
            p5 = e5,
            p6 = e6,
            p7 = e7,
            p8 = e8,
            p9 = e9,
            p10 = e10
        )
        objeto = evaluaciones.save()        

    else:
        return HttpResponse ("<h2>No se ha podido obtener el id del proceso</h2>")

    return render(request, '6_operaciones.html', {'id_proceso': var_idproceso})

def creatividad(request):

    if request.method == 'GET':

        var_idproceso = request.GET['id_proceso']
        e1 = request.GET['eva6.1']
        e2 = request.GET['eva6.2']
        e3 = request.GET['eva6.3']
        e4 = request.GET['eva6.4']
        e5 = request.GET['eva6.5']
        e6 = request.GET['eva6.6']
        e7 = request.GET['eva6.7']
        e8 = request.GET['eva6.8']
        e9 = request.GET['eva6.9']
        e10 = request.GET['eva6.10']
        
        evaluaciones = Evaluaciones(
            id_proceso = var_idproceso,
            nro_pilar = 6,
            p1 = e1,
            p2 = e2,
            p3 = e3,                       
            p4 = e4,
            p5 = e5,
            p6 = e6,
            p7 = e7,
            p8 = e8,
            p9 = e9,
            p10 = e10
        )
        objeto = evaluaciones.save()        

    else:
        return HttpResponse ("<h2>No se ha podido obtener el id del proceso</h2>")

    return render(request, '7_creatividad.html', {'id_proceso': var_idproceso})

def tecnologia(request):

    if request.method == 'GET':

        var_idproceso = request.GET['id_proceso']
        e1 = request.GET['eva7.1']
        e2 = request.GET['eva7.2']
        e3 = request.GET['eva7.3']
        e4 = request.GET['eva7.4']
        e5 = request.GET['eva7.5']
        e6 = request.GET['eva7.6']
        e7 = request.GET['eva7.7']
        e8 = request.GET['eva7.8']
        e9 = request.GET['eva7.9']
        e10 = request.GET['eva7.10']
        
        evaluaciones = Evaluaciones(
            id_proceso = var_idproceso,
            nro_pilar = 7,
            p1 = e1,
            p2 = e2,
            p3 = e3,                       
            p4 = e4,
            p5 = e5,
            p6 = e6,
            p7 = e7,
            p8 = e8,
            p9 = e9,
            p10 = e10
        )
        objeto = evaluaciones.save()        

    else:
        return HttpResponse ("<h2>No se ha podido obtener el id del proceso</h2>")

    return render(request, '8_tecnologia.html', {'id_proceso': var_idproceso})

def dashboard(request):

    if request.method == 'GET':

        var_idproceso = request.GET['id_proceso']
        e1 = request.GET['eva8.1']
        e2 = request.GET['eva8.2']
        e3 = request.GET['eva8.3']
        e4 = request.GET['eva8.4']
        e5 = request.GET['eva8.5']
        e6 = request.GET['eva8.6']
        e7 = request.GET['eva8.7']
        e8 = request.GET['eva8.8']
        e9 = request.GET['eva8.9']
        e10 = request.GET['eva8.10']
        
        evaluaciones = Evaluaciones(
            id_proceso = var_idproceso,
            nro_pilar = 8,
            p1 = e1,
            p2 = e2,
            p3 = e3,                       
            p4 = e4,
            p5 = e5,
            p6 = e6,
            p7 = e7,
            p8 = e8,
            p9 = e9,
            p10 = e10
        )
        objeto = evaluaciones.save()

        resultados = Evaluaciones.objects.raw("select * from panel_evaluaciones")

        result_tot = []

        cursor = connection.cursor()
        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where id_proceso = ''' + str(var_idproceso) + ''' and nro_pilar = 1 group by nro_pilar''')
        result_p1 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where id_proceso = ''' + str(var_idproceso) + ''' and nro_pilar = 2 group by nro_pilar''')
        result_p2 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where id_proceso = ''' + str(var_idproceso) + ''' and nro_pilar = 3 group by nro_pilar''')
        result_p3 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where id_proceso = ''' + str(var_idproceso) + ''' and nro_pilar = 4 group by nro_pilar''')
        result_p4 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where id_proceso = ''' + str(var_idproceso) + ''' and nro_pilar = 5 group by nro_pilar''')
        result_p5 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where id_proceso = ''' + str(var_idproceso) + ''' and nro_pilar = 6 group by nro_pilar''')
        result_p6 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where id_proceso = ''' + str(var_idproceso) + ''' and nro_pilar = 7 group by nro_pilar''')
        result_p7 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where id_proceso = ''' + str(var_idproceso) + ''' and nro_pilar = 8 group by nro_pilar''')
        result_p8 = cursor.fetchone()

        promedio_p1 = result_p1[0] / result_p1[1]
        promedio_p2 = result_p2[0] / result_p2[1]
        promedio_p3 = result_p3[0] / result_p3[1]
        promedio_p4 = result_p4[0] / result_p4[1]
        promedio_p5 = result_p5[0] / result_p5[1]
        promedio_p6 = result_p6[0] / result_p6[1]
        promedio_p7 = result_p7[0] / result_p7[1]
        promedio_p8 = result_p8[0] / result_p8[1]

        result_tot.append(promedio_p1)
        result_tot.append(promedio_p2)
        result_tot.append(promedio_p3)
        result_tot.append(promedio_p4)
        result_tot.append(promedio_p5)
        result_tot.append(promedio_p6)
        result_tot.append(promedio_p7)
        result_tot.append(promedio_p8)

        print(promedio_p1, promedio_p2, promedio_p3, promedio_p4, promedio_p5, promedio_p6, promedio_p7, promedio_p8)
        print('++++++  id_proceso: ' + str(var_idproceso) + '++++++++++++++++++++')
        print(result_tot)

    else:
        return HttpResponse("<h2>No se ha podido finalizar el Diagnóstico</h2>")

    return render(request, 'dashboard.html', {'id_proceso':var_idproceso, 'resultados':resultados, 'p1':result_p1[0], 'p2':result_p2[0], 'p3':result_p3[0], 'p4':result_p4[0], 'p5':result_p5[0], 'p6':result_p6[0], 'p7':result_p7[0], 'p8':result_p8[0]})

def resumen(request):

    if request.method == 'GET':
        resultados = Evaluaciones.objects.raw("select * from panel_evaluaciones")

        result_tot = []

        cursor = connection.cursor()
        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where nro_pilar = 1 group by nro_pilar''')
        result_p1 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where nro_pilar = 2 group by nro_pilar''')
        result_p2 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where nro_pilar = 3 group by nro_pilar''')
        result_p3 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where nro_pilar = 4 group by nro_pilar''')
        result_p4 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where nro_pilar = 5 group by nro_pilar''')
        result_p5 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where nro_pilar = 6 group by nro_pilar''')
        result_p6 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where nro_pilar = 7 group by nro_pilar''')
        result_p7 = cursor.fetchone()

        cursor.execute('''select sum(p1+p2+p3+p4+p5+p6+p7+p8+p9+p10) as suma, count(1)*10 as total  
                            from panel_evaluaciones where nro_pilar = 8 group by nro_pilar''')
        result_p8 = cursor.fetchone()

        promedio_p1 = result_p1[0] / result_p1[1]
        promedio_p2 = result_p2[0] / result_p2[1]
        promedio_p3 = result_p3[0] / result_p3[1]
        promedio_p4 = result_p4[0] / result_p4[1]
        promedio_p5 = result_p5[0] / result_p5[1]
        promedio_p6 = result_p6[0] / result_p6[1]
        promedio_p7 = result_p7[0] / result_p7[1]
        promedio_p8 = result_p8[0] / result_p8[1]

        result_tot.append(promedio_p1)
        result_tot.append(promedio_p2)
        result_tot.append(promedio_p3)
        result_tot.append(promedio_p4)
        result_tot.append(promedio_p5)
        result_tot.append(promedio_p6)
        result_tot.append(promedio_p7)
        result_tot.append(promedio_p8)

        print(promedio_p1, promedio_p2, promedio_p3, promedio_p4, promedio_p5, promedio_p6, promedio_p7, promedio_p8)
        print('***********************')
        print(result_tot)

    else:
        return HttpResponse("<h2>No se ha generar el resumen del Diagnóstico</h2>")

    return render(request, 'dashboard_resumen.html', {'resultados':resultados, 'p1':result_p1[0], 'p2':result_p2[0], 'p3':result_p3[0], 'p4':result_p4[0], 'p5':result_p5[0], 'p6':result_p6[0], 'p7':result_p7[0], 'p8':result_p8[0]})
