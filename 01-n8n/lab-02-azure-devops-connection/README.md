# Lab 02 — Azure DevOps Connection

## What

Connect n8n to a real Azure DevOps organization and query real work items,
using Personal Access Token (PAT) authentication over the REST API.

## Why

n8n has no dedicated native node for Azure DevOps (unlike GitHub or Jira).
In practice, this means using the generic **HTTP Request** node against
Azure DevOps' REST API directly — the same technique used to integrate with
any system that doesn't have a first-class connector. This is also the
foundation for Lab 03, where an AI agent will read/write Azure DevOps data
through this same connection pattern.

## Setup

- Created a free Azure DevOps organization (`julio-marques-portfolio`) and
  project (`ai-automation-labs`), separate from any employer's
  organization — kept strictly personal for portfolio purposes
- Azure DevOps requires an Azure subscription linked to create an
  organization; used the free trial ($200 credit / 12 months free tier, no
  auto-charge after expiry — Microsoft requires manual upgrade to be
  billed)
- Generated a PAT scoped to **Work Items (Read)** and **Project and Team
  (Read)** — least privilege needed for this lab
- In n8n: HTTP Request node → Authentication → Generic Credential Type →
  Basic Auth, with **User left blank** and **Password = the PAT**

## Workflow structure

`Manual Trigger → HTTP Request (POST, WIQL query)`

The HTTP Request node calls:
```
POST https://dev.azure.com/{organization}/{project}/_apis/wit/wiql?api-version=7.1
Content-Type: application/json

{
  "query": "Select [System.Id], [System.Title], [System.State] From WorkItems"
}
```

**WIQL** (Work Item Query Language) is Azure DevOps' SQL-like syntax for
querying work items. This returns the matching work item IDs plus
metadata — a follow-up call to `_apis/wit/workitems?ids=...` would fetch
full field values for each one (not needed for this lab, but the natural
next step).

## Problem encountered: PAT scope mismatch (401 error)

The first version of the workflow authenticated fine against a simpler
endpoint (`GET _apis/projects`, listing the organization's projects) using
a PAT scoped only to **"Project and Team (Read)"**. Reusing the same PAT
against the work items WIQL endpoint failed with:
```
Authorization failed - please check your credentials (401)
```

**Cause:** Azure DevOps PAT scopes are granular per API area. "Project and
Team" and "Work Items" are separate scopes — a token valid for one is not
automatically valid for the other.

**Resolution:** generated a new PAT with the **"Work Items (Read)"** scope
explicitly added, and updated the existing n8n credential's password with
the new token (no need to recreate the credential itself).

## How to run

1. Open n8n at `localhost:5678`
2. Import [`workflow.json`](workflow.json)
3. Create a Basic Auth credential named `Azure DevOps PAT`: User blank,
   Password = your own PAT (scoped to Work Items: Read)
4. Update the URL in the HTTP Request node to match your own organization
   and project
5. Execute the workflow

## What I learned

- n8n's **generic HTTP Request + credential** pattern is how you integrate
  with any API that lacks a dedicated node — a reusable skill, not
  Azure DevOps-specific
- Azure DevOps PAT scopes are fine-grained per API area; a 401 doesn't
  always mean a wrong token — it can mean an under-scoped one
- Azure DevOps organizations require a linked Azure subscription to be
  created (free trial works, no charge unless manually upgraded), but
  running the org day-to-day on the free tier doesn't touch that
  subscription's credits
- **WIQL** as the query language for work items, and the two-step pattern
  (query for IDs → fetch full details) used by the real Azure DevOps API
- Keeping personal-portfolio cloud resources (Azure DevOps org, PAT)
  fully separate from any employer's tenant
