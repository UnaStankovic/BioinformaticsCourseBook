# za zadat hromozom treba da izdvojimo crvene grane
def chromosome_to_cycle(chromosome):

    nodes = [0 for i in range(2*len(chromosome))]
    
    for j in range(len(chromosome)):
        i = chromosome[j]
        if i > 0:
            #dodajemo cvorove
            nodes[2*j - 1] = 2*i -1
            nodes[2*j] = 2*i
        else:
            nodes[2*j - 1] = -2*i
            nodes[2*j] = -2*i -1
    
    return nodes
    
    
def color_edges(P):
    edges = {}
    nodes = []
    for chrom in P:
        nodes = chromosome_to_cycle(chrom)
        
        for j in range(0, len(chrom)):
            edges[nodes[2*j]] = nodes[2*j + 1]
            edges[nodes[2*j+1]] = nodes[2*j]
        
    
    return edges
    
def main():
    print(color_edges([[1,-2,-3,4]]))
    
if __name__ == "__main__":
    main()
           
