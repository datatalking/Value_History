import os
import sqlite3
from pathlib import Path
import pandas as pd
from typing import List, Optional
import logging
from datetime import datetime
import pyodbc


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

EXPECTED_HEADERS = [
		"Major", "Minor", "TaxYr", "OmitYr", "ApprLandVal", "ApprImpsVal",
		"ApprImpIncr", "LandVal", "ImpsVal", "TaxValReason", "TaxStatus",
		"LevyCode", "ChangeDate", "ChangeDocId", "Reason", "SplitCode"]

UN_EXPECTED_HEADERS = ["ZipCode", "Address", "Value"]


class RealEstateDBLoader:
	"""
	Loads real estate data from CSV files into SQLite database.
	"""

	# TODO move out of the class
	EXPECTED_HEADERS = [
		"Major", "Minor", "TaxYr", "OmitYr", "ApprLandVal", "ApprImpsVal",
		"ApprImpIncr", "LandVal", "ImpsVal", "TaxValReason", "TaxStatus",
		"LevyCode", "ChangeDate", "ChangeDocId", "Reason", "SplitCode"
	]
		("Major", "Minor", "TaxYr", "OmitYr", "ApprLandVal", "ApprImpsVal",
		 "ApprImpIncr", "LandVal", "ImpsVal", "TaxValReason", "TaxStatus",
		 "LevyCode", "ChangeDate", "ChangeDocId", "Reason", "SplitCode")

	def __init__(self, db_path: str = "data/real_estate.db"):
		"""
		Initialize the database loader.
		Args: db_path: Path to SQLite database file
		"""
		self.db_path = Path(db_path)
		self.db_path.parent.mkdir(parents=True, exist_ok=True)

	def _create_table(self, conn: sqlite3.Connection) -> None:
		"""
		Create the real estate table if it doesn't exist.
		"""

		create_table_sql = """
        CREATE TABLE IF NOT EXISTS real_estate (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Major TEXT,
            Minor TEXT,
            TaxYr INTEGER,
            OmitYr INTEGER,
            ApprLandVal INTEGER,
            ApprImpsVal INTEGER,
            ApprImpIncr INTEGER,
            LandVal INTEGER,
            ImpsVal INTEGER,
            TaxValReason TEXT,
            TaxStatus TEXT,
            LevyCode TEXT,
            ChangeDate TIMESTAMP,
            ChangeDocId TEXT,
            Reason TEXT,
            SplitCode TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
		conn.execute(create_table_sql)

	def _verify_headers(self, csv_path: Path) -> bool:
		"""
		Verify if CSV file has the expected headers.
		Args: csv_path: Path to CSV file
		Returns: bool: True if headers match, False otherwise
		"""
		try:
			df = pd.read_csv(csv_path, nrows=0)
			csv_headers = df.columns.tolist()
			return set(csv_headers) == set(self.EXPECTED_HEADERS)
		except Exception as e:
			logger.error(f"Error reading CSV headers from {csv_path}: {str(e)}")
			return False

	def find_valid_csv(self, search_paths: List[str] = [".", "data"]) -> Optional[Path]:
		"""
		Find first CSV file with matching headers in given paths.
		Args: search_paths: List of paths to search for CSV files
		Returns: Optional[Path]: Path to valid CSV file or None if not found
		"""
		for path in search_paths:
			base_path = Path(path)
			if not base_path.exists():
				continue

			for file in base_path.glob("*.csv"):
				if self._verify_headers(file):
					logger.info(f"Found valid CSV file: {file}")
					return file

		logger.warning("No valid CSV files found")
		return None

	def load_data(self, csv_path: Path) -> bool:
		"""
		Load data from CSV file into SQLite database.
		Args: csv_path: Path to CSV file
		Returns: bool: True if successful, False otherwise
		"""
		try:
			df = pd.read_csv(csv_path)

			# Convert ChangeDate to datetime
			df['ChangeDate'] = pd.to_datetime(df['ChangeDate'])

			with sqlite3.connect(self.db_path) as conn:
				self._create_table(conn)

				# Insert data in chunks to handle large files
				chunk_size = 1000
				for i in range(0, len(df), chunk_size):
					chunk = df.iloc[i:i + chunk_size]
					chunk.to_sql('real_estate', conn, if_exists='append', index=False)

				logger.info(f"Successfully loaded {len(df)} records into database")
				return True

		except Exception as e:
			logger.error(f"Error loading data: {str(e)}")
			return False


def main():
	"""
	Main function to run the database loader.
	"""

	loader = RealEstateDBLoader()
	csv_file = loader.find_valid_csv()

	if csv_file:
		if loader.load_data(csv_file):
			logger.info("Data loading completed successfully")
		else:
			logger.error("Failed to load data")
	else:
		logger.error("No valid CSV file found")


if __name__ == "__main__":
	main()