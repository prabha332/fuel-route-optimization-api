# 🚗 Fuel Route Optimization API

A Django REST API that optimizes long-distance fuel stops based on cost and vehicle range constraints.



👉 Better:

### ✔ Keep consistent headings:

```md id="m4k8zn"
## 🔹 Overview

A production-style Django REST API that calculates an optimized driving route between two locations in the USA and recommends cost-efficient fuel stops based on vehicle range and dynamic fuel pricing.

The system is designed for long-distance logistics planning where the objective is to minimize total fuel cost while respecting range constraints.


## 💡 Problem Statement
Long-distance travel often results in inefficient fuel planning, leading to unnecessary cost increases.

This system solves:

- Optimal fuel stop selection  
- Range-constrained route segmentation  
- Fuel cost minimization across journey segments
  


### ✔ Better:

```md
## 🧠 System Design

### Core Logic Flow
Accept start and end coordinates
Compute total distance
Split route based on 500-mile constraint
Evaluate available fuel stations
Select lowest-cost valid stations
Return optimized stop sequence


## 🏗️ Architecture

Client  
⬇  
Django URL Router  
⬇  
Django API View (Controller Layer)  
⬇  
Service Layer (Business Logic)  
⬇  
Optimization Engine (Fuel Stop Algorithm)  
⬇  
Data Layer (Fuel Prices CSV)  
⬇  
Response (JSON API Output)


🛠️ Tech Stack

- Python 3
- Django / Django REST Framework
- CSV-based dataset (fuel prices)
- Geospatial calculations (Haversine formula)
- Modular service-based architecture

  
📁 Project Structure
fuel_route_clean/
│
├── api/
│   ├── services/
│   │   ├── fuel_optimizer.py   # Core optimization engine
│   │   ├── route_service.py    # Route computation logic
│   │
│   ├── views.py
│   ├── urls.py
│
├── fuel_data/
│   ├── fuel_prices.csv
│
├── manage.py


🚀 Installation & Setup
git clone https://github.com/your-username/fuel-route-optimization-api.git
cd fuel-route-optimization-api

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

## 📡 API Endpoint

### POST `/api/route/`

#### Request
```json
{
  "start": { "lat": 37.78, "lon": -122.42 },
  "end": { "lat": 25.76, "lon": -80.19 }
}

Response
{
  "total_distance_miles": 2591.23,
  "fuel_stops": [
    {
      "location": "Stop 1",
      "lat": 35.22,
      "lon": -90.11,
      "price": 3.45
    }
  ],
  "total_gallons_used": 259.12,
  "estimated_fuel_cost": 320.50,
  "message": "Optimized route generated successfully"
}


🗺️ Route Visualization 

The API returns coordinates that can be visualized using:

Google Maps API
Leaflet.js
Mapbox


🔍 Design Assumptions
Vehicle fuel efficiency is constant
Maximum range: 500 miles
Fuel stations loaded from static CSV
Distance approximated using geospatial formula


📊 Performance Consideration
Efficient greedy + constraint-based optimization
Lightweight CSV dataset for fast lookup
Modular service architecture for scalability


🧪 Testing Example
Use Postman or curl:
curl -X POST http://127.0.0.1:8000/api/route/ \
-H "Content-Type: application/json" \
-d '{"start":{"lat":37.78,"lon":-122.42},"end":{"lat":25.76,"lon":-80.19}}'


🎥 Demo Video



📈 Future Improvements
Google Maps API integration (real route data)
Live fuel price API integration
Graph-based shortest path optimization (Dijkstra / A*)
Frontend dashboard (React + Map UI)
Docker deployment + CI/CD pipeline


👨‍💻 Author
Prabhavati Agre



Future enhancement: direct map rendering via GeoJSON output.
