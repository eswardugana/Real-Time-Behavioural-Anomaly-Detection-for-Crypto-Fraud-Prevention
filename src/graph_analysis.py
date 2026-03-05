import networkx as nx

def build_transaction_graph(df):
    G = nx.from_pandas_edgelist(
        df,
        source='from_address',
        target='to_address',
        edge_attr='value',
        create_using=nx.DiGraph()
    )
    return G

def calculate_graph_features(G):
    centrality = nx.degree_centrality(G)
    return centrality