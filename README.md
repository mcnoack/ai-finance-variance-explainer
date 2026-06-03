# AI Finance Variance Explainer

## Overview

This project is a simple AI-assisted finance analysis tool. It uses fake sample budget vs. actual data to identify major variances and generate plain-English commentary for business users.

The goal is to demonstrate how AI, automation, and analytics can support finance teams by reducing manual work and improving the speed and consistency of variance explanations.

## Business Problem

Finance analysts often spend time reviewing budget vs. actual results, identifying major drivers, and writing commentary for leadership. This process can be repetitive, especially when working with large Excel files or recurring monthly reports.

## Solution

This project will:

- Load fake budget vs. actual data
- Calculate favorable and unfavorable variances
- Identify the largest drivers
- Generate a first-draft business explanation
- Provide follow-up questions for the analyst to investigate

## Example Use Case

A finance analyst uploads monthly cost center data. The tool identifies the largest unfavorable variances and creates a draft explanation that can be reviewed, edited, and used in a leadership update.

## Skills Demonstrated

- Python
- Pandas
- Excel/CSV data handling
- Finance analysis
- Variance analysis
- AI prompting
- Business communication

## Data Note

This project uses fake sample data only. It does not include any company data, proprietary information, internal reports, or confidential business details.

## Example Output

```text
Top Variance Drivers
--------------------
Assembly Labor was unfavorable by $75,000. Primary driver: Overtime usage increased due to production delays.
Procurement was unfavorable by $45,000. Primary driver: Supplier price increases on purchased components.
Quality Inspection was unfavorable by $30,000. Primary driver: Additional inspection hours required.
Engineering Support was favorable by $-20,000. Primary driver: Lower contractor utilization than planned.
Maintenance was favorable by $-7,000. Primary driver: Fewer repair events than forecasted.

Draft Leadership Commentary
---------------------------
Overall results were unfavorable by $123,000. The largest unfavorable drivers were related to labor and material cost increases. These were partially offset by favorable contractor and maintenance spending. Recommended follow-up areas include overtime usage, supplier price changes, and quality inspection requirements.
```

## Project Status

In progress.
