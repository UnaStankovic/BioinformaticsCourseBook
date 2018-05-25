def cycle_to_chromosome(nodes):

    chromosomes = [0 for i in range(len(nodes)//2)]
    
    for j in range(len(nodes)//2):
        if nodes[2*j] < nodes[2*j + 1]:
            chromosomes[j] = nodes[2*j +1] // 2
        else:
            chromosomes[j] = -nodes[2*j] // 2
    
    return chromosomes
    
def main():
    nodes = [1, 2, 4, 3, 6, 5, 7, 8]
    print(cycle_to_chromosome(nodes))
    
if __name__ == "__main__":
    main()
            

