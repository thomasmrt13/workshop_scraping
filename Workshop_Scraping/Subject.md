# Subject

Before continuing, make sure you've done all the [installations](https://github.com/paulmondon/Workshop_Scraping/blob/main/Installations.md)

## Step 01 - Get file

get the `scraping.py` file which contains all the code you will need to complete

## Step 02 - Open palace page

Open palace shop page `https://shop.palaceskateboards.com/` with selenium.

Help yourself with the documentation `https://www.selenium.dev/documentation/`

## Step 03 - Collect all items

To scrap all the items informations we first need to collect all of them.

All items are stored in a div and have a class in common.

![plot](https://github.com/paulmondon/Workshop_Scraping/blob/main/asides/images/workshop.png)

Open the console with f12 and find this class, it will look like this

![plot](https://github.com/paulmondon/Workshop_Scraping/blob/main/asides/images/class.png)

## step 04 - The Availability

Now that we have stored all the articles we want to retrieve the data of these articles.

First of all we want to know if the article is available. For that we will use the button "ADD TO CART" which is only displayed on the available items.

Find the css selector of the button.

![plot](https://github.com/paulmondon/Workshop_Scraping/blob/main/asides/images/add.png)

## step 05 - The Name

Now we are going to retrieve the name of the article.

Find the css selector of the name.

![plot](https://github.com/paulmondon/Workshop_Scraping/blob/main/asides/images/nom.png)

## step 06 - The Price

Now we are going to retrieve the name of the article.

Find the css selector of the name.

![plot](https://github.com/paulmondon/Workshop_Scraping/blob/main/asides/images/disponibilité.png)

## step 07 - The Image

Now we are going to retrieve the image of the article.

Find the css selector of the name.

![plot](https://github.com/paulmondon/Workshop_Scraping/blob/main/asides/images/image.png)
