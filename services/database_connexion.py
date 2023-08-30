import pandas as pd
import pymongo
import config

#Récupération des variables d'environnement
cluster =config.environ['CLUSTER']
username =config.environ['USERNAME']
dbname =config.environ['DBNAME']
password =config.environ['PASSWORD']

# Connexion à la base de données MongoDB
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{cluster}.kxpd59z.mongodb.net/")

# Spécifiez la base de données que vous souhaitez utiliser
db = client[f"{dbname}"]

# Récupérer les données de chaque collection
balance = pd.DataFrame(list(db["BALANCE"].find())).rename(columns={"value": "BALANCE"})
balance_frequency = pd.DataFrame(list(db["BALANCE_FREQUENCY"].find())).rename(columns={"value": "BALANCE_FREQUENCY"})
purchases = pd.DataFrame(list(db["PURCHASES"].find())).rename(columns={"value": "PURCHASES"})
oneoff_purchases = pd.DataFrame(list(db["ONEOFF_PURCHASES"].find())).rename(columns={"value": "ONEOFF_PURCHASES"})
installments_purchases = pd.DataFrame(list(db["INSTALLMENTS_PURCHASES"].find())).rename(columns={"value": "INSTALLMENTS_PURCHASES"})

cash_advance = pd.DataFrame(list(db["CASH_ADVANCE"].find())).rename(columns={"value": "CASH_ADVANCE"})
purchases_frequency = pd.DataFrame(list(db["PURCHASES_FREQUENCY"].find())).rename(columns={"value": "PURCHASES_FREQUENCY"})
oneoff_purchases_frequency = pd.DataFrame(list(db["ONEOFF_PURCHASES_FREQUENCY"].find())).rename(columns={"value": "ONEOFF_PURCHASES_FREQUENCY"})
purchases_installments_frequency = pd.DataFrame(list(db["PURCHASES_INSTALLMENTS_FREQUENCY"].find())).rename(columns={"value": "PURCHASES_INSTALLMENTS_FREQUENCY"})
cash_advance_frequency = pd.DataFrame(list(db["CASH_ADVANCE_FREQUENCY"].find())).rename(columns={"value": "CASH_ADVANCE_FREQUENCY"})

cash_advance_trx = pd.DataFrame(list(db["CASH_ADVANCE_TRX"].find())).rename(columns={"value": "CASH_ADVANCE_TRX"})
purchases_trx = pd.DataFrame(list(db["PURCHASES_TRX"].find())).rename(columns={"value": "PURCHASES_TRX"})
credit_limit = pd.DataFrame(list(db["CREDIT_LIMIT"].find())).rename(columns={"value": "CREDIT_LIMIT"})
payments = pd.DataFrame(list(db["PAYMENTS"].find())).rename(columns={"value": "PAYMENTS"})
minimum_payments = pd.DataFrame(list(db["MINIMUM_PAYMENTS"].find())).rename(columns={"value": "MINIMUM_PAYMENTS"})

prc_full_payment = pd.DataFrame(list(db["PRC_FULL_PAYMENT"].find())).rename(columns={"value": "PRC_FULL_PAYMENT"})
tenure = pd.DataFrame(list(db["TENURE"].find())).rename(columns={"value": "TENURE"})
cluster_result = pd.DataFrame(list(db["cluster_result"].find())).rename(columns={"value": "cluster_result"})

# Fusionner les dataframes en utilisant la colonne "_id" en commun
liste_balance = [i for i in balance["BALANCE"]]
liste_balance_frequency = [i for i in balance_frequency["BALANCE_FREQUENCY"]]
liste_purchases = [i for i in purchases["PURCHASES"]]
liste_oneoff_purchases = [i for i in oneoff_purchases["ONEOFF_PURCHASES"]]
liste_installments_purchases = [i for i in installments_purchases["INSTALLMENTS_PURCHASES"]]
liste_cash_advance = [i for i in cash_advance["CASH_ADVANCE"]]
liste_purchases_frequency = [i for i in purchases_frequency["PURCHASES_FREQUENCY"]]
liste_oneoff_purchases_frequency = [i for i in oneoff_purchases_frequency["ONEOFF_PURCHASES_FREQUENCY"]]
liste_purchases_installments_frequency = [i for i in purchases_installments_frequency["PURCHASES_INSTALLMENTS_FREQUENCY"]]
liste_cash_advance_frequency = [i for i in cash_advance_frequency["CASH_ADVANCE_FREQUENCY"]]
liste_cash_advance_trx = [i for i in cash_advance_trx["CASH_ADVANCE_TRX"]]
liste_purchases_trx = [i for i in purchases_trx["PURCHASES_TRX"]]
liste_credit_limit = [i for i in credit_limit["CREDIT_LIMIT"]]
liste_payments = [i for i in payments["PAYMENTS"]]
liste_minimum_payments = [i for i in minimum_payments["MINIMUM_PAYMENTS"]]
liste_prc_full_payment = [i for i in prc_full_payment["PRC_FULL_PAYMENT"]]
liste_tenure = [i for i in tenure["TENURE"]]
liste_cluster_result = [i for i in cluster_result["cluster_result"]]


data_copy = pd.DataFrame()
data_copy["BALANCE"] = liste_balance
data_copy["BALANCE_FREQUENCY"] = liste_balance_frequency
data_copy["PURCHASES"] = liste_purchases
data_copy["ONEOFF_PURCHASES"] = liste_oneoff_purchases
data_copy["INSTALLMENTS_PURCHASES"] = liste_installments_purchases

data_copy["CASH_ADVANCE"] = liste_cash_advance
data_copy["PURCHASES_FREQUENCY"] = liste_purchases_frequency
data_copy["ONEOFF_PURCHASES_FREQUENCY"] = liste_oneoff_purchases_frequency
data_copy["PURCHASES_INSTALLMENTS_FREQUENCY"] = liste_purchases_installments_frequency
data_copy["CASH_ADVANCE_FREQUENCY"] = liste_cash_advance_frequency

data_copy["CASH_ADVANCE_TRX"] = liste_cash_advance_trx
data_copy["PURCHASES_TRX"] = liste_purchases_trx
data_copy["CREDIT_LIMIT"] = liste_credit_limit
data_copy["PAYMENTS"] = liste_payments
data_copy["MINIMUM_PAYMENTS"] = liste_minimum_payments

data_copy["PRC_FULL_PAYMENT"] = liste_prc_full_payment
data_copy["TENURE"] = liste_tenure
data_copy["cluster_result"] = liste_cluster_result

data_copy['cluster_result'] = data_copy['cluster_result'].replace({1:'Cluster 1.0', 2:'Cluster 2.0', 3:'Cluster 3.0', 4:'Cluster 4.0'})
# Affichage du DataFrame
#print(data_copy.head())


















    