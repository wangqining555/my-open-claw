# Harness Technical Framework

This diagram shows Harness as a layered platform with a central control plane, a distributed execution plane, and integrations across the software delivery lifecycle.

```mermaid
flowchart TB
    subgraph Personas["Users / Personas"]
        Dev["Developers"]
        Ops["Ops / SRE"]
        Plat["Platform Engineers"]
        Sec["Security Teams"]
        Fin["FinOps"]
    end

    subgraph Experience["Experience Layer"]
        UI["Unified UI / API / RBAC / SSO"]
        IDP["IDP: Golden Paths / Scorecards / Catalog"]
    end

    subgraph Products["Harness Product Domains"]
        CI["CI"]
        CD["CD"]
        GitOps["GitOps"]
        FF["Feature Flags"]
        IACM["IACM"]
        STO["STO"]
        SRM["SRM"]
        CCM["CCM"]
        CDE["CDE"]
        CE["Chaos Engineering"]
    end

    subgraph ControlPlane["Shared Control Plane"]
        Pipelines["Pipelines / Triggers / Approvals"]
        Templates["Templates / Reusable Modules"]
        Policy["Policy as Code / Governance"]
        Connectors["Secrets / Connectors / Service Accounts"]
        Insights["Audit / Notifications / Analytics / AIDA"]
    end

    subgraph ExecutionPlane["Distributed Execution Plane"]
        Delegate["Harness Delegate"]
        Runners["Build Runners / Ephemeral Workers"]
        Agents["GitOps Agents / K8s Agents"]
    end

    subgraph Integrations["External Integrations"]
        SCM["GitHub / GitLab / Bitbucket"]
        Artifact["Docker / Artifact Repositories"]
        Cloud["AWS / Azure / GCP"]
        K8s["Kubernetes / Helm / Argo CD"]
        ITSM["Jira / ServiceNow / Slack"]
        Security["SAST / DAST / SIEM / CSPM"]
        Observe["Logs / Metrics / Traces / APM"]
    end

    subgraph Targets["Delivery Targets"]
        Apps["Applications / Services / APIs"]
        Envs["Dev / Test / Staging / Prod"]
        Estate["Cloud / On-prem / Hybrid"]
    end

    Personas --> Experience
    Experience --> Products
    Experience --> ControlPlane
    Products <--> ControlPlane
    ControlPlane --> ExecutionPlane
    ExecutionPlane --> Integrations
    Integrations --> Targets

    SCM --> CI
    SCM --> GitOps
    Artifact --> CI
    Cloud --> CD
    K8s --> CD
    K8s --> GitOps
    Security --> STO
    Observe --> SRM
    ITSM --> Pipelines

    CI --> Runners
    CD --> Delegate
    GitOps --> Agents
    CCM --> Cloud
    SRM --> Apps
```

## Suggested interpretation

- Experience layer: one entry point for developers, platform teams, security teams, and FinOps.
- Product domains: Harness capabilities are organized around CI/CD, GitOps, security, reliability, and cost.
- Shared control plane: governance, pipelines, templates, connectors, and analytics are reused across products.
- Execution plane: Delegates, runners, and agents execute work close to customer infrastructure.
- Integrations and targets: Harness connects upstream tools and deploys or evaluates downstream runtime environments.

## Presentation version

If you need a simplified executive view, you can collapse the diagram into four blocks:

1. Developer portal and governance
2. Delivery and operations products
3. Control plane plus execution plane
4. Enterprise integrations and runtime targets
