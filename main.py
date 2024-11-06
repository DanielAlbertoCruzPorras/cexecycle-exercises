for i in range(1, 11):
    
    row = [i * j for j in range(1, 11)]
    
    # Se usa f-string con un ancho de 3 caracteres para cada número 
    # así se asegura el alineamiento a la derecha
    print(" ".join(f"{num:3}" for num in row)) 
    #print(row) # Fué para visualizar mejor lo que ocurre