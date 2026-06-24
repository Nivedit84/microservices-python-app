# Devops Project: video-converter
Converting mp4 videos to mp3 in a microservices architecture.

## Architecture

<p align="center">
  <img src="./Project documentation/ProjectArchitecture.png" width="600" title="Architecture" alt="Architecture">
  </p>

# 🎥 Kubernetes Observability Platform

Production-grade observability implementation for a microservices-based video conversion platform running on Kubernetes.

## 🚀 Project Goals

This project is focused on learning and implementing modern observability practices for cloud-native applications:

- Metrics with Prometheus
- Dashboards with Grafana
- Distributed Tracing with OpenTelemetry
- Trace Visualization with Jaeger
- Kubernetes Monitoring
- Service Discovery using ServiceMonitors

---

## 🏗️ Architecture

![Architecture](docs/architecture.png)

---

## 🔧 Technology Stack

### Platform
- Kubernetes
- Amazon EKS
- Docker
- Helm

### Application
- Python
- RabbitMQ
- MongoDB
- PostgreSQL

### Observability
- Prometheus
- Grafana
- OpenTelemetry
- OpenTelemetry Collector
- Jaeger
- kube-state-metrics
- node-exporter

---

## 📊 Current Progress

### Gateway Service

✅ Prometheus Metrics

✅ OpenTelemetry Instrumentation

✅ Distributed Tracing

✅ ServiceMonitor Integration

✅ Grafana Dashboard

### Converter Service

✅ Prometheus Metrics

✅ ServiceMonitor Integration

✅ Grafana Dashboard

⬜ OpenTelemetry Instrumentation

⬜ Distributed Tracing

### Planned

⬜ Auth Service Instrumentation

⬜ Notification Service Instrumentation

⬜ Loki Logging

⬜ Alertmanager

⬜ Slack Alerts

⬜ SLO Dashboards

---

## 📈 Gateway Dashboard

![Gateway Dashboard](docs/screenshots/gateway-dashboard.png)

### Metrics

- Request Rate
- Error Rate
- Response Time
- P95 Latency
- Request Throughput

---

## 📈 Converter Dashboard

![Converter Dashboard](docs/screenshots/converter-dashboard.png)

### Metrics

- Conversion Requests
- Conversion Duration
- Success Rate
- Failure Rate
- Processing Time

---

## 🔍 Distributed Tracing

### Trace Flow

Gateway Service

↓

OpenTelemetry SDK

↓

OTel Collector

↓

Jaeger

![Jaeger Trace](docs/screenshots/jaeger-trace.png)

---

## 🛠️ Troubleshooting Scenarios

### Prometheus Target Down

- Verify ServiceMonitor
- Verify Service Labels
- Verify Endpoints
- Check Prometheus Targets

### Missing Metrics

- Verify `/metrics` endpoint
- Check scrape status
- Validate ServiceMonitor selectors

### Missing Traces

- Verify OTel Collector
- Verify Exporters
- Check Jaeger

---

## 🎯 Learning Outcomes

Through this project I am gaining hands-on experience with:

- Kubernetes Observability
- Prometheus Monitoring
- Grafana Dashboarding
- OpenTelemetry
- Distributed Tracing
- Service Discovery
- Kubernetes Troubleshooting
- SRE Practices

---

## 🚧 Roadmap

- [x] Gateway Metrics
- [x] Gateway Tracing
- [x] Converter Metrics
- [ ] Converter Tracing
- [ ] Auth Service Metrics
- [ ] Notification Service Metrics
- [ ] Loki Integration
- [ ] Alertmanager
- [ ] Slack Notifications
- [ ] Tempo Migration
- [ ] SLO & Error Budget Tracking
