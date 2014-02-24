import argparse

import plot
import testing

parser = argparse.ArgumentParser(description="Launch server.")
parser.add_argument('mode', metavar='MODE',
                    choices=['roundtrip', 'throughput', 'sizes'],
                    help='Select mode of operation.')
parser.add_argument('type', metavar='TYPE',
                    choices=['TCP', 'UDP'],
                    help='Choose between TCP or UDP for transmissions.')
parser.add_argument('host', metavar='HOST',
                    help='Set host to connect to.')
parser.add_argument('port', metavar='PORT',
                    type=int,
                    help='Set port to use.')

args = parser.parse_args()

roundtrip_msgsizes = range(0, 10, 4)
throughput_msgsizes = range(10, 22, 2)
size_msgsizes = range(16, 21)

if args.mode == 'roundtrip':
    plot.bar_chart(*testing.roundtrip(roundtrip_msgsizes, **args.__dict__),
                   title='Round Trip Time',
                   xlabel='Packet Size (B)', ylabel='RTT (ms)', ymul=1000)
elif args.mode == 'throughput':
    print(testing.throughput(throughput_msgsizes, **args.__dict__))
else:
    print(testing.sizes(sizes_msgsizes, **args.__dict__))
