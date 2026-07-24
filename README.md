# Secure API Gateway + Security Monitor

[![Java](https://img.shields.io/badge/Java-17-blue.svg)](https://adoptium.net/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.1.5-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![Podman](https://img.shields.io/badge/Podman-4.9.3-892CA0.svg)](https://podman.io/)

A production-ready microservices architecture with JWT authentication and a Python-based security scanner.

## Architecture

Java Spring Boot API Gateway (Port: 8080) -> Python FastAPI Security Scanner (Port: 8000)

Features:
- JWT Authentication
- SQL Injection Detection
- XSS Protection
- Path Traversal Detection
- Security Score (0-100)

## Quick Start

git clone https://github.com/Sudeepxl20/secure-api-gateway.git
cd secure-api-gateway
podman-compose up -d --build
podman ps
./scripts/test-api.sh

## API Endpoints

### Get JWT Token
POST /api/auth/login
{ "username": "admin", "password": "password123" }

### Scan for Vulnerabilities
POST /api/scan/analyze
Headers: Authorization: Bearer <token>
{ "data": "your_data_here" }

## Testing

curl http://localhost:8080/actuator/health

curl -X POST http://localhost:8080/api/auth/login -H "Content-Type: application/json" -d '{"username":"admin","password":"password123"}'

## Project Structure

secure-api-gateway/
├── api-gateway/          # Java Spring Boot
├── security-scanner/     # Python FastAPI
├── logs/                 # Application logs
├── scripts/              # Utility scripts
├── podman-compose.yml
└── README.md

## Container Management

podman-compose up -d      # Start
podman-compose logs -f    # View logs
podman-compose down       # Stop
./scripts/nuke.sh         # Clean

## Technologies

- Java 17 + Spring Boot 3.1.5
- Python 3.11 + FastAPI 0.104.1
- JWT Authentication
- Podman Containerization

## Contact

Sudeep Krishna
GitHub: @Sudeepxl20
Project: https://github.com/Sudeepxl20/secure-api-gateway
