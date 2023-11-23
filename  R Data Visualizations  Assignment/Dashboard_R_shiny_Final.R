# Assuming 'shiny' package is installed
# install.packages("shiny")
library(shiny)
data <- read.csv("housing.csv")
library(ggplot2)
library(dplyr)
library(hexbin)

# Define UI
ui <- fluidPage(
  titlePanel("Housing.CSV Visualizations"),
  
  # Define the main panel
  mainPanel(
    h2("Visualization Assignemt"),
    # Your main panel content goes here
  ),
  
  # Define three tabs
  tabsetPanel(
    tabPanel("How many homes Where",
             h3("How many homes are NEAR BAY, <1H OCEAN, INLAND, NEAR OCEAN, and ISLAND"),
             plotOutput("barChart")
    ),
    
    tabPanel("Population VS Households",
             h3("Population VS Households"),
             plotOutput("scatterPlot1")
    ),
    
    tabPanel("Total Rooms VS Total Bedrooms",
             h3("Total Rooms VS Total Bedrooms"),
             plotOutput("scatterPlot2")
    )
  )
)

# Define server logic
server <- function(input, output) {
  output$barChart <- renderPlot({
    ggplot(data, aes(x = ocean_proximity)) +
      geom_bar(fill = "skyblue") +
      geom_text(
        aes(label = ifelse(ocean_proximity == "ISLAND", "5", ""), y = 0),
        vjust = -0.5,
        color = "black",
        size = 5
      ) +
      labs(title = "Distribution of Ocean Proximity", x = "Ocean Proximity", y = "Count")
  })
  
  
  
  
  output$scatterPlot1 <- renderPlot({
    # Create a scatter plot
    ggplot(data, aes(x = population, y = households)) +
      geom_point(color = "blue") +
      labs(title = "Population Vs Households Scatter Plot", x = "Population", y = "Households")
  })
  
  
  output$scatterPlot2 <- renderPlot({
    # Create a scatter plot Total rooms vs total bedrooms
    ggplot(data, aes(x = total_rooms, y = total_bedrooms)) +
      geom_point(color = "red" , size = 3 , shape = 4) +
      labs(title = "total_rooms Vs total_bedrooms Scatter Plot", x = "total_rooms", y = "total_bedrooms")
    
  })
  
  
  
}

# Run the Shiny app
shinyApp(ui = ui, server = server)
