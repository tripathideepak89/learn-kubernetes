# AWS Kubernetes Cluster Access Python Program

Welcome to the AWS Kubernetes Cluster Access Python Program repository! This program allows you to access a Kubernetes cluster in another AWS account using Python.

## Overview

This Python program enables you to interact with a Kubernetes cluster hosted in an AWS account. It configures the kubectl command-line tool with the necessary AWS credentials and context to retrieve information about namespaces, pods, and the Kubernetes version number from the cluster.

## Prerequisites

Before using this program, ensure you have the following prerequisites installed and configured:

- AWS CLI: Install and configure the AWS CLI with credentials for the AWS account where the Kubernetes cluster resides.
- kubectl: Install kubectl on your local machine to interact with the Kubernetes cluster.
- Python: Ensure you have Python installed on your system to run the Python program.

## Usage

1. Clone this repository:

```
git clone https://github.com/tripathideepak89/learn-kubernetes.git
```

2. Navigate to the cloned repository:

```
cd learn-kubernetes
```

3. Open the aws_kubernetes_access.py file and replace the placeholders with your AWS credentials, AWS region, Kubernetes cluster name, and Kubernetes context name.

4. Run the Python program:

```
python aws_kubernetes_access.py
```
This will configure kubectl with the appropriate AWS credentials and context, and retrieve information about namespaces, pods, and the Kubernetes version number from the cluster.

## Contributing

Contributions to this repository are welcome! If you have improvements, suggestions, or bug fixes, please open an issue or submit a pull request.

