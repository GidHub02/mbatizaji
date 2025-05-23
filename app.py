import pandas as pd
from shiny import App, ui, render

df = pd.read_csv("ccd.csv")

customer_name = df['Customer'].tolist()

app_ui = ui.page_fluid(
    ui.h2("Customer Segmentation Data"),
    ui.input_select("Selected_Customer","Select a customer"),
    ui.output_table("Age")
)

def server(input,output,session):
    @output
    @render.table
    def customer_seg():
        return df[df["Customer"] == input.Selected_Customer]
    
app = App(app_ui, server)    #shiny run --reload app