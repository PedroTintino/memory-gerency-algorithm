# Code by Pedro Vieira.
# Today we gonna do a worst-fit code to my OS homework using Python and the previous code (best-fit one) only changing the logic.
# Now we looking for the non-best place to put it up

# First we need to create a function to turn memory on blocks
def worstFit(blockSize, m, processSize, n):
    # Now we need to hold "in use" blocks id
    allocation = [-1] * n
    # Above we're declaring a list "alocation" assigning to all the items a value "-1", which means that the process hasn't been allocated.
    # Now we gonna find the worst block to suit our process
    for i in range(n):
        worstIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if worstIdx == -1:
                    worstIdx = j
                elif blockSize[worstIdx] < blockSize[j]:
                    worstIdx = j

        # If we find a block for the current process
        if worstIdx != -1:
            allocation[i] = worstIdx
            # Reducing the available memory 'cause we already use it.
            blockSize[worstIdx] -= processSize[i]

    # Creating the table
    print("Process No. Process Size     Block no.")
    for i in range(n):
        print(i + 1, "         ", processSize[i], end="         ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


def get_block_sizes():
    block_sizes = input("Digite os tamanhos dos blocos de memória separados por espaço: ").split()
    return list(map(int, block_sizes))


def get_task_sizes():
    task_sizes = input("Digite os tamanhos dos processos separados por espaço: ").split()
    return list(map(int, task_sizes))


if __name__ == '__main__':
    blockSize = get_block_sizes()
    taskSize = get_task_sizes()
    m = len(blockSize)
    n = len(taskSize)

    worstFit(blockSize, m, taskSize, n)
