# 1- First-fit algorithm by Pedro Vieira.


#Função que fará o processo de alocação
def firstFit(blockSize, m, processSize, n):

  #Passará a ID do bloco para o processo
  allocation = [-1] * n

  #Inicialmente nenhum bloco é relacionado aos processos
  # Primeiro precisamos encontrar um local em que o processo caiba, considerando seu tamanho
  for i in range(n):
    for j in range(m):
      if blockSize[j] >= processSize[i]:

        # caso o if acima seja cumprido, designaremos o processo "i" ao bloco "j"
        allocation[i] = j

        # Aqui removemos do tamanho do bloco o tamanho do processo
        blockSize[j] -= processSize[i]

        break

  print(" Processo N. Tamanho do processo      Alocação N.")
  for i in range(n):
    print(" ",
          i + 1,
          "         ",
          processSize[i],
          "                  ",
          end=" ")
    if allocation[i] != -1:
      print(allocation[i] + 1)
    else:
      print("Não pode ser alocado")


def get_block_sizes():
    block_sizes = input("Digite os tamanhos dos blocos de memória separados por espaço: ").split()
    return list(map(int, block_sizes))

def get_process_sizes():
    process_sizes = input("Digite os tamanhos dos processos separados por espaço: ").split()
    return list(map(int, process_sizes))

if __name__ == '__main__':
    blockSize = get_block_sizes()
    processSize = get_process_sizes()
    m = len(blockSize)
    n = len(processSize)

    firstFit(blockSize, m, processSize, n)

