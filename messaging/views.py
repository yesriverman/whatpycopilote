import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

VERIFY_TOKEN = "soufiane_token"

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == "GET":
        # Verification handshake
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge)
        return HttpResponse("Verification failed", status=403)

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            # Navigate into payload
            entry = data.get("entry", [])[0]
            changes = entry.get("changes", [])[0]
            value = changes.get("value", {})
            messages = value.get("messages", [])

            if messages:
                msg = messages[0]
                sender = msg.get("from")
                text = msg.get("text", {}).get("body")

                if sender and text:
                    # Echo back the message
                    send_whatsapp_message(sender, f"Echo: {text}")
                    return JsonResponse({"status": "message sent"})

            return JsonResponse({"error": "no messages"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "invalid request"}, status=400)

# VERIFY_TOKEN = "soufiane_token"  # must match the token you set in Meta dashboard

# @csrf_exempt
# def whatsapp_webhook(request):
#     if request.method == "GET":
#         mode = request.GET.get("hub.mode")
#         token = request.GET.get("hub.verify_token")
#         challenge = request.GET.get("hub.challenge")

#         if mode == "subscribe" and token == VERIFY_TOKEN:
#             return HttpResponse(challenge)
#         return HttpResponse("Verification failed", status=403)

#     if request.method == "POST":
#         sender = None
#         incoming_message = None

#         # Try form data
#         sender = request.POST.get("from")
#         incoming_message = request.POST.get("text")

#         # Try JSON body if form data is empty
#         if not sender or not incoming_message:
#             try:
#                 data = json.loads(request.body.decode("utf-8"))
#                 sender = data.get("from")
#                 incoming_message = data.get("text")
#             except Exception:
#                 pass

#         if sender and incoming_message:
#             send_whatsapp_message(sender, f"Echo: {incoming_message}")
#             return JsonResponse({"status": "message sent"})
#         return JsonResponse({"error": "missing data"}, status=400)

#     return JsonResponse({"error": "invalid request"}, status=400)

# @csrf_exempt
# def whatsapp_webhook(request):
#     if request.method == "POST":
#         sender = None
#         incoming_message = None

#         # Try form data first
#         sender = request.POST.get("from")
#         incoming_message = request.POST.get("text")

#         # If empty, try JSON body
#         if not sender or not incoming_message:
#             try:
#                 data = json.loads(request.body.decode("utf-8"))
#                 sender = data.get("from")
#                 incoming_message = data.get("text")
#             except Exception:
#                 pass

#         if sender and incoming_message:
#             send_whatsapp_message(sender, f"Echo: {incoming_message}")
#             return JsonResponse({"status": "message sent"})
#         return JsonResponse({"error": "missing data"}, status=400)

#     return JsonResponse({"error": "invalid request"}, status=400)

# def whatsapp_webhook(request):
#     if request.method == "POST":
#         sender = request.POST.get("from")
#         incoming_message = request.POST.get("text")

#         if sender and incoming_message:
#             send_whatsapp_message(sender, f"Echo: {incoming_message}")
#             return JsonResponse({"status": "message sent"})
#         return JsonResponse({"error": "missing data"}, status=400)

#     return JsonResponse({"error": "invalid request"}, status=400)


def send_whatsapp_message(to, message):
    url = f"https://graph.facebook.com/v17.0/{settings.WHATSAPP_PHONE_ID}/messages"
    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()



# Create your views here.
# from django.http import JsonResponse

# def whatsapp_webhook(request):
#     if request.method == "POST":
#         # Later: handle incoming WhatsApp messages here
#         return JsonResponse({"status": "message received"})
#     return JsonResponse({"error": "invalid request"}, status=400)

# import requests
# from django.conf import settings
# from django.http import JsonResponse

# def send_whatsapp_message(to, message):
#     url = f"https://graph.facebook.com/v17.0/{settings.WHATSAPP_PHONE_ID}/messages"
#     headers = {
#         "Authorization": f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "messaging_product": "whatsapp",
#         "to": to,
#         "type": "text",
#         "text": {"body": message}
#     }
#     response = requests.post(url, headers=headers, json=data)
#     return response.json()

# def whatsapp_webhook(request):
#     if request.method == "POST":
#         # Example: send a reply back to the sender
#         sender = request.POST.get("from")
#         incoming_message = request.POST.get("text")

#         if sender and incoming_message:
#             send_whatsapp_message(sender, f"Echo: {incoming_message}")
#             return JsonResponse({"status": "message sent"})
#         return JsonResponse({"error": "missing data"}, status=400)

#     return JsonResponse({"error": "invalid request"}, status=400)
