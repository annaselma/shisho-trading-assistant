from binance import Client
from  datetime import datetime
import pandas as pd
import configparser
import time
from sqlalchemy import create_engine,inspect,text
from sqlalchemy_utils import database_exists, create_database

config = configparser.ConfigParser()
config.read("config.ini")

key = config["binance"]["api_key"]
secret = config["binance"]["api_secret"]



def get_historical_data(market):
    client = Client(key,secret)
    start_date=str(datetime(2005,1,1).timestamp()*1000)
    end_date=str(datetime.now().timestamp()*1000)

    historical_data = client.get_historical_klines(market, Client.KLINE_INTERVAL_1DAY, start_date, end_date)
    historical_df =pd.DataFrame(historical_data)

    historical_df.columns = ['open_time','open','high','low','close','volume','close_time','quote_asset_volume','number_of_trades','tb_base_volume','tb_quote_volume','ignore']
    historical_df['open_time'] = pd.to_datetime(historical_df['open_time']/1000, unit = 's')
    historical_df['close_time'] = pd.to_datetime(historical_df['close_time']/1000, unit = 's')
    historical_df['market'] = [market for i in range(historical_df['open_time'].size)]
    numeric_columns = ['open','high','low','close','volume','quote_asset_volume','number_of_trades','tb_base_volume','tb_quote_volume']
    historical_df[numeric_columns] = historical_df[numeric_columns].apply(pd.to_numeric, axis = 1)
    
    return historical_df

def get_dayli_data(market):
    client = Client(key,secret)
    today_date=datetime.now()

    start_date=str(datetime(today_date.year,today_date.month,today_date.day).timestamp()*1000)
    end_date=str(datetime.now().timestamp()*1000)

    historical_data = client.get_historical_klines(market,Client.KLINE_INTERVAL_1DAY,start_date,end_date)
    historical_df =pd.DataFrame(historical_data)

    historical_df.columns = ['open_time','open','high','low','close','volume','close_time','quote_asset_volume','number_of_trades','tb_base_volume','tb_quote_volume','ignore']
    historical_df['open_time'] = pd.to_datetime(historical_df['open_time']/1000, unit = 's')
    historical_df['close_time'] = pd.to_datetime(historical_df['close_time']/1000, unit = 's')
    historical_df['market'] = [market for i in range(historical_df['open_time'].size)]
    numeric_columns = ['open','high','low','close','volume','quote_asset_volume','number_of_trades','tb_base_volume','tb_quote_volume']
    historical_df[numeric_columns] = historical_df[numeric_columns].apply(pd.to_numeric, axis = 1)
    
    return historical_df




def save_historical_database(dataframe):
    engine = create_engine(
        "mariadb+mysqldb://{user}:{password}@{host}:{port}/{database}".format(
            user=config["database"]["DB_USER"],
            password=config["database"]["DB_PASSWORD"],
            host=config["database"]["DB_HOST"],
            port=config["database"]["DB_PORT"],
            database=config["database"]["DB_DATABASE"],
        )
    )

    if not database_exists(engine.url):
        #print("Database not exist!")
        create_database(engine.url, encoding='utf8')
    else:
        #print("Database exist!")
        engine.connect()
    
    inspector = inspect(engine)
    table_name="historic_data"
    
    if not inspector.has_table(table_name):
        dataframe.to_sql(table_name, engine, index=False, if_exists='replace')
    else:
        market=dataframe['market'][0]
                
        query = f"DELETE FROM {table_name} WHERE  market='{market}';commit;"

        with engine.connect() as connection:
            connection.execute(text(query))
        
        dataframe.to_sql(table_name, engine, index=False,if_exists='append')



def save_dayli_database(dataframe):
    engine = create_engine(
        "mariadb+mysqldb://{user}:{password}@{host}:{port}/{database}".format(
            user=config["database"]["DB_USER"],
            password=config["database"]["DB_PASSWORD"],
            host=config["database"]["DB_HOST"],
            port=config["database"]["DB_PORT"],
            database=config["database"]["DB_DATABASE"],
        )
    )

    if not database_exists(engine.url):
        #print("Database not exist!")
        create_database(engine.url, encoding='utf8')
    else:
        #print("Database exist!")
        engine.connect()

    inspector = inspect(engine)
    table_name="streaming_data"
    
    if not inspector.has_table(table_name):
        dataframe.to_sql(table_name, engine, index=False, if_exists='replace')
    else:
        today_date=dataframe['open_time'][0]
        market=dataframe['market'][0]
                
        query = f"DELETE FROM {table_name} WHERE open_time = '{today_date}' and market='{market}';commit;"

        with engine.connect() as connection:
            connection.execute(text(query))
            
        dataframe.to_sql(table_name, engine, index=False, if_exists='append')


def main():
    print("Script started.")
    symbole="ETHBTC"

    time.sleep(5)
    print("Fetch historical data...")
    his_data=get_historical_data(symbole)
    save_historical_database(his_data)
    print("Fetch historical data... : OK")
    
    try:
        while True:
            print("Fetch streaming data...")
            val_ret = get_dayli_data(symbole)
            save_dayli_database(val_ret)
            print("Fetch streaming data... : OK")
            time.sleep(5)  # pause de 5 secondes
            print("Script is still running...")
            time.sleep(60) # pause de 60 secondes

            
    except KeyboardInterrupt:
        print("Script terminated by user.")


if __name__ == "__main__":
    main()
