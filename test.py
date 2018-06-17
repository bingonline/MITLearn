import matplotlib.pylab as py
import numpy
import random
#py.figure(1)
#py.plot([1,2,3,4],[1,7,3,5])
#py.show()


def stdDev(X):
    mean=sum(X)/float(len(X))
    tor=0.0
    for x in X:
        tor+=(x-mean)**2
    return (tor/len(x))**0.5



def throwNeedles(numNeedles):
    inCircle=0
    for needles in xrange(1,numNeedles+1,1):
        x=random.random()
        y=random.random()
        if (x*x+y*y)**0.5<=1.0:
            inCircle+=1
    return 4*(inCircle/float(numNeedles))


def getEst(numNeedles,numTrials):
    estimates=[]
    for t in range(numTrials):
        piGuess=throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev=stdDev(estimates)
    curEst=sum(estimates)/len(estimates)
    print 'est.='+str(curEst)+'std.dev='+str(round(sDev,6))
    return (curEst,sDev)
def estPi(precision,numTrials):
    numNeedles=1000
    sDev=precision
    while sDev>precision/2.0:
        curEst,sDev=getEst(numNeedles,numTrials)
        numNeedles*=2
    return curEst

random.seed(0)
estPi(0.005,100)