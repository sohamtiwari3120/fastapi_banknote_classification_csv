## BANKNOTE AUTHENTICATION APP



Simple FastAPI application that detects whether a banknote is authentic or not.



#### About the dataset
The dataset was taken from [this kaggle dataset](https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data)

From the kaggle dataset page:
*Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained.*

*Wavelet Transform tool were used to extract features from images.
Dataset can be used for Binary Classification sample problems*

The dataset is a .CSV file containing five columns:

 1. *variance* - (float) variance of Wavelet Transformed image
 2. *skewness* - (float) skewness of Wavelet Transformed image
 3. *curtosis* - (float) curtosis of Wavelet Transformed image
 4. *entropy* - (float) entropy of Wavelet Transformed image
 5. *class* - (integer) label 0 or 1


#### About the model
Simple random forest model is fit on the dataset. Jupyter notebook provided in repository.
The model is then saved as a pickle file and loaded in the FastAPI and Streamlit apps.

#### Deployment
There are three important files in the repository related to deployment:

 - `app.py`: FastAPI code
 - `main.py`: Streamlit code
 - `Dockerfile`: builds python3.8-slim image with necessary dependencies to run FastAPI app. Automatically starts FastAPI server everytime you run the container.


#### Commands
To build Docker image:

    cd <folder_containing_Dockerfile>
    docker build -t <image_name> .

FastAPI server runs by default on port 8000. Change port number inside`main.py`. To start FastAPI server:

    python main.py

To run Streamlit app (runs on port 8501 by default):

    streamlit run app.py --server.port <port_number>

#### Tutorial
Followed this [YouTube playlist.](https://youtube.com/playlist?list=PLZoTAELRMXVNKtpy0U_Mx9N26w8n0hIbs)