import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt

class LinkStateRoutingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Link State Routing")
        
        self.create_widgets()

        
    def create_widgets(self):
        # Network Topology Input
        ttk.Label(self.root, text="Network Topology").grid(row=0, column=0)
        self.topology_entry = tk.Text(self.root, width=50, height=10)
        self.topology_entry.grid(row=0, column=1)
        
        # Button to Display Graph
        self.display_button = ttk.Button(self.root, text="Display Graph", command=self.display_graph)
        self.display_button.grid(row=1, column=0, columnspan=2)
        
        # Shortest Path Input
        ttk.Label(self.root, text="Shortest Path Source").grid(row=2, column=0)
        self.source_entry = ttk.Entry(self.root, width=20)
        self.source_entry.grid(row=2, column=1)
        
        ttk.Label(self.root, text="Shortest Path Destination").grid(row=3, column=0)
        self.dest_entry = ttk.Entry(self.root, width=20)
        self.dest_entry.grid(row=3, column=1)
        
        # Button to Display Shortest Path
        self.shortest_path_button = ttk.Button(self.root, text="Display Shortest Path", command=self.display_shortest_path)
        self.shortest_path_button.grid(row=4, column=0, columnspan=2)
        
    def display_graph(self):
        topology = self.topology_entry.get("1.0", tk.END)  # Parse topology input and create network graph
        graphs = topology.split('\n\n')  # Split multiple inputs by empty lines
        
        for graph_str in graphs:
            G = nx.Graph()
            edges = graph_str.strip().split('\n')
            for edge in edges:
                nodes, weight = edge.split()[:2], edge.split()[2]
                G.add_edge(nodes[0], nodes[1], weight=int(weight))
            
            # Display Graph
            plt.figure()
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True)
            edge_labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
            plt.show()
        
    def display_shortest_path(self):
        source = self.source_entry.get()
        dest = self.dest_entry.get()
        topology = self.topology_entry.get("1.0", tk.END)  # Parse topology input and create network graph
        graphs = topology.split('\n\n')  # Split multiple inputs by empty lines
        
        for graph_str in graphs:
            G = nx.Graph()
            edges = graph_str.strip().split('\n')
            for edge in edges:
                nodes, weight = edge.split()[:2], edge.split()[2]
                G.add_edge(nodes[0], nodes[1], weight=int(weight))
            
            # Calculate Shortest Path
            try:
                shortest_path = nx.shortest_path(G, source=source, target=dest)
                shortest_path_length = nx.shortest_path_length(G, source=source, target=dest)
                print(f"Shortest Path: {shortest_path}, Length: {shortest_path_length}")
                
                # Highlight Shortest Path on Graph
                plt.figure()
                pos = nx.spring_layout(G)
                nx.draw(G, pos, with_labels=True)
                shortest_path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
                nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='r', width=2)
                edge_labels = nx.get_edge_attributes(G, 'weight')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
                plt.show()
            except nx.NetworkXNoPath:
                print("No path exists between the given source and destination.")

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = LinkStateRoutingApp(root)
    root.mainloop()
