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
          
def main():
    print(chromosome_to_cycle([1, -2, -3, 4]))
    
if __name__ == "__main__":
    main()
           

    
