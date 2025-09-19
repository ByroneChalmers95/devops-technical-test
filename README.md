# Senior DevOps Engineer – Technical Test

This test assesses your ability to containerize, extend, and design secure, scalable deployments for real-world civic technology software. Please ensure your responses and deliverables are clear, well-structured, and production-minded.

## Instructions
- All code and your response should be on a public GitHub repository.
- Share the GitHub repository link with wasim@opencitieslab.org.
- Time limit: Each candidate will receive 3 days to complete the test from time of receipt.

## Exercise Tasks
### 1. Containerization
- Fork and clone https://github.com/opendatadurban/mycandidate.
- Write a Dockerfile to containerize the application, ensuring all dependencies are handled and using best practices for image security and efficiency.
- Provide a sample docker-compose.yml

### 2. API Extension
Add a new REST API endpoint:
GET /api/v1/wards/<ward_id>/candidates

  Returns a JSON array of all candidates standing for election in the specified ward.
  Use the codebase’s existing models and data to implement this endpoint.
  Document the endpoint (parameters, sample response) within the code or in a Markdown file.
  Implement a basic unit test for this endpoint


### 3. AWS Architecture Design
Design an architecture diagram (Using a tool like draw.io, Lucidchart; include as PDF, PNG, or embed in Markdown):

- Use either ECS or EKS for container orchestration.
- Incorporate secure networking, load balancing, storage, and secrets management.
- Show scaling considerations and your rationale.
- Highlight security best practices.
- Provide Instance Sizing Recommendations
- CI/CD Pipeline Proposal


Deliverables
- Dockerfile and docker-compose.yml
- API source code changes (forked repo)
- Unit test code
- Architecture diagram (attach as image or PDF)
- Textual description (short summary) of security and scaling considerations
- CI/CD pipeline: Description, diagram, or both

Bonus
- Comments or suggestions on DevOps improvements for this codebase.
- Automated security/vulnerability scanning integration in your pipeline.

## Assessment Criteria
- Code & containerization quality
- Security best practices
- Clarity of documentation
- AWS architectural soundness
- CI/CD pipeline completeness
- Thoughtfulness in scaling and cost recommendations

Let us know if you have any questions — Good luck!

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