import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456@sql",
  database="dbteste3"
)

mycursor = mydb.cursor()

trimestres = ['1T2020', '1T2021', '2T2020', '2T2021', '3T2020', '3T2021', '4T2020', '4T2021']

def passarTabelasTri(trimestres):
    try:
        for trimestre in trimestres:
            mycursor.execute(f"""
                CREATE TABLE trimestre{trimestre}(
                DATA DATE,
                REG_ANS text,
                CD_CONTA_CONTABIL text,
                DESCRICAO text,
                VL_SALDO_FINAL text    
            )
            """)

            # csv_data = csv.reader(open(f'teste3/{trimestre}.csv'), delimiter=';')
            # next(csv_data)
            # data = csv_data.split()
            # sql = (f'INSERT INTO trimestre{trimestre} (DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_FINAL) VALUES ()')
            # for row in data:
            #     mycursor.execute(sql, row)

            # mycursor.execute(f"""
            #     LOAD DATA INFILE '/teste3/1T2020.csv'
            #     INTO TABLE trimestre{trimestre}
            #     FIELDS TERMINATED BY ';'
            #     ENCLOSED BY '"'
            #     LINES TERMINATED BY '\n'
            #     IGNORE 1 ROWS;
            # """)


            with open(f'teste3/{trimestre}.csv', 'r') as f:
                next(f) 
                fs = f.split()               
                sql = (f'INSERT INTO trimestre{trimestre} (DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_FINAL)')             
                for row in fs:
                    mycursor.execute(sql,row)                    

        print(f'{trimestre} copiado')

        #passarTabelaRegistro()
    except Exception as e:
        print(e)

def passarTabelaRegistro():
    try: 
        mycursor.execute("""
            CREATE TABLE registro(
            Registro_ANS text,
            CNPJ text,
            Razão_Social text,
            Nome_Fantasia text,
            Modalidade text,
            Logradouro text,
            Número text,
            Complemento text,
            Bairro text,
            Cidade text, 
            UF text,
            CEP text,
            DDD text,
            Telefone text,
            Fax text, 
            Endereço_eletrônico text,
            Representante text,
            Cargo_Representante text,
            Data_Registro_ANS DATE
        )
        """)
        
    except Exception:
        print('Tabela Registro passado para o BD')

passarTabelasTri(trimestres)