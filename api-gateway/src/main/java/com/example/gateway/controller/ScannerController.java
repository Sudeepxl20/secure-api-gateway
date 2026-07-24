package com.example.gateway.controller;

import com.example.gateway.model.ScanResult;
import com.example.gateway.service.ScannerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import jakarta.servlet.http.HttpServletRequest;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/scan")
public class ScannerController {

    @Autowired
    private ScannerService scannerService;

    @PostMapping("/analyze")
    public ScanResult analyzeRequest(HttpServletRequest request, @RequestBody(required = false) String body) {
        String endpoint = request.getRequestURI();
        String method = request.getMethod();
        
        Map<String, String> headers = new HashMap<>();
        Enumeration<String> headerNames = request.getHeaderNames();
        if (headerNames != null) {
            while (headerNames.hasMoreElements()) {
                String headerName = headerNames.nextElement();
                headers.put(headerName, request.getHeader(headerName));
            }
        }
        
        return scannerService.scanRequest(endpoint, method, headers, body);
    }
}