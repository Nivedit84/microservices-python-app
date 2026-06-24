# Devops Project: video-converter
Converting mp4 videos to mp3 in a microservices architecture.

## Architecture

<p align="center">
  <img src="./Project documentation/ProjectArchitecture.png" width="600" title="Architecture" alt="Architecture">
  </p>

This project demonstrates the implementation of a complete observability stack for a microservices-based video conversion platform running on Kubernetes.

The application converts MP4 videos into MP3 files using multiple interconnected services deployed on Amazon EKS. The primary objective of this project is to design, deploy, and operate a production-style observability platform covering metrics, logs, traces, dashboards, and alerting.

The platform provides:

Metrics collection using Prometheus
Visualization using Grafana
Log aggregation using Loki
Distributed tracing using OpenTelemetry and Tempo
Alerting using Alertmanager
Kubernetes workload monitoring
Application performance monitoring for microservices

Application Components

The application consists of:

Gateway Service
Auth Service
Converter Service
Notification Service
RabbitMQ
MongoDB
PostgreSQL

Application flow:

User Uploads Video

↓

Gateway Service

↓

Auth Service

↓

RabbitMQ

↓

Converter Service

↓

MongoDB

↓

Notification Service

↓

Email Notification

Observability Architecture

Metrics Flow

Application Pods

↓

/metrics Endpoint

↓

ServiceMonitor

↓

Prometheus

↓

Grafana

Logs Flow

Application Pods

↓

Promtail

↓

Loki

↓

Grafana

Tracing Flow

Application Services

↓

OpenTelemetry SDK

↓

OpenTelemetry Collector

↓

Tempo

↓

Grafana

Alerting Flow

Prometheus Rules

↓

Alertmanager

↓

Email / Slack Notifications

Technology Stack
Platform
Amazon EKS
Kubernetes
Helm
Docker
Application
Python Microservices
RabbitMQ
MongoDB
PostgreSQL
Observability
Prometheus
Grafana
Loki
Promtail
Alertmanager
OpenTelemetry Collector
Tempo
kube-state-metrics
node-exporter
Observability Objectives

This project focuses on implementing:

Metrics

Monitor:

HTTP request rate
Request latency
Error rates
CPU utilization
Memory utilization
Pod health
Node health
RabbitMQ metrics
Logs

Centralized log aggregation for:

Gateway Service
Auth Service
Converter Service
Notification Service
Traces

Distributed tracing across:

Gateway → Auth → RabbitMQ → Converter → Database

Tracing helps identify:

Slow requests
Service bottlenecks
Database latency
Failed requests
Alerting

Alerts configured for:

High CPU usage
High memory usage
Pod restarts
Service downtime
Increased error rates
RabbitMQ queue backlog
Kubernetes Monitoring Components
Prometheus

Prometheus collects metrics from:

Application Services
Kubernetes Nodes
Pods
Deployments
RabbitMQ
MongoDB
PostgreSQL

Metrics are discovered using Kubernetes ServiceMonitors.

Grafana

Grafana dashboards include:

Cluster Overview Dashboard
Application Dashboard
Gateway Dashboard
RabbitMQ Dashboard
Infrastructure Dashboard
Loki

Loki provides centralized logging for all Kubernetes workloads.

OpenTelemetry

OpenTelemetry is used to collect:

Metrics
Logs
Traces

Telemetry is routed through an OpenTelemetry Collector.

Tempo

Tempo stores and visualizes distributed traces.

Alertmanager

Alertmanager manages:

Alert routing
Deduplication
Grouping
Notification delivery
Key Dashboards
Infrastructure Dashboard

Monitors:

Node CPU
Node Memory
Disk Usage
Network Traffic
Application Dashboard

Monitors:

Requests per second
Error rate
P95 latency
Active pods
Service availability
RabbitMQ Dashboard

Monitors:

Queue depth
Consumer count
Message rate
Processing latency
Troubleshooting Scenarios
Target Down

Verify:

ServiceMonitor configuration
Kubernetes Service
Endpoints
Prometheus Targets page
Missing Logs

Verify:

Promtail Pods
Loki Health
Log Labels
Missing Traces

Verify:

OpenTelemetry Collector
Tempo
Trace Exporters
Alerts Not Firing

Verify:

Alert Rules
Prometheus Evaluation
Alertmanager Routing
Learning Outcomes

Through this project I gained hands-on experience with:

Kubernetes Observability
Prometheus Monitoring
Grafana Dashboarding
OpenTelemetry Instrumentation
Distributed Tracing
Centralized Logging
Alerting Strategies
Kubernetes Troubleshooting
Production Monitoring Design
SRE and DevOps Best Practices
Future Enhancements
Thanos for long-term metrics storage
Prometheus High Availability
SLO and Error Budget Tracking
GitOps deployment using ArgoCD
Multi-cluster observability
Synthetic monitoring
Advanced alert routing
