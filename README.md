# Devops Project: video-converter
Converting mp4 videos to mp3 in a microservices architecture.

## Architecture

<p align="center">
  <img src="./Project documentation/ProjectArchitecture.png" width="600" title="Architecture" alt="Architecture">
  </p>

📌 Overview

This project focuses on building a production-style observability platform for a microservices-based video conversion application running on Kubernetes.

The application converts MP4 videos into MP3 files using multiple Python services communicating through RabbitMQ and backed by MongoDB and PostgreSQL.

The primary goal is to gain hands-on experience with modern observability practices including metrics collection, distributed tracing, dashboarding, alerting, and Kubernetes monitoring.

🏗️ Application Architecture
Microservices
Service	Purpose
Gateway Service	Entry point for uploads and downloads
Auth Service	Authentication and authorization
Converter Service	Converts MP4 files to MP3
Notification Service	Sends email notifications
RabbitMQ	Message broker between services
MongoDB	Stores converted files metadata
PostgreSQL	Stores authentication data
Request Flow
User
  │
  ▼
Gateway Service
  │
  ▼
Auth Service
  │
  ▼
RabbitMQ
  │
  ▼
Converter Service
  │
  ▼
MongoDB
  │
  ▼
Notification Service
  │
  ▼
Email Notification
🔭 Observability Architecture
                 ┌─────────────────┐
                 │   Grafana       │
                 └────────┬────────┘
                          │
          ┌───────────────┼───────────────┐
          │                               │
          ▼                               ▼
    Prometheus                      Jaeger
          ▲                               ▲
          │                               │
   ServiceMonitor                 OTel Collector
          ▲                               ▲
          │                               │
    Application Pods ─────────────────────┘
⚙️ Technology Stack
Platform
Kubernetes
Amazon EKS
Helm
Docker
Application
Python
RabbitMQ
MongoDB
PostgreSQL
Observability
Prometheus
Grafana
OpenTelemetry
OpenTelemetry Collector
Jaeger
kube-state-metrics
node-exporter
✅ Current Progress
Gateway Service

Implemented:

OpenTelemetry instrumentation
Distributed tracing
Prometheus metrics exposure
ServiceMonitor integration
Grafana dashboard

Metrics collected:

HTTP request count
Request duration
Error rate
Request throughput

Tracing:

End-to-end request traces visible in Jaeger
Trace propagation through service boundaries
Converter Service

Implemented:

Prometheus metrics exposure
ServiceMonitor integration
Grafana dashboard

Metrics collected:

Conversion requests
Conversion duration
Success / failure count
Worker performance metrics
📊 Dashboards
Gateway Dashboard

Monitors:

Requests per second
Error rate
Average response time
P95 latency
Request volume
Converter Dashboard

Monitors:

Conversion throughput
Conversion latency
Failed conversions
Processing time
📈 Metrics Collection Flow
Application
    │
    ▼
/metrics
    │
    ▼
ServiceMonitor
    │
    ▼
Prometheus
    │
    ▼
Grafana Dashboard
🔍 Distributed Tracing Flow
Gateway Service
      │
      ▼
OpenTelemetry SDK
      │
      ▼
OTel Collector
      │
      ▼
Jaeger

Current tracing implementation is available for the Gateway Service and is used to analyze request latency and application behavior.

🧪 Troubleshooting Scenarios Practiced
Prometheus Target Down
Validate ServiceMonitor
Verify Service labels
Check Endpoints
Inspect Prometheus Targets page
Missing Metrics
Verify /metrics endpoint
Check Prometheus scrape status
Validate ServiceMonitor selectors
Missing Traces
Verify OTel Collector configuration
Check exporter connectivity
Inspect Jaeger traces
🎯 Learning Outcomes

Through this project I am gaining hands-on experience with:

Kubernetes Observability
Prometheus Monitoring
Grafana Dashboard Design
OpenTelemetry Instrumentation
Distributed Tracing
Jaeger Tracing Analysis
Kubernetes Service Discovery
ServiceMonitor Configuration
Production Monitoring Workflows
DevOps and SRE Troubleshooting
🚀 Upcoming Enhancements
Instrument Auth Service
Instrument Notification Service
Centralized Logging with Loki
Alertmanager Integration
Slack Alerting
SLO & Error Budget Dashboards
Jaeger → Tempo Migration
GitOps Deployment using ArgoCD
Thanos for Long-Term Metrics Storage
Multi-Service Distributed Tracing
