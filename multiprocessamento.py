import multiprocessing 
import os 

#definindo as funções
def primeiroProcesso(): 
    print("ID do processo em execução 'Primeiro Processo': {}".format(os.getpid())) 
  
def segundoProcesso(): 
        print("ID do processo em execução 'Segundo Processo': {}".format(os.getpid())) 

#inicio do programa
if __name__ == "__main__": 
    
    print("ID do processo principal: {}".format(os.getpid())) 

    #criando múltiplos processos
    processoUm = multiprocessing.Process(target=primeiroProcesso) 
    processoDois = multiprocessing.Process(target=segundoProcesso)

    #inicializando os processos
    processoUm.start() 
    processoDois.start() 
    
    print("ID do processo 'Um': {}".format(processoUm.pid)) 
    print("ID do processo 'Dois': {}".format(processoDois.pid)) 
    
    #esperando os processos inicializados terminarem sua execução
    processoUm.join() 
    processoDois.join() 
  
    print("Ambos os processos concluíram a execução!") 
  
    print("O processo 'Um' está ativo: {}".format(processoUm.is_alive())) 
    print("O processo 'Dois' está ativo: {}".format(processoDois.is_alive())) 