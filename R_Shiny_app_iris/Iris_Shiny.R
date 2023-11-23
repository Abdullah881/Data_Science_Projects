# Install and load required packages
if (!require("shiny")) install.packages("shiny")
if (!require("ggplot2")) install.packages("ggplot2")
if (!require("dplyr")) install.packages("dplyr")

library(shiny)
library(ggplot2)
library(dplyr)

# Load the Iris dataset
data(iris)

# Define UI
ui <- fluidPage(
  titlePanel("Iris Data Explorer"),
  
  # Sidebar layout with input and output definitions
  sidebarLayout(
    sidebarPanel(
      # Interactive element: Choose a species
      selectInput("species", "Choose a Species:", choices = unique(iris$Species)),
      
      # Add more interactive elements as needed
    ),
    
    mainPanel(
      # Output: Tabset with plots
      tabsetPanel(
        tabPanel("Scatter Plot", plotOutput("scatterPlot")),
        tabPanel("Box Plot", plotOutput("boxPlot")),
        tabPanel("Histogram", plotOutput("histogram"))
        
        # Add more tabs as needed
      )
    )
  )
)

# Define server logic
server <- function(input, output) {
  # Reactive function to filter data based on selected species
  filtered_data <- reactive({
    iris %>% filter(Species == input$species)
  })
  
  # Output: Scatter plot
  output$scatterPlot <- renderPlot({
    ggplot(filtered_data(), aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
      geom_point() +
      ggtitle("Scatter Plot of Sepal Length vs Sepal Width")
  })
  
  # Output: Box plot
  output$boxPlot <- renderPlot({
    ggplot(filtered_data(), aes(x = Species, y = Sepal.Length)) +
      geom_boxplot() +
      ggtitle("Box Plot of Sepal Length by Species")
  })
  
  # Output: Histogram
  output$histogram <- renderPlot({
    ggplot(filtered_data(), aes(x = Sepal.Length, fill = Species)) +
      geom_histogram(binwidth = 0.2, position = "identity", color = 'blue') +
      ggtitle("Histogram of Sepal Length by Species")
  })
}

# Run the application
shinyApp(ui = ui, server = server)
