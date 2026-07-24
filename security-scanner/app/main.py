from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from datetime import datetime
from .models import ScanRequest, ScanResult
from .scanner import SecurityScanner

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[logging.FileHandler('/app/logs/scanner.log'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Security Scanner")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

scanner = SecurityScanner()

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/api/scan", response_model=ScanResult)
async def scan_request(scan_request: ScanRequest):
    logger.info(f"Scanning: {scan_request.method} {scan_request.endpoint}")
    return scanner.scan_request(scan_request)

@app.get("/api/scan/{request_id}")
async def get_scan(request_id: str):
    return scanner.scan_history.get(request_id, {"error": "Not found"})