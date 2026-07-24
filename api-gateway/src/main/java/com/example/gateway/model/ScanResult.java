package com.example.gateway.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ScanResult {
    private String requestId;
    private int securityScore;
    private String riskLevel;
    private String message;
    private long timestamp;
}
