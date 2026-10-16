# AI Finance Variance Explainer

## Overview

This project is an automated financial variance analysis pipeline. It takes budget vs. actual cost data, isolates key variances, and creates clear executive commentary for leadership.

Having spent 8 years in corporate finance, I built this to eliminate the manual, repetitive work of month-end reporting—while addressing two critical technical constraints: ensuring 100% mathematical accuracy and keeping sensitive cost data private.

## Business Problem

Finance analysts spend hours every month recalculating variances in Excel, digging through cost centers, and drafting executive explanations from scratch. 

While generative AI seems like an obvious solution, applying off-the-shelf chatbots to corporate finance creates two major risks:
1. **AI is bad at math:** Generative models predict words rather than calculating equations. Allowing an LLM to compute variance totals or percentages leads to hallucinations and audit failures.
2. **Data security:** In defense and manufacturing environments, cost center actuals, labor rates, and supplier pricing cannot be uploaded to public cloud APIs like ChatGPT.

## How This Project Solves It

- **Python & Pandas handle all calculations:** All variance math (actual vs. budget, percentage changes, net totals, and ranking) is computed deterministically in code. The AI never calculates numbers; it only interprets the finished math.
- **Runs 100% locally and offline:** The pipeline runs an open-source model (`llama3.2:3b`) on-device using Ollama. No data leaves the machine, satisfying zero-egress and defense-style privacy constraints.
- **Strict output structure via Pydantic:** Instead of generic chatbot text, the model is constrained by a schema that guarantees consistent outputs: an Executive Summary, Key Risks, and Recommended Analyst Inquiries.

## Architecture & Tech Stack

- **Python:** Core pipeline logic
- **Pandas:** Exact financial arithmetic, sorting, and data structuring
- **Pydantic:** Schema validation to enforce structured JSON outputs
- **Ollama (`llama3.2:3b`):** Local, on-premise language model running via Apple Silicon Metal acceleration

## Example Output

```text
=== TOP VARIANCE DRIVERS (Deterministic Math) ===
Assembly Labor         | Unfavorable | $    75,000 ( +15.0%) | Driver: Overtime usage increased due to production delays
Procurement            | Unfavorable | $    45,000 ( +15.0%) | Driver: Supplier price increases on purchased components
Quality Inspection     | Unfavorable | $    30,000 ( +16.7%) | Driver: Additional inspection hours required
Engineering Support    | Favorable   | $    20,000 (  -8.9%) | Driver: Lower contractor utilization than planned
Maintenance            | Favorable   | $     7,000 (  -7.4%) | Driver: Fewer repair events than forecasted

=== GENERATING LOCAL AI COMMENTARY (Ollama Offline) ===

Executive Summary:
The current financial performance of our organization is characterized by an unfavorable net performance of $123,000.00, a total unfavorable drift of $150,000.00, and a total favorable offset of $-27,000.00. The primary drivers of these unfavorable variances are the increased overtime usage in Assembly Labor due to production delays, supplier price increases on purchased components in Procurement, and additional inspection hours required in Quality Inspection. Lower contractor utilization in Engineering Support and fewer repair events in Maintenance provided partial offsets.

Key Risks:
- Increased overtime usage in Assembly Labor due to production delays
- Supplier price increases on purchased components in Procurement
- Additional inspection hours required in Quality Inspection

Recommended Analyst Inquiries:
- Implement measures to reduce overtime usage in Assembly Labor
- Negotiate with suppliers to mitigate price increases on purchased components
- Optimize inspection processes to reduce additional hours required