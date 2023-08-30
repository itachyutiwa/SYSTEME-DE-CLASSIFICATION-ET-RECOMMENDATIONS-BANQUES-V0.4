import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import services.statistiques_et_kpi as statistiques_et_kpi


# Affichage de l'histogramme du solde des comptes dans le
def hist_solde_compte(data):
    fig = px.histogram(data, x='BALANCE', nbins=20, title='',
                       labels={'BALANCE':'Solde', 'Nombre':'Fréquence'})
    fig.update_traces(marker_color='blue')  # Change la couleur du graphique en bleu
    fig.add_vline(x=statistiques_et_kpi.avg_balance(data), line_color='red', line_dash='dash', line_width=2,
                  annotation_text=f'Solde moyen: {statistiques_et_kpi.avg_balance(data):.2f}', annotation_position='top left')
    return fig


def pie_ratio_achats_ponctuels(data):
    fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
    
    # Ajout du graphique camembert
    brown_colors = ['#8B0000', ' #DC143C']
    fig.add_trace(go.Pie(labels=['Achats ponctuels', 'Achats en plusieurs fois'],
                         values=[statistiques_et_kpi.oneoff_purchase_ratio(data), 1-statistiques_et_kpi.oneoff_purchase_ratio(data)],
                         textposition='inside',
                         hole=0.6,
                         showlegend=False,
                         marker=dict(colors=brown_colors)), 1, 1)
    
    # Ajout du titre
    fig.update_layout(title={'text': "",
                             'y':0.90,
                             'x':0.50,
                             'xanchor': 'center',
                             'yanchor': 'top'})
    
    # Ajout de l'annotation
    fig.add_annotation(text='Majorité des achats: Achats ponctuels',
                       x=0.70,
                       y=0.60,
                       showarrow=True,
                       arrowhead=1,
                       arrowcolor='black',
                       arrowsize=1.5,
                       arrowwidth=2,
                       ax=80,
                       ay=-70)

    return fig

def barr_transaction_par_grp_client(data):
    sorted_clusters = statistiques_et_kpi.grouped_df(data).sort_values().index
    cluster_map = {cluster: i for i, cluster in enumerate(sorted_clusters)}

    # Définir la palette de couleurs pour chaque cluster
    colors = ['red', 'blue', 'purple', 'orange']

    # Création du graphique en barres groupées pour le nombre de transactions par groupe de clients
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=[cluster_map[cluster] for cluster in statistiques_et_kpi.grouped_df(data).index], 
        y=statistiques_et_kpi.grouped_df(data).values,
        marker_color=[colors[cluster_map[cluster]] for cluster in statistiques_et_kpi.grouped_df(data).index]
    ))

    # Configuration des axes et du titre
    fig.update_layout(
        xaxis_title='Groupe de clients',
        yaxis_title='Nombre total de transactions',
        title=''
    )

    # Ajout de la légende pour les couleurs de chaque cluster
    for i in cluster_map.values():
        fig.add_trace(go.Scatter(x=[None], y=[None], mode='markers', marker=dict(size=10, color=colors[i]), name='Cluster {}'.format(i+1)))

    return fig


def nuage_de_points_montant_total_des_achats(data):
    fig = px.scatter(data, x='ADB', y='TOTAL_PURCHASES', color='cluster_result', color_discrete_sequence=px.colors.qualitative.Dark24)
    fig.update_traces(marker=dict(size=5))
    fig.update_layout(title='',
                      xaxis_title='Solde moyen quotidien (ADB)',
                      yaxis_title='Montant total des achats')
    return fig
