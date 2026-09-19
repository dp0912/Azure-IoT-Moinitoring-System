# Security and Access Control

## VM Access

The Ubuntu virtual machine uses SSH public-key authentication.
The private SSH key is stored locally and is never committed to
the repository.

Inbound SSH traffic is controlled through an Azure Network
Security Group (NSG).

## Storage Security

The telemetry archive uses a private Azure Blob Storage container.
Anonymous blob access is disabled and secure transfer is required.

The storage account requires TLS 1.2 or later.

## Azure RBAC

Azure role-based access control (RBAC) is used to manage access
to Azure resources. Permissions are assigned according to the
principle of least privilege.

## Secret Management

Secrets, private keys, environment files, and runtime logs are
excluded from Git using `.gitignore`.

Examples include:

- `.env`
- `*.pem`
- `*.key`
- `*.log`
- `telemetry.log`

No Azure credentials or private SSH keys are stored in the
repository.
