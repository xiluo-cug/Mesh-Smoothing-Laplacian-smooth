import copy
import numpy as np
import open3d as o3d  
  
def laplacian_smoothing(mesh, num_iterations=10, lambda_value=0.5):  
    """  
    对 mesh 进行 Laplacian 平滑。  
      
    参数:  
        mesh (o3d.geometry.TriangleMesh): 要进行平滑的 mesh。  
        num_iterations (int): 平滑迭代的次数。  
        lambda_value (float): 平滑的强度。  
      
    返回:  
        o3d.geometry.TriangleMesh: 平滑后的 mesh。  
    """  
    # 创建一个平滑函数  
    smoothing_function = o3d.geometry.TriangleMesh.filter_smooth_laplacian(mesh, number_of_iterations=num_iterations, lambda_filter=lambda_value)  
    print(smoothing_function)
      
    # 执行平滑  
    #smoothed_mesh = smoothing_function  
      
    return smoothing_function  
  
# 加载 mesh  
mesh= o3d.io.read_triangle_mesh('/home/xiluo/data/Reconstruction/CAP-UDF/320000_mesh.obj')
# 进行 Laplacian 平滑  
mesh = laplacian_smoothing(mesh, num_iterations=2, lambda_value=0.5)  
# 计算法向量
mesh.compute_vertex_normals()
# 创建副本并反转法向量
mesh_flipped = copy.deepcopy(mesh)
mesh_flipped.triangles = o3d.utility.Vector3iVector(np.asarray(mesh.triangles)[:, ::-1])
o3d.io.write_triangle_mesh("s320000_mesh.obj",mesh)
# 可视化原始和反转法向量的两个三角网格
o3d.visualization.draw_geometries([mesh, mesh_flipped])


