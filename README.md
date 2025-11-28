# Project 2: Pandas Time Series Resampling

This project generates simulated daily temperature data using Pandas and NumPy.

## Setup

1.  **Install Python**: Ensure you have Python installed on your system.
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main script to generate and display the data:

```bash
python main.py
```

## Example Output

```text
--- Original Daily Data (First 5 Rows) ---
            Temperature_C
2025-01-01      17.483571
2025-01-02      14.308678
2025-01-03      18.238443
2025-01-04      22.615149
2025-01-05      13.829233

--- Index Check ---
Index type: <class 'pandas.core.indexes.datetimes.DatetimeIndex'>
Index dtype: datetime64[ns]

--- Weekly Average Temperature ---
2025-01-05    17.295015
2025-01-12    15.760840
...

--- Monthly Average Temperature ---
2025-01-31    15.567890
2025-02-28    14.672613
2025-03-31    15.006963
Freq: ME, Name: Temperature_C, dtype: float64

--- Daily Data with 7-Day Rolling Mean (Last 5 Rows) ---
            Temperature_C  7D_Rolling_Mean
2025-03-27      16.379766        14.773820
2025-03-28      13.068638        14.659929
2025-03-29      13.593634        14.492723
2025-03-30      13.546337        14.570814
2025-03-31      17.566198        15.305389
```
