from django.http import JsonResponse
# from apps.flights.utils.vda_parse import parse_ldm_text

def check_parse(request):
    text = request.POST.get('text')
    parsed_flights = parse_ldm_text(text)
    success = len(parsed_flights) > 0
    return JsonResponse({'success': success})