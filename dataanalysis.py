import pandas as pd
import csv

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm
import operator

def sort_by_column(csv_cont, col, reverse=False):
    header = csv_cont[0]
    body = csv_cont[1:]
    if isinstance(col, str):
        col_index = header.index(col)
    else:
        col_index = col
    body = sorted(body,
           key=operator.itemgetter(col_index),
           reverse=reverse)
    body.insert(0, header)
    return body

def csv_to_list(csv_file, delimiter=','):
    with open(csv_file, 'r') as csv_con:
        reader = csv.reader(csv_con, delimiter=delimiter)
        return list(reader)

def convert_cells_to_floats(csv_cont):
    for row in range(len(csv_cont)):
        for cell in range(len(csv_cont[row])):
            try:
                csv_cont[row][cell] = float(csv_cont[row][cell])
            except ValueError:
                pass



def write_csv(dest, csv_cont):
    """ New CSV file. """
    with open(dest, 'wb') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        for row in csv_cont:
            writer.writerow(row)

csv_cont = csv_to_list('house.csv')


convert_cells_to_floats(csv_cont)
csv_sorted = sort_by_column(csv_cont, 'price')
# print csv_sorted
write_csv('housesorted.csv', csv_sorted)


data = pd.read_csv('housesorted.csv',usecols =['price','tax','year','bedroom','bathroom','lot'],error_bad_lines=False )
#sns.pairplot(data, x_vars=['tax','year','bedroom'], y_vars='price', size=7, aspect=0.8)
#plt.show()
data = data[['price','tax','year','bedroom','bathroom','lot']]
x_vars=['tax','year','bedroom','bathroom','lot']

X = data[x_vars]
print type(X)

y = data['price']

X_train,X_test, y_train, y_test = train_test_split(X, y, random_state=1)

linreg = LinearRegression()
model=linreg.fit(X, y)

linear_model = sm.OLS(y,X)
results = linear_model.fit()
print results.summary()
print linreg.intercept_

B1,B2,B3,B4,B5 = linreg.coef_[0],linreg.coef_[1],linreg.coef_[2],linreg.coef_[3],linreg.coef_[4]
print linreg.coef_
x1,x2,x3,x4,x5 = input('input as: tax,year,bedroom,bathroom,lot')



y_pred = B0 + B1*x1 + B2*x2 + B3*x3 + B4*x4 +B5*x5
print 'y_pred=' + str(y_pred)
