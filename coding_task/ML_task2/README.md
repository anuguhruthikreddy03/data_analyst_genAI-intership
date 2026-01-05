Project: Diminos Pizza – Delivery Performance Analysis
📌 Project Overview
This project analyzes the delivery performance of a Diminos Pizza franchise owned by Kanav. As a freelance Data Scientist, the goal is to evaluate historical order data to ensure the franchise meets its service level agreements (SLA) and identify areas for improvement to help Kanav retain his franchise license.

🎯 Project Goals
Performance Benchmarking: Check if the 95th percentile of order delivery time is less than 31 minutes.

Identify Delays: Determine when and why delivery delays occur.

Actionable Recommendations: Provide data-driven advice to improve service speed and consistency.

🛠️ Tech Stack
Language: Python

Libraries: Pandas (Data manipulation), NumPy (Calculations), Matplotlib & Seaborn (Data Visualization).

🚀 Data Process
Data Loading: Imported raw order data containing order IDs, placement times, and delivery times.

Cleaning & Engineering: * Converted timestamps to datetime objects.

Calculated delivery_time_min for every order.

Extracted time-based features like order_day and order_hour.

Outlier Handling: Identified and accounted for extreme delays (e.g., technical errors showing multi-day delivery times).

📊 Key Insights
SLA Check: The 95th percentile delivery time is 27.26 minutes, which is safely below the 31-minute target.

Average Performance: The average delivery time is approximately 20.50 minutes, with a median of 15.80 minutes.

Sales Patterns:

Revenue and order volume are consistent.

Weekends generally see higher sales than weekdays.

Peak ordering times occur during specific months and days.

Customer Behavior: Most customers order only one or two items per transaction.

✅ Conclusion
The franchise is currently meeting its primary performance goal (95% of orders under 31 minutes). However, ongoing monitoring of weekend peak hours is recommended to maintain these standards as order volume grows
