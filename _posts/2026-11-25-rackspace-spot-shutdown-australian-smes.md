---
title: "Rackspace Spot Shutdown: What Australian SMEs Must Do"
date: "2026-11-25"
image: "/assets/images/rackspace-spot-shutdown-australian-smes.jpg"
---

## Rackspace Spot Shuts Down After a Security Breach – What It Means for Your Small Business  

A recent security notification from Rackspace has confirmed that its **Rackspace Spot** cloud platform will be permanently discontinued on **8 December 2026**. The decision follows a breach that gave hackers access to customer Kubernetes clusters, allowing them to read secrets and create unauthorised pods. While the incident involved a global provider, the ripple effects are relevant for any Australian small business that relies on cloud services, containerised applications, or third‑party infrastructure.

### Why This News Matters to Small Business Owners in Australia  

- **Your data could be on the same platform** – Many Australian SMEs use Rackspace Spot or similar Kubernetes‑based services to run websites, point‑of‑sale systems, or internal tools. If you (or a trusted partner) have ever deployed containers on Spot, the breach may have exposed credentials, API tokens or configuration files.  
- **Supply‑chain risk is real** – A compromise of one cloud service can cascade to other tools you use, especially if you share authentication tokens across environments.  
- **Regulatory pressure** – Under the **Privacy Act** and OAIC guidelines, businesses must protect personal information and promptly report data breaches. A breach of this nature could trigger reporting obligations if customer data was accessed.  
- **Cost of migration** – The shutdown forces you to move workloads before the deadline. Without a clear migration plan, you could face downtime, lost sales, or additional expenses.

### What Happened at Rackspace Spot  

| Date | Event |
|------|-------|
| **17 Nov 2024** | Hackers used compromised credentials to create unauthorised pods, read Kubernetes Secrets, and list nodes/volumes in customer clusters. |
| **18 Nov 2024** | Rackspace discovered the intrusion after a customer report; the admin console was locked down. |
| **21 Nov 2024** | Service was restored following an extended outage. |
| **8 Dec 2026** | Planned permanent shutdown of the Spot platform; all workloads will be terminated and data become inaccessible after 5 pm CT. |

Rackspace has stated that the affected Spot environment is segmented from its core infrastructure and that there is no evidence of unauthorised access to other Rackspace customers. Nonetheless, the company advises **all Spot customers** to treat their API tokens, refresh tokens, kubeconfigs and Kubernetes Secrets as potentially compromised.

### Practical Steps for Australian Small Businesses  

#### 1. Confirm Whether You Use Rackspace Spot  
- Check contracts, invoices or cloud‑management dashboards for any reference to **Rackspace Spot** or Kubernetes workloads.  
- If you’re unsure, contact your IT provider or the person who set up your cloud environment.

#### ​2. Retrieve and Backup Your Data Immediately  
- Download any stored data, configuration files and logs before the 8 December deadline.  
- Store backups in a separate, secure location (e.g., an on‑premises NAS or a trusted Australian cloud provider).

#### 3. Rotate All Secrets and Tokens  
- Assume every API token, refresh token, kubeconfig and Kubernetes Secret is compromised.  
- Generate new credentials and update any applications that rely on them.  

#### 4. Review Access Logs (From 16 Nov 2024 Onwards)  
- Look for suspicious pod prefixes such as **i1**, **glm-**, or **probe**.  
- Identify any unauthorised objects and remove them promptly.  

#### 5. Plan Your Migration  
- Evaluate alternative cloud platforms that meet Australian data‑sovereignty requirements (e.g., Microsoft Azure Australia, Amazon Web Services (Sydney) Region, or local providers).  
- Compare costs, support levels and compatibility with your existing containers.  

#### 6. Strengthen Your Overall Cyber Security Posture  

- **Enable multi‑factor authentication (MFA)** for all cloud and admin accounts.  
- **Use a password manager** and enforce strong, unique passwords.  
- **Regularly patch** container images and underlying operating systems.  
- **Monitor for unusual activity** with a security information and event management (SIEM) tool or a managed service.  

#### 7. Leverage Australian Resources  

- **Australian Cyber Security Centre (ACSC)** – guidance on cloud security and incident response.  
- **ReportCyber** – where you can report a suspected breach or cyber‑crime.  
- **Scamwatch** – information on phishing or social‑engineering attempts that often follow a breach.  
- **Office of the Australian Information Commissioner (OAIC)** – advice on privacy obligations after a data breach.  

### How This Incident Highlights a Broader Trend  

The Rackspace Spot shutdown is a reminder that **small business cyber security** is not just about firewalls or antivirus. Modern applications increasingly rely on containers and cloud‑native services, which introduce new attack surfaces such as Kubernetes Secrets. Even if you are not directly using Spot, the tactics employed—compromised credentials and unauthorised pod creation—are common across many platforms.  

By treating credentials as the most valuable asset and regularly reviewing access, you reduce the risk of a similar breach affecting your business.  

### Take Action Today  

If you suspect that any of your cloud credentials may have been exposed, or simply want to ensure your passwords and secrets are robust, **call CyberSurf on 0400 886 063**. We’ll provide a free **Password Check‑Up** and help you determine whether the Rackspace Spot incident could impact your environment.  

Staying ahead of threats is the best way to protect your customers, your reputation, and your bottom line. Let’s make sure your business is ready.

---

*Source: [Rackspace shuts down Spot cloud platform after security breach](https://www.bleepingcomputer.com/news/security/rackspace-shuts-down-spot-cloud-platform-after-security-breach/). Written in CyberSurf's own words for Australian small businesses.*