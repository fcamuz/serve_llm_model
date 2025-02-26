# SpaCy NER API Service

This repository contains a FastAPI application that provides Named Entity Recognition (NER) services using spaCy, containerized with Docker.

## Prerequisites

- Python 3.9 or higher
- Docker Desktop
- Azure CLI
- An Azure account with an Azure Container Registry (ACR)

## Project Structure

Copy

Insert at cursor
markdown
serve-llm-local/
│
├── app.py # FastAPI application
├── Dockerfile # Docker configuration
└── requirements.txt # Python dependencies


## Local Development

1. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```


2. Run the application locally:
```
uvicorn app:app --reload
```

# Docker Operations
## Building Local Docker Image
1. Build the Docker image:
```
docker build -t spacy-ner-api 
```

2. Run the container locally:
```
docker run -p 8000:8000 spacy-ner-api
```
3.Test the local container:

- Open your browser and navigate to ```http://localhost:8000/docs```

- Or use curl to test the API endpoints

## Pushing to Azure Container Registry
1.Log in to Azure:
```
az login
```

2. Log in to your Azure Container Registry:
```
az acr login --name <your-registry-name>
```

3.Tag your local image:
```
docker tag spacy-ner-api <registry-name>.azurecr.io/spacy-ner-api:latest
```

4.Push the image to ACR:
```
docker push <registry-name>.azurecr.io/spacy-ner-api:latest
```

## Deploying to Azure Container Instances
1. Create a container instance:
```
az container create \
    --resource-group <your-resource-group> \
    --name spacy-ner-container \
    --image <registry-name>.azurecr.io/spacy-ner-api:latest \
    --cpu 1 \
    --memory 1.5 \
    --registry-login-server <registry-name>.azurecr.io \
    --registry-username <registry-username> \
    --registry-password <registry-password> \
    --dns-name-label <unique-dns-name> \
    --ports 8000
```
Copy

2.Get the container's FQDN:
```
az container show \
    --resource-group <your-resource-group> \
    --name spacy-ner-container \
    --query ipAddress.fqdn \
    --output table
```
## API Documentation
Once deployed, you can access the API documentation at:

- Swagger UI: http://<your-container-url>:8000/docs

- ReDoc: http://<your-container-url>:8000/redoc

## Environment Variables
The following environment variables can be configured:

- PORT: The port number the API will listen on (default: 8000)

- Add any other environment variables your application uses

## Troubleshooting
### Common Docker Issues
- Ensure Docker Desktop is running

- Check Docker logs for build errors

- Verify proper network connectivity

### Azure Container Registry Issues
- Verify Azure CLI is logged in

- Ensure proper ACR permissions

- Check network connectivity to ACR

### Container Instance Issues
- Verify resource group exists

- Check container logs using Azure portal

- Ensure proper networking rules are in place

## Contributing
1.Fork the repository

2.Create your feature branch

3.Commit your changes

4.Push to the branch

5. Create a new Pull Request

License



This README provides a comprehensive guide for users to:
- Set up the project locally
- Build and test Docker images
- Deploy to Azure Container Registry
- Deploy to Azure Container Instances [[1]](https://yourtechie.hashnode.dev/creating-your-custom-docker-image-on-azure-container-registry-and-deploying-with-container-instances)
- Troubleshoot common issues

Remember to:
- Replace placeholders like `<your-registry-name>`, `<your-resource-group>`, etc., with actual values
- Add any specific configuration or environment variables your application requires
- Include any additional deployment or setup steps specific to your application
- Add appropriate license information
