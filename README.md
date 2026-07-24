# 🔐 Secure API Gateway + Security Monitor

[![Java](https://img.shields.io/badge/Java-17-blue.svg)](https://adoptium.net/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.1.5-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![Podman](https://img.shields.io/badge/Podman-4.9.3-892CA0.svg)](https://podman.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **production-ready microservices architecture** showcasing a secure API Gateway with JWT authentication and a Python-based security scanner. Built with Java Spring Boot and Python FastAPI, fully containerized with Podman.

## 🏗️ Architecture

┌─────────────────────────────────────────────────────────────┐
│ External Clients │
│ (curl, Postman, browser) │
└─────────────────────┬───────────────────────────────────────┘
│ HTTPS/HTTP
▼
┌─────────────────────────────────────────────────────────────┐
│ Java Spring Boot API Gateway │
│ (Port: 8080) │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ - JWT Authentication │ │
│ │ - Request/Response Logging │ │
│ │ - Route requests to scanner │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
│ REST API
▼
┌─────────────────────────────────────────────────────────────┐
│ Python FastAPI Security Scanner │
│ (Port: 8000) │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ - Analyze request headers/patterns │ │
│ │ - Detect SQL injection, XSS, path traversal │ │
│ │ - Return security score (0-100) │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
│
▼
┌───────────────┐
│ Log Files │
│ (on host) │
└───────────────┘

## 🚀 Technologies Used

### Backend
- **Java 17** + **Spring Boot 3.1.5** - Main API Gateway
- **Python 3.11** + **FastAPI 0.104.1** - Security Scanner
- **JWT (JSON Web Tokens)** - Authentication
- **Maven** - Java dependency management

### Containerization
- **Podman** / **Docker** - Container runtime
- **Podman-Compose** - Multi-container orchestration

### Security Features
- JWT-based authentication
- SQL injection detection
- XSS protection scanning
- Path traversal detection
- Security header validation
- Request/response logging

## 📦 Quick Start

### Prerequisites

```bash
# Install Podman
sudo apt install podman podman-compose
# Clone the repository
git clone https://github.com/Sudeepxl20/secure-api-gateway.git
cd secure-api-gateway

# Build containers
podman-compose build

# Start services
podman-compose up -d

# Check status
podman ps

# Run tests
./scripts/test-api.sh
# Login - Get JWT Token
POST /api/auth/login
{
  "username": "admin",
  "password": "password123"
}

# Response
{
  "token": "eyJhbGciOiJIUzI1NiJ9...",
  "username": "admin",
  "message": "Login successful"
}
# Analyze request for security vulnerabilities
POST /api/scan/analyze
Headers: Authorization: Bearer <token>
{
  "data": "your_data_here"
}

# Response
{
  "requestId": "abc123",
  "securityScore": 75,
  "riskLevel": "MEDIUM",
  "message": "Security score: 75/100",
  "timestamp": 1234567890
}
# Health check
curl http://localhost:8080/actuator/health

# Get JWT token
curl -X POST http://localhost:8080/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password123"}'

# Test scanner with token
TOKEN="your_token_here"
curl -X POST http://localhost:8080/api/scan/analyze \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"data":"DROP TABLE users; --"}'
# Run all tests
./scripts/test-api.sh
# Run all tests
./scripts/test-api.sh
secure-api-gateway/
├── api-gateway/          # Java Spring Boot application
│   ├── src/
│   │   └── main/
│   │       ├── java/com/example/gateway/
│   │       │   ├── config/      # Security & JWT config
│   │       │   ├── controller/  # REST endpoints
│   │       │   ├── filter/      # JWT filter
│   │       │   ├── model/       # Data models
│   │       │   └── service/     # Business logic
│   │       └── resources/
│   │           └── application.yml
│   ├── Dockerfile
│   └── pom.xml
├── security-scanner/     # Python FastAPI application
│   ├── app/
│   │   ├── main.py       # FastAPI app
│   │   ├── scanner.py    # Security detection logic
│   │   └── models.py     # Pydantic models
│   ├── Dockerfile
│   └── requirements.txt
├── logs/                 # Application logs
├── scripts/              # Utility scripts
│   ├── manage.sh        # Main management script
│   ├── test-api.sh      # Test script
│   └── nuke.sh          # Complete cleanup
├── podman-compose.yml    # Container orchestration
└── README.md            # This file
podman-compose up -d
podman-compose logs -f
podman-compose down
./scripts/nuke.sh
📝 Logging
All logs are stored in the logs/ directory:

gateway.log - API Gateway request/response logs

scanner.log - Security scanner activity logs


🔒 Security Notes
Change the JWT secret in application.yml before production

Use environment variables for sensitive data in production

Enable HTTPS for production deployments

Use strong passwords instead of password123
🤝 Contributing
Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request


📄 License
This project is licensed under the MIT License - see the LICENSE file for details.


🎯 Key Features Demonstrated
✅ Microservices architecture

✅ JWT authentication and authorization

✅ Inter-service communication (Java ↔ Python)

✅ Containerization with Podman/Docker

✅ Security vulnerability detection

✅ Centralized logging

✅ RESTful API design

✅ Linux CLI management

📧 Contact
Sudeep Krishna

GitHub: @Sudeepxl20

Email: sudeepkrishna2004@gmail.com

Project Link: https://github.com/Sudeepxl20/secure-api-gateway
Made with ❤️ for learning and portfolio
