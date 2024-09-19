import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Frame, Table, Spacer, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import plotly.graph_objects as go
from plotly.offline import plot
import numpy as np

# Define a class to represent the report generator
class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        # Create a PDF canvas
        pdf = canvas.Canvas("report.pdf", pagesize=A4)

        # Set the font and font size
        pdf.setFont("Helvetica", 12)

        # Add a title to the report
        pdf.drawString(1 * inch, 10 * inch, "Vulnerability Report")

        # Add a table to the report
        table_data = self.data.values.tolist()
        table = Table(table_data, colWidths=[1.5 * inch] * len(self.data.columns))
        table.setStyle(TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
        ]))
        table.wrapOn(pdf, 6 * inch, 9 * inch)
        table.drawOn(pdf, 1 * inch, 8 * inch)

        # Add a chart to the report
        plt.figure(figsize=(6, 4))
        sns.countplot(x="vulnerability", data=self.data)
        plt.title("Vulnerability Distribution")
        plt.xlabel("Vulnerability")
        plt.ylabel("Count")
        plt.savefig("chart.png")
        pdf.drawImage("chart.png", 1 * inch, 4 * inch, width=6 * inch, height=4 * inch)

        # Add an interactive chart to the report
        fig = go.Figure(data=[go.Bar(y=self.data['vulnerability'].value_counts())])
        fig.update_layout(title="Vulnerability Distribution", xaxis_title="Vulnerability", yaxis_title="Count")
        plot(fig, filename="interactive_chart.html")
        pdf.drawImage("interactive_chart.html", 1 * inch, 2 * inch, width=6 * inch, height=4 * inch)

        # Add a summary to the report
        summary = self.data.describe()
        summary_table = Table(summary.values.tolist(), colWidths=[1.5 * inch] * len(summary.columns))
        summary_table.setStyle(TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
        ]))
        summary_table.wrapOn(pdf, 6 * inch, 2 * inch)
        summary_table.drawOn(pdf, 1 * inch, 2 * inch)

        # Add a heatmap to the report
        corr_matrix = self.data.corr()
        plt.figure(figsize=(6, 4))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
        plt.title("Correlation Matrix")
        plt.xlabel("Feature")
        plt.ylabel("Feature")
        plt.savefig("heatmap.png")
        pdf.drawImage("heatmap.png", 1 * inch, 4 * inch, width=6 * inch, height=4 * inch)

        # Add a clustering analysis to the report
        from sklearn.cluster import KMeans
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(self.data.drop('vulnerability', axis=1))
        labels = kmeans.labels_
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x=self.data['feature1'], y=self.data['feature2'], hue=labels)
        plt.title("Clustering Analysis")
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.savefig("clustering.png")
        pdf.drawImage("clustering.png", 1 * inch, 4 * inch, width=6 * inch, height=4 * inch)

        # Save the report to a PDF file
        pdf.save()

# Load the data
data = pd.read_csv("ai_training_data.csv")

# Create an instance of the report generator
generator = ReportGenerator(data)

# Generate the report
generator.generate_report()
