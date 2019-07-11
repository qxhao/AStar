import map_2d
import AStar

if __name__ == '__main__':
    ##构建地图
    mapTest = map_2d.map2d()
    mapTest.showMap()
    ##构建A*
    aStar = AStar.AStar(mapTest, AStar.Node(AStar.Point(4, 4)), AStar.Node(AStar.Point(11, 23)))
    print("A* start:")
    ##开始寻路
    if aStar.start():
        aStar.setMap()
        mapTest.showMap()
    else:
        print("no way")
