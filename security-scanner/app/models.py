from pydantic import BaseModel, Field
from typing import Optional, Dict

class ScanRequest(BaseModel):
    endpoint: str
    method: str
    headers: Dict[str, str] = Field(default_factory=dict)
    body: Optional[str] = None

class ScanResult(BaseModel):
    request_id: str
    security_score: int
    risk_level: str
    message: str
    timestamp: int
    details: Optional[Dict] = Field(default_factory=dict)