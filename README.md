# 🔐 Secure API Gateway + Security Monitor

[![Java](https://img.shields.io/badge/Java-17-blue.svg)](https://adoptium.net/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.1.5-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![Podman](https://img.shields.io/badge/Podman-4.9.3-892CA0.svg)](https://podman.io/)

A production-ready microservices architecture with JWT authentication and a Python-based security scanner.

## 🏗️ Architecture

External Client (curl/Postman) -> Java Spring Boot API Gateway (Port: 8080) -> Python FastAPI Security Scanner (Port: 8000)

## 🚀 Quick Start

` + "```bash" + `
# Clone the repository
git clone https://github.com/Sudeepxl20/secure-api-gateway.git
cd secure-api-gateway

# Build and start containers
podman-compose up -d --build

# Check status
podman ps

# Run tests
./scripts/test-api.sh
` + "```" + `

## 🔐 API Endpoints

### 1. Get JWT Token
` + "```bash" + `
POST /api/auth/login
{
  "username": "admin",
  "password": "password123"
}
` + "```" + `

### 2. Scan for Vulnerabilities
` + "```bash" + `
POST /api/scan/analyze
Headers: Authorization: Bearer <token>
{
  "data": "your_data_here"
}
` + "```" + `

## 🧪 Testing

` + "```bash" + `
# Health check
curl http://localhost:8080/actuator/health

# Get token
curl -X POST http://localhost:8080/api/auth/login \\
  -H "Content-Type: application/json" \\
  -d '{"username":"admin","password":"password123"}'

# Test scanner
TOKEN="your_token_here"
curl -X POST http://localhost:8080/api/scan/analyze \\
  -H "Authorization: Bearer $TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{"data":"DROP TABLE users; --"}'
` + "```" + `

## 📁 Project Structure

secure-api-gateway/
├── api-gateway/          # Java Spring Boot
│   ├── src/main/java/    # Source code
│   └── Dockerfile
├── security-scanner/     # Python FastAPI
│   ├── app/              # Source code
│   └── Dockerfile
├── logs/                 # Application logs
├── scripts/              # Utility scripts
├── podman-compose.yml    # Container orchestration
└── README.md

## 🐳 Container Management

` + "```bash" + `
# Start services
podman-compose up -d

# View logs
podman-compose logs -f

# Stop services
podman-compose down

# Clean everything
./scripts/nuke.sh
` + "```" + `

## 🔒 Security Notes

- Change JWT secret in application.yml before production
- Use environment variables for sensitive data
- Enable HTTPS for production

## 🎯 Technologies Used

- Java 17 + Spring Boot 3.1.5
- Python 3.11 + FastAPI 0.104.1
- JWT for authentication
- Podman for containerization
- Podman-Compose for orchestration

## 📧 Contact

**Sudeep Krishna**
- GitHub: [@Sudeepxl20](https://github.com/Sudeepxl20)
- Email: sudeepkrishna2004@gmail.com

Project Link: [https://github.com/Sudeepxl20/secure-api-gateway](https://github.com/Sudeepxl20/secure-api-gateway)

---
Made with ❤️ for learning and portfolio
