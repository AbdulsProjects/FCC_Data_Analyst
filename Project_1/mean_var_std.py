import numpy as np

def calculate(list):
    # If input isnt 9 numbers long, return this and stop function
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
        return
    
    # Creation of the 3,3 matrix from list
    matrix=np.reshape(list,(3,3))
    # Creation of empty dictionary that will store calculated values
    dictionary={'mean':[[0,0,0],[0,0,0],0], 'variance':[[0,0,0],[0,0,0],0], 'standard deviation':[[0,0,0],[0,0,0],0], 
                'max':[[0,0,0],[0,0,0],0], 'min':[[0,0,0],[0,0,0],0], 'sum':[[0,0,0],[0,0,0],0]}
    
    # for loop that calculates and inserts values for rows/columns
    for i in range(3):
        # Calculating means
        dictionary['mean'][0][i] = np.mean(matrix[:,i])
        dictionary['mean'][1][i] = np.mean(matrix[i])
        
        #Calculating variance
        dictionary['variance'][0][i] = np.var(matrix[:,i])
        dictionary['variance'][1][i] = np.var(matrix[i])
        
        #Calculating standard deviation
        dictionary['standard deviation'][0][i] = np.std(matrix[:,i])
        dictionary['standard deviation'][1][i] = np.std(matrix[i])

        #Calculating max
        dictionary['max'][0][i] = np.amax(matrix[:,i])
        dictionary['max'][1][i] = np.amax(matrix[i])

        #Calculating min
        dictionary['min'][0][i] = np.amin(matrix[:,i])
        dictionary['min'][1][i] = np.amin(matrix[i])
        
        #Calculating sum
        dictionary['sum'][0][i] = np.sum(matrix[:,i])
        dictionary['sum'][1][i] = np.sum(matrix[i])

    #Code used to calculate values for flattened matrix
    dictionary['mean'][2] = np.mean(list)
    dictionary['variance'][2] = np.var(list)
    dictionary['standard deviation'][2] = np.std(list)
    dictionary['max'][2] = np.amax(list)
    dictionary['min'][2] = np.amin(list)
    dictionary['sum'][2] = np.sum(list)

    return dictionary
