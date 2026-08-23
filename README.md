# Administrative Data Quality Monitor 🌷

An interactive administrative data review tool built with Python and Streamlit.

This project simulates a simple administrative workflow where operational records need to be checked before further processing. The app helps identify incomplete records, duplicate document IDs, overdue tasks, inconsistent statuses, and records that may require follow-up.

## Live Demo

Coming soon.

## What This Project Does

The app reviews administrative records and automatically checks for common data quality issues such as:

• Missing required information  
• Duplicate document IDs  
• Overdue open records  
• Completed records without a completion date  
• Completion dates that do not match the current status  
• Open records that have remained unresolved for more than 30 days  

Records with issues are organized into a follow-up queue based on their review priority.

## Main Features

### Administrative Health Summary

Provides a quick overview of:

• Total records checked  
• Clear records  
• Records requiring review  
• Administrative health score  
• Overdue records  

### Follow-up Queue

Records requiring attention can be filtered by:

• Priority  
• Department  
• Person in Charge (PIC)  

This makes it easier to identify which records should be handled first.

### PIC Workload

The app summarizes the number of open administrative records assigned to each PIC, providing a simple view of current workload distribution.

### Data Upload

Users can:

• Try the built-in synthetic dataset  
• Upload their own CSV file  
• Upload their own Excel file  

### Export Results

Reviewed records can be downloaded as CSV for further administrative processing or analysis.

## Workflow

```text
Administrative Records
        ↓
Data Quality Check
        ↓
Issue Detection
        ↓
Priority Assignment
        ↓
Follow-up Queue
        ↓
PIC Workload Review
        ↓
Export Reviewed Data
```

## Tools

Python  
Pandas  
Streamlit  
OpenPyXL  

## Dataset

The built-in dataset is synthetically generated for demonstration purposes.

It represents administrative records such as purchase requests, travel requests, invoices, employee documents, internal memos, asset records, and vendor documents.

No confidential organizational data is used in this project.

## Why I Built This

Administrative work often involves more than entering data. Records also need to be checked for completeness, consistency, deadlines, and follow-up status.

I built this project to demonstrate how a simple data workflow can support administrative monitoring while reducing the time needed to manually review large numbers of records.

## Run Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run admin_quality_workspace.py
```

## Project Structure

```text
administrative-data-quality-monitor/
├── admin_quality_workspace.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Notes

This project is intended for portfolio and learning purposes. The review rules are simplified examples of administrative data quality checks and should not be treated as organizational policies.
