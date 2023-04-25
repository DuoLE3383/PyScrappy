# import the function
from news import scrappi

# call the function with the desired number of pages and genre
df = scrappi(n_pages=5, genre='business')

# display the resulting pandas dataframe
print(df)