#Quelques statistiques descriptives
# calculer la moyenne de la balance
def balance_mean(data):
    balance_mean = round(data['BALANCE'].mean(),2)
    return balance_mean

# calculer le taux de fréquence d'achat moyen
def purchases_freq_mean(data):
    purchases_freq_mean = round(data['PURCHASES_FREQUENCY'].mean()*100,2)
    return purchases_freq_mean

# calculer le nombre total d'achats
def purchases_trx_sum(data):
    purchases_trx_sum = round(float(data['PURCHASES_TRX'].sum()),2)
    return purchases_trx_sum

# calculer le montant des paiements moyens
def payments_mean(data):
    payments_mean = round(data['PAYMENTS'].mean(),2)
    return payments_mean


##Quelques Keys Performances Indicators
# KPI 1 : Solde moyen des comptes
def avg_balance(data):
    avg_balance = data['BALANCE'].mean()
    return avg_balance

# Calcul du ratio d'achats ponctuels
def oneoff_purchase_ratio(data):
    oneoff_purchase_ratio = data['ONEOFF_PURCHASES'].sum() / data['PURCHASES'].sum()
    return oneoff_purchase_ratio

# Calcul du nombre total de transactions pour chaque groupe de clients
def grouped_df(data):
    grouped_df = data.groupby('cluster_result')['PURCHASES_TRX'].sum()
    return grouped_df

