# Anime-recommendations

#### Authors

-Eugene Lee

-Simon Lee

# Objective

We are building a Content based recommendation system. The goal is to make informed recommendations of animes based on our dataset that we got from [kaggle](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database) which takes into account data coming from [myanimelist.net](myanimelist.net). We use the BERT transformer model to translate our text and for our machine learning pipeline to work properly. We take into account numerous features as well in order to train our model.

### features
We load our original datafile. Here are the current features: </br>
```anime_id``` - important for the next portion during our web scraping -> url + anime_id = scrape synopsis</br>
```name``` - name of anime</br>
```genre``` - genre of anime (can have multiple genres, rich quality data)</br>
```type``` - type of medium (TV, OVA, Movie)</br>
```episode``` - episode count</br>
```rating``` - ratings based on ?</br>
```members``` - useless metric. </br>
```synopsis``` - lengthy overview of what the anime is about

# library requirement to run the jupyter notebook

```
bs4                       0.0.1                    pypi_0    pypi
conda                     4.12.0           py39hecd8cb5_0   
conda-env                 2.6.0                         1       
mpi                       1.0                       mpich  
numpy                     1.21.5           py39h2e5f0a9_1  
pandas                    1.4.2            py39he9d5cce_0  
pip                       21.2.4           py39hecd8cb5_0      
python                    3.9.12               hdfd78df_0  
requests                  2.27.1             pyhd3eb1b0_0 
scikit-learn              1.0.2            py39hae1ba45_1   
scipy                     1.7.3            py39h8c7af03_0  
seaborn                   0.11.2             pyhd3eb1b0_0   
sympy                     1.10.1           py39hecd8cb5_0  
tqdm                      4.64.0           py39hecd8cb5_0   
```

# How to run the code

simply run the ```anime_pipeline.ipynb``` notebook