import drawpyo

diagram = drawpyo.File(file_name="test2.drawio", file_path=r"E:\Robins Codespace\drawpyo_diagrams")
page = drawpyo.Page(file=diagram)
page.width = 700
page.height = 400

def mkSrvr(locX: float, locY: float, numSrvr: int, distSrvr: float) -> list:
    '''
    To make server diagrams (1u) by given number of input

    Args:
        locX: Relative location (%) in X axis (0 ~ 1)
        locY: Relative location (%) in Y axis (0 ~ 1)
        numSrvr: Number of Servers to generate
        distSrvr: Distance between servers (0 ~ 1 ~ server height)
    '''

    srvr = drawpyo.diagram.object_from_library(page=page, 
                              library="servers",
                              obj_name="1u_rack_server",
                              )
    rackHeight = srvr.geometry.height * numSrvr
    estHeight_srvrs = rackHeight + rackHeight * distSrvr
    movable_length = page.height - estHeight_srvrs
    
    rel_min_Y = page.height/2 - movable_length/2

    min_X = (page.width * locX - srvr.geometry.width)
    if min_X < 0:
        min_X = 0

    min_Y = page.height * locY - estHeight_srvrs/2
    if min_Y < 0:
        min_Y = 0

    max_Y = page.height * locY + estHeight_srvrs/2 + srvr.geometry.height
    if max_Y > movable_length:
        max_Y = movable_length

    srvrs = [0] * numSrvr
    srvrs[0].position = (0, 0)
    for i in range(numSrvr):
        srvrs[i] = srvr
        
        if i != 0:
            srvrs[i].position = (min_X, min_Y + (srvr.geometry.height + srvr.geometry.height*distSrvr) * i)
    return srvrs


def mkConPnts(obj, numPnts: int, locPnts: int):
    """To make Connection Points in an Object
    
    Args:
        numPnts: Number of Connection points in the object
        locPnts: Location of the connection points
                    1 -> Top;
                    2 -> Bottom;
                    3 -> Left;
                    4 -> Right;
    """
    distPnts = 1/(numPnts + 1)

    pnts = []
    for i in range(1, numPnts+1):
        pnt = [0,0,0,0,0]
        if locPnts == 1:
            pnt[0] = distPnts * i
        elif locPnts == 2:
            pnt[0] = distPnts * i
            pnt[1] = 1
        elif locPnts == 3:
            pnt[1] = distPnts * i
        elif locPnts == 4:
            pnt[0] = 1
            pnt[1] = distPnts * i
        pnts.append(pnt)
    # print(pnts)
    obj.apply_style_string(f"points={pnts}")


if __name__ == "__main__":
    srvr = mkSrvr(1)
    mkConPnts(srvr[0], 1, 2)
    diagram.write()