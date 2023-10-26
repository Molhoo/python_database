from docopt import docopt
from cod_asli import *
from tabulate import tabulate

usage = '''
Usage:
    spent_app.py --init
    spent_app.py --Show [<daily_activity>]
    spent_app.py --Add <amuont_money> <daily_activity> [<message>]

 '''
args = docopt(usage)

if args['--init']:
    init()
    print('Your Table Successfully Created .' )
if args['--Show']:
    daily_activity = args['<daily_activity>']
    amuont_money , result = Show(daily_activity)
    print('Total everyday money : ' , amuont_money )
    print(tabulate(result))

if args['--Add']:
    try:
        amuont_money = float(args['<amuont_money>'])
        Add(amuont_money , args['<daily_activity>'] , args['<message>'] )
        print('Item Added ... .')
    except:
        print(usage)
