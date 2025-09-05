# Freelancer Revenue Insight Dashboard

## Project Overview
The Freelancer Revenue Insight Dashboard is a data analysis project designed to visualize and analyze the revenue, client trends, service performance, and invoice cycles for a solopreneur freelance business. This project demonstrates how Python can transform simple income data into actionable business insights.

## Raw Data
The raw data used in this project is contained in the `freelancer_income_data.csv` file. The dataset includes the following columns:

- **Invoice Date**: The date when the invoice was issued.
- **Client**: The name of the client for whom the service was provided.
- **Service**: The type of service rendered.
- **Amount**: The amount charged for the service.
- **Payment Date**: The date when the payment was received.
- **Status**: The payment status of the invoice (e.g., Paid, Unpaid).

### Sample Data
| Invoice Date | Client          | Service              | Amount | Payment Date | Status |
|--------------|-----------------|----------------------|--------|--------------|--------|
| 9/12/2024    | ABC Corp        | Web Scraping         | 450    | 9/15/2024    | Paid   |
| 9/20/2024    | XYZ Ltd         | RPA Audit            | 600    | 9/25/2024    | Paid   |
| 10/1/2024    | Freelance Co    | Data Cleanup         | 300    |              | Unpaid |
| 10/5/2024    | Tech Solutions   | Data Analysis        | 500    | 10/10/2024   | Paid   |
| 10/10/2024   | Creative Agency  | Web Development      | 700    | 10/15/2024   | Paid   |
| 10/15/2024   | Marketing Inc    | SEO Optimization     | 400    |              | Unpaid |
| 11/1/2024    | Design Studio    | Graphic Design       | 350    | 11/5/2024    | Paid   |
| 11/10/2024   | ABC Corp        | Web Scraping         | 450    | 11/15/2024   | Paid   |
| 11/20/2024   | XYZ Ltd         | RPA Audit            | 600    |              | Unpaid |
| 12/1/2024    | Freelance Co    | Data Cleanup         | 300    | 12/5/2024    | Paid   |
| 12/10/2024   | Tech Solutions   | Data Analysis        | 500    |              | Unpaid |
| 12/15/2024   | Creative Agency  | Web Development      | 700    | 12/20/2024   | Paid   |

## Code Overview
The code for this project is contained in the `freelancer_insights.ipynb` Jupyter Notebook. The notebook includes the following sections:

1. **Data Loading**: The code loads the CSV data into a Pandas DataFrame.
2. **Exploration**: Initial exploration of the dataset using `head()`, `info()`, and `describe()` methods.
3. **Visualizations**:
   - **Client Distribution Pie Chart**: Visualizes the distribution of revenue by client.
   - **Top 5 Most Profitable Services**: Bar chart showing the top five services based on revenue.
   - **Invoice Payment Delay Histogram**: Histogram displaying the payment delays for paid invoices.
   - **Monthly Revenue Trend Line**: Line chart showing the trend of monthly revenue.
4. **Linear Regression**: Implements a linear regression model to predict future revenue based on historical data.
5. **Scatter Plot with Regression Line**: Visualizes actual monthly revenue alongside the regression line and predicted revenue for the next month.

### Required Libraries
The following Python libraries are required to run the code:
- `pandas`
- `matplotlib`
- `scikit-learn`

You can install these libraries using pip:
```bash
pip install pandas matplotlib scikit-learn
