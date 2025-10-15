# Monthly Report Automation

## Overview
This automation streamlines a recurring monthly workflow that currently requires manual file handling and formatting.  
The process involves exporting data from a website, cleaning and reformatting it, updating a master Excel workbook, and sending the results via email.

## Goals
- Reduce human error and manual time spent.
- Ensure consistent data formatting and structure.
- Maintain a reliable monthly record through a master Excel file.
- Automate delivery of all final files to a designated recipient.

## Process Summary
1. **Data Export**
    - Log in to the specified website.
    - Download multiple files (e.g., CSV/XLSX formats).

2. **Data Cleaning and Reformatting**
    - Open each exported file.
    - Standardize column order, names, and data types.
    - Apply any required cell formatting or value transformations.

3. **Master File Update**
    - Identify the specific sheet that contributes to the ongoing master workbook.
    - Append or merge the new month's data into the master Excel file.

4. **Email Delivery**
    - Attach all processed files (including the updated master file).
    - Send them to a designated recipient with a standardized email subject and message.

## Future Enhancements
- Schedule the automation to run monthly.
- Add logging for audit trails and failure alerts.
- Store processed files in a versioned archive folder.

## Tools and Technologies (Proposed)
- **Python** for scripting (Pandas, openpyxl, smtplib)
- **Task Scheduler / Cron** for execution
- **Email SMTP** or Outlook API for delivery

---
**Author:** Rob Mahin  
**Last Updated:** 10/14/2025