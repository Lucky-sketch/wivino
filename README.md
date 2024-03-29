# wivino

# Project README: Vivino Database Analysis

This project focuses on analyzing the Vivino database using SQL queries. The database contains information about wines, wineries, countries, regions, and more.

## Repository Contents

- `requirements.txt`: This file contains all the dependencies required to set up the project environment. You can install them using the following command:

    ```
    pip install -r requirements.txt
    ```

- `analysis.ipynb`: This Jupyter Notebook file contains the analysis of various questions related to wine, such as the most popular wines and the countries producing the highest-rated wines.

- `tools.py`: This Python file provides a function to find all the tables and connections between tables within the database.

- Database: The database itself contains tables with information about wines, wineries, countries, regions, and other relevant data.

## Important Notes

- **Wineries Table**: The wineries table does not link properly to the wines table. The "Match" column provides only four items, which are not useful. The names of wineries are included in the wine names in the "vintages" table.

- **Wines Count**: The `wines_count` variable is located in the `most_used_grapes_per_country` table. However, it does not make sense because it is the same for all entries, likely representing a worldwide figure rather than per country.

- **Regions Count**: The `regions_count` variable from the `countries` table may not correspond to the actual number of regions found in the database. For example, there may be fewer regions in a country than indicated by the `count` variable.

- **User Structure Count**: It is not clear what the `user_structure_count` variable means.

- **Grape Information**: It is not possible to find the exact grape for an individual wine. String matching can be attempted to circumvent this limitation, but the matching rate may not be very high due to many wines not referencing the name of their grape.

## Contact Information

If you have any questions or inquiries regarding this project, please feel free to email Mark Shevchenko at mark2004kyki@gmail.com.
