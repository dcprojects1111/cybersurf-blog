---
title: "VMware vCenter Zero-Day Patch: What to Do Now"
date: "2026-11-20"
image: "/assets/images/vmware-vcenter-zero-day-patch.jpg"
tags: [breaking]
---

*Developing story, last updated 10:30 AM (Brisbane time). We will update this post if things change.*

## What has happened  

Broadcom announced a security update (VMSA‑2026‑0009) on 19 November that patches a critical authentication‑bypass flaw in VMware vCenter Server, the Directory Service component, and related products such as SDDC Manager and VMware Tools for Windows. The vulnerability is tracked as **CVE‑2026‑123890**.  

Researchers at Google’s Mandiant and the Google Threat Intelligence Group say a suspected Chinese state‑linked group, Armory Castle (formerly UNC5221), has been exploiting this zero‑day since early September 2026. The attackers can gain an unauthenticated network connection, bypass login, and obtain an administrator session on the vCenter server. From there they can run commands, steal files (including the vCenter directory database), and create forged authentication tokens that bypass multi‑factor checks.  

Broadcom classifies the fix as an **emergency update** and notes there are no official work‑arounds, although tighter network restrictions and firewall rules can lower exposure. The flaw works whether or not Enhanced Linked Mode is enabled.

## Does it affect you?  

If your business runs any version of **VMware vCenter Server, SDDC Manager or VMware Tools for Windows** that is *earlier* than the versions listed as “fixed” in Broadcom’s advisory, you are potentially vulnerable. This includes installations that are standalone, part of VMware Cloud Foundation, vSphere Foundation, Telco Cloud Platform, or Telco Cloud Infrastructure.  

It is not yet known whether Australian organisations have been targeted, but many small‑to‑medium enterprises use VMware for virtualised servers or desktops. Check your inventory; if you have any of the products above, you should treat the issue as relevant.

## What to do right now  

- **Apply the November 19 patches** (VMSA‑2026‑0009) to every affected VMware component as soon as possible.  
- **Verify your version numbers** against the “fixed” releases listed in the advisory; if you’re unsure, contact your VMware reseller or support line.  
- **Limit network exposure** – restrict inbound traffic to vCenter servers to only trusted IP ranges using firewalls or VLAN segmentation.  
- **Monitor for unusual activity** – look for new admin accounts, unexpected SSO sessions, or unfamiliar file transfers in vCenter logs.  
- **Review privileged accounts** – ensure only required personnel have administrator rights and that strong, unique passwords are used.  
- **General advice:** keep all software up to date, enforce least‑privilege access, and maintain regular backups of critical systems.

## Where to get help  

- **Australian Cyber Security Centre (ACSC)** – https://www.cyber.gov.au for guidance on patching and hardening virtual environments.  
- **ReportCyber** – https://www.cyber.gov.au/report‑cyber‑incidents to log any suspected breach.  
- **VMware status page** – check the official VMware advisory and support portal for the latest patch information.  
- **Your IT provider or managed service partner** – they can verify versions and apply updates on your behalf.

Stay calm and act promptly. If you need a friendly hand walking you through the patching process, give CyberSurf a call on **0400 886 063**. We're here to help Australian businesses stay secure.