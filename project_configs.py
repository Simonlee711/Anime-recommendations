import os

home_dir = os.environ["HOME"]
project_dir = "Anime-recommendations/"


# if not os.path.exists(project_dir):
#     os.makedirs(project_dir)

# should either be "data" or "data2" - need to handle different file naming conventions and file formats
# data 1 is where the batches are created
# data 2 is where the batches are developed and saved
dataset = "data/"
dataset2 = "data2/"


# directory containing .csv files of batched animes
data_dir = os.path.join(project_dir, dataset)
preprocessed_data_dir = os.path.join(project_dir, dataset2)


#################################################
# Model save Configurations
#################################################

X_scaler_pickle = "../../models/train_X_scaler.pkl"
y_scaler_pickle = "../../models/train_y_scaler.pkl"


#################################################
# Batch file configuration
#################################################

# Batch size select
batch_size = 100
# batch_size = 50
# batch_size = 250


#################################################
# Model Configs
#################################################

# padding if input window to avoid issues with convolution at endpoints
padding_size = 4

# number of windows in batch
batch_size = 32

# number of filters in CNN layers
num_filters = 128


#################################################
# Plotting Configs
#################################################
style = 'ggplot'
font_family  = 'sans-serif' 
font_serif = 'Ubuntu' 
font_monospace = 'Ubuntu Mono' 
font_size = 14 
axes_label_size = 12 
axes_label_weight = 'bold' 
axes_title_size = 12 
xtick_label_size = 12 
ytick_label_size = 12 
legend_font_size = 12 
figure_title_size = 12 
image_cmap= 'jet' 
image_interpolation = 'none' 
figure_size = (12, 10) 
axes_grid=True
lines_line_width = 2 
lines_marker_size = 8