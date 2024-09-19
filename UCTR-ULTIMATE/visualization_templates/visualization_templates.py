import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class VisualizationTemplates:
    def __init__(self, incident_data):
        self.incident_data = incident_data

    def generate_visualizations(self):
        # Generate a bar chart of incident types
        plt.figure(figsize=(6, 4))
        sns.countplot(x="incident_type", data=self.incident_data)
        plt.title("Incident Types")
        plt.xlabel("Incident Type")
        plt.ylabel("Count")
        plt.savefig("incident_types.png")

        # Generate a heatmap of incident response steps
        corr_matrix = self.incident_data.corr()
        plt.figure(figsize=(6, 4))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
        plt.title("Incident Response Steps")
        plt.xlabel("Step")
        plt.ylabel("Step")
        plt.savefig("incident_response_steps.png")

        # Generate a scatter plot of incident response times
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x="incident_response_time", y="incident_severity", data=self.incident_data)
        plt.title("Incident Response Times")
        plt.xlabel("Response Time")
        plt.ylabel("Severity")
        plt.savefig("incident_response_times.png")

# Load the incident data
incident_data = pd.read_csv("incident_data.csv")

# Create an instance of the visualization templates
templates = VisualizationTemplates(incident_data)

# Generate the visualizations
templates.generate_visualizations()
