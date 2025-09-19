<!--  -->

#Below From Byrone

## API Endpoints

### Get Candidates by Ward
**GET** `/api/v1/wards/<ward_id>/candidates`

Returns all candidates for the given ward.

#### Parameters
- `ward_id` (int): ID of the ward

#### Example Request
```bash
curl http://localhost:8000/api/v1/wards/1/candidates


### 3. AWS Architecture Design

Below is the architecture design for the MyCandidate Flask App:

![AWS Architecture](doc/DevOps-Technical-Test2025-09-19_113309.png)
######


# Senior DevOps Engineer – Technical Test by Byrone Chalmers

This repository contains my completed submission for the **Senior DevOps Engineer Technical Test**.  
The deliverables include containerization, API extension, unit testing, AWS architecture design, and CI/CD pipeline documentation.

---

## 📦 1. Containerization

### Dockerfile
- Multi-stage build for smaller, secure images
- Uses non-root user for security
- Installs dependencies efficiently

### docker-compose.yml
- Brings up the web service + Redis
- Maps port `8000` for local development

#### Run locally
```bash
docker build -t mycandidate .
docker run -p 8000:8000 mycandidate
