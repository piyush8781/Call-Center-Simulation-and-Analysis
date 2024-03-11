# Call-Center-Simulation-and-Analysis
## Project Description
This project involves generating random data for the calls table within the call_center database. The calls table simulates real-time call data in a call center environment. Additionally, the call_center database contains several static tables such as companies, issues, locations, csrs, and status.

The primary purpose of this project is to provide a realistic simulation of call center operations. The generated data reflects various aspects of calls received, including location, company, issue type, CSR (Customer Service Representative) handling the call, call duration, status, and customer rating.

## Database Connection
The project utilizes Microsoft SQL Server as the backend database system. Specifically, it connects to the call_center database within the SQL Server instance. The connection is established using the pyodbc library in Python, enabling seamless interaction with the SQL Server database.

## Power BI Integration
The SQL Server database is integrated with Power BI using direct query mode. This integration allows Power BI to retrieve real-time data directly from the SQL Server database, ensuring that the dashboard reflects the latest information regarding call center operations.

## Functionality
* The Python script generates random call data and inserts it into the calls table within the call_center database.
* The data generation process includes random selection of call parameters such as location, company, issue type, CSR, call duration, status, and customer rating.
* Power BI retrieves the call data from the SQL Server database in real-time through direct query mode.
* The Power BI dashboard presents visualizations and insights based on the retrieved call data, allowing users to analyze call center performance and trends.
## Call Center Simulation and Analysis Video Demonstration


https://github.com/piyush8781/Call-Center-Simulation-and-Analysis/assets/163038938/b2d644b8-2576-46d9-b0c1-a81627357e68

