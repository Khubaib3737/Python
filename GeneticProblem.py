geneSet = "abcdefghhijklmaanopqrstzriuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!. "
target = "Ali"
import random
import datetime

def Calculate_Fitness(guess):
    return sum(1 for expected,actual in zip(target,guess) if expected==actual)

def Cross_Over(length):
    genes=[]
    while len(genes)<length:
        sampleSize=min(length-len(genes),len(geneSet))
        genes.extend(random.sample(geneSet,sampleSize))
    return "".join(genes)

def Mutation(parent):
    index=random.randrange(0,len(parent))
    childGenes=list(parent)
    newGene,alternate=random.sample(geneSet,2)
    childGenes[index]=alternate if newGene==childGenes[index] else newGene
    return "".join(childGenes)

def Display(guess):
    timeDiff=datetime.datetime.now()-startTime
    fitness=Calculate_Fitness(guess)
    print("{}\t{}\t{}".format(guess,fitness,timeDiff))

#Driver_Code    
random.seed()
startTime=datetime.datetime.now()
bestParent=Cross_Over(len(target))
bestFitness=Calculate_Fitness(bestParent)
Display(bestParent)
while True:
    child=Mutation(bestParent)
    childFitness=Calculate_Fitness(child)
    if bestFitness>=childFitness:
        continue
    Display(child)
    if childFitness>=len(bestParent):
        break
        exit(0)
    bestFitness=childFitness