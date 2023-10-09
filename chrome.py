#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import required modules

import pandas as pd
import numpy as np
import csv

# For connect to google sheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from df2gspread import df2gspread as d2g


# Configure the connection
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

# Give the path to the Service Account Credential json file
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/christophertrauco/.config/gspread/poc-g-sheets-00caec6d2d75.json', scope)
# Authorise your Notebook
gc = gspread.authorize(credentials)

file = 'groups'

##### Trau.co Email Groups

# https://docs.google.com/spreadsheets/d/1_Z7NKyuxHwCLe3BBYnc1lVVbuAOmHsRoBm9a1KzIC_o/edit#gid=0
spreadsheet_key = "1X6SJZ0rlVuqhbNdsfYLTnaSXQOgRKWQY7NR2DRiIgB"

# csv to df
data = f"{file}.csv"
df = pd.read_csv(data)
df2 = df.reset_index()

wks_name = 'Data'
cell_of_start_df = 'A1'
# upload the dataframe of the clients we want to delete
d2g.upload(df2,
           spreadsheet_key,
           wks_name,
           credentials=credentials,
           col_names=True,
           row_names=False,
           start_cell = cell_of_start_df,
           clean=True)
print ('The sheet is updated successfully')
