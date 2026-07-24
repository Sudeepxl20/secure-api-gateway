#!/bin/bash
echo "🧪 Testing Secure API Gateway..."

# Get token
TOKEN=$(curl -s -X POST http://localhost:8080/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password123"}' \
  | grep -o '"token":"[^"]*"' | cut -d'"' -f4)

if [ -z "$TOKEN" ]; then
    echo "❌ Failed to get token!"
    exit 1
fi

echo "✅ Got token: $TOKEN"
echo ""

echo "📡 Testing health endpoint..."
curl -s http://localhost:8080/actuator/health | python3 -m json.tool
echo ""

echo "📡 Testing scanner with normal request..."
curl -s -X POST http://localhost:8080/api/scan/analyze \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"data":"Hello World"}' \
  | python3 -m json.tool
echo ""

echo "📡 Testing scanner with SQL injection..."
curl -s -X POST http://localhost:8080/api/scan/analyze \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"data":"DROP TABLE users; --"}' \
  | python3 -m json.tool
echo ""

echo "✅ All tests complete!"
