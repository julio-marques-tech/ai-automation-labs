# Roadmap — Cloud & Containers Track (AWS + Kubernetes)

Interview-ready understanding of how AI systems get from prototype to
production: containers, orchestration, and the AWS services that host
them. The target depth is **consultant/analyst**: explain and reason about
architecture with confidence, backed by one hands-on deployment. It is not
cluster administration, and not CKA/CKAD certification prep.

## Scope

**In scope**
- AWS foundations (compute, storage, networking, IAM, databases, cost)
  via AWS Cloud Quest: Cloud Practitioner
- Containers beyond "running someone else's image": writing a Dockerfile
- Kubernetes core concepts on a **local** cluster: pods, deployments,
  services, ConfigMaps/Secrets, scaling, self-healing
- Deploying one of the portfolio's own AI services on Kubernetes
- Mapping the local setup to AWS options (EKS, ECS/Fargate, Lambda,
  Bedrock, SageMaker) with an architecture diagram

**Out of scope**
- Running a real EKS cluster (control plane alone is ~USD 0.10/h,
  ~USD 73/month, plus nodes; a forgotten cluster is the classic surprise
  bill). Concepts are identical on a local cluster.
- Cluster administration: networking plugins, storage classes, RBAC
  hardening, Helm chart authoring, service meshes
- Kubernetes certifications (CKA/CKAD)

## Execution order

1. **Lab 00 — AWS foundations (Cloud Quest)** — complete AWS Cloud Quest:
   Cloud Practitioner on AWS Skill Builder. Since the quests run in AWS's
   sandbox and leave no artifacts, the repo deliverable is a structured
   note per quest: the business problem, the architecture built, the AWS
   services involved, and the interview takeaway. Optional: sit the
   **AWS Certified Cloud Practitioner (CLF-C02)** exam afterwards.
   *No Python needed — can start immediately.*
2. **Lab 01 — Containers for real** — write a Dockerfile for one of the
   Python track's own scripts; image layers, build vs run, tags,
   environment variables, volumes. Builds on the Docker setup from the
   n8n track. *Requires basic Python (Lab 01+).*
3. **Lab 02 — Kubernetes core concepts (local)** — local cluster via
   `kind` (or Docker Desktop's built-in Kubernetes); `kubectl` basics;
   pods, deployments, replica sets, services, namespaces,
   ConfigMaps/Secrets; kill a pod and watch it come back; scale up and
   down. *No Python needed.*
4. **Lab 03 — An AI service on Kubernetes** — deploy one of the
   portfolio's own services (the RAG pipeline wrapped as a small API,
   and/or Ollama) on the local cluster; health checks, resource
   requests/limits, rolling update. *Requires Python Fundamentals Lab 04
   and a finished RAG pipeline.*
5. **Lab 04 — Mapping to AWS** — how the Lab 03 setup would run on AWS:
   EKS vs ECS/Fargate vs Lambda vs managed AI (Bedrock, SageMaker
   endpoints), with honest trade-offs (cost, operational burden, team
   skills). Deliverable: an architecture diagram (also closes the
   "produce at least one UML/architecture diagram" gap from the
   job-posting analysis).
6. **Lab 05 — Documentation and interview prep** — track README, key
   takeaways, and a short "how would you deploy this AI system?" answer
   script.

## Technical decisions

- **Local cluster over EKS:** zero cost and zero risk of a runaway bill;
  the Kubernetes API and concepts are the same. AWS is covered through
  Cloud Quest's sandbox and the Lab 04 mapping.
- **`kind` as default:** lightweight (Kubernetes nodes run as Docker
  containers), reuses the existing Docker/WSL2 setup. Docker Desktop's
  built-in Kubernetes is an acceptable alternative.
- **Cloud Quest as the AWS entry point:** free sandbox, gamified, and
  aligned with the CLF-C02 exam. It does not cover Kubernetes, which is
  why the track exists beyond it.

## Why this track (scope change, 2026-09-29)

Kubernetes was originally listed as an accepted out-of-scope gap
(2026-09-07 job-posting analysis). Revisited because it keeps appearing
in the market the user is targeting. Brought back **at explain-and-reason
depth only**. The honest assessment stands: for functional/AI consulting
roles, nobody expects cluster operation, but being able to discuss
orchestration, scaling, and deployment options credibly is a
differentiator.

## Status

See [PROGRESS.md](PROGRESS.md) for the detailed log of each lab.
