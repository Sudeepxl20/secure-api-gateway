import re
import uuid
import time
from typing import Dict, List
from .models import ScanRequest, ScanResult

class SecurityScanner:
    """
    Security scanner that analyzes HTTP requests for potential vulnerabilities.
    Detects SQL injection, XSS, path traversal, and other security issues.
    """
    
    def __init__(self):
        self.scan_history = {}
        self.vulnerability_patterns = {
            'sql_injection': {
                'patterns': [r"('|\").*('|\")", r"\b(OR|AND)\s+\d+=\d+", r";\s*DROP\s+TABLE"],
                'weight': 20
            },
            'xss': {
                'patterns': [r"<script>", r"javascript:", r"onerror=", r"alert\("],
                'weight': 15
            },
            'path_traversal': {
                'patterns': [r"\.\./", r"\.\.\\", r"/etc/passwd"],
                'weight': 15
            },
            'command_injection': {
                'patterns': [r";\s*\w+", r"\|\s*\w+", r"&\s*\w+"],
                'weight': 25
            }
        }
        self.sensitive_keywords = ['password', 'secret', 'key', 'token', 'auth']

    def scan_request(self, scan_request: ScanRequest) -> ScanResult:
        """Scan an HTTP request for security vulnerabilities."""
        request_id = str(uuid.uuid4())[:8]
        timestamp = int(time.time() * 1000)
        
        vulnerabilities = []
        total_weight = 0
        
        # Check endpoint for suspicious patterns
        endpoint_vulns = self._analyze_string(scan_request.endpoint, 'endpoint')
        vulnerabilities.extend(endpoint_vulns)
        total_weight += sum(v['weight'] for v in endpoint_vulns)
        
        # Check headers for sensitive information
        header_vulns = self._analyze_headers(scan_request.headers)
        vulnerabilities.extend(header_vulns)
        total_weight += sum(v['weight'] for v in header_vulns)
        
        # Check body for vulnerabilities
        if scan_request.body:
            body_vulns = self._analyze_string(scan_request.body, 'body')
            vulnerabilities.extend(body_vulns)
            total_weight += sum(v['weight'] for v in body_vulns)
        
        # Calculate security score (100 - total_weight, min 0)
        security_score = max(0, 100 - total_weight)
        
        # Determine risk level
        if security_score >= 80:
            risk_level = "LOW"
        elif security_score >= 60:
            risk_level = "MEDIUM"
        elif security_score >= 40:
            risk_level = "HIGH"
        else:
            risk_level = "CRITICAL"
        
        result = ScanResult(
            request_id=request_id,
            security_score=security_score,
            risk_level=risk_level,
            message=f"Security score: {security_score}/100",
            timestamp=timestamp,
            details={'vulnerabilities': vulnerabilities}
        )
        
        self.scan_history[request_id] = result
        return result

    def _analyze_string(self, text: str, source: str) -> List[Dict]:
        """Analyze a string for vulnerability patterns."""
        vulnerabilities = []
        for vuln_type, config in self.vulnerability_patterns.items():
            for pattern in config['patterns']:
                if re.search(pattern, text, re.IGNORECASE):
                    vulnerabilities.append({
                        'type': vuln_type,
                        'source': source,
                        'weight': config['weight']
                    })
                    break
        for keyword in self.sensitive_keywords:
            if keyword in text.lower():
                vulnerabilities.append({
                    'type': 'sensitive_data',
                    'source': source,
                    'weight': 5
                })
        return vulnerabilities

    def _analyze_headers(self, headers: Dict[str, str]) -> List[Dict]:
        """Analyze HTTP headers for security issues."""
        vulnerabilities = []
        security_headers = ['x-frame-options', 'x-content-type-options', 'x-xss-protection']
        missing = [h for h in security_headers if h not in headers]
        if missing:
            vulnerabilities.append({
                'type': 'missing_security_headers',
                'source': 'headers',
                'weight': 10 * len(missing)
            })
        return vulnerabilities
