# Harness Technical Architecture

This version is a static architecture view rather than a process flow. It highlights the main deployment boundaries of Harness: access layer, SaaS control plane, customer-side execution plane, enterprise toolchain, and runtime targets.

```mermaid
flowchart LR
    classDef person fill:#EEF4FF,stroke:#5B8DEF,color:#1D2A57;
    classDef edge fill:#F7F8FA,stroke:#9AA4B2,color:#111827;
    classDef platform fill:#E8FFF5,stroke:#26A269,color:#0F5132;
    classDef module fill:#FFF5E8,stroke:#F59E0B,color:#7C4A03;
    classDef runtime fill:#F3E8FF,stroke:#8B5CF6,color:#4C1D95;

    U["Developers / Platform / Ops / Security / FinOps"]:::person

    subgraph Access["Access Layer"]
        direction TB
        Portal["Web Console / API / CLI"]:::edge
        Auth["SSO / RBAC / Audit"]:::edge
        IDP["Internal Developer Portal<br/>Catalog / Scorecards / Golden Paths"]:::edge
    end

    subgraph SaaS["Harness SaaS Control Plane"]
        direction TB

        subgraph Shared["Shared Platform Services"]
            direction LR
            Pipeline["Pipeline Orchestration"]:::platform
            Template["Templates / Variables / Reuse"]:::platform
            Policy["Policy as Code / Governance"]:::platform
            Connector["Secrets / Connectors / Credentials"]:::platform
            Data["Audit / Events / Analytics / AIDA"]:::platform
        end

        subgraph Product["Product Modules"]
            direction LR
            CI["CI"]:::module
            CD["CD"]:::module
            GitOps["GitOps"]:::module
            FF["Feature Flags"]:::module
            IACM["IACM"]:::module
            STO["STO"]:::module
            SRM["SRM"]:::module
            CCM["CCM"]:::module
            CDE["CDE"]:::module
        end
    end

    subgraph Exec["Customer Execution Plane<br/>(VPC / Data Center / Private Network)"]
        direction TB
        Delegate["Harness Delegate Cluster"]:::platform
        Runner["Build Runners / Ephemeral Workers"]:::platform
        Agent["GitOps / K8s Agents"]:::platform
        Private["Private Endpoints / Internal Resources"]:::platform
    end

    subgraph Tools["Enterprise Toolchain"]
        direction TB
        SCM["GitHub / GitLab / Bitbucket"]:::edge
        Artifact["Artifact Registry / Docker Registry"]:::edge
        Cloud["AWS / Azure / GCP"]:::edge
        ITSM["Jira / ServiceNow / Slack"]:::edge
        SecTool["SAST / DAST / SIEM / CSPM"]:::edge
        Obs["Logs / Metrics / Traces / APM"]:::edge
    end

    subgraph Runtime["Runtime Targets"]
        direction TB
        K8s["Kubernetes / Helm"]:::runtime
        VM["VM / Bare Metal"]:::runtime
        Serverless["Serverless / Managed Services"]:::runtime
        App["Applications / Services / APIs"]:::runtime
    end

    U --- Portal
    U --- IDP
    Portal --- Auth
    Portal --- SaaS
    IDP --- SaaS

    Product --- Shared
    SaaS --- Exec
    SaaS --- Tools
    Exec --- Runtime
    Exec --- Tools

    CI --- Runner
    CD --- Delegate
    GitOps --- Agent
    STO --- SecTool
    SRM --- Obs
    CCM --- Cloud
    IACM --- Cloud
    Connector --- Private
    Delegate --- K8s
    Delegate --- VM
    Agent --- K8s
    Runner --- Artifact
    SCM --- CI
    SCM --- GitOps
```

## How to read this architecture

- Access layer: users interact through the Harness console, API, CLI, and IDP capabilities.
- SaaS control plane: Harness hosts orchestration, governance, analytics, and product logic here.
- Customer execution plane: sensitive execution stays close to enterprise infrastructure through Delegates, runners, and agents.
- Enterprise toolchain: Harness integrates with source control, cloud, security, ITSM, and observability systems.
- Runtime targets: applications are built, deployed, validated, and operated on Kubernetes, VMs, or managed cloud services.

## Executive simplification

For a PPT-style summary, you can present Harness as five static blocks:

1. User access layer
2. Harness SaaS control plane
3. Product modules
4. Customer-side execution plane
5. Enterprise integrations and runtime environment
