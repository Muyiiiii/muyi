import GPUtil

def get_gpu_memory_usage():
    # 获取GPU使用情况
    gpus = GPUtil.getGPUs()
    gpu_memory_info = []
    for gpu in gpus:
        gpu_memory_info.append((gpu.id, gpu.name, f"{gpu.memoryUsed} MB", f"{gpu.memoryTotal} MB", f"{gpu.memoryUtil * 100:.1f}%"))

    return gpu_memory_info

def display_gpu_memory_usage():
    gpu_memory_info = get_gpu_memory_usage()

    if gpu_memory_info:
        print("GPU Memory Usage:")
        for info in gpu_memory_info:
            print(f"GPU ID: {info[0]}, Name: {info[1]}, Memory Used: {info[2]}, Total Memory: {info[3]}, Memory Utilization: {info[4]}")
    else:
        print("No GPU found.")