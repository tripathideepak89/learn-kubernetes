import subprocess

def run_kubectl_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return None

def main():
    # Set AWS credentials and context for the Kubernetes cluster
    aws_access_key_id = "YOUR_AWS_ACCESS_KEY_ID"
    aws_secret_access_key = "YOUR_AWS_SECRET_ACCESS_KEY"
    aws_region = "YOUR_AWS_REGION"
    cluster_name = "YOUR_CLUSTER_NAME"
    context_name = "YOUR_CONTEXT_NAME"

    # Configure kubectl with AWS credentials and context
    configure_command = f"aws eks --region {aws_region} update-kubeconfig --name {cluster_name} --profile default --kubeconfig /tmp/kubeconfig"
    subprocess.run(configure_command, shell=True, check=True)

    # Set the context for kubectl
    set_context_command = f"kubectl config use-context {context_name} --kubeconfig /tmp/kubeconfig"
    subprocess.run(set_context_command, shell=True, check=True)

    # Get namespaces
    namespaces = run_kubectl_command("kubectl get namespaces --kubeconfig /tmp/kubeconfig")
    print("Namespaces:")
    print(namespaces)

    # Get pods
    pods = run_kubectl_command("kubectl get pods --all-namespaces --kubeconfig /tmp/kubeconfig")
    print("\nPods:")
    print(pods)

    # Get Kubernetes version
    version = run_kubectl_command("kubectl version --short --kubeconfig /tmp/kubeconfig")
    print("\nKubernetes Version:")
    print(version)

if __name__ == "__main__":
    main()
