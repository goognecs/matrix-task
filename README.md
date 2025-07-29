
# Matrix Smallest Path Sum - Kubernetes Job Deployment

This repo contains updates of my code of a sample cloud resume.
## Task Description
You are given an N×N matrix of positive integers (example matrix size: 80×80).

## Goal: 
Find the path from the top-left corner to the bottom-right corner of the matrix such that:
1. The sum of the visited elements along the path is minimal.
2. Movement is only allowed to the right or down at each step.

You need both:
The minimum sum of the path.
The actual path (coordinates or values) taken.
## Solution Overview

### 1. Algorithm:
Use Dynamic Programming to compute the minimal sum path. For each cell (j, i):

#### grid[j][i]+=min(grid[j - 1][i], grid[j][i - 1])

reconstruct the path by backtracking from the bottom-right.

### 2.Input:
The matrix is not hardcoded in the program.
It is provided via a Kubernetes ConfigMap that mounts the input file matrix.txt.

### 3. Deployment:
* Containerize into a Docker image.
* Load docker image into local Kubernetes cluster.
* Run program as a Kubernetes Job.
* Mount ConfigMap as a volume to access the matrix file.

### 4. Output:
The Job prints the result showing:
* Minimal sum value &
* List of path elements or coordinates.
Check the log with kubectl logs job/minimumpath-job.

## Instructions
###  Build the Docker Image
 --> docker build -t minimumpath:latest .

### Load Docker Image into Kind Cluster
 --> kind load docker-image minimumpath:latest --name necslab

### Create ConfigMap and load data from matrix.txt
 --> cd matrix-task
 --> kubectl create configmap matrix-data --from-file=matrix.txt
 
 --> Verify: kubectl get configmap matrix-data -o yaml
 
### Deploy the Job
 --> kubectl apply -f job-min-path.yaml

### Check Job and Logs
 --> kubectl logs job/minimumpath-job

