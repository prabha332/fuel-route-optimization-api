from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .services.fuel_optimizer import optimize_fuel_route


@csrf_exempt
def optimize_route(request):

    if request.method == "GET":
        return JsonResponse({
            "message": "Use POST method with JSON body: {start, end}"
        })

    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        data = json.loads(request.body)

        start = data.get("start")
        end = data.get("end")

        if not start or not end:
            return JsonResponse({"error": "Start and End required"}, status=400)

        result = optimize_fuel_route(start, end)

        map_url = f"https://www.google.com/maps/dir/{start['lat']},{start['lon']}/{end['lat']},{end['lon']}"

        return JsonResponse({
            "start": start,
            "end": end,
            "total_distance_miles": result["total_distance"],
            "fuel_stops": result["fuel_stops"],
            "total_gallons_used": result["total_gallons"],
            "estimated_fuel_cost": result["total_cost"],
            "map_url": map_url,
            "message": "✅ Route optimized successfully"
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)