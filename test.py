import requests

BASE_URL = "http://127.0.0.1:5000"

def test_api(endpoint):
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url)
        result = response.json()
        # Kiểm tra key có đầy đủ không
        assert "success" in result, "'success' key missing"
        assert "message" in result, "'message' key missing"
        assert "data" in result, "'data' key missing"
        print(f"[OK] {endpoint} -> {result['success']}, message: {result['message']}")
    except Exception as e:
        print(f"[ERROR] {endpoint} -> {e}")

# Test tất cả endpoint chính
endpoints = [
    "/universities",
    "/majors",
    "/exam_groups",
    "/admission_scores"
]

for ep in endpoints:
    test_api(ep)
