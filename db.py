from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI
import psycopg2
import yfinance as yf

#data_loc = "/home/ildiko/Desktop/ildiko-web/initial_data.csv"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
#df = pd.read_csv(data_loc)
#del df[df.columns[0]]

#this creates the table and gets pushed on server, if=exist='replace' it will replace it entirely! careful!
#df.to_sql('account_details', con = engine, if_exists='replace')
#print(engine.execute("SELECT * FROM account_details").fetchone())

con = psycopg2.connect(SQLALCHEMY_DATABASE_URI)
cur = con.cursor()

#query to update current prices 
def update_current_price(ticker, new_price):
    sql = """ UPDATE account_details SET current_price=(%s) WHERE stock_symbol = (%s)"""
    with con: 
        cur.execute(sql, (new_price, ticker))

def return_current_prices_list():
    sql = """ SELECT current_price FROM account_details"""
    a = [i[0] for i in engine.execute(sql)]
    return a
    
#query to insert record to db
def insert_stock(symbol, boughtat):
    sql = """ INSERT INTO account_details VALUES(%s, %s, %s)"""
    with con: 
        cur.execute(sql, (symbol, boughtat, boughtat,))

#query to remove record from db 
def remove_stock(symbol):
    sql = """DELETE FROM account_details WHERE stock_symbol =(%s)"""
    with con: 
        cur.execute(sql, (symbol,))
        
#query to sum current price column 
def sum_share_value():
    sql = """SELECT  SUM(current_price) FROM account_details"""
    a = engine.execute(sql)
    return [i for i in a][0][0]

#query to return the amount spent on shares
def sum_amount_spent():
    sql="""SELECT SUM(stock_price_bought) FROM account_details"""
    a = engine.execute(sql)
    return [i for i in a ][0][0]

#query to return held stocks as a list 
def stocks_list():
    sql = """ SELECT stock_symbol FROM account_details"""
    breakdown = [i[0] for i in engine.execute(sql)]
    return breakdown

def boughat_list():
    sql = """ SELECT stock_price_bought FROM account_details"""
    a = [i[0] for i in engine.execute(sql)]
    return a 

#industries column added to table
# sql = """ ALTER TABLE account_details ADD COLUMN IF NOT EXISTS industry varchar"""
# engine.execute(sql)

def add_industry(symbol):
    stock = yf.Ticker(str(symbol))
    industry = stock.info['industry']
    sql = """UPDATE account_details SET industry =%s WHERE stock_symbol = %s"""
    with con: 
        cur.execute(sql, (industry, symbol))
        
#return industries 
def return_industries():
    sql = """ SELECT industry FROM account_details"""
    a = [i[0] for i in engine.execute(sql)]
    return a 

# obj =engine.execute("""SELECT column_name FROM information_schema.columns where TABLE_NAME = 'account_details'""")
#print(sum_share_value())
#print(stocks_list())
#print(engine.execute("SELECT * FROM account_details").fetchall())
