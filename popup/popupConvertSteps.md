# Steps to generate pop-ups

1. Open `Master NPDES Field Geodatabase Schema Reference.xlsx`
2. Filter the target pop-up, e.g., Structure
3. ~Filter the _View_ column to _TRUE_~
4. Copy the matching columns with the HTML, including the title
5. Open [HTML Table Generator](https://www.tablesgenerator.com/html_tables)
6. Click File > Paste Table Data
7. Paste the data in and hit OK
8. Check _Do not generate CSS_ and click _Generate_
9. Click _Copy to clipboard_ button
10. Paste into Notepad++
11. Open replace dialog
12. Find `(&lt;)|(&gt;)` and replace all with (?1<)(?2>)
13. Insert any Survey123 links at the top
13. Save the HTML table code in GitHub
14. Copy the HTML and paste in AGOL Popup config (custom)
