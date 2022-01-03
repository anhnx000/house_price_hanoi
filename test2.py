from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from json import dumps
import sqlite3

import csv, sqlite3
df = pandas.read_csv(C:\Users\XA\Documents\python_rest_1611\python_rest_1611\data_clean_train_15_11.csv)
df.to_sql(table_name, conn, if_exists='append', index=False)