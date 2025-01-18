from quantum_layer import QuantumLayer
from agent_layer import Agent, HierarchicalSwarm
import numpy as np

def main():
    """主程序入口"""
    print("初始化梅西 ($MEIXI) 系统...")
    
    # 初始化量子层
    quantum = QuantumLayer()
    print("量子层初始化完成")
    
    # 初始化分层蜂群
    swarm = HierarchicalSwarm()
    swarm.add_level("Level1")  # 领导层
    swarm.add_level("Level2")  # 工作层
    
    # 创建并添加代理
    leader = Agent(name="Leader1", role="Leader")
    worker1 = Agent(name="Worker1", role="Worker")
    worker2 = Agent(name="Worker2", role="Worker")
    
    swarm.add_agent_to_level("Level1", leader)
    swarm.add_agent_to_level("Level2", worker1)
    swarm.add_agent_to_level("Level2", worker2)
    print("分层蜂群初始化完成")
    
    # 示例任务
    test_data = np.array([1, 2, 3, 4, 5])
    print("\n执行量子状态探索...")
    quantum_states = quantum.quantum_state_exploration(test_data)
    print(f"探索到 {len(quantum_states)} 个量子状态")
    
    print("\n委派任务给蜂群...")
    tasks = ["数据分析", "路线优化"]
    for task in tasks:
        print(f"\n将任务 '{task}' 委派给领导层:")
        results = swarm.delegate_task_to_level("Level1", task)
        for result in results:
            print(result)
            
        print(f"\n将任务 '{task}' 委派给工作层:")
        results = swarm.delegate_task_to_level("Level2", task)
        for result in results:
            print(result)

if __name__ == "__main__":
    main()
