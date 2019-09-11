import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "docker",
                                  host = "172.21.0.2",
                                  port = "5432",
                                  database = "lexus")
    cursor = connection.cursor()

    # Create Table
    create_table_query = '''CREATE TABLE mobile(
        ticker   integer          not null
        constraint tickers_data_ticker_foreign
        references "Tickers",
        time    date    not null,
        cotacao double precision,
        P/L     double precision,
        P/VP    double precision,
        PSR     double precision,
           double precision,
        constraint "Tickers_Data_pkey"
        primary key (ticker, time)
        
        
        ); '''


    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")