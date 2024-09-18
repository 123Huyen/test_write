#this program is used to test writing data to the tag in KEPServerEX

import asyncio
from asyncua import Client, ua

async def test_write():
    #connecc to the server
    url = 'opc.tcp://localhost:49320'
    async with Client(url) as opc_client:
        print('Client connected')
        root = opc_client.get_root_node()
        print('Root node is:', root)
        objects = await root.get_child('0:Objects')
        print('Objects node is:', objects)
        
        #access the PyTest node
        try:
            pytest_node = await objects.get_child('2:PyTest')
            print('pytest node is:', pytest_node)

            #browse all children of the PyTest node
            pytest_children = await pytest_node.get_children()
            print('pytest_children:', pytest_children)
            for child in pytest_children:
                browse_name = await child.read_browse_name()
                print('child:',child, 'browse name:', browse_name)
                
                #check the node class before reading the value
                node_class = await child.read_node_class()
                print('node class is:', node_class)
                if node_class == ua.NodeClass.Variable:
                    value = await child.read_value()
                    print('value:', value)
                else:
                    print('child is not a variable, skipping value read')
        except Exception as e:
            print('Error accesing pyTest node:', e)
        
#run the async function
if __name__=='__main__':
    asyncio.run(test_write())

        
        
