# Inventory-App
This project aims to optimize stock replenishment and automate the process by integrating ERP data related to stock and sales. The data undergoes transformation and is stored in a MySQL database, which serves as the backbone for the dashboard used to track inventory levels and sales performance.

]# Overview
The Inventory App processes stock and sales data originating from an ERP system. The data is extracted, transformed, and loaded (ETL) into a MySQL database, allowing for efficient management and visualization of stock replenishment processes. The resulting dashboard provides real-time insights into inventory status and sales performance, aiding decision-making and optimization strategies.

# Features
* Data extraction from ERP system for stock and sales data
* Transformation of raw data into structured format using Python (Pandas and Numpy)
* Storage of transformed data in MySQL database for easy querying and scalability
* Dynamic dashboard using Dash for visualizing inventory levels and sales performance
* Real-time updates to the dashboard as new data is processed

# Data Processing Flow
1.Extract: Stock and sales data is retrieved from the ERP system.
2.Transform: Using Python libraries (Pandas and Numpy), the data is cleaned, filtered, and aggregated for analysis.
3 Load: Transformed data is stored in a MySQL database for querying and visualization.
4. Visualize: Dash is used to build an interactive dashboard that displays the data and insights related to stock and sales.

# Technologies Used
1. Python: For data processing and backend logic.
2. Pandas: For data manipulation and transformation.
3. Numpy: For numerical operations and calculations.
4. Dash: For creating the interactive dashboard.
5. MySQL: For storing the transformed data and supporting efficient querying.

# Installation
Prerequisites
* Python 3.x
* MySQL database
