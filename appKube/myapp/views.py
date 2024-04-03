from django.shortcuts import render
from rest_framework.response import Response

from django.http import JsonResponse
from kubernetes import client, config
"""
def pod_info(request):
    # Configura la conexión con el clúster de Kubernetes
    config.load_incluster_config()
    v1 = client.CoreV1Api()

    # Obtiene el nombre del pod actual
    pod_name = client.utils.get_pod_name()
    # Obtiene la información del pod
    pod = v1.read_namespaced_pod(name=pod_name, namespace="default")
    # Obtiene la dirección IP del pod
    pod_ip = pod.status.pod_ip

    # Crea un diccionario con la información del pod
    pod_info = {"name": pod_name, "ip": pod_ip}

    # Devuelve la información del pod como respuesta en formato JSON
    return JsonResponse(pod_info)
"""

import socket
from django.http import JsonResponse
from rest_framework import status
import os
import socket
from django.http import JsonResponse

def pod_info(request):
    try:
        # Configura la conexión con el clúster de Kubernetes
        config.load_incluster_config()
        v1 = client.CoreV1Api()

        # Obtiene el nombre del pod actual
        pod_name = os.environ.get("POD_NAME")
        # Obtiene la información del pod
        pod = v1.read_namespaced_pod(name=pod_name, namespace="default")
        # Obtiene la dirección IP del pod
        pod_ip = pod.status.pod_ip

        # Crea un diccionario con la información del pod
        pod_info = {"name": pod_name, "ip": pod_ip}

        # Devuelve la información del pod como respuesta en formato JSON
        return JsonResponse(pod_info)
    except:
        try:
            # Si no puede obtener información del pod de Kubernetes, obtiene la información del servidor local
            server_name = socket.gethostname()
            server_ip = socket.gethostbyname(server_name)
            server_info = {"name": server_name, "ip": server_ip}
            return JsonResponse(server_info)
        except:
            # Si no puede obtener la información del servidor local, devuelve una respuesta de fallback
            fallback_response = {"response": "funciona"}
            return JsonResponse(fallback_response)


