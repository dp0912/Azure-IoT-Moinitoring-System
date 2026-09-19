# Linux Deployment

The Python telemetry simulator is deployed to an Ubuntu Server 24.04 LTS
virtual machine hosted in Microsoft Azure.

## Deployment Process

1. Provision Azure VM.
2. Connect using SSH public-key authentication.
3. Install Python, Git and required Linux packages.
4. Clone the GitHub repository.
5. Create a Python virtual environment.
6. Run the telemetry simulator.
7. Configure the application as a systemd service.

## Service Management

Check status:

sudo systemctl status iot-monitor

Restart:

sudo systemctl restart iot-monitor

View logs:

journalctl -u iot-monitor
