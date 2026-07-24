package com.example.gateway.service;

import com.example.gateway.model.ScanResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@Service
public class ScannerService {

    @Autowired
    private RestTemplate restTemplate;

    @Value("${scanner.service.url}")
    private String scannerUrl;

    public ScanResult scanRequest(String endpoint, String method, Map<String, String> headers, String body) {
        try {
            Map<String, Object> request = new HashMap<>();
            request.put("endpoint", endpoint);
            request.put("method", method);
            request.put("headers", headers);
            request.put("body", body != null ? body : "");
            
            String url = scannerUrl + "/api/scan";
            return restTemplate.postForObject(url, request, ScanResult.class);
        } catch (Exception e) {
            return new ScanResult("error", 50, "MEDIUM", "Scanner error: " + e.getMessage(), System.currentTimeMillis());
        }
    }
}