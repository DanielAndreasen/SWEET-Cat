#!/usr/bin/python


def simbad(stars, output):
    """Function to make script for Simbad. Takes a list of stars

    :stars: A list of stars
    :returns: An output file called SimbadQuery.txt for Simbad to read

    """

    t = ''
    for star in stars:
        t += star + '\n'

    with open(output, 'wb') as f:
        f.write(t)

    with open('SimbadQuery.txt', 'wb') as result:
        result.write('Simbad script for planet hosts\n')

        ttt = '|%IDLIST(HD|Gl|GJ|BD|HIP|CoroT|WASP|Kepler|KOI|KIC|HAT|NGC|XO'
        ttt += '|Qatar|TrES|OGLE|1)|%COO(A)|%COO(D)|%SP(S)|%FLUXLIST(V;F)|%'
        ttt += 'FLUXLIST(V;E)|%PLX(V)|%PLX(E)\"\n'

        for star in stars:
            # line2 = line.replace('\n', '')
            line3 = 'format object form1 \"' + star + ttt
            result.write(line3.replace('\r', ''))
            result.write('query id '+star.replace('-', ' ') + '\n')

        result.write('format display\n')
