#!/usr/bin/env python

# get csv file created at task_2 and generate report (calculate amount of pages) to pdf file

from reportlab.pdfgen import canvas
import csv

def countCsvRows(filePath):
    with open(filePath, 'r') as csvFile:
        csvDataReader = csv.reader(csvFile)
        rowCount = sum(1 for row in csvDataReader)
    return rowCount

def createPdfReport(filePath):
    rowCount = countCsvRows(filePath)

    c = canvas.Canvas("report.pdf")
    c.drawString(100, 750, f"Amount of links in {filePath}: {rowCount}")
    c.save()

createPdfReport("./sitemap.csv")