# 🚗 Fuel Route Optimization API

> 🚀 **Live Demo:** [Watch on Loom](https://www.loom.com/share/31bd14797106446e8d044c82bd038a29) | Built with **Django REST Framework + Python**

A production-style Django REST API that calculates an optimized driving route between two locations in the USA and recommends cost-efficient fuel stops based on vehicle range and dynamic fuel pricing.

The system is designed for long-distance logistics planning where the objective is to **minimize total fuel cost** while respecting range constraints.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [System Design](#-system-design)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [API Endpoint](#-api-endpoint)
- [Route Visualization](#-route-visualization)
- [Design Assumptions](#-design-assumptions)
- [Performance Considerations](#-performance-considerations)
- [Testing Example](#-testing-example)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🔹 Overview

A production-style Django REST API that calculates an optimized driving route between two locations in the USA and recommends cost-efficient fuel stops based on vehicle range and dynamic fuel pricing.

The system is designed for long-distance logistics planning where the objective is to **minimize total fuel cost** while respecting range constraints.

---

## 💡 Problem Statement

Long-distance travel often results in inefficient fuel planning, leading to unnecessary cost increases.

**This system solves:**
- ✅ Optimal fuel stop selection
- ✅ Range-constrained route segmentation
- ✅ Fuel cost minimization across journey segments

---

## 🧠 System Design

### Core Logic Flow

```
1. Accept start and end coordinates
2. Compute total distance
3. Split route based on 500-mile range constraint
4. Evaluate available fuel stations at each segment
5. Select lowest-cost valid stations
6. Return optimized stop sequence
```

---

## 🏗️ Architecture

```
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
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| Django | Web framework |
| Django REST Framework | API layer |
| CSV Dataset | Fuel prices data source |
| Haversine Formula | Geospatial distance calculation |
| Modular Service Architecture | Separation of concerns |

---

## 📁 Project Structure

```
fuel_route_clean/
│
├── api/
│   ├── services/
│   │   ├── fuel_optimizer.py      # Core optimization engine
│   │   ├── route_service.py       # Route computation logic
│   │
│   ├── views.py                   # API controller
│   ├── urls.py                    # URL routing
│
├── fuel_data/
│   ├── fuel_prices.csv            # Static fuel pricing dataset
│
├── manage.py                      # Django entry point
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/prabha332/fuel-route-optimization-api.git
cd fuel-route-optimization-api

# 2. Create a virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac / Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Start the server
python manage.py runserver
```

The API will be running at: `http://127.0.0.1:8000/`

---

## 📡 API Endpoint

### `POST /api/route/`

Calculates the optimized fuel stop route between two coordinates.

#### Request Body

```json
{
  "start": { "lat": 37.78, "lon": -122.42 },
  "end":   { "lat": 25.76, "lon": -80.19  }
}
```

#### Response

```json
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
```

#### Response Fields

| Field | Type | Description |
|---|---|---|
| `total_distance_miles` | float | Total route distance in miles |
| `fuel_stops` | array | List of optimized fuel stop locations |
| `total_gallons_used` | float | Estimated total fuel consumed |
| `estimated_fuel_cost` | float | Total estimated cost in USD |
| `message` | string | Status message |

---

## 🗺️ Route Visualization

The API returns coordinates that can be visualized using:

- 🌍 [Google Maps API](https://developers.google.com/maps)
- 🗺️ [Leaflet.js](https://leafletjs.com/)
- 📍 [Mapbox](https://www.mapbox.com/)

> Future enhancement: direct map rendering via GeoJSON output.

---

## 🔍 Design Assumptions

| Assumption | Value |
|---|---|
| Vehicle fuel efficiency | Constant (10 MPG) |
| Maximum range per tank | 500 miles |
| Fuel station data source | Static CSV file |
| Distance calculation | Haversine geospatial formula |
| Route type | Straight-line approximation |

---

## 📊 Performance Considerations

- ⚡ **Greedy + constraint-based optimization** for fast computation
- 📄 **Lightweight CSV dataset** for quick data lookup
- 🧩 **Modular service architecture** for easy scalability and testing
- 🔄 Stateless API design — each request is independently processed

---

## 🧪 Testing Example

### Using curl

```bash
curl -X POST http://127.0.0.1:8000/api/route/ \
  -H "Content-Type: application/json" \
  -d '{"start": {"lat": 37.78, "lon": -122.42}, "end": {"lat": 25.76, "lon": -80.19}}'
```

### Using Postman

1. Set method to `POST`
2. URL: `http://127.0.0.1:8000/api/route/`
3. Body → raw → JSON
4. Paste the request body and hit **Send**

---

## 🎥 Demo Video

▶️ [Watch the full demo on Loom](https://www.loom.com/share/31bd14797106446e8d044c82bd038a29)

---

## 📈 Future Improvements

- [ ] Google Maps API integration for real road route data
- [ ] Live fuel price API integration (e.g., GasBuddy API)
- [ ] Graph-based shortest path optimization (Dijkstra / A*)
- [ ] Frontend dashboard with React + interactive Map UI
- [ ] Docker deployment + CI/CD pipeline
- [ ] GeoJSON output for direct map rendering
- [ ] Unit & integration test coverage

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Prabhavati Agre**

- 🐙 GitHub: [@prabha332](https://github.com/prabha332)

---

⭐ *If you found this project useful, please consider giving it a star on GitHub!*
