#!/usr/bin/env python
from collections import OrderedDict
import argparse


# for Period calculation
pMagnitude = OrderedDict ([
    (''     ,   1),
    ('mili' ,   1000),
    ('micro',   1000000),
    ('nano' ,   1000000000),
    ('pico' ,   1000000000000),
])

# for Frequency calculation
fMagnitude = OrderedDict ([
    (''     ,   1),
    ('kilo' ,   1000),
    ('mega' ,   1000000),
    ('giga' ,   1000000000),
    ('tera' ,   1000000000000),
])

def calculatePeriod(magnitude,frequency):
    """ calculates the period of the frequency passed in """
    
    # calculate the period
    period = float(1) / float(frequency)
    
    # adjust the magnitude and period if necessary
    finalMag = fMagnitude[magnitude]
    while(period < 1):
        period   *= 1000
        finalMag *= 1000
    
    # get the index into the period dict for our new magnitude
    pIndex = pMagnitude.values().index(finalMag)
    
    # finally get the period canonical magnitude.
    pmag = pMagnitude.keys()[pIndex]
    
    return (period,pmag)
#
def calculateFrequency(magnitude,period):
    """ convert period to frequency """

    # calculate the frequency
    frequency = float(1) / float(period)
    
    # adjust the magnitude if requred
    finalMag  = pMagnitude[magnitude]
    while(frequency < 1):
        frequency *= 1000
        finalMag  /= 1000
    
    # cross reference to get our magnitude.
    fIndex    = fMagnitude.values().index(finalMag)
    fmag      = fMagnitude.keys()[fIndex]

    return(frequency,fmag)
#


if  __name__ == "__main__":

    # Instantiate the parser
    parser = argparse.ArgumentParser(description='frequency/period calculator')

    # Required positional argument
    parser.add_argument('temporal', type=float,
    help='The temporal to be calculated')
    
    parser.add_argument('magnitude', type=str,
    help='The magnitude of the temporal\n [kilo,mega,giga]|[mili,micro,nano]')

    args = parser.parse_args()
    args.magnitude = args.magnitude.lower()
    
    # Calculate frequency
    if(args.magnitude in pMagnitude.keys()):
        
        print( "reciprocal of %d %sseconds is" %
        (args.temporal,args.magnitude) ),

        print("%f %shertz" % 
        calculateFrequency(args.magnitude,args.temporal) ),
    
    # Calculate period
    elif(args.magnitude in fMagnitude.keys()):
        print( "reciprocal of %d %shertz is" % 
        (args.temporal,args.magnitude) ),
        print( "%f %sseconds" %
         calculatePeriod(args.magnitude,args.temporal) ),
    
    # Abort
    else:
        print "No known magnitude"
    #
#
