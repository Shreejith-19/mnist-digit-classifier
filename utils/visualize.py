import pandas as pd
import matplotlib.pyplot as plt
import math

class Visualize:
        def pixels_to_image(self,df_array,indx):
            #this style of doctring commentin is called google-style doctring
            """
            Displays 28x28 grayscale image from raw datframe

            Args:
                df_array(pandas.DataFrame): data of labels and features
            
            Returns:
                None
            """
            image = df_array.drop(columns = ["label"]).iloc[indx].to_numpy().reshape(28,28)
            plt.imshow(image,cmap = "gray")
            plt.axis("off")
            plt.tight_layout()
            plt.show()
        def display_images(self,df_array,number_of_images):
            """
            diplays the first n-images in the dataset from raw data

            Args:
                df_array(pandas.Dataframe): data of labels and features
                number_of_images(int): number of images to be displayed
            
            Returns:
                None
            """
            cols = 5
            rows = math.ceil(number_of_images/cols)
            _, ax = plt.subplots(rows,cols)
            ax = ax.flatten()
            df_features = df_array.drop(columns = ["label"])

            for i in range(number_of_images):
                image = df_features.iloc[i].to_numpy().reshape(28,28)
                ax[i].imshow(image, cmap = "gray")
                #0 -> black 255 -> black
                ax[i].axis("off")
            plt.tight_layout()
            plt.show()
    