import drawpyo

diagram = drawpyo.File(file_name="test.drawio", file_path=r"E:\Robins Codespace\drawpyo_diagrams")
page = drawpyo.Page(file=diagram)
page.width = 700
page.height = 400

server_1 = drawpyo.diagram.object_from_library(page=page, 
                              library="servers",
                              obj_name="1u_rack_server",
                              points=[[0.2,1,0,0,0],[0.4,1,0,0,0],[0.6,1,0,0,0],[0.8,1,0,0,0]]
                              )

print(f'Srvr 1 height: {server_1.height} \nSrvr 2 width: {server_1.width}')
server_2 = drawpyo.diagram.object_from_library(page=page, 
                              library="servers",
                              obj_name="1u_rack_server",
                              points=[[0.2,1,0,0,0],[0.4,1,0,0,0],[0.6,1,0,0,0],[0.8,1,0,0,0]]
                              )

link = drawpyo.diagram.Edge(
    page=page,
    source=server_1,
    target=server_2,
    label = "mLOM 1/1",
    label_position = -0.5
)

diagram.write()