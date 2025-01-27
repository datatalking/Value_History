# Real Estate Data Migration Analytics Project REDMAP

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Coverage](https://img.shields.io/badge/Coverage-85%25-green)
![Status](https://img.shields.io/badge/Status-In_Progress-orange)

## Overview

The Real Estate Data Migration Analytics Project involves the processing and transformation of **81,000,000 property records** from various data sources into a consolidated database. This project establishes **data standards** and prepares the database for **cloud-based hosting and advanced analytics integration**. After consolidating property data, we merge it with an existing real estate database that contains rich datasets, including:

- Property addresses and ownership details
- Sales history and transaction records
- Proximity to schools, public transportation, and essential amenities
- Walkability scores and crime statistics
- Ingesting real estate data from 1973, with annual data dumps from 2017 through 2012 loaded
- Project began in April 2018

This comprehensive migration aims to create a robust, standardized, and scalable real estate data platform for insights and business applications.

---

## Key Features

1. **Multi-Format Data Processing**:
   - Handles data dumps in various formats:
     - v1.0 **CSV**
     - v1.1 **TXT**
     - v1.2 **XLS**
     - v1.9 **TSV**, and **Parquet**.
   - Ensures compatibility across diverse file structures and column mappings.

2. **Standardized Schema Enforcement**:
   - Validates headers against a pre-defined schema.
   - Cleans and transforms raw data into consistent formats (e.g., dates, numerical values).

3. **Database Creation and Population**:
   - Stores standardized records in a **SQLite database** for local processing.
   - Prepares the database for migration to **SQL Server** for cloud hosting.

4. **Rich Data Integration**:
   - Merges property data with additional datasets, such as ownership details, sales history, and location-based metrics.

5. **Cloud Readiness**:
   - Optimizes the database for deployment in **cloud-based platforms** like Azure SQL Database or AWS RDS.

---

## Workflow

### Step 1: Data Extraction and Cleaning

- Identify valid files across dozens of data dumps in CSV, TSV, and Parquet formats.
- Verify headers against expected standards to ensure proper data alignment.
- Clean and normalize data:
  - Convert timestamps to UTC-compliant formats.
  - Normalize numerical columns (e.g., property values).
  - Handle missing or inconsistent entries.

### Step 2: Database Standardization

- Create a structured SQLite database to consolidate property data.
- Implement chunked loading to process large files without overwhelming system resources.
- Enforce primary keys, indexes, and constraints for efficient querying.

### Step 3: Integration with Existing Real Estate Database

- Merge new property data with datasets containing:
  - Property addresses
  - Owner information
  - Historical sales records
  - Proximity metrics (schools, transportation, crime, etc.)

### Step 4: Cloud Migration Preparation

- Optimize the database schema for compatibility with **SQL Server**.
- Validate data types, constraints, and indexes for seamless migration.
- Perform sample migrations to ensure cloud readiness.

---

## Technology Stack

- **Languages**: Python 3.9+
- **Databases**: SQLite (local), SQL Server (target)
- **Libraries**:
  - **pandas**: For data processing and transformation.
  - **sqlite3**: For local database interactions.
  - **pyodbc**: For SQL Server integration.
  - **logging**: For real-time process monitoring.

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/real-estate-migration.git
   cd real-estate-migration
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the project:
   - Update `config.py` with database paths and connection strings.

4. Run the main script:
   ```bash
   python main.py
   ```

---

## Testing

- Unit tests are located in the `tests` folder and ensure:
  - Proper schema validation.
  - Data consistency during transformations.
  - Correct data loading into the database.

- Run tests with:
  ```bash
  pytest --cov=.
  ```

---

## Future Work

- Automate the cloud upload process for large datasets.
- Integrate real-time analytics and dashboards for property insights.
- Expand datasets to include zoning laws, flood risk, and climate data.

---

## Contributors

- **Your Name** - Andrew Schell


---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

