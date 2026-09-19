# Azure Cost Management

Cost governance is implemented for the Azure IoT Monitoring System to provide visibility into cloud resource usage and reduce the risk of unexpected Azure consumption.

## Resource Organization

Azure resources are organized using consistent tags:

| Tag | Value |
|---|---|
| Project | Azure-IoT-Monitoring |
| Environment | Development |
| Owner | Dhruvin-Patel |
| Purpose | Cloud-Portfolio |

These tags make project resources easier to identify, organize, and analyze.

## Cost Analysis

Azure Cost Management is used to monitor resource consumption across the project.

Cost analysis can be grouped by resource and Azure service to identify which components contribute to cloud usage.

Major resources monitored include:

- Azure Linux Virtual Machine
- Managed Disk
- Virtual Network resources
- Azure Storage
- Log Analytics Workspace
- Azure Monitor resources

## Budget

A monthly Azure Cost Management budget is configured for the project resource group.

Budget:

`budget-iot-monitoring`

The budget provides notifications as project spending approaches configured thresholds.

Budget alerts provide visibility into spending but do not automatically stop Azure resources.

## Cost Optimization

The project uses several cost-conscious design decisions:

- Small B-series development VM
- VM deallocation when not in use
- Locally redundant Blob Storage
- Limited telemetry/log ingestion
- No unnecessary load balancer
- No unnecessary application gateway
- Development-scale resources
- Azure Cost Management budget alerts

## FinOps Practices Demonstrated

This project demonstrates:

- Azure resource tagging
- Cost analysis
- Resource-level cost visibility
- Monthly budgets
- Budget threshold alerts
- Development environment cost optimization
