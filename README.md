# Azure-IoT-Moinitoring-System
Cloud-based IoT telemetry monitoring and alerting platform built with Microsoft Azure, Linux and Python.


# Azure Cloud IoT Monitoring & Alerting System

## Overview

This project demonstrates the migration of an existing hardware-based IoT
monitoring concept to a cloud-hosted monitoring and alerting platform using
Microsoft Azure.

The original implementation used physical sensors and an Arduino-based
architecture. Since the original hardware is no longer connected, this
version uses a Python telemetry simulator to generate realistic light,
sound, and distance measurements.

The primary focus of this version is Azure cloud infrastructure, Linux,
monitoring, logging, alerting, storage, security, governance, and cost
management.

## Project Status

🚧 In Progress

## Original Project

This project builds upon my original hardware-based Alert and Monitoring
System:

https://github.com/dp0912/Alert_and_Monitoring_System

## Technologies

- Microsoft Azure
- Ubuntu Linux
- Python
- Bash
- Git/GitHub
- Azure Virtual Machines
- Azure Virtual Network
- Azure Monitor
- Log Analytics
- KQL
- Azure Storage
- Azure RBAC
- Azure Cost Management

## Planned Architecture

Architecture diagram coming soon.

## Project Roadmap

- [x] Deploy Azure Linux VM
- [x] Configure Azure networking
- [ ] Develop telemetry simulator
- [ ] Deploy application to Linux
- [ ] Configure Azure Monitor
- [ ] Configure alerting
- [ ] Configure Log Analytics
- [ ] Create KQL queries
- [ ] Configure Azure Storage
- [ ] Review RBAC and security
- [ ] Configure tags and cost management
- [ ] Complete project documentation


## Azure Infrastructure

The application is hosted on an Ubuntu Linux virtual machine in Microsoft
Azure.

## Configuration

- Operating System: Ubuntu Server 24.04 LTS
- Compute: Azure Virtual Machine
- VM Size: Standard_B2ats_v2
- Networking: Azure VNet and subnet
- Storage: Managed OS disk
- Environment: Development

The infrastructure is organized within a dedicated Azure Resource Group.

## IoT Telemetry Simulator

The physical sensor layer from the original project is replaced with a
Python-based telemetry simulator.

The simulator generates:

- Light level (%)
- Sound level (dB)
- Distance (cm)
- Device status
- Alert conditions

This allows the Azure monitoring architecture to be demonstrated without
requiring the original physical hardware.
