import pandas as pd

# df = pd.read_json('users.json')
# df.to_csv('users.csv')

def csv():
    pd.read_json('C:/Users/Ivson/PycharmProjects/'
                 'Frexco/templates/static/users.json').to_csv('C:/Users/Ivson/PycharmProjects/'
                                                              'Frexco/templates/static/users.csv')

def xlsx():
    pd.read_json('C:/Users/Ivson/PycharmProjects/'
                 'Frexco/templates/static/users.json').to_excel('C:/Users/Ivson/PycharmProjects/'
                                                                'Frexco/templates/static/users.xlsx')
