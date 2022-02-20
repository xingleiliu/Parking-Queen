![foxdemo](https://github.com/xingleiliu/Parking-Queen/blob/main/image/log_regtangular.png)
# Parking Queen | Athenahacks 2022 Project 
**Contributors: Xinglei Liu, Qinyang Fang, Yiqi Xiong**

* [Inspiration](##Inspiration)
* What it does
* Perview of Our Website!
* How we built it
* Challenges we faced
* Accomplishments that we're proud of
* New skills we learned
* What's next for Parking Queen
* Reference
* Hold down Cmd (on Windows: Ctrl) and click on [this link](#block-elements) to jump to header `Block Elements`. 

## Inspiration
As we all know, the United States is a country on the wheels, especially Los Angeles. Everyone has suffered from finding a parking spot more or less due to the scarcity of space and information opacity. Not hard to imagine parking around famous tourist attractions like Santa Monica Beach, or a popular restaurant, it can waste a lot of time and make people irritable. The long term consequences of such small things like parking will lead to a bad impression on LA which is also a tourist city, and also decline life expectancy for local residents. We wanted to create a web application that helps tourists and LA residents to park easier with rates and time filters at an input destination. Our mission is to make life easier, our cities more accessible, and our world more connected.
 
## What it does
Parking Queen is a website that can find real-time vacant meter parking spots in LA. This app will allow users to input a destination address, and it can be a broad location, such as Santa Monica Beach, or a specific address like 105 W 9th St. The users are able to select how long they want to park, from 1hr to 4+hours, and the radius within their input address, from 0 to 5 mi, before finding the spots. Space type like single-space or multi-space is also an option for the users to choose. Finally, after clicking the “Find Parking Spaces” button, the website will tell the users how many spots it has found or tell them to try with a larger radius. On the map, different rates are marked with different color pins. There are a total of 4 different colors with legend on the bottom left on the map, which are below $1/hr, $1-$2/hr, $2-$3/hr and above $3/hr. Therefore, all the available spots can be easily seen on the map.

## Perview of Our Website!
![foxdemo](https://github.com/xingleiliu/Parking-Queen/blob/main/image/web_preview.png)

## How we built it
Using the real-time data, the search time frame is set to 10 minutes before the current time. We merged this part with one fixed dataset that contains details about meter locations. The fixed dataset is stored in Firebase. Users can input their destination into the search bar, and the Google Map API will convert it to (latitude, longitude) coordinates. Then, we chose Vincenty’s Distance to calculate the distance between the input destination point and the vacant parking spots. The vacant spaces that meet the filter requirements will have a “True” boolean value, and the results will be spots only marked as “True”. Filters include radius around destination, parking time range, and meter types. Map has pins that show the different parking prices based on different colors at the found spots.
 
## Challenges we faced
Since we were handling the real-time meter parking data, the first challenge that we had was how to visualize them on the map. We tried to use Google My Maps  and ArcGIS Online to make our map, but it is hard for these web mapping applications to automatically update results as data feed updates. 

When cleaning the dataset, dealing with datetime format was very challenging. First, the date format was in string and contained different characters that needed to be removed. Second, we did not know that the time was UTC time which caused no results after searching, and we stalled for a long time.

The last challenging part is to pipeline all the functions and build the web application. We have researched and tried several different frameworks and found Streamlit as a convenient tool to build the web application.

## Accomplishments that we're proud of
We are really proud of the finished product, as there were definitely moments where we doubted if our idea could be realized, but we accomplished our original goal and added more functions than first thought. Additionally, this website can really solve our daily parking problems when coming to school or hanging out with friends. Since the UI is very easy to use (sliders), and the computation time is in seconds, we would definitely use it and recommend it to families and friends.

## New skills we learned
We had a new experience of working with real-time data and non-real-time data at the same time. We learned another map visualization tool Folium that we were not familiar with before and learned how to embed the map on a website. We also got familiar with using web app building tool Streamlit and learned to deploy a web app to make it shareable.

## What's next for Parking Queen
 
In the future, we will combine a “Locate Me” function using some geolocation API, and sort the output parking spots based on nearest to farthest distance. We will have a side-bar to show these sorted results, and add a navigation function for route planning from “Locate Me” to one of the results spots chosen by the user on the UI interface. 

## Reference

Dataset: https://www.laexpresspark.org/la-city-open-data/ <br>
https://towardsdatascience.com/folium-map-how-to-create-a-table-style-pop-up-with-html-code-76903706b88a
