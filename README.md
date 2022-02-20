# Parking Queen | Athenahacks 2022 Project 
![foxdemo](https://github.com/xingleiliu/Parking-Queen/blob/main/logo_icon.png)

**Contributors: Xinglei Liu, Qinyang Fang, Yiqi Xiong**

## Inspiration

As we all know, the United States is a country on the wheels, especially Los Angeles. Everyone has suffered from finding a parking spot more or less due to the scarcity of space and information opacity. Not hard to imagine parking around famous tourist attractions like Santa Monica Beach, or a popular restaurant, it can waste a lot of time and make people irritable. The long term consequences of such small things like parking will lead to a bad impression on LA which is also a tourist city, and also decline life expectancy for local residents. We wanted to create a web application that helps tourists and LA residents to park easier with rates and time filters at an input destination. Our mission is to make life easier, our cities more accessible, and our world more connected.
 
## What it does
Parking Queen is a website that can find real-time vacant meter parking spots in LA. This app will allow users to input a destination address, and it can be a broad location, such as Santa Monica Beach, or a specific address like 105 W 9th St. The users are able to select how long they want to park, from 1hr to 4+hours, and the radius within their input address, from 0 to 5 mi, before finding the spots. Space type like single-space or multi-space is also an option for the users to choose. Finally, after clicking the “Find Parking Spaces” button, the website will tell the users how many spots it has found or tell them to try with a larger radius. On the map, different rates are marked with different color pins. There are a total of 4 different colors with legend on the bottom left on the map, which are below $1/hr, $1-$2/hr, $2-$3/hr and above $3/hr. Therefore, all the available spots can be easily seen on the map.

## How we built it
Using the real-time data, the search time frame is set to 10 minutes before the current time. We merged this part with one fixed dataset that contains details about meter locations. Users can input their destination into the search bar, and the Google Map API will convert it to (latitude, longitude) coordinates. Then, we chose Vincenty’s Distance to calculate the distance between the input destination point and the vacant parking spots. The vacant spaces that meet the filter requirements will have a “True” boolean value, and the results will be spots only marked as “True”. Filters include radius around destination, parking time range, and meter types. Map has pins that show the different parking prices based on different colors at the found spots.
