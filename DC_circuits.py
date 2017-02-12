# import matplotlib and make it run headless, otherwise in SchewDraw it will return and error
# when tries to connect to Xserver and $Display environmental variable
# matplotlib.pyplot enables controlling the number of active plots
import matplotlib
matplotlib.use('Agg')

#Documentation:  http://cdelker.bitbucket.org/SchemDraw.html
import SchemDraw as schem
import SchemDraw.elements as e

# Import library to parametrize the used of SchemDraw
from ParamSchemDraw import electricComponent, resistor, vSource, iSource

# Folder to save the schematics in server
path = '/projects/15860edd-0fa5-4a0a-820c-2bb86b4c0cd5/ENUNCIADOS/IMAGENS/'
# Image extension
extension = '.png'

################################################################################
# Circuit Example

# TODO
# change params to **kwargs
# modify classes to support location of label. ? Is it really necessary?

def example_01(params, ekey, label=True):
    # Parameters
    V1 = vSource(params['$V_1$'], '$V_1$')
    V2 = vSource(params['$V_2$'], '$V_2$')

    R1 = resistor(params['$R_1$'], '$R_1$')
    R2 = resistor(params['$R_2$'], '$R_2$')
    R3 = resistor(params['$R_3$'], '$R_3$')
    R4 = resistor(params['$R_4$'], '$R_4$')

    # new drawing
    d = schem.Drawing()

    # add the first voltage source, his name, the first resistor and a dot
    V1.schem = d.add( e.SOURCE_V , label=V1.label)
    R1.schem = d.add( e.RES, d='right', label= R1.label )
    d.add( e.DOT )

    #save node position to stack, add vertical resistor, a dot and pop stack (point draw start point to the node)
    d.push()
    R2.schem = d.add( e.RES, d='down', label= R2.label )
    d.add( e.DOT )
    d.pop()

    # add resistor, a dota and save node
    R3.schem = d.add( e.RES, d='right', label= R3.label )
    d.add( e.DOT )
    d.push()

    # draw 2nd voltage source, add his name,a dot and return to the start node
    # the source must be drawed down, so if one wants the voltage drop from up to down, the source must be reversed
    V2.schem = d.add( e.SOURCE_V, d='down', reverse='True', label= V2.label )
    d.add( e.DOT )
    d.pop()

    # add a line to the right, then a resistor
    d.add( e.LINE, d='right', l=2.5)
    R4.schem = d.add( e.RES, d='down', label= R4.label )

    # Link all the ground nodes, add a dot to V1 and a ground signal
    d.add( e.LINE, to=V1.schem.start )
    d.add( e.DOT )
    d.add( e.GND )

    # Add labels if the circuit requires parametrization
    if label:
        V1.schem.add_label(V1.voltageEng, loc='bot')
        V2.schem.add_label(V2.voltageEng, loc='bot')
        R1.schem.add_label(R1.resistanceEng, loc='bot')
        R2.schem.add_label(R2.resistanceEng, loc='bot')
        R3.schem.add_label(R3.resistanceEng, loc='bot')
        R4.schem.add_label(R4.resistanceEng, loc='bot')

    # draw the circuit, but don't show
    d.draw(showplot = False)

    # save schematic (full path + Circuit ID + parametrize identifier + extension)
    filename = 'test_0_' + str(ekey) + extension
    d.save(path + filename)

    # close all open plots
    matplotlib.pyplot.close('all')

    return filename

def DC_001(params, ekey, label=True):
    V1 = vSource(params['$V_1$'], '$V_1$')
    V2 = vSource(params['$V_2$'], '$V_2$')
    I1 = vSource(params['$I_1$'], '$I_1$')
    I2 = vSource(params['$I_2$'], '$I_2$')
    I3 = vSource(params['$I_1$'], '$I_3$')

    d = schem.Drawing()
    I1.schem = d.add( e.SOURCE_I , reverse='True', label=I1.label)
    V1.schem = d.add( e.SOURCE_V, d='right', label= V1.label )
    d.push()
    d.add( e.DOT )
    V2.schem = d.add( e.SOURCE_V, d='down', reverse='True', label= V2.label )
    d.pop()
    d.add( e.LINE, d='right', l=2.5)
    d.push()
    I2.schem = d.add( e.SOURCE_I, d='down', label= I2.label )
    d.pop()
    d.add( e.LINE, d='right', l=2.5)
    d.push()
    I3.schem = d.add( e.SOURCE_I, d='down', reverse='True', label= I3.label )
    d.add( e.LINE, to=I1.schem.end )
    d.add( e.DOT )
    d.add( e.GND )

    if label:
        V1.schem.add_label(V1.voltageEng, loc='bot')
        V2.schem.add_label(V2.voltageEng, loc='bot')
        I1.schem.add_label(I1.currentEng, loc='bot')
        I2.schem.add_label(I2.currentEng, loc='bot')
        I3.schem.add_label(I3.currentEng, loc='bot')

    d.draw(showplot = False)

    # save schematic (full path + Circuit ID + parametrize identifier + extension)
    filename = 'test_0_' + str(ekey) + extension
    d.save(path + filename)

    matplotlib.pyplot.close('all')

    return filename
