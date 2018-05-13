def cycle_to_chromosome(nodes):

    chromosomes = [0 for i in range(len(nodes)//2)]
    
    for j in range(len(nodes)//2):
        if nodes[2*j] < nodes[2*j + 1]:
            chromosomes[j] = nodes[2*j +1] // 2
        else:
            chromosomes[j] = -nodes[2*j] // 2
    
    return chromosomes
    
def cycle_to_chromosome(nodes):

    chromosomes = [0 for i in range(len(nodes)//2)]
    
    for j in range(len(nodes)//2):
        if nodes[2*j] < nodes[2*j + 1]:
            chromosomes[j] = nodes[2*j +1] // 2
        else:
            chromosomes[j] = -nodes[2*j] // 2
    
    return chromosomes
    
def color_edges(P):
    edges = {}
    
    for chrom in P:
        nodes = chromosome_to_cycle(chrom)
        
        for j in range(len(chrom)):
            edges[nodes[2*j - 1]] = nodes[2*j]
            edges[nodes[2*j]] = nodes[2*j -1]
        
    
    return edges
    

def graph_to_genom(genome_graph):
    P = []
    for nodes in genome_graph:
        chromosome = cycle_to_chromosome(nodes)
        P.append(chromosome)
    return P
        
        
           
def main():
    print(color_edges([[1,-2,-3,4]]))
    
if __name__ == "__main__":
    main()

            

