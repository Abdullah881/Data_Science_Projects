data <- read.csv("housing.csv")
library(ggplot2)
library(dplyr)
library(hexbin)
# Create a bar chart
ggplot(data, aes(x = ocean_proximity)) +
  geom_bar(fill = "skyblue") +
  labs(title = "Distribution of Ocean Proximity", x = "Ocean Proximity", y = "Count")


# Create a bar chart
ggplot(data, aes(x = ocean_proximity)) +
  geom_bar(fill = "skyblue") +
  geom_text(
    aes(label = ifelse(ocean_proximity == "ISLAND", "5", ""), y = 0),
    vjust = -0.5,
    color = "black",
    size = 5
  ) +
  labs(title = "Distribution of Ocean Proximity", x = "Ocean Proximity", y = "Count")

# Create a scatter plot
ggplot(data, aes(x = population, y = households)) +
  geom_point(color = "blue") +
  labs(title = "Population Vs Households Scatter Plot", x = "Population", y = "Households")


ggplot(data, aes(x = population, y = households)) +
  geom_hex(color = "white", bins = 30) +
  scale_fill_gradient(low = "white", high = "blue") +
  labs(title = "Population Vs Households Hexbin Plot", x = "Population", y = "Households") +
  theme_minimal()

ggplot(data, aes(x = population, y = households)) +
  geom_point(color = "blue", alpha = 0.3) +  # Adjust the alpha value as needed
  labs(title = "Population Vs Households Alpha Scatter Plot", x = "Population", y = "Households")

# Create a scatter plot Total rooms vs total bedrooms
ggplot(data, aes(x = total_rooms, y = total_bedrooms)) +
  geom_point(color = "blue") +
  labs(title = "total_rooms Vs total_bedrooms Scatter Plot", x = "total_rooms", y = "total_bedrooms")




  ggplot(data, aes(x = total_rooms, y = total_bedrooms)) +
    geom_point(color = "red" , size = 3 , shape = 4) +
    labs(title = "total_rooms Vs total_bedrooms Scatter Plot", x = "total_rooms", y = "total_bedrooms")
  
