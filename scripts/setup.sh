#!/bin/bash

set -e

echo "Updating package repositories..."
sudo apt update

echo "Installing required packages..."
sudo apt install -y python3 python3-pip python3-venv git curl

echo "Linux environment setup complete."
