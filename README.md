# fpcalc
frequency period calculator

## args
<pre>
usage: fpcalc.py [-h] temporal magnitude

positional arguments:
  temporal    The temporal to be calculated
  magnitude   The magnitude of the temporal [kilo,mega,giga]|[mili,micro,nano]

optional arguments:
  -h, --help  show this help message and exit
</pre>
## example
<pre>

$p$g > ./fpcalc.py 32.768 kilo
reciprocal of 32.768 kilohertz is 30.517578 microseconds

$p$g > ./fpcalc.py 30.518 micro
reciprocal of 30.518 microseconds is 32.767547 kilohertz
</pre>
