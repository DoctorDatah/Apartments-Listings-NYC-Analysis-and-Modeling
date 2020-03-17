### directory structure
------------

The directory structure of project:

```

├── README.md          <- The top-level README for project report.
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│   └── models         <- models are saved here
│
├── _docs              <- docs used in report
│
│
├── notebooks          <- Jupyter notebooks. 
│
├── images             <- Generated graphics and figures to be used in reporting
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scrap and format data
│   │   └── read_write.py
│   │
│   ├── d01_data           <- Scrap and format data
│   │   └── scrape_renthope.py
│   │   └── format_scraped_data.py
│   │
│   ├── d02_intermediate   <- Initial Data prepossessing  
│   │   └── intial_preprocessing.py
│   │   └── zip_code.py
│   │
│   ├── d03_eda            <- Scripts for EDA figures and calculations 
│   │   ├── listings_eda.py
│   │   └── train_model.py
│   │
│   ├── d04_modeling   <- Scripts for modeling 
        └── features_transformations.py
        └── models.py

```
