import torch
import dgl

def pyg_data_to_dgl_graph(pyg_data_obj):
    print(pyg_data_obj)

    # 获取边索引
    edge_index = pyg_data_obj.edge_index
    
    # DGL需要的边索引格式是两列的数组，而不是两行的索引
    src, dst = edge_index
    edge_list = torch.stack((src, dst), dim=1)
    
    # 创建DGL图
    g = dgl.graph((edge_list[:, 0], edge_list[:, 1]), num_nodes=pyg_data_obj.x.shape[0])
    
    # 添加节点特征
    if 'x' in pyg_data_obj:
        g.ndata['feature'] = pyg_data_obj.x
    
    # 添加边特征
    if 'edge_attr' in pyg_data_obj:
        g.edata['feat'] = pyg_data_obj.edge_attr
    
    # 添加节点标签
    if 'y' in pyg_data_obj:
        g.ndata['label'] = pyg_data_obj.y

    # 添加节点标签
    if 'train_mask' in pyg_data_obj:
        g.ndata['train_mask'] = pyg_data_obj.train_mask

    # 添加节点标签
    if 'test_mask' in pyg_data_obj:
        g.ndata['test_mask'] = pyg_data_obj.test_mask

    # 添加节点标签
    if 'val_mask' in pyg_data_obj:
        g.ndata['val_mask'] = pyg_data_obj.val_mask

    
    return g