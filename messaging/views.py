import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt   # <-- Add this decorator
def whatsapp_webhook(request):
    if request.method == "POST":
        sender = request.POST.get("from")
        incoming_message = request.POST.get("text")

        if sender and incoming_message:
            send_whatsapp_message(sender, f"Echo: {incoming_message}")
            return JsonResponse({"status": "message sent"})
        return JsonResponse({"error": "missing data"}, status=400)

    return JsonResponse({"error": "invalid request"}, status=400)


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
